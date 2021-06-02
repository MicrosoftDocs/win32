---
description: The following example associates an asynchronous procedure call (APC) function, also known as a completion routine, with a waitable timer when the timer is set.
ms.assetid: aea3c080-caf2-4c16-adc5-51357a0340b8
title: Using Waitable Timers with an Asynchronous Procedure Call
ms.topic: article
ms.date: 05/31/2018
---

# Using Waitable Timers with an Asynchronous Procedure Call

The following example associates an [asynchronous procedure call](asynchronous-procedure-calls.md) (APC) function, also known as a completion routine, with a [waitable timer](waitable-timer-objects.md) when the timer is set. The address of the completion routine is the fourth parameter to the [**SetWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-setwaitabletimer) function. The fifth parameter is a void pointer that you can use to pass arguments to the completion routine.

The completion routine will be executed by the same thread that called [**SetWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-setwaitabletimer). This thread must be in an alertable state to execute the completion routine. It accomplishes this by calling the [**SleepEx**](/windows/win32/api/synchapi/nf-synchapi-sleepex) function, which is an alertable function.

Each thread has an APC queue. If there is an entry in the thread's APC queue at the time that one of the alertable functions is called, the thread is not put to sleep. Instead, the entry is removed from the APC queue and the completion routine is called.

If no entry exists in the APC queue, the thread is suspended until the wait is satisfied. The wait can be satisfied by adding an entry to the APC queue, by a timeout, or by a handle becoming signaled. If the wait is satisfied by an entry in the APC queue, the thread is awakened and the completion routine is called. In this case, the return value of the function is **WAIT\_IO\_COMPLETION**.

After the completion routine is executed, the system checks for another entry in the APC queue to process. An alertable function will return only after all APC entries have been processed. Therefore, if entries are being added to the APC queue faster than they can be processed, it is possible that a call to an alertable function will never return. This is especially possible with waitable timers, if the period is shorter than the amount of time required to execute the completion routine.

When you are using a waitable timer with an APC, the thread that sets the timer should not wait on the handle of the timer. By doing so, you would cause the thread to wake up as a result of the timer becoming signaled rather than as the result of an entry being added to the APC queue. As a result, the thread is no longer in an alertable state and the completion routine is not called. In the following code, the call to [**SleepEx**](/windows/win32/api/synchapi/nf-synchapi-sleepex) awakens the thread when an entry is added to the thread's APC queue after the timer is set to the signaled state.


```C++
#define UNICODE 1
#define _UNICODE 1

#include <windows.h>
#include <stdio.h>
#include <tchar.h>

#define _SECOND 10000000

typedef struct _MYDATA {
   TCHAR *szText;
   DWORD dwValue;
} MYDATA;

VOID CALLBACK TimerAPCProc(
   LPVOID lpArg,               // Data value
   DWORD dwTimerLowValue,      // Timer low value
   DWORD dwTimerHighValue )    // Timer high value

{
   // Formal parameters not used in this example.
   UNREFERENCED_PARAMETER(dwTimerLowValue);
   UNREFERENCED_PARAMETER(dwTimerHighValue);

   MYDATA *pMyData = (MYDATA *)lpArg;

   _tprintf( TEXT("Message: %s\nValue: %d\n\n"), pMyData->szText,
          pMyData->dwValue );
   MessageBeep(0);

}

int main( void ) 
{
   HANDLE          hTimer;
   BOOL            bSuccess;
   __int64         qwDueTime;
   LARGE_INTEGER   liDueTime;
   MYDATA          MyData;

   MyData.szText = TEXT("This is my data");
   MyData.dwValue = 100;

   hTimer = CreateWaitableTimer(
           NULL,                   // Default security attributes
           FALSE,                  // Create auto-reset timer
           TEXT("MyTimer"));       // Name of waitable timer
   if (hTimer != NULL)
   {
      __try 
      {
         // Create an integer that will be used to signal the timer 
         // 5 seconds from now.
         qwDueTime = -5 * _SECOND;

         // Copy the relative time into a LARGE_INTEGER.
         liDueTime.LowPart  = (DWORD) ( qwDueTime & 0xFFFFFFFF );
         liDueTime.HighPart = (LONG)  ( qwDueTime >> 32 );

         bSuccess = SetWaitableTimer(
            hTimer,           // Handle to the timer object
            &liDueTime,       // When timer will become signaled
            2000,             // Periodic timer interval of 2 seconds
            TimerAPCProc,     // Completion routine
            &MyData,          // Argument to the completion routine
            FALSE );          // Do not restore a suspended system

         if ( bSuccess ) 
         {
            for ( ; MyData.dwValue < 1000; MyData.dwValue += 100 ) 
            {
               SleepEx(
                  INFINITE,     // Wait forever
                  TRUE );       // Put thread in an alertable state
            }

         } 
         else 
         {
            printf("SetWaitableTimer failed with error %d\n", GetLastError());
         }

      } 
      __finally 
      {
         CloseHandle( hTimer );
      }
   } 
   else 
   {
      printf("CreateWaitableTimer failed with error %d\n", GetLastError());
   }

   return 0;
}
```



## Related topics

<dl> <dt>

[Using Waitable Timer Objects](using-waitable-timer-objects.md)
</dt> </dl>

 

 
