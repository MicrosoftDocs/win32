---
description: To read from a file view, dereference the pointer returned by the MapViewOfFile function as shown in the examples below.
ms.assetid: c2a3da09-d116-4c2c-9e6c-ec9e80c88b99
title: Reading and Writing From a File View
ms.topic: article
ms.date: 05/31/2018
---

# Reading and Writing From a File View

To read from a file view, dereference the pointer returned by the [**MapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile) function as shown in the examples below.

Reading from or writing to a file view of a file other than the page file can cause an **EXCEPTION\_IN\_PAGE\_ERROR** exception. For example, accessing a mapped file that resides on a remote server can generate an exception if the connection to the server is lost. Exceptions can also occur because of a full disk, an underlying device failure, or a memory allocation failure. When writing to a file view, exceptions can also occur because the file is shared and a different process has locked a byte range. To guard against exceptions due to input and output (I/O) errors, all attempts to access memory mapped files should be wrapped in structured exception handlers. When you receive **EXCEPTION\_IN\_PAGE\_ERROR** in your **\_\_except** filter, make sure that the address is within the mapping you are currently accessing. If so, recover or fail gracefully; otherwise, do not handle the exception.

The following example uses the pointer returned by **MapViewOfFile** to read from the file view:


```C++
  DWORD dwLength;

  __try
  {
    dwLength = *((LPDWORD) lpMapAddress);
  }
  __except(GetExceptionCode()==EXCEPTION_IN_PAGE_ERROR ?
    EXCEPTION_EXECUTE_HANDLER : EXCEPTION_CONTINUE_SEARCH)
  {
    // Failed to read from the view.
  }
```



The following example uses the pointer returned by **MapViewOfFile** to write to the file view:


```C++
  DWORD dwLength;

  __try
  {
    *((LPDWORD) lpMapAddress) = dwLength;
  }
  __except (GetExceptionCode() == EXCEPTION_IN_PAGE_ERROR ? 
    EXCEPTION_EXECUTE_HANDLER : EXCEPTION_CONTINUE_SEARCH)
  {
    // Failed to write to the view.
  }
```



The [**FlushViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-flushviewoffile) function copies the specified number of bytes of the file view to the physical file, without waiting for the cached write operation to occur:


```C++
  if (!FlushViewOfFile(lpMapAddress, dwBytesToFlush)) 
  {
    printf("Could not flush memory to disk (%d).\n", GetLastError()); 
  }
```



If you are mapping a compressed or sparse file on an NTFS partition, there is additional potential for an I/O error when paging in a portion of the file. In this case, the address space mapped by [**MapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile) may not be backed by allocated disk space. This is because a sparse file can have regions of zeros for which NTFS does not allocate disk space, and a compressed file can take up less disk space than the actual data that it represents. If you read from or write to a portion of a sparse or compressed file that is not backed by disk space, the operating system may try to allocate disk space. If the disk is full, this can result in an exception indicating an I/O error.

## Related topics

<dl> <dt>

[Structured Exception Handling](../debug/structured-exception-handling.md)
</dt> </dl>

 

 
