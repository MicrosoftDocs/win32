---
title: NtCreateNamedPipeFile function
description: Creates and opens the server-end handle of the first instance of a specific named pipe or another instance of an existing named pipe.
ms.date: 02/27/2023
ms.topic: reference
---

# NtCreateNamedPipeFile function

Creates and opens the server-end handle of the first instance of a specific named pipe or another instance of an existing named pipe. The function returns a handle that can be used to access the pipe.

## Syntax

```C++
NTSTATUS NtCreateNamedPipeFile(
  [out]          PHANDLE            FileHandle,
  [in]           ULONG              DesiredAccess,
  [in]           POBJECT_ATTRIBUTES ObjectAttributes,
  [out]          PIO_STATUS_BLOCK   IoStatusBlock,
  [in]           ULONG              ShareAccess,
  [in]           ULONG              CreateDisposition,
  [in]           ULONG              CreateOptions,
  [in]           ULONG              NamedPipeType,
  [in]           ULONG              ReadMode,
  [in]           ULONG              CompletionMode,
  [in]           ULONG              MaximumInstances,
  [in]           ULONG              InboundQuota,
  [in]           ULONG              OutboundQuota,
  [in, optional] PLARGE_INTEGER     DefaultTimeout
);
```

## Parameters

### *FileHandle* \[out\]

Pointer to a variable that receives the file handle if the call is successful.

### *DesiredAccess* \[in\]

A bitmask of flags specifying the type of access to the file or directory that the caller requires. This set of system-defined DesiredAccess flags determines the following specific access rights for file objects.

| Flag | Description |
|--------|--------|
| DELETE | The file can be deleted. |
| FILE_READ_DATA | Data can be read from the file. |
| FILE_READ_ATTRIBUTES | FileAttributes flags, described below, can be read. |
| FILE_READ_EA | Extended attributes (EAs) associated with the file can be read. |
| READ_CONTROL | The access control list (ACL) and ownership information associated with the file can be read. |
| FILE_WRITE_DATA | Data can be written to the file. |
| FILE_WRITE_ATTRIBUTES | FileAttributes flags can be written. |
| FILE_WRITE_EA | EAs associated with the file can be written. |
| FILE_APPEND_DATA | Data can be appended to the file. |
| WRITE_DAC | The discretionary access control list (DACL) associated with the file can be written. |
| WRITE_OWNER | Ownership information associated with the file can be written. |
| SYNCHRONIZE | The caller can synchronize the completion of an I/O operation by waiting for the returned FileHandle to be set to the Signaled state. This flag must be set if the **CreateOptions** `FILE_SYNCHRONOUS_IO_ALERT` or `FILE_SYNCHRONOUS_IO_NONALERT` flag is set. |
| FILE_EXECUTE | Data can be read into memory from the file using system paging I/O. |

Alternatively, for any file object that does not represent a directory, you can specify one or more of the following generic **ACCESS_MASK** flags. The **STANDARD_RIGHTS_XXX** flags are predefined system values that are used to enforce security on system objects. You can also combine these generic flags with additional flags from the preceding table.

| Desired access to file values | Maps to DesiredAccess flags |
|--------|--------|
| GENERIC_READ | STANDARD_RIGHTS_READ, FILE_READ_DATA, FILE_READ_ATTRIBUTES, FILE_READ_EA, SYNCHRONIZE. |
| GENERIC_WRITE | STANDARD_RIGHTS_WRITE, FILE_WRITE_DATA, FILE_WRITE_ATTRIBUTES, FILE_WRITE_EA, FILE_APPEND_DATA, SYNCHRONIZE. |
| GENERIC_EXECUTE | STANDARD_RIGHTS_EXECUTE, SYNCHRONIZE, FILE_READ_ATTRIBUTES, FILE_EXECUTE. |

For directories (the `FILE_DIRECTORY_FILE` **CreateOptions** flag is set), you can specify one or more of the following **ACCESS_MASK** flags, which you can also combine with any compatible flags that were described earlier.

| Desired access to directory values | Description |
|--------|--------|
| FILE_LIST_DIRECTORY | Files in the directory can be listed. |
| FILE_TRAVERSE | The directory can be traversed; that is, it can be part of the pathname of a file. |

The `FILE_READ_DATA`, `FILE_WRITE_DATA`, `FILE_EXECUTE`, and `FILE_APPEND_DATA` **DesiredAccess** flags are incompatible with creating or opening a directory file.

### *ObjectAttributes* \[in\]

