---
Description: The RemoveTraceCallback function stops an EventClassCallback function from receiving events for an event trace class.
ms.assetid: da779e8d-4984-44e3-8731-647a422b55b2
title: RemoveTraceCallback function (Evntrace.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RemoveTraceCallback
api_type: 
- DllExport
api_location: 
- Sechost.dll
- Advapi32.dll
- API-MS-Win-DownLevel-AdvAPI32-l2-1-1.dll
- API-MS-Win-Eventing-Obsolete-l1-1-0.dll
- KernelBase.dll
---

# RemoveTraceCallback function

\[Do not use this function; it may be unavailable in subsequent versions.\]

The **RemoveTraceCallback** function stops an [**EventClassCallback**](eventclasscallback.md) function from receiving events for an event trace class.

## Syntax


```C++
ULONG RemoveTraceCallback(
  _In_ LPCGUID pGuid
);
```



## Parameters

<dl> <dt>

*pGuid* \[in\]
</dt> <dd>

Pointer to the class GUID of the event trace class for which the callback receives events. Use the same class GUID that you passed to the [**SetTraceCallback**](settracecallback.md) to begin receiving the events.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/en-us/library/ms681381(v=VS.85).aspx). The following table includes some common errors and their causes.



| Return code                                                                                                 | Description                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>    | The *pGuid* parameter is **NULL**.<br/>                                                                           |
| <dl> <dt>**ERROR\_WMI\_GUID\_NOT\_FOUND**</dt> </dl> | There is no [**EventClassCallback**](eventclasscallback.md) function associated with the event trace class.<br/> |



 

## Remarks

Consumers call this function.

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                                                                                                                                                                                                   |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                                                                                                                                                                                         |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |



## See also

<dl> <dt>

[**EventClassCallback**](eventclasscallback.md)
</dt> <dt>

[**ProcessTrace**](processtrace.md)
</dt> <dt>

[**SetTraceCallback**](settracecallback.md)
</dt> </dl>

 

 




