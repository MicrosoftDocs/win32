---
title: NtCreateNamedPipeFile function
description: Creates an instance of a named pipe and returns a handle for subsequent pipe operations.
ms.date: 09/09/2022
ms.topic: reference
---

# NtCreateNamedPipeFile function

Creates an instance of a named pipe and returns a handle for subsequent pipe operations. A named pipe server process uses this function either to create the first instance of a specific named pipe and establish its basic attributes or to create a new instance of an existing named pipe.

> [!NOTE]
> This function is the user-mode equivalent to the [**CreateNamedPipeA**](/windows/win32/api/winbase/nf-winbase-createnamedpipea) Win32 function.

## Syntax

```C++
HANDLE NtCreateNamedPipeFile(
  [in]           LPCSTR                lpName,
  [in]           DWORD                 dwOpenMode,
  [in]           DWORD                 dwPipeMode,
  [in]           DWORD                 nMaxInstances,
  [in]           DWORD                 nOutBufferSize,
  [in]           DWORD                 nInBufferSize,
  [in]           DWORD                 nDefaultTimeOut,
  [in, optional] LPSECURITY_ATTRIBUTES lpSecurityAttributes
);
```

## Parameters

#### *lpName* \[in\]

The unique pipe name. This string must have the following form:

\\\\.\\pipe&#92;<i>pipename</i>

The pipename part of the name can include any character other than a backslash, including numbers and special characters. The entire pipe name string can be up to 256 characters long. Pipe names are not case sensitive.

#### *dwOpenMode* \[in\]

The open mode. The open mode consists of access flags (one of three values) logically ORed with a writethrough flag (one of two values) and an overlapped flag (one of two values).

The function fails if <i>dwOpenMode</i> specifies anything other than 0 or the flags listed in the following tables.

This parameter must specify one of the following pipe access modes. The same mode must be specified for each instance of the pipe.

<table>
<tr>
<th>Mode</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="PIPE_ACCESS_DUPLEX"></a><a id="pipe_access_duplex"></a><dl>
<dt><b>PIPE_ACCESS_DUPLEX</b></dt>
<dt>0x00000003</dt>
</dl>
</td>
<td width="60%">
The pipe is bi-directional; both server and client processes can read from and write to the pipe. This mode gives the server the equivalent of <b>GENERIC_READ</b> and <b>GENERIC_WRITE</b> access to the pipe. The client can specify <b>GENERIC_READ</b> or <b>GENERIC_WRITE</b>, or both, when it connects to the pipe using the 
<a href="/windows/desktop/api/fileapi/nf-fileapi-createfilea">CreateFile</a> function.

</td>
</tr>
<tr>
<td width="40%"><a id="PIPE_ACCESS_INBOUND"></a><a id="pipe_access_inbound"></a><dl>
<dt><b>PIPE_ACCESS_INBOUND</b></dt>
<dt>0x00000001</dt>
</dl>
</td>
<td width="60%">
The flow of data in the pipe goes from client to server only. This mode gives the server the equivalent of <b>GENERIC_READ</b> access to the pipe. The client must specify <b>GENERIC_WRITE</b> access when connecting to the pipe. If the client must read pipe settings by calling the <a href="/windows/desktop/api/namedpipeapi/nf-namedpipeapi-getnamedpipeinfo">GetNamedPipeInfo</a> or <a href="/windows/desktop/api/winbase/nf-winbase-getnamedpipehandlestatea">GetNamedPipeHandleState</a> functions, the client must specify <b>GENERIC_WRITE</b> and <b>FILE_READ_ATTRIBUTES</b> access when connecting to the pipe.

</td>
</tr>
<tr>
<td width="40%"><a id="PIPE_ACCESS_OUTBOUND"></a><a id="pipe_access_outbound"></a><dl>
<dt><b>PIPE_ACCESS_OUTBOUND</b></dt>
<dt>0x00000002</dt>
</dl>
</td>
<td width="60%">
The flow of data in the pipe goes from server to client only. This mode gives the server the equivalent of <b>GENERIC_WRITE</b> access to the pipe. The client must specify <b>GENERIC_READ</b> access when connecting to the pipe. If the client must change pipe settings by calling the <a href="/windows/desktop/api/namedpipeapi/nf-namedpipeapi-setnamedpipehandlestate">SetNamedPipeHandleState</a> function, the client must specify <b>GENERIC_READ</b> and <b>FILE_WRITE_ATTRIBUTES</b> access when connecting to the pipe.

