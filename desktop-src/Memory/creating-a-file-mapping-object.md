---
description: The first step in mapping a file is to open the file by calling the CreateFile function.
ms.assetid: e00d8742-b717-419c-902c-9a286d75d8aa
title: Creating a File Mapping Object
ms.topic: article
ms.date: 05/31/2018
---

# Creating a File Mapping Object

The first step in mapping a file is to open the file by calling the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function. To ensure that other processes cannot write to the portion of the file that is mapped, you should open the file with exclusive access. In addition, the file handle should remain open until the process no longer needs the file mapping object. An easy way to obtain exclusive access is to specify zero in the *fdwShareMode* parameter of **CreateFile**. The handle returned by **CreateFile** is used by the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function to create a file mapping object.

The [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function returns a handle to the file mapping object. This handle will be used when [creating a file view](creating-a-file-view.md) so that you can access the shared memory. When you call **CreateFileMapping**, you specify an object name, the number of bytes to be mapped from the file, and the read/write permission for the mapped memory. The first process that calls **CreateFileMapping** creates the file mapping object. Processes calling **CreateFileMapping** for an existing object receive a handle to the existing object. You can tell whether or not a successful call to **CreateFileMapping** created or opened the file mapping object by calling the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function. **GetLastError** returns **NO\_ERROR** to the creating process and **ERROR\_ALREADY\_EXISTS** to subsequent processes.

The [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function fails if the access flags conflict with those specified when the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function opened the file. For example, to read and write to the file:

-   Specify the **GENERIC\_READ** and **GENERIC\_WRITE** values in the *fdwAccess* parameter of [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea).
-   Specify the **PAGE\_READWRITE** value in the *fdwProtect* parameter of [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga).

Creating a file mapping object does not commit physical memory, it only reserves it.

## File Mapping Size

The size of the file mapping object is independent of the size of the file being mapped. However, if the file mapping object is larger than the file, the system expands the file before [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) returns. If the file mapping object is smaller than the file, the system maps only the specified number of bytes from the file.

The *dwMaximumSizeHigh* and *dwMaximumSizeLow* parameters of [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) allow you to specify the number of bytes to be mapped from the file:

-   When you do not want the size of the file to change (for example, when mapping read-only files), call [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) and specify zero for both *dwMaximumSizeHigh* and *dwMaximumSizeLow*. Doing this creates a file mapping object that is exactly the same size as the file. Otherwise, you must calculate or estimate the size of the finished file because file mapping objects are static in size; once created, their size cannot be increased or decreased. An attempt to map a file with a length of zero in this manner fails with an error code of **ERROR\_FILE\_INVALID**. Programs should test for files with a length of zero and reject such files.

-   The size of a file mapping object that is backed by a named file is limited by disk space. The size of a file view is limited to the largest available contiguous block of unreserved virtual memory. This is at most 2 GB minus the virtual memory already reserved by the process.

The size of the file mapping object that you select controls how far into the file you can "see" with memory mapping. If you create a file mapping object that is 500 Kb in size, you have access only to the first 500 Kb of the file, regardless of the size of the file. Since it does not cost you any system resources to create a larger file mapping object, create a file mapping object that is the size of the file (set the *dwMaximumSizeHigh* and *dwMaximumSizeLow* parameters of [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) both to zero) even if you do not expect to view the entire file. The cost in system resources comes in creating the views and accessing them.

If you want to view a portion of the file that does not start at the beginning of the file, you must create a file mapping object. This object is the size of the portion of the file that you want to view plus the offset into the file.

## Related topics

<dl> <dt>

[Creating a View Within a File](creating-a-view-within-a-file.md)
</dt> </dl>

 

 
