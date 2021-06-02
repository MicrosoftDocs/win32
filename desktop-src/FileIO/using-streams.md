---
description: Example code that shows how to use basic NTFS file system streams.
ms.assetid: 9cd5f418-404c-40f5-aa51-ef4d2a5f238e
title: Using Streams
ms.topic: article
ms.date: 05/31/2018
---

# Using Streams

The example in this topic demonstrates how to use basic NTFS file system streams.

This example creates a file, called "TestFile," with a size of 16 bytes. However, the file also has an additional ::$DATA stream type, named "Stream" which adds an additional 23 bytes that is not reported by the operating system. Therefore, when you view the file size property for the file, you see only the size of default ::$DATA stream for the file.


```C++
#include <windows.h>
#include <stdio.h>

void main( )
 {
  HANDLE hFile, hStream;
  DWORD dwRet;

  hFile = CreateFile( TEXT("TestFile"), // Filename
                      GENERIC_WRITE,    // Desired access
                      FILE_SHARE_WRITE, // Share flags
                      NULL,             // Security Attributes
                      OPEN_ALWAYS,      // Creation Disposition
                      0,                // Flags and Attributes
                      NULL );           // OVERLAPPED pointer
  if( hFile == INVALID_HANDLE_VALUE )
   {
    printf( "Cannot open TestFile\n" );
    return;
   }
  else
   {
    WriteFile( hFile,              // Handle
               "This is TestFile", // Data to be written
               16,                 // Size of data, in bytes
               &dwRet,             // Number of bytes written
               NULL );             // OVERLAPPED pointer
    CloseHandle( hFile );
    hFile = INVALID_HANDLE_VALUE;
   }

  hStream = CreateFile( TEXT("TestFile:Stream"), // Filename
                        GENERIC_WRITE,           // Desired access
                        FILE_SHARE_WRITE,        // Share flags
                        NULL,                    // Security Attributes
                        OPEN_ALWAYS,             // Creation Disposition
                        0,                       // Flags and Attributes
                        NULL );                  // OVERLAPPED pointer
  if( hStream == INVALID_HANDLE_VALUE )
    printf( "Cannot open TestFile:Stream\n" );
  else
   {
    WriteFile( hStream,                   // Handle
               "This is TestFile:Stream", // Data to be written
               23,                        // Size of data
               &dwRet,                    // Number of bytes written
               NULL);                     // OVERLAPPED pointer
    CloseHandle( hStream );
    hStream = INVALID_HANDLE_VALUE;
   }
}
```



If you type **Type TestFile** at a command prompt, it displays the following output:

``` syntax
This is TestFile
```

However, if you type the words **Type TestFile:Stream**, it generates the following error:

"The filename, directory name, or volume label syntax is incorrect."

To view what is in TestFile:stream, use one of the following commands:

**More < TestFile:Stream**

**More < TestFile:Stream:$DATA**

The text displayed is as follows:

``` syntax
This is TestFile:Stream
```

## Related topics

<dl> <dt>

[File Streams](file-streams.md)
</dt> </dl>

 

 