</td>
</tr>
</table>
 

This parameter can also include one or more of the following flags, which enable the write-through and overlapped modes. These modes can be different for different instances of the same pipe.

<table>
<tr>
<th>Mode</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="PIPE_WRITETHROUGH"></a><a id="pipe_writethrough"></a><dl>
<dt><b>PIPE_WRITETHROUGH</b></dt>
<dt>0x80000000</dt>
</dl>
</td>
<td width="60%">
Write-through mode is enabled. This mode affects only write operations on byte-type pipes and, then, only when the client and server processes are on different computers. If this mode is enabled, the redirector is not permitted to delay the transmission of data to the named pipe buffer on the remote server. This disables a performance enhancement for applications that need synchronization with every write operation.
</td>
</tr>
<tr>
<td width="40%"><a id="FILE_FLAG_OVERLAPPED"></a><a id="file_flag_overlapped"></a><dl>
<dt><b>FILE_FLAG_OVERLAPPED</b></dt>
<dt>0x40000000</dt>
</dl>
</td>
<td width="60%">
Overlapped mode is enabled. If this mode is enabled, functions performing read, write, and connect operations that may take a significant time to be completed can return immediately. This mode enables the thread that started the operation to perform other operations while the time-consuming operation executes in the background. For example, in overlapped mode, a thread can handle simultaneous input and output (I/O) operations on multiple instances of a pipe or perform simultaneous read and write operations on the same pipe handle.
</td>
</tr>
<tr>
<td width="40%"><a id="FILE_FLAG_WRITETHROUGH"></a><a id="file_flag_writethrough"></a><dl>
<dt><b>FILE_FLAG_WRITE_THROUGH</b></dt>
<dt>0x80000000</dt>
</dl>
</td>
<td width="60%">
The intermediate buffering behavior described by FILE_FLAG_OVERLAPPED will not be permitted in this pipe.
</td>
</tr>
</table>

This parameter can include any combination of the following security access modes. These modes can be different for different instances of the same pipe.

<table>
<tr>
<th>Mode</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="WRITE_DAC"></a><a id="write_dac"></a><dl>
<dt><b>WRITE_DAC</b></dt>
<dt>0x00040000L</dt>
</dl>
</td>
<td width="60%">
The caller will have write access to the named pipe's discretionary access control list (ACL).

</td>
</tr>
<tr>
<td width="40%"><a id="WRITE_OWNER"></a><a id="write_owner"></a><dl>
<dt><b>WRITE_OWNER</b></dt>
<dt>0x00080000L</dt>
</dl>
</td>
<td width="60%">
The caller will have write access to the named pipe's owner.

</td>
</tr>
<tr>
<td width="40%"><a id="ACCESS_SYSTEM_SECURITY"></a><a id="access_system_security"></a><dl>
<dt><b>ACCESS_SYSTEM_SECURITY</b></dt>
<dt>0x01000000L</dt>
</dl>
</td>
<td width="60%">
The caller will have write access to the named pipe's SACL. For more information, see 
<a href="/windows/desktop/SecAuthZ/access-control-lists">Access-Control Lists (ACLs)</a> and 
<a href="/windows/desktop/SecAuthZ/sacl-access-right">SACL Access Right</a>.

</td>
</tr>
</table>

#### *dwPipeMode* \[in\]

The pipe mode. This parameter contains a combination of one type mode flag, one read mode flag, and one wait mode flag.


The function fails if <i>dwPipeMode</i> specifies anything other than 0 or the flags listed in the following tables.

One of the following type modes can be specified. The same type mode must be specified for each instance of the pipe.

<table>
<tr>
<th>Mode</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="PIPE_TYPE_BYTE"></a><a id="pipe_type_byte"></a><dl>
<dt><b>PIPE_TYPE_BYTE</b></dt>
<dt>0x00000000</dt>
</dl>
</td>
<td width="60%">
Data is written to the pipe as a stream of bytes. This mode cannot be used with PIPE_READMODE_MESSAGE. The pipe does not distinguish bytes written during different write operations.

