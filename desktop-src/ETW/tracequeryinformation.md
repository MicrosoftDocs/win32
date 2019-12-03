---
Description: Queries event tracing session settings for the specified information class.
ms.assetid: 3CC91F7C-7F82-4B3B-AA50-FE03CFEC0278
title: TraceQueryInformation function (Evntrace.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TraceQueryInformation
api_type: 
- DllExport
api_location: 
- Sechost.dll
- Advapi32.dll
- API-MS-Win-Eventing-Controller-l1-1-0.dll
- KernelBase.dll
---

# TraceQueryInformation function

The **TraceQueryInformation** function queries event tracing session settings for the specified information class.

## Syntax


```C++
ULONG WINAPI TraceQueryInformation(
  _In_      TRACEHANDLE            SessionHandle,
  _In_      TRACE_QUERY_INFO_CLASS InformationClass,
  _Out_     PVOID                  TraceInformation,
  _In_      ULONG                  InformationLength,
  _Out_opt_ PULONG                 ReturnLength
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

The information class to query. The information that the class captures is included in the extended data section of the event. For a list of information classes that you can query, see the [**TRACE\_QUERY\_INFO\_CLASS**](https://msdn.microsoft.com/library/Aa364147(v=VS.85).aspx) enumeration.

</dd> <dt>

*TraceInformation* \[out\]
</dt> <dd>

A pointer to a buffer to receive the returned information class specific data. The information class determines the contents of this parameter. For example, for the **TraceStackTracingInfo** information class, this parameter is an array of [**CLASSIC\_EVENT\_ID**](classic-event-id.md) structures. The structures specify the event GUIDs for which stack tracing is enabled. The array is limited to 256 elements.

</dd> <dt>

*InformationLength* \[in\]
</dt> <dd>

The size, in bytes, of the data returned in the *TraceInformation* buffer. If the function fails, this value indicates the required size of the *TraceInformation* buffer that is needed.

</dd> <dt>

*ReturnLength* \[out, optional\]
</dt> <dd>

A pointer a value that receives the size, in bytes, of the specific data returned in the *TraceInformation* buffer.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the following error codes.



| Return code                                                                                              | Description                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_BAD\_LENGTH**</dt> </dl>        | The program issued a command but the command length is incorrect. This error is returned if the *InformationLength* parameter is less than a minimum size.<br/> |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl> | The parameter is incorrect. <br/>                                                                                                                               |
| <dl> <dt>**ERROR\_NOT\_SUPPORTED**</dt> </dl>     | The request is not supported.<br/>                                                                                                                              |
| <dl> <dt>**Other**</dt> </dl>                     | Use [**FormatMessage**](https://msdn.microsoft.com/en-us/library/ms679351(v=VS.85).aspx) to obtain the message string for the returned error.<br/>                                                           |



 

## Remarks

The **TraceQueryInformation** function queries event tracing session settings for the specified information class. Call this function after calling [**StartTrace**](starttrace.md).

## Requirements



|                                     |                                                                                                                                                                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                                                                                                                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                                                                                                                                                      |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                     |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8 and Windows Server 2012</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8 and Windows Server 2012</dt> </dl> |



## See also

<dl> <dt>

[**TRACE\_QUERY\_INFO\_CLASS**](https://msdn.microsoft.com/library/Aa364147(v=VS.85).aspx)
</dt> <dt>

[**TraceSetInformation**](tracesetinformation.md)
</dt> </dl>

 

 