Pointer to an `OBJECT_ATTRIBUTES` structure already initialized by the **InitializeObjectAttributes** routine. If the caller is running in the system process context, this parameter can be `NULL`. Otherwise, the caller must set the `OBJ_KERNEL_HANDLE` attribute in the call to **InitializeObjectAttributes**.

Members of this structure for a file object include the following:

| Member | Value |
|--------|--------|
| ULONG Length | The number of bytes of the supplied **ObjectAttributes** data. This value must be at least `sizeof(OBJECT_ATTRIBUTES)`. |
| PUNICODE_STRING ObjectName | Pointer to a buffered Unicode string that contains the name of the file to be created or opened. This value must be a fully qualified file specification, unless it is the name of a file relative to the directory specified by RootDirectory. For example, "\Device\Floppy1\myfile.dat" or "??\B:\myfile.dat" could be the fully qualified file specification, as long as the floppy disk drive driver and overlying file system are already loaded. (Note: "??" replaces "\DosDevices" as the name of the Win32 object namespace. "\DosDevices" still works, but "??" is translated faster by the object manager.) |
| HANDLE RootDirectory | Optional handle to a directory that was obtained by a previous call to **NtCreateNamedPipeFile**. If this value is NULL, the **ObjectName** member must be a fully qualified file specification that includes the full path to the target file. If this value is non-NULL, the **ObjectName** member specifies a file name relative to this directory. |
| PSECURITY_DESCRIPTOR SecurityDescriptor | Optional security descriptor to be applied to a file. ACLs specified by such a security descriptor are only applied to the file when it is created. If the value is NULL when a file is created, the ACL placed on the file is file-system-dependent; most file systems propagate some part of such an ACL from the parent directory file combined with the caller's default ACL. |
| ULONG Attributes | A set of flags that controls the file object attributes. If the caller is running in the system process context, this parameter can be zero. Otherwise, the caller must set the `OBJ_KERNEL_HANDLE` flag. The caller can also optionally set the `OBJ_CASE_INSENSITIVE` flag, which indicates that name-lookup code should ignore the case of **ObjectName** instead of performing an exact-match search. |

### *IoStatusBlock* \[out\]

Pointer to a variable of type `IO_STATUS_BLOCK` that receives the final completion status and information about the requested operation. On return from **NtCreateNamedPipeFile**, the **Information** member of the variable contains one of the following values:

- FILE_CREATED
- FILE_OPENED
- FILE_OVERWRITTEN
- FILE_SUPERSEDED
- FILE_EXISTS
- FILE_DOES_NOT_EXIST

### *ShareAccess* \[in\]

Specifies the type of share access to the file that the caller would like, as zero, or one, or a combination of the following flags. To request exclusive access, set this parameter to zero. To help you avoid sharing violation errors, specify all the following share access flags.

| ShareAccess flags | Description |
|--------|--------|
| FILE_SHARE_READ | The file can be opened for read access by other threads' file create calls. |
| FILE_SHARE_WRITE | The file can be opened for write access by other threads' file create calls. |
| FILE_SHARE_DELETE | The file can be opened for delete access by other threads' file create calls. |

Device drivers and intermediate drivers usually set ShareAccess to zero, which gives the caller exclusive access to the open file.

### *CreateDisposition* \[in\]

Value that determines how the file should be handled when the file already exists. **CreateDisposition** can be one of the following:

| Value | Description |
|--------|--------|
| FILE_SUPERSEDE | If the file already exists, replace it with the given file. If it does not exist, create the given file. |
| FILE_CREATE | If the file already exists, fail the request and do not create or open the given file. If it does not exist, create the given file. |
| FILE_OPEN | If the file already exists, open it instead of creating a new file. If it does not exist, fail the request and do not create a new file. |
| FILE_OPEN_IF | If the file already exists, open it. If it does not exist, create the given file. |
| FILE_OVERWRITE | If the file already exists, open it and overwrite it. If it does not exist, fail the request. |
| FILE_OVERWRITE_IF | If the file already exists, open it and overwrite it. If it does not exist, create the given file. |

### *CreateOptions* \[in\]

Specifies the options to be applied when creating or opening the file, as a compatible combination of the following flags.

