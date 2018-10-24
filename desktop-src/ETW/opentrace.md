---
Description: The OpenTrace function opens a real-time trace session or log file for consuming.
ms.assetid: 505e643b-6b4f-4f93-96c8-7fe8abdd6234
title: OpenTrace function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OpenTrace
- OpenTraceA
- OpenTraceW
api_type: 
- DllExport
api_location: 
- Sechost.dll
- Advapi32.dll
- AdvAPI32Legacy.dll
- API-MS-Win-DownLevel-AdvAPI32-l2-1-1.dll
- API-MS-Win-Eventing-Consumer-l1-1-0.dll
- API-MS-Win-Eventing-Legacy-l1-1-0.dll
- KernelBase.dll
---

# OpenTrace function

The **OpenTrace** function opens a real-time trace session or log file for consuming.

## Syntax


```C++
TRACEHANDLE OpenTrace(
  _Inout_ PEVENT_TRACE_LOGFILE Logfile
);
```



## Parameters

<dl> <dt>

*Logfile* \[in, out\]
</dt> <dd>

Pointer to an [**EVENT\_TRACE\_LOGFILE**](event-trace-logfile.md) structure. The structure specifies the source from which to consume events (from a log file or the session in real time) and specifies the callbacks the consumer wants to use to receive the events.

</dd> </dl>

## Return value

If the function succeeds, it returns a handle to the trace.

If the function fails, it returns INVALID\_PROCESSTRACE\_HANDLE.

> [!Note]
>
> If your code base supports Windows 7 and Windows Vista, and also supports earlier operating systems such as Windows XP and Windows Server 2003, do not use the constants described above. Instead, determine the operating system on which you are running and compare the return value to the following values.
>
> 
>
> | Operating system                   | Application   | Return value to compare |
> |------------------------------------|---------------|-------------------------|
> | Windows 7 and Windows Vista        | 32-bit        | 0x00000000FFFFFFFF      |
> | Windows 7 and Windows Vista        | 64-bit        | 0XFFFFFFFFFFFFFFFF      |
> | Windows XP and Windows Server 2003 | 32- or 64-bit | 0XFFFFFFFFFFFFFFFF      |
>
> 
>
>  

 

If the function returns INVALID\_PROCESSTRACE\_HANDLE, you can use the [**GetLastError**](https://msdn.microsoft.com/en-us/library/ms679360(v=VS.85).aspx) function to obtain extended error information. The following table lists some common errors and their causes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl> | The *Logfile* parameter is **NULL**.<br/>                                                                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**ERROR\_BAD\_PATHNAME**</dt> </dl>      | If you did not specify the **LoggerName** member of [**EVENT\_TRACE\_LOGFILE**](event-trace-logfile.md), you must specify a valid log file name.<br/>                                                                                                                                                                                                                                            |
| <dl> <dt>**ERROR\_ACCESS\_DENIED**</dt> </dl>     | Only users with administrative privileges, users in the Performance Log Users group, and services running as LocalSystem, LocalService, NetworkService can consume events in real time. To grant a restricted user the ability to consume events in real time, add them to the Performance Log Users group.<br/> **Windows XP and Windows 2000:** Anyone can consume real time events.<br/> |



 

## Remarks

Consumers call this function.

After calling **OpenTrace**, call the [**ProcessTrace**](processtrace.md) function to process the events. When you have finished processing events, call the [**CloseTrace**](closetrace.md) function.

Note that you can process events from only one real-time session.

Windows Vista and earlier: If the function fails it will returns INVALID\_HANDLE\_VALUE. To avoid compile-time errors, cast INVALID\_HANDLE\_VALUE to TRACEHANDLE as follows: `(TRACEHANDLE)INVALID_HANDLE_VALUE`.

## Examples

For an example that uses **OpenTrace**, see [Using TdhFormatProperty to Consume Event Data](using-tdhformatproperty-to-consume-event-data.md) or [Retrieving Event Data Using MOF](retrieving-event-data-using-mof.md).

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| Unicode and ANSI names<br/>   | **OpenTraceW** (Unicode) and **OpenTraceA** (ANSI)<br/>                                                                                                                                                                                                                                                                |



## See also

<dl> <dt>

[**CloseTrace**](closetrace.md)
</dt> <dt>

[**EVENT\_TRACE\_LOGFILE**](event-trace-logfile.md)
</dt> <dt>

[**ProcessTrace**](processtrace.md)
</dt> </dl>

 

 




