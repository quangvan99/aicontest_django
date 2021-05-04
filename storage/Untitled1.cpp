#include <iostream>
#include <pthread.h>
#include <time.h>
using namespace std;
void * fun_thread1(void *data)
{
    for(int i=0;i<5;i++)
    { 
        cout<<endl<<"In Thread 1"<<endl;
    }     
}
void * fun_thread2(void *data)
{
    for(int i=0;i<5;i++)
    { 
        cout<<endl<<"In Thread 2"<<endl;
    }     
}
int main(int argc, char *argv[])
{
    int status;
    clock_t td, ts;
    // creating thread objects
    td =1000*clock()*1.0/CLOCKS_PER_SEC;
    pthread_t thrd_1;
    pthread_t thrd_2;
    // create thread
    pthread_create(&thrd_1,NULL,fun_thread1,(void *)0);
    pthread_create(&thrd_2,NULL,fun_thread2,(void *)0);    
    pthread_join(thrd_1, (void **)&status);
    pthread_join(thrd_2, (void **)&status);
    ts=1000*clock()*1.0/CLOCKS_PER_SEC;
    cout<<"Time : "<< ts-td <<"s\n";
    system("PAUSE");
//    return EXIT_SUCCESS;
}