| CreateOptions flag | Description |
|--------|--------|
| FILE_DIRECTORY_FILE (0x00000001) | The file being created or opened is a directory file. With this flag, the Disposition parameter must be set to one of `FILE_CREATE`, `FILE_OPEN`, or `FILE_OPEN_IF`. **CreateOptions** flags that are compatible with this flag are as follows: `FILE_SYNCHRONOUS_IO_ALERT`, `FILE_SYNCHRONOUS_IO_NONALERT`, `FILE_WRITE_THROUGH`, `FILE_OPEN_FOR_BACKUP_INTENT`, and `FILE_OPEN_BY_FILE_ID`. |
| FILE_WRITE_THROUGH (0x00000002) | System services, file systems, and drivers that write data to the file must actually transfer the data into the file before any requested write operation is considered complete. |
| FILE_SEQUENTIAL_ONLY (0x00000004) | All accesses to the file will be sequential. |
| FILE_NO_INTERMEDIATE_BUFFERING (0x00000008) | The file cannot be cached or buffered in a driver's internal buffers. This flag is incompatible with the **DesiredAccess** `FILE_APPEND_DATA` flag. |
| FILE_SYNCHRONOUS_IO_ALERT (0x00000010) | All operations on the file are performed synchronously. Any wait on behalf of the caller is subject to premature termination from alerts. This flag also causes the I/O system to maintain the file position context. If this flag is set, the **DesiredAccess** `SYNCHRONIZE` flag also must be set so that the I/O Manager uses the file object as a synchronization object. |
| FILE_SYNCHRONOUS_IO_NONALERT (0x00000020) | All operations on the file are performed synchronously. Waits in the system to synchronize I/O queuing and completion are not subject to alerts. This flag also causes the I/O system to maintain the file position context. If this flag is set, the **DesiredAccess** `SYNCHRONIZE` flag also must be set so that the I/O Manager uses the file object as a synchronization object. |
| FILE_NON_DIRECTORY_FILE (0x00000040) | The file being opened must not be a directory file or this call fails. The file object being opened can represent a data file; a logical, virtual, or physical device; or a volume. |
| FILE_CREATE_TREE_CONNECTION (0x00000080) | Create a tree connection for this file in order to open it over the network. |
| FILE_COMPLETE_IF_OPLOCKED (0x00000100) | Complete this operation immediately with an alternate success code if the target file is oplocked, rather than blocking the caller's thread. If the file is oplocked, another caller already has access to the file over the network. |
| FILE_NO_EA_KNOWLEDGE (0x00000200) | If the extended attributes on an existing file being opened indicate that the caller must understand extended attributes to properly interpret the file, fail this request because the caller does not understand how to deal with extended attributes. |
| FILE_OPEN_REMOTE_INSTANCE (0x00000400) | Reserved for system use; do not use. |
| FILE_RANDOM_ACCESS (0x00000800) | Accesses to the file can be random, so no sequential read-ahead operations should be performed on the file by file systems or the operating system. |
| FILE_DELETE_ON_CLOSE (0x00001000) | Delete the file when the last handle to it is passed to **FltClose**. |
| FILE_OPEN_BY_FILE_ID (0x00002000) | The file is being opened by ID. The file name contains the name of a device and a 64-bit ID to be used to open the file. |
| FILE_OPEN_FOR_BACKUP_INTENT (0x000004000) | The file is being opened for backup intent; therefore, the system should check for certain access rights and grant the caller the appropriate accesses to the file before checking the input DesiredAccess against the file's security descriptor. |
| FILE_NO_COMPRESSION (0x00008000) | Suppress inheritance of `FILE_ATTRIBUTE_COMPRESSED` from the parent directory. This allows creation of a non-compressed file in a directory that is marked compressed. |
| FILE_OPEN_REQUIRING_OPLOCK (0x00010000) | The file is being opened and an opportunistic lock (oplock) on the file is being requested as a single atomic operation. The file system checks for oplocks before it performs the create operation, and the create operation will fail with a return code of `STATUS_CANNOT_BREAK_OPLOCK` if the create operation would break an existing oplock. This flag is available in Windows 7, Windows Server 2008 R2 and later Windows operating systems. |
| FILE_DISALLOW_EXCLUSIVE (0x00020000) | When opening an existing file, if `FILE_SHARE_READ` is not specified and file system access checks would not grant the caller write access to the file, fail this open with `STATUS_ACCESS_DENIED`. This was default behavior prior to Windows 7. |
| FILE_SESSION_AWARE (0x00040000) | The file or device is being opened with session awareness. If this flag is not specified, then per-session devices (such as a device using RemoteFX USB Redirection) cannot be opened by processes running in session 0. This flag has no effect for callers not in session 0. This flag is supported only on server editions of Windows. This flag is not supported before Windows Server 2012. |
| FILE_RESERVE_OPFILTER (0x00100000) | This flag allows an application to request a filter opportunistic lock (oplock) to prevent other applications from getting share violations. If there are already open handles, the create request will fail with `STATUS_OPLOCK_NOT_GRANTED`. |
| FILE_OPEN_REPARSE_POINT (0x00200000) | Open a file with a reparse point and bypass normal reparse point processing for the file. For more information, see the following Remarks section. |
| FILE_OPEN_NO_RECALL (0x00400000) | Instructs any filters that perform offline storage or virtualization to not recall the contents of the file as a result of this open. |
| FILE_OPEN_FOR_FREE_SPACE_QUERY (0x00800000) | This flag instructs the file system to capture the user associated with the calling thread. Any subsequent calls to **FltQueryVolumeInformation** or **ZwQueryVolumeInformationFile** using the returned handle will assume the captured user, rather than the calling user at the time, for purposes of computing the free space available to the caller. This applies to the following **FsInformationClass** values: `FileFsSizeInformation`, `FileFsFullSizeInformation`, and `FileFsFullSizeInformationEx`. |

