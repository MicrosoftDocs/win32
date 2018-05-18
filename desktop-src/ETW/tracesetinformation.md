---
Description: 'Enables or disables event tracing session settings for the specified information class.'
ms.assetid: 'f4cdbe32-6885-4844-add5-560961c3dd1d'
title: TraceSetInformation function
---

# TraceSetInformation function

The **TraceSetInformation** function enables or disables event tracing session settings for the specified information class.

## Syntax


```C++
ULONG WINAPI TraceSetInformation(
  _In_ TRACEHANDLE      SessionHandle,
  _In_ TRACE_INFO_CLASS InformationClass,
  _In_ PVOID            TraceInformation,
  _In_ ULONG            InformationLength
);
```



## Parameters

<dl> <dt>

*SessionHandle* \[in\]
</dt> <dd>

A handle of the event tracing session that wants to capture the specified information. The [**StartTrace**](starttrace.md) function returns this handle.

</dd> <dt>

*InformationClass* \[in\]
</dt> <dd>

The information class to enable or disable. The information that the class captures is included in the extended data section of the event. For a list of information classes that you can enable, see the [**TRACE\_INFO\_CLASS**](trace-info-class.md) enumeration.

</dd> <dt>

*TraceInformation* \[in\]
</dt> <dd>

A pointer to information class specific data; the information class determines the contents of this parameter. For example, for the **TraceStackTracingInfo** information class, this parameter is an array of [**CLASSIC\_EVENT\_ID**](classic-event-id.md) structures. The structures specify the event GUIDs for which stack tracing is enabled. The array is limited to 256 elements.

</dd> <dt>

*InformationLength* \[in\]
</dt> <dd>

The size, in bytes, of the data in the *TraceInformation* buffer.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the following error codes.



| Return code                                                                                              | Description                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_BAD\_LENGTH**</dt> </dl>        | The program issued a command but the command length is incorrect. This error is returned if the *InformationLength* parameter is less than a minimum size.<br/> |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl> | The parameter is incorrect. <br/>                                                                                                                               |
| <dl> <dt>**ERROR\_NOT\_SUPPORTED**</dt> </dl>     | The request is not supported.<br/>                                                                                                                              |
| <dl> <dt>**Other**</dt> </dl>                     | Use [**FormatMessage**](base.formatmessage) to obtain the message string for the returned error.<br/>                                                           |



 

## Remarks

Call this function after calling [**StartTrace**](starttrace.md).

If the *InformationClass* parameter is set to **TraceStackTracingInfo**, calling this function enables stack tracing of the specified kernel events. Subsequent calls to this function overwrites the previous list of kernel events for which stack tracing is enabled. To disable stack tracing, call this function with *InformationClass* set to **TraceStackTracingInfo** and *InformationLength* set to 0.

The extended data section of the event will include the call stack. The [**StackWalk\_Event**](stackwalk-event.md) MOF class defines the layout of the extended data.

Typically, on 64-bit computers, you cannot capture the kernel stack in certain contexts when page faults are not allowed. To enable walking the kernel stack on x64, set the **DisablePagingExecutive** Memory Management registry value to 1. The **DisablePagingExecutive** registry value is located under the following registry key:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\Memory Management**

You should consider the cost of setting this registry value before doing so.

## Requirements



|                                     |                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                                                                                                                                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                                                                                                                                                                                      |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7 and Windows Server 2008 R2</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7 and Windows Server 2008 R2</dt> </dl> |



## See also

<dl> <dt>

[**TRACE\_INFO\_CLASS**](trace-info-class.md)
</dt> <dt>

[**TraceQueryInformation**](tracequeryinformation.md)
</dt> </dl>

 

 




