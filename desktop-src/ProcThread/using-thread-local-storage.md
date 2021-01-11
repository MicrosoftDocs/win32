---
description: Thread local storage (TLS) enables multiple threads of the same process to use an index allocated by the TlsAlloc function to store and retrieve a value that is local to the thread.
ms.assetid: b7f5a206-a827-4b6b-86f6-5e3aea1246b7
title: Using Thread Local Storage
ms.topic: article
ms.date: 05/31/2018
---

# Using Thread Local Storage

[Thread local storage](thread-local-storage.md) (TLS) enables multiple threads of the same process to use an index allocated by the [**TlsAlloc**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlsalloc) function to store and retrieve a value that is local to the thread. In this example, an index is allocated when the process starts. When each thread starts, it allocates a block of dynamic memory and stores a pointer to this memory in the TLS slot using the [**TlsSetValue**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlssetvalue) function. The CommonFunc function uses the [**TlsGetValue**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlsgetvalue) function to access the data associated with the index that is local to the calling thread. Before each thread terminates, it releases its dynamic memory. Before the process terminates, it calls [**TlsFree**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlsfree) to release the index.


```C++
#include <windows.h> 
#include <stdio.h> 
 
#define THREADCOUNT 4 
DWORD dwTlsIndex; 
 
VOID ErrorExit (LPCSTR message);
 
VOID CommonFunc(VOID) 
{ 
   LPVOID lpvData; 
 
// Retrieve a data pointer for the current thread. 
 
   lpvData = TlsGetValue(dwTlsIndex); 
   if ((lpvData == 0) && (GetLastError() != ERROR_SUCCESS)) 
      ErrorExit("TlsGetValue error"); 
 
// Use the data stored for the current thread. 
 
   printf("common: thread %d: lpvData=%lx\n", 
      GetCurrentThreadId(), lpvData); 
 
   Sleep(5000); 
} 
 
DWORD WINAPI ThreadFunc(VOID) 
{ 
   LPVOID lpvData; 
 
// Initialize the TLS index for this thread. 
 
   lpvData = (LPVOID) LocalAlloc(LPTR, 256); 
   if (! TlsSetValue(dwTlsIndex, lpvData)) 
      ErrorExit("TlsSetValue error"); 
 
   printf("thread %d: lpvData=%lx\n", GetCurrentThreadId(), lpvData); 
 
   CommonFunc(); 
 
// Release the dynamic memory before the thread returns. 
 
   lpvData = TlsGetValue(dwTlsIndex); 
   if (lpvData != 0) 
      LocalFree((HLOCAL) lpvData); 
 
   return 0; 
} 
 
int main(VOID) 
{ 
   DWORD IDThread; 
   HANDLE hThread[THREADCOUNT]; 
   int i; 
 
// Allocate a TLS index. 
 
   if ((dwTlsIndex = TlsAlloc()) == TLS_OUT_OF_INDEXES) 
      ErrorExit("TlsAlloc failed"); 
 
// Create multiple threads. 
 
   for (i = 0; i < THREADCOUNT; i++) 
   { 
      hThread[i] = CreateThread(NULL, // default security attributes 
         0,                           // use default stack size 
         (LPTHREAD_START_ROUTINE) ThreadFunc, // thread function 
         NULL,                    // no thread function argument 
         0,                       // use default creation flags 
         &IDThread);              // returns thread identifier 
 
   // Check the return value for success. 
      if (hThread[i] == NULL) 
         ErrorExit("CreateThread error\n"); 
   } 
 
   for (i = 0; i < THREADCOUNT; i++) 
      WaitForSingleObject(hThread[i], INFINITE); 
 
   TlsFree(dwTlsIndex);

   return 0; 
} 
 
VOID ErrorExit (LPCSTR message)
{ 
   fprintf(stderr, "%s\n", message); 
   ExitProcess(0); 
}
```



## Related topics

<dl> <dt>

[Using Thread Local Storage in a Dynamic-Link Library](../dlls/using-thread-local-storage-in-a-dynamic-link-library.md)
</dt> </dl>

 

 
