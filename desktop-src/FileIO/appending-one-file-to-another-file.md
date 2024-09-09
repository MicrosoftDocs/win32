---
description: Example code that shows how an application can append one file to the end of another file, including how to open and close files, read and write to files, and lock and unlock files.
ms.assetid: e4d1f842-16a1-47e4-84b4-9bb44aaa1dc5
title: Appending One File to Another File
ms.topic: article
ms.date: 05/31/2018
---

# Appending One File to Another File

The code example in this topic shows you how to open and close files, read and write to files, and lock and unlock files.

In the example, the application appends one file to the end of another file. First, the application opens the file being appended with permissions that allow only the application to write to it. However, during the append process other processes can open the file with read-only permission, which provides a snapshot view of the file being appended. Then, the file is locked during the actual append process to ensure the integrity of the data being written to the file.

This example does not use transactions. If you were using transacted operations, you would only be able have read-only access. In this case, you would only see the appended data after the transaction commit operation completed.

The example also shows that the application opens two files by using [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea):

-   One.txt is opened for reading.
-   Two.txt is opened for writing and shared reading.

Then the application uses [**ReadFile**](/windows/desktop/api/FileAPI/nf-fileapi-readfile) and [**WriteFile**](/windows/desktop/api/FileAPI/nf-fileapi-writefile) to append the contents of One.txt to the end of Two.txt by reading and writing the 4 KB blocks. However, before writing to the second file, the application uses [**SetFilePointer**](/windows/desktop/api/FileAPI/nf-fileapi-setfilepointer) to set the pointer of the second file to the end of that file, and uses [**LockFile**](/windows/desktop/api/FileAPI/nf-fileapi-lockfile) to lock the area to be written. This prevents another thread or process with a duplicate handle from accessing the area while the write operation is in progress. When each write operation is complete, [**UnlockFile**](/windows/desktop/api/FileAPI/nf-fileapi-unlockfile) is used to unlock the locked area.


```C++
#include <windows.h>
#include <stdio.h>

void main()
{
  HANDLE hFile;
  HANDLE hAppend;
  DWORD  dwBytesRead, dwBytesWritten, dwPos;
  BYTE   buff[4096];

  // Open the existing file.

  hFile = CreateFile(TEXT("one.txt"), // open One.txt
            GENERIC_READ,             // open for reading
            0,                        // do not share
            NULL,                     // no security
            OPEN_EXISTING,            // existing file only
            FILE_ATTRIBUTE_NORMAL,    // normal file
            NULL);                    // no attr. template

  if (hFile == INVALID_HANDLE_VALUE)
  {
     printf("Could not open one.txt."); 
     return;
  }

  // Open the existing file, or if the file does not exist,
  // create a new file.

  hAppend = CreateFile(TEXT("two.txt"), // open Two.txt
              FILE_APPEND_DATA | FILE_GENERIC_READ,    // open for appending and locking
              FILE_SHARE_READ,                         // allow multiple readers
              NULL,                                    // no security
              OPEN_ALWAYS,                             // open or create
              FILE_ATTRIBUTE_NORMAL,                   // normal file
              NULL);                                   // no attr. template

  if (hAppend == INVALID_HANDLE_VALUE)
  {
     printf("Could not open two.txt."); 
     return;
  }

  // Append the first file to the end of the second file.
  // Lock the second file to prevent another process from
  // accessing it while writing to it. Unlock the
  // file when writing is complete.

  while (ReadFile(hFile, buff, sizeof(buff), &dwBytesRead, NULL)
      && dwBytesRead > 0)
    {
    dwPos = SetFilePointer(hAppend, 0, NULL, FILE_END);
    if (!LockFile(hAppend, dwPos, 0, dwBytesRead, 0))
    {
       printf("Could not lock two.txt");
    }
    WriteFile(hAppend, buff, dwBytesRead, &dwBytesWritten, NULL);
    UnlockFile(hAppend, dwPos, 0, dwBytesRead, 0);
    }

  // Close both files.

  CloseHandle(hFile);
  CloseHandle(hAppend);
}
```



 

 