</td>
</tr>
<tr>
<td width="40%"><a id="PIPE_TYPE_MESSAGE"></a><a id="pipe_type_message"></a><dl>
<dt><b>PIPE_TYPE_MESSAGE</b></dt>
<dt>0x00000004</dt>
</dl>
</td>
<td width="60%">
Data is written to the pipe as a stream of messages. The pipe treats the bytes written during each write operation as a message unit. The <a href="/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror">GetLastError</a> function returns <b>ERROR_MORE_DATA</b> when a message is not read completely. This mode can be used with either <b>PIPE_READMODE_MESSAGE</b> or <b>PIPE_READMODE_BYTE</b>.

</td>
</tr>
</table>
 

One of the following read modes can be specified. Different instances of the same pipe can specify different read modes.

<table>
<tr>
<th>Mode</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="PIPE_READMODE_BYTE"></a><a id="pipe_readmode_byte"></a><dl>
<dt><b>PIPE_READMODE_BYTE</b></dt>
<dt>0x00000000</dt>
</dl>
</td>
<td width="60%">
Data is read from the pipe as a stream of bytes. This mode can be used with either <b>PIPE_TYPE_MESSAGE</b> or <b>PIPE_TYPE_BYTE</b>.

</td>
</tr>
<tr>
<td width="40%"><a id="PIPE_READMODE_MESSAGE"></a><a id="pipe_readmode_message"></a><dl>
<dt><b>PIPE_READMODE_MESSAGE</b></dt>
<dt>0x00000002</dt>
</dl>
</td>
<td width="60%">
Data is read from the pipe as a stream of messages. This mode can be only used if <b>PIPE_TYPE_MESSAGE</b> is also specified.

</td>
</tr>
</table>
 

One of the following wait modes can be specified. Different instances of the same pipe can specify different wait modes.

<table>
<tr>
<th>Mode</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="PIPE_WAIT"></a><a id="pipe_wait"></a><dl>
<dt><b>PIPE_WAIT</b></dt>
<dt>0x00000000</dt>
</dl>
</td>
<td width="60%">
Blocking mode is enabled. When the pipe handle is specified in the 
<a href="/windows/desktop/api/fileapi/nf-fileapi-readfile">ReadFile</a>, 
<a href="/windows/desktop/api/fileapi/nf-fileapi-writefile">WriteFile</a>, or 
<a href="/windows/desktop/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe">ConnectNamedPipe</a> function, the operations are not completed until there is data to read, all data is written, or a client is connected. Use of this mode can mean waiting indefinitely in some situations for a client process to perform an action.

</td>
</tr>
<tr>
<td width="40%"><a id="PIPE_NOWAIT"></a><a id="pipe_nowait"></a><dl>
<dt><b>PIPE_NOWAIT</b></dt>
<dt>0x00000001</dt>
</dl>
</td>
<td width="60%">
Nonblocking mode is enabled. In this mode, <a href="/windows/desktop/api/fileapi/nf-fileapi-readfile">ReadFile</a>, <a href="/windows/desktop/api/fileapi/nf-fileapi-writefile">WriteFile</a>, and 
<a href="/windows/desktop/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe">ConnectNamedPipe</a> always return immediately.

Note that nonblocking mode is supported for compatibility with Microsoft LAN Manager version 2.0 and should not be used to achieve asynchronous I/O with named pipes. For more information on asynchronous pipe I/O, see 
<a href="/windows/desktop/ipc/synchronous-and-overlapped-input-and-output">Synchronous and Overlapped Input and Output</a>.

</td>
</tr>
</table>


#### *nMaxInstances* \[in\]

The maximum number of instances that can be created for this pipe. The first instance of the pipe can specify this value; the same number must be specified for other instances of the pipe. Acceptable values are in the range 1 through **PIPE_UNLIMITED_INSTANCES-1** and <b>PIPE_UNLIMITED_INSTANCES</b>.
If this parameter is <b>PIPE_UNLIMITED_INSTANCES</b>, the number of pipe instances that can be created is limited only by the availability of system resources. If <i>nMaxInstances</i> is greater than <b>PIPE_UNLIMITED_INSTANCES</b>, the return value is <b>INVALID_HANDLE_VALUE</b> and <a href="/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror">GetLastError</a> returns <b>ERROR_INVALID_PARAMETER</b>.

#### *nOutBufferSize* \[in\]

The number of bytes to reserve for the output buffer. For a discussion on sizing named pipe buffers, see the following Remarks section.

