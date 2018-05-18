---
Description: 'An application can change the current directory by calling the SetCurrentDirectory function.'
ms.assetid: 'b08e7739-55d4-4690-9ce5-2a8cb29214e9'
title: Changing the Current Directory
---

# Changing the Current Directory

The directory at the end of the active path is called the current directory; it is the directory in which the active application started, unless it has been explicitly changed. An application can determine which directory is current by calling the [**GetCurrentDirectory**](getcurrentdirectory.md) function. It is sometimes necessary to use the [**GetFullPathName**](getfullpathname.md) function to ensure the drive letter is included if the application requires it.

> [!Note]  
> Although each process can have only one current directory, if the application switches volumes by using the [**SetCurrentDirectory**](setcurrentdirectory.md) function, the system remembers the last current path for each volume (drive letter). This behavior will manifest itself only when specifying a drive letter without a fully qualified path when changing the current directory point of reference to a different volume. This applies to either Get or Set operations.

 

An application can change the current directory by calling the [**SetCurrentDirectory**](setcurrentdirectory.md) function.

The following example demonstrates the use of [**GetCurrentDirectory**](getcurrentdirectory.md) and [**SetCurrentDirectory**](setcurrentdirectory.md).


```C++
#include <windows.h> 
#include <stdio.h>
#include <tchar.h>

#define BUFSIZE MAX_PATH
 
void _tmain(int argc, TCHAR **argv) 
{ 
   TCHAR Buffer[BUFSIZE];
   DWORD dwRet;

   if(argc != 2)
   {
      _tprintf(TEXT("Usage: %s <dir>\n"), argv[0]);
      return;
   }

   dwRet = GetCurrentDirectory(BUFSIZE, Buffer);

   if( dwRet == 0 )
   {
      printf("GetCurrentDirectory failed (%d)\n", GetLastError());
      return;
   }
   if(dwRet > BUFSIZE)
   {
      printf("Buffer too small; need %d characters\n", dwRet);
      return;
   }

   if( !SetCurrentDirectory(argv[1]))
   {
      printf("SetCurrentDirectory failed (%d)\n", GetLastError());
      return;
   }
   _tprintf(TEXT("Set current directory to %s\n"), argv[1]);

   if( !SetCurrentDirectory(Buffer) )
   {
      printf("SetCurrentDirectory failed (%d)\n", GetLastError());
      return;
   }
   _tprintf(TEXT("Restored previous directory (%s)\n"), Buffer);
}
```



 

 



