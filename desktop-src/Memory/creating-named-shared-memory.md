---
Description: To share data, multiple processes can use memory-mapped files that the system paging file stores.
ms.assetid: 17458be2-3ef7-42f2-a717-abf73ac4846f
title: Creating Named Shared Memory
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Named Shared Memory

To share data, multiple processes can use memory-mapped files that the system paging file stores.

## First Process

The first process creates the file mapping object by calling the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function with **INVALID\_HANDLE\_VALUE** and a name for the object. By using the **PAGE\_READWRITE** flag, the process has read/write permission to the memory through any file views that are created.

Then the process uses the file mapping object handle that [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) returns in a call to [**MapViewOfFile**](https://www.bing.com/search?q=**MapViewOfFile**) to create a view of the file in the process address space. The **MapViewOfFile** function returns a pointer to the file view, `pBuf`. The process then uses the [**CopyMemory**](/windows/desktop/api/WinBase/) function to write a string to the view that can be accessed by other processes.

Prefixing the file mapping object names with "Global\\" allows processes to communicate with each other even if they are in different terminal server sessions. This requires that the first process must have the [**SeCreateGlobalPrivilege**](https://msdn.microsoft.com/windows/desktop/973796a6-bc2e-4e64-92db-5e17b9c25460) privilege.

When the process no longer needs access to the file mapping object, it should call the [**CloseHandle**](https://msdn.microsoft.com/windows/desktop/9b84891d-62ca-4ddc-97b7-c4c79482abd9) function. When all handles are closed, the system can free the section of the paging file that the object uses.


```C++
#include <windows.h>
#include <stdio.h>
#include <conio.h>
#include <tchar.h>

#define BUF_SIZE 256
TCHAR szName[]=TEXT("Global\\MyFileMappingObject");
TCHAR szMsg[]=TEXT("Message from first process.");

int _tmain()
{
   HANDLE hMapFile;
   LPCTSTR pBuf;

   hMapFile = CreateFileMapping(
                 INVALID_HANDLE_VALUE,    // use paging file
                 NULL,                    // default security
                 PAGE_READWRITE,          // read/write access
                 0,                       // maximum object size (high-order DWORD)
                 BUF_SIZE,                // maximum object size (low-order DWORD)
                 szName);                 // name of mapping object

   if (hMapFile == NULL)
   {
      _tprintf(TEXT("Could not create file mapping object (%d).\n"),
             GetLastError());
      return 1;
   }
   pBuf = (LPTSTR) MapViewOfFile(hMapFile,   // handle to map object
                        FILE_MAP_ALL_ACCESS, // read/write permission
                        0,
                        0,
                        BUF_SIZE);

   if (pBuf == NULL)
   {
      _tprintf(TEXT("Could not map view of file (%d).\n"),
             GetLastError());

       CloseHandle(hMapFile);

      return 1;
   }


   CopyMemory((PVOID)pBuf, szMsg, (_tcslen(szMsg) * sizeof(TCHAR)));
    _getch();

   UnmapViewOfFile(pBuf);

   CloseHandle(hMapFile);

   return 0;
}
```



## Second Process

A second process can access the string written to the shared memory by the first process by calling the [**OpenFileMapping**](/windows/desktop/api/WinBase/nf-winbase-openfilemappinga) function specifying the same name for the mapping object as the first process. Then it can use the [**MapViewOfFile**](https://www.bing.com/search?q=**MapViewOfFile**) function to obtain a pointer to the file view, `pBuf`. The process can display this string as it would any other string. In this example, the message box displayed contains the message "Message from first process" that was written by the first process.


```C++
#include <windows.h>
#include <stdio.h>
#include <conio.h>
#include <tchar.h>
#pragma comment(lib, "user32.lib")

#define BUF_SIZE 256
TCHAR szName[]=TEXT("Global\\MyFileMappingObject");

int _tmain()
{
   HANDLE hMapFile;
   LPCTSTR pBuf;

   hMapFile = OpenFileMapping(
                   FILE_MAP_ALL_ACCESS,   // read/write access
                   FALSE,                 // do not inherit the name
                   szName);               // name of mapping object

   if (hMapFile == NULL)
   {
      _tprintf(TEXT("Could not open file mapping object (%d).\n"),
             GetLastError());
      return 1;
   }

   pBuf = (LPTSTR) MapViewOfFile(hMapFile, // handle to map object
               FILE_MAP_ALL_ACCESS,  // read/write permission
               0,
               0,
               BUF_SIZE);

   if (pBuf == NULL)
   {
      _tprintf(TEXT("Could not map view of file (%d).\n"),
             GetLastError());

      CloseHandle(hMapFile);

      return 1;
   }

   MessageBox(NULL, pBuf, TEXT("Process2"), MB_OK);

   UnmapViewOfFile(pBuf);

   CloseHandle(hMapFile);

   return 0;
}
```



## Related topics

<dl> <dt>

[Sharing Files and Memory](sharing-files-and-memory.md)
</dt> </dl>

 

 