#### *nInBufferSize* \[in\]

The number of bytes to reserve for the input buffer. For a discussion on sizing named pipe buffers, see the following Remarks section.

#### *nDefaultTimeOut* \[in\]

The default time-out value, in milliseconds, used when a timeout value is not specified when waiting for an instance of a named pipe. This parameter is only meaningful when the first instance of a named pipe is created. Each instance of a named pipe must specify the same value.

A value of zero will result in a default time-out of 50 milliseconds.

#### *lpSecurityAttributes* \[in, optional\]

A pointer to a 
<a href="/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)">SECURITY_ATTRIBUTES</a> structure that specifies a security descriptor for the new named pipe and determines whether child processes can inherit the returned handle. If <i>lpSecurityAttributes</i> is <b>NULL</b>, the named pipe gets a default security descriptor and the handle cannot be inherited. The ACLs in the default security descriptor for a named pipe grant full control to the LocalSystem account, administrators, and the creator owner. They also grant read access to members of the Everyone group and the anonymous account.

## Returns

If the function succeeds, the return value is a handle to the server end of a named pipe instance.

If the function fails, the return value is <b>INVALID_HANDLE_VALUE</b>. To get extended error information, call 
<a href="/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror">GetLastError</a>.

## Remarks

To create an instance of a named pipe, the user must have <b>FILE_CREATE_PIPE_INSTANCE</b> access to the named pipe object. If a new named pipe is being created, the access control list (ACL) from the security attributes parameter defines the discretionary access control for the named pipe.

All instances of a named pipe must specify the same pipe type (byte-type or message-type), pipe access (duplex, inbound, or outbound), instance count, and time-out value. If different values are used, this function fails and <a href="/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror">GetLastError</a> returns <b>ERROR_ACCESS_DENIED</b>.

 A client process connects to a named pipe by using the <a href="/windows/desktop/api/fileapi/nf-fileapi-createfilea">CreateFile</a> or <a href="/windows/desktop/api/winbase/nf-winbase-callnamedpipea">CallNamedPipe</a> function. The client side of a named pipe starts out in byte mode, even if the server side is in message mode. To avoid problems receiving data, set the client side to message mode as well. To change the mode of the pipe, the pipe client must open a read-only pipe with <b>GENERIC_READ</b> and  <b>FILE_WRITE_ATTRIBUTES</b> access.

The pipe server should not perform a blocking read operation until the pipe client has started. Otherwise, a race condition can occur. This typically occurs when initialization code, such as the C run-time, needs to lock and examine inherited handles.

Every time a named pipe is created, the system creates the inbound and/or outbound buffers using nonpaged pool, which is the physical memory used by the kernel. The number of pipe instances (as well as objects such as threads and processes) that you can create is limited by the available nonpaged pool. Each read or write request requires space in the buffer for the read or write data, plus additional space for the internal data structures.

The input and output buffer sizes are advisory. The actual buffer size reserved for each end of the named pipe is either the system default, the system minimum or maximum, or the specified size rounded up to the next allocation boundary. The buffer size specified should be small enough that your process will not run out of nonpaged pool, but large enough to accommodate typical requests.

Whenever a pipe write operation occurs, the system first tries to charge the memory against the pipe write quota. If the remaining pipe write quota is enough to fulfill the request, the write operation completes immediately. If the remaining pipe write quota is too small to fulfill the request, the system will try to expand the buffers to accommodate the data using nonpaged pool reserved for the process. The write operation will block until the data is read from the pipe so that the additional buffer quota can be released. Therefore, if your specified buffer size is too small, the system will grow the buffer as needed, but the downside is that the operation will block. If the operation is overlapped, a system thread is blocked; otherwise, the application thread is blocked.

To free resources used by a named pipe, the application should always close handles when they are no longer needed, which is accomplished either by calling the <a href="/windows/desktop/api/handleapi/nf-handleapi-closehandle">CloseHandle</a> function or when the process associated with the instance handles ends. Note that an instance of a named pipe may have more than one handle associated with it. An instance of a named pipe is always deleted when the last handle to the instance of the named pipe is closed.

## Requirements


| Requirement | Value |
|-----------------|-------------------------------------------------|
| Header<br/>                   | <dl> <dt>ntioapi.h/dt> </dl> |
| Library<br/>                  | <dl> <dt>ntdll.lib</dt> </dl> |