### *NamedPipeType* \[in\]

Type of named pipe to create (byte-type or message-type).

### *ReadMode* \[in\]

Mode in which to read the pipe (byte-type or message-type).

### *CompletionMode* \[in\]

Specifies how the operation is to be completed.

### *MaximumInstances* \[in\]

Maximum number of simultaneous instances of the named pipe.

### *InboundQuota* \[in\]

Specifies the pool quota that is reserved for writes to the inbound side of the named pipe.

### *OutboundQuota* \[in\]

Specifies the pool quota that is reserved for writes to the inbound side of the named pipe.

### *DefaultTimeout* \[in, optional\]

An optional pointer to a timeout value that is used if a timeout value is not specified when waiting for an instance of a named pipe.

## Returns

The function value is the final status of the create/open operation.

## Remarks

To create an instance of a named pipe, the user must have **FILE_CREATE_PIPE_INSTANCE** access to the named pipe object. If a new named pipe is being created, the access control list (ACL) from the security attributes parameter defines the discretionary access control for the named pipe.

All instances of a named pipe must specify the same pipe type (byte-type or message-type), pipe access (duplex, inbound, or outbound), instance count, and time-out value. If different values are used, this function fails and [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns **ERROR_ACCESS_DENIED**.

 A client process connects to a named pipe by using the [CreateFile](/windows/win32/api/fileapi/nf-fileapi-createfilea) or [CallNamedPipe](/windows/win32/api/winbase/nf-winbase-callnamedpipea) function. The client side of a named pipe starts out in byte mode, even if the server side is in message mode. To avoid problems receiving data, set the client side to message mode as well. To change the mode of the pipe, the pipe client must open a read-only pipe with **GENERIC_READ** and **FILE_WRITE_ATTRIBUTES** access.

The pipe server should not perform a blocking read operation until the pipe client has started. Otherwise, a race condition can occur. This typically occurs when initialization code, such as the C run-time, needs to lock and examine inherited handles.

Every time a named pipe is created, the system creates the inbound and/or outbound buffers using nonpaged pool, which is the physical memory used by the kernel. The number of pipe instances (as well as objects such as threads and processes) that you can create is limited by the available nonpaged pool. Each read or write request requires space in the buffer for the read or write data, plus additional space for the internal data structures.

The input and output buffer sizes are advisory. The actual buffer size reserved for each end of the named pipe is either the system default, the system minimum or maximum, or the specified size rounded up to the next allocation boundary. The buffer size specified should be small enough that your process will not run out of nonpaged pool, but large enough to accommodate typical requests.

Whenever a pipe write operation occurs, the system first tries to charge the memory against the pipe write quota. If the remaining pipe write quota is enough to fulfill the request, the write operation completes immediately. If the remaining pipe write quota is too small to fulfill the request, the system will try to expand the buffers to accommodate the data using nonpaged pool reserved for the process. The write operation will block until the data is read from the pipe so that the additional buffer quota can be released. Therefore, if your specified buffer size is too small, the system will grow the buffer as needed, but the downside is that the operation will block. If the operation is overlapped, a system thread is blocked; otherwise, the application thread is blocked.

To free resources used by a named pipe, the application should always close handles when they are no longer needed, which is accomplished either by calling the [CloseHandle](/windows/win32/api/handleapi/nf-handleapi-closehandle) function or when the process associated with the instance handles ends. Note that an instance of a named pipe may have more than one handle associated with it. An instance of a named pipe is always deleted when the last handle to the instance of the named pipe is closed.

## Requirements

| Requirement | Value |
|--------|--------|
| Header | ntioapi.h |
| Library | ntdll.lib |
