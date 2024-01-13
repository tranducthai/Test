#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_SIZE 1000
#define MAX_QUESTION_SIZE 10
typedef struct
{
	char studentID[11];
	char questionID[50];
	char submitDate[11];
	char submitTime[10];
	int result;
} LOG;


void readExamDetail(char lstExamQuestions[][50], int* numQuestions)
{
	int index = 0;
	char nextLine[255];
	while (1)
	{
		fgets(nextLine, sizeof(nextLine), stdin);
		nextLine[strcspn(nextLine, "\r\n")] = 0;

		if (strcmp(nextLine, "-1") == 0) break;

		strcpy(lstExamQuestions[index], nextLine);

		index++;
	}
	*numQuestions = index;
}

int readLog(LOG* logArr)
{
	int lineCount = 0;
	char nextLine[255];
	while (1)
	{
		fgets(nextLine, sizeof(nextLine), stdin);
		nextLine[strcspn(nextLine, "\r\n")] = 0;

		if (strcmp(nextLine, "-1") == 0) break;

	
		sscanf(nextLine, "%s %s %s %s %d", logArr[lineCount].studentID,
			logArr[lineCount].questionID, logArr[lineCount].submitDate,
			logArr[lineCount].submitTime, &logArr[lineCount].result);

		lineCount++;
	}
	return lineCount;
}
//============================================================================

int numberofSubmits(LOG* logArr, int size)
{

	LOG std[1000];
	int i,j,k,n;
	int dem=0;
	std[0]=logArr[0];
	int sl=1;
	for(i=1;i<size;i++)
{
for(j=0;j<sl;j++)
if(strcmp(logArr[i].studentID,std[j].studentID)==0)
{
	dem++;break;
}
if(dem==0) 
{
	std[sl]=logArr[i];
	sl++;
}
dem=0;
}
return sl;

}



int getResultofStudentId(char lstExamQuestions[][50], int numQuestions, LOG* logArr, int size, const char* studentID)
{
	// CODE t?i dây
   LOG std[1000];
   int sl=0;
   int i,j;
   for(i=0;i<size;i++)
   if(strcmp(studentID,logArr[i].studentID)==0)
   {
   	std[sl]=logArr[i];
   	sl++;
   }
   int res[1000]={};
   for(i=0;i<numQuestions;i++)
   {
   	for(j=0;j<sl;j++)
   	if(strcmp(lstExamQuestions[i],std[j].questionID)==0) 
   	{
   		if(std[j].result>res[i]) res[i]=std[j].result;
	   }
   }
   int toTal=0;
   for(i=0;i<numQuestions;i++)
   toTal=toTal+res[i];
	return toTal;
}


void printStudentExamDetail(char lstExamQuestions[][50], int numQuestions, LOG* logArr, int size, const char* studentID)
{
	int chiso;
LOG std[1000];
int scr[1000]={};
   int sl=0;
   int i,j;
   
   
   for(i=0;i<size;i++)
   if(strcmp(studentID,logArr[i].studentID)==0)
   {
   	std[sl]=logArr[i];
   	sl++;
   }
   
   

   for(i=0;i<sl;i++)
   {
   	chiso=atoi(&std[i].questionID[9]);
   	if(std[i].result>scr[chiso]) scr[chiso]=std[i].result;
   }
   	for(i=0;i<sl;i++)
   	
   	{
  chiso=atoi(&std[i].questionID[9]);
   	if(std[i].result<scr[chiso]) std[i].result=-1;
    }
    LOG alt[1000];
    
    int num=0;
    int dem=0;
    for(i=0;i<sl;i++)
{  
  if(std[i].result>=0)
  {
  	for(j=0;j<num;j++)
  	 {
  	 	if(strcmp(std[i].questionID,alt[j].questionID)==0)
  	 	{
  	 		dem++;break;
		}
		      
	 }
	if(dem==0) 
	{
	printf("%s %s %s %d\n",std[i].questionID,std[i].submitDate,std[i].submitTime,std[i].result); 
	alt[num]=std[i];
	num++;
}
dem=0;
  }




}
}



void printSubmitStatistic(char lstExamQuestions[][50], int numQuestions, LOG* logArr, int size)
{
	// CODE t?i dây
	int i,j;
	int per[1000];
	int tot[1000];
	double ave[1000];
	for(i=0;i<numQuestions;i++)
	{
		for(j=0;j<size;j++)
		if(strcmp(lstExamQuestions[i],logArr[j].questionID)==0)
		{
			tot[i]=tot[i]+logArr[j].result;
			per[i]++;
		}
	if(per[i]==0) ave[i]=0;
	else ave[i]=(double)tot[i]/per[i];	
	}
	for(i=0;i<numQuestions;i++)
	printf("%s %d %.2lf\n",lstExamQuestions[i],per[i],ave[i]);
}



//===========================================
void getStudentResult(char lstExamQuestions[][50], int numQuestions, LOG* logArr, int size)
{
	char nextStudentID[255];
	while (1)
	{
		fgets(nextStudentID, sizeof(nextStudentID), stdin);
		nextStudentID[strcspn(nextStudentID, "\r\n")] = 0;

		if (strcmp(nextStudentID, "$") == 0) break;

		int result = getResultofStudentId(lstExamQuestions, numQuestions, logArr, size, nextStudentID);
		printf("StudentId %s result %d\n", nextStudentID, result);
	}
}
void getStudentSubmitDetail(char lstExamQuestions[][50], int numQuestions, LOG* logArr, int size)
{
	char nextStudentID[255];
	while (1)
	{
		fgets(nextStudentID, sizeof(nextStudentID), stdin);
		nextStudentID[strcspn(nextStudentID, "\r\n")] = 0;

		if (strcmp(nextStudentID, "$") == 0) break;

		printStudentExamDetail(lstExamQuestions, numQuestions, logArr, size, nextStudentID);
	}
}
int main()
{
	char lstExamQuestions[10][50];
	int lstQuestionSize = 0;
	LOG* logArr = NULL;
	int size;
	logArr = (LOG*)malloc(MAX_SIZE * sizeof(LOG));
	char nextCommand[100];
	while (1)
	{
		fgets(nextCommand, sizeof(nextCommand), stdin);
		nextCommand[strcspn(nextCommand, "\r\n")] = 0;
		if (strlen(nextCommand) == 0) continue;
		if (nextCommand[0] != '?') break;
		if (strcmp(&nextCommand[2], "loadLogSubmit") == 0) {
			size = readLog(logArr);
		}
		else if (strcmp(&nextCommand[2], "loadExamQuestions") == 0) {
			readExamDetail(lstExamQuestions, &lstQuestionSize);
			printf("Number of Questions: %d\n", lstQuestionSize);
		}
		else if (strcmp(&nextCommand[2], "numberofSubmits") == 0) {
			printf("Number of submit: %d\n", numberofSubmits(logArr, size));
		}
		else if (strcmp(&nextCommand[2], "getSubmitStatistic") == 0) {
			printSubmitStatistic(lstExamQuestions, lstQuestionSize, logArr, size);
		}
		else if (strcmp(&nextCommand[2], "getStudentResults") == 0) {
			getStudentResult(lstExamQuestions, lstQuestionSize, logArr, size);
		}
		else if (strcmp(&nextCommand[2], "getStudentSubmitDetail") == 0) {
			getStudentSubmitDetail(lstExamQuestions, lstQuestionSize, logArr, size);
		}

	}

	free(logArr);
	return 0;
}

