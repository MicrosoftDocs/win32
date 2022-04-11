---
description: Considerations for creating or opening a file by using the CreateFile function.
ms.assetid: 094cac29-c66d-409e-8928-878dc693d393
title: Creating and Opening Files
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Opening Files

The [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function can create a new file or open an existing file. You must specify the file name, creation instructions, and other attributes. When an application creates a new file, the operating system adds it to the specified directory.

The operating system assigns a unique identifier, called a *handle*, to each file that is opened or created using [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea). An application can use this handle with functions that read from, write to, and describe the file. It is valid until all references to that handle are closed. When an application starts, it inherits all open handles from the process that started it if the handles were created as inheritable.

An application should check the value of the handle returned by [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) before attempting to use the handle to access the file. If an error occurs, the handle value will be **INVALID\_HANDLE\_VALUE** and the application can use the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function for extended error information.

When an application uses [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea), it must use the *dwDesiredAccess* parameter to specify whether it intends to read from the file, write to the file, both read and write, or neither. This is known as requesting an *access mode*. The application must also use the *dwCreationDisposition* parameter to specify what action to take if the file already exists, known as the *creation disposition*. For example, an application can call **CreateFile** with *dwCreationDisposition* set to **CREATE\_ALWAYS** to always create a new file, even if a file of the same name already exists (thus overwriting the existing file). Whether this succeeds or not depends on factors such as the previous file's attributes and security settings (see the following sections for more information).

An application also uses [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) to specify whether it wants to share the file for reading, writing, both, or neither. This is known as the *sharing mode*. An open file that is not shared (*dwShareMode* set to zero) cannot be opened again, either by the application that opened it or by another application, until its handle has been closed. This is also referred to as exclusive access.

When a process uses [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) to attempt to open a file that has already been opened in a sharing mode (*dwShareMode* set to a valid nonzero value), the system compares the requested access and sharing modes to those specified when the file was opened. If you specify an access or sharing mode that conflicts with the modes specified in the previous call, **CreateFile** fails.

The following table illustrates the valid combinations of two calls to [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) using various access modes and sharing modes (*dwDesiredAccess*, *dwShareMode* respectively). It does not matter in which order the **CreateFile** calls are made. However, any subsequent file I/O operations on each file handle will still be constrained by the current access and sharing modes associated with that particular file handle.




| First call to <a href="/windows/desktop/api/FileAPI/nf-fileapi-createfilea"><strong>CreateFile</strong></a> | Valid second calls to <a href="/windows/desktop/api/FileAPI/nf-fileapi-createfilea"><strong>CreateFile</strong></a> | 
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| <strong>GENERIC_READ</strong>, <strong>FILE_SHARE_READ</strong><br /> | <ul><li><strong>GENERIC_READ</strong>, <strong>FILE_SHARE_READ</strong></li><li><strong>GENERIC_READ</strong>, <strong>FILE_SHARE_READ</strong> <strong>FILE_SHARE_WRITE</strong></li></ul> | 
| <strong>GENERIC_READ</strong>, <strong>FILE_SHARE_WRITE</strong><br /> | <ul><li><strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong></li><li><strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong> <strong>FILE_SHARE_WRITE</strong></li></ul> | 
| <strong>GENERIC_READ</strong>, <strong>FILE_SHARE_READ</strong> | <strong>FILE_SHARE_WRITE</strong><br /> <ul><li><strong>GENERIC_READ</strong>, <strong>FILE_SHARE_READ</strong></li><li><strong>GENERIC_READ</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li><li><strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong></li><li><strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li><li><strong>GENERIC_READ</strong> <strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong></li><li><strong>GENERIC_READ</strong> <strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li></ul> | 
| <strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong><br /> |<ul><li><strong>GENERIC_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li><li><strong>GENERIC_READ</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li></ul> | 
| <strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_WRITE</strong><br /> | <ul><li><strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_WRITE</strong></li><li><strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li></ul> | 
| <strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong> | <strong>FILE_SHARE_WRITE</strong><br /> <ul><li><strong>GENERIC_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li><li><strong>GENERIC_READ</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li><li><strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_WRITE</strong></li><li><strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li><li><strong>GENERIC_READ</strong>, <strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_WRITE</strong></li><li><strong>GENERIC_READ</strong>, <strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li></ul> | 
| <strong>GENERIC_READ</strong>, <strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong><br /> | <ul><li><strong>GENERIC_READ</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li></ul> | 
| <strong>GENERIC_READ</strong>, <strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_WRITE</strong><br /> | <ul><li><strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li></ul> | 
| <strong>GENERIC_READ</strong>, <strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong><br /> | <ul><li><strong>GENERIC_READ</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li><li><strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li><li><strong>GENERIC_READ</strong>, <strong>GENERIC_WRITE</strong>, <strong>FILE_SHARE_READ</strong>, <strong>FILE_SHARE_WRITE</strong></li></ul> | 




 

In addition to the standard file attributes, you can also specify security attributes by including a pointer to a [**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure as the fourth parameter of [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea). However, the underlying file system must support security for this to have any effect (for example, the NTFS file system supports it but the various FAT file systems do not). For more information about security attributes, see [Access Control](/windows/desktop/SecAuthZ/access-control).

An application creating a new file can supply an optional handle to a template file, from which [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) takes file attributes and extended attributes for creation of the new file.

## CreateFile Scenarios

There are several fundamental scenarios for initiating access to a file using the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function. These are summarized as:

-   Creating a new file when a file with that name does not already exist.
-   Creating a new file even if a file of the same name already exists, clearing its data and starting empty.
-   Opening an existing file only if it exists, and only intact.
-   Opening an existing file only if it exists, truncating it to be empty.
-   Opening a file always: as-is if it exists, creating a new one if it does not exist.

These scenarios are controlled by the proper use of the *dwCreationDisposition* parameter. Below is a breakdown of how these scenarios map to values for this parameter and what happens when they are used.

When creating or opening a new file when a file with that name does not already exist (*dwCreationDisposition* set to either **CREATE\_NEW**, **CREATE\_ALWAYS**, or **OPEN\_ALWAYS**), the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function performs the following actions:

-   Combines the file attributes and flags specified by *dwFlagsAndAttributes* with **FILE\_ATTRIBUTE\_ARCHIVE**.
-   Sets the file length to zero.
-   Copies the extended attributes supplied by the template file to the new file if the *hTemplateFile* parameter is specified (this overrides all **FILE\_ATTRIBUTE\_\*** flags specified earlier).
-   Sets the inherit flag specified by the **bInheritHandle** member and the security descriptor specified by the **lpSecurityDescriptor** member of the *lpSecurityAttributes* parameter ([**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure), if supplied.

When creating a new file even if a file of the same name already exists (*dwCreationDisposition* set to **CREATE\_ALWAYS**), the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function performs the following actions:

-   Checks current file attributes and security settings for write access, failing if denied.
-   Combines the file attributes and flags specified by *dwFlagsAndAttributes* with **FILE\_ATTRIBUTE\_ARCHIVE** and the existing file attributes.
-   Sets the file length to zero (that is, any data that was in the file is no longer available and the file is empty).
-   Copies the extended attributes supplied by the template file to the new file if the *hTemplateFile* parameter is specified (this overrides all **FILE\_ATTRIBUTE\_\*** flags specified earlier).
-   Sets the inherit flag specified by the **bInheritHandle** member of the *lpSecurityAttributes* parameter ([**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure) if supplied, but ignores the **lpSecurityDescriptor** member of the **SECURITY\_ATTRIBUTES** structure.
-   If otherwise successful (that is, [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) returns a valid handle), calling [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) will yield the code **ERROR\_ALREADY\_EXISTS**, even though for this particular use-case it is not actually an error as such (if you intended to create a "new" (empty) file in place of the existing one).

When opening an existing file (*dwCreationDisposition* set to either **OPEN\_EXISTING**, **OPEN\_ALWAYS**, or **TRUNCATE\_EXISTING**), the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function performs the following actions:

-   Checks current file attributes and security settings for requested access, failing if denied.
-   Combines the file flags (**FILE\_FLAG\_\***) specified by *dwFlagsAndAttributes* with existing file attributes, and ignores any file attributes (**FILE\_ATTRIBUTE\_\***) specified by *dwFlagsAndAttributes*.
-   Sets the file length to zero only if *dwCreationDisposition* is set to **TRUNCATE\_EXISTING**, otherwise the current file length is maintained and the file is opened as-is.
-   Ignores the *hTemplateFile* parameter.
-   Sets the inherit flag specified by the **bInheritHandle** member of the *lpSecurityAttributes* parameter ([**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure) if supplied, but ignores the **lpSecurityDescriptor** member of the **SECURITY\_ATTRIBUTES** structure.

## File Attributes and Directories

File attributes are part of the metadata associated with a file or directory, each with its own purpose and rules on how it can be set and changed. Some of these attributes apply only to files, and some only to directories. For example, the **FILE\_ATTRIBUTE\_DIRECTORY** attribute applies only to directories: It is used by the file system to determine whether an object on disk is a directory, but it cannot be changed for an existing file system object.

Some file attributes can be set for a directory but have meaning only for files created in that directory, acting as default attributes. For example, **FILE\_ATTRIBUTE\_COMPRESSED** can be set on a directory object, but because the directory object itself contains no actual data, it is not truly compressed; however, directories marked with this attribute tell the file system to compress any new files added to that directory. Any file attribute that can be set on a directory and will also be set for new files added to that directory is referred to as an *inherited attribute*.

The [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function provides a parameter for setting certain file attributes when a file is created. In general, these attributes are the most common for an application to use at file creation time, but not all possible file attributes are available to **CreateFile**. Some file attributes require the use of other functions, such as [**SetFileAttributes**](/windows/desktop/api/FileAPI/nf-fileapi-setfileattributesa), [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol), or [**DecryptFile**](/windows/desktop/api/WinBase/nf-winbase-decryptfilea) after the file already exists. In the case of **FILE\_ATTRIBUTE\_DIRECTORY**, the [**CreateDirectory**](/windows/desktop/api/FileAPI/nf-fileapi-createdirectorya) function is required at creation time because **CreateFile** cannot create directories. The other file attributes that require special handling are **FILE\_ATTRIBUTE\_REPARSE\_POINT** and **FILE\_ATTRIBUTE\_SPARSE\_FILE**, which require **DeviceIoControl**. For more information, see [**SetFileAttributes**](/windows/desktop/api/FileAPI/nf-fileapi-setfileattributesa).

As stated previously, file attribute inheritance occurs when a file is created with file attributes read from the directory attributes where the file will be located. The following table summarizes these inherited attributes and how they relate to [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) capabilities.



| Directory attribute state                                      | [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) inheritance override capability for new files      |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------|
| **FILE\_ATTRIBUTE\_COMPRESSED** set.<br/>                | No control. Use [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) to clear.<br/>    |
| **FILE\_ATTRIBUTE\_COMPRESSED** not set.<br/>            | No control. Use [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) to set.<br/>      |
| **FILE\_ATTRIBUTE\_ENCRYPTED** set.<br/>                 | No control. Use [**DecryptFile**](/windows/desktop/api/WinBase/nf-winbase-decryptfilea).<br/>                      |
| **FILE\_ATTRIBUTE\_ENCRYPTED** not set.<br/>             | Can be set using [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea).<br/>                       |
| **FILE\_ATTRIBUTE\_NOT\_CONTENT\_INDEXED** set.<br/>     | No control. Use [**SetFileAttributes**](/windows/desktop/api/FileAPI/nf-fileapi-setfileattributesa) to clear.<br/> |
| **FILE\_ATTRIBUTE\_NOT\_CONTENT\_INDEXED** not set.<br/> | No control. Use [**SetFileAttributes**](/windows/desktop/api/FileAPI/nf-fileapi-setfileattributesa) to set.<br/>   |



 

## Related topics

<dl> <dt>

[Access Control](/windows/desktop/SecAuthZ/access-control)
</dt> <dt>

[**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea)
</dt> <dt>

[**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol)
</dt> <dt>

[**File Attribute Constants**](file-attribute-constants.md)
</dt> <dt>

[File Compression and Decompression](file-compression-and-decompression.md)
</dt> <dt>

[File Encryption](file-encryption.md)
</dt> <dt>

[File Management Functions](file-management-functions.md)
</dt> <dt>

[Handles and Objects](/windows/desktop/SysInfo/handles-and-objects)
</dt> <dt>

[Handle Inheritance](/windows/desktop/SysInfo/handle-inheritance)
</dt> <dt>

[Opening a File for Reading or Writing](opening-a-file-for-reading-or-writing.md)
</dt> <dt>

[**SetFileAttributes**](/windows/desktop/api/FileAPI/nf-fileapi-setfileattributesa)
</dt> </dl>

 

