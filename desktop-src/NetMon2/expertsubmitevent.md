---
description: The ExpertSubmitEvent function indicates that an event condition exists and provides a data structure that describes the condition.
ms.assetid: 2339b530-427b-4028-aef6-c2cdd1353f77
title: ExpertSubmitEvent function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExpertSubmitEvent
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# ExpertSubmitEvent function

The **ExpertSubmitEvent** function indicates that an event condition exists and provides a data structure that describes the condition.

## Syntax


```C++
DWORD WINAPI ExpertSubmitEvent(
  _In_ HEXPERTKEY   hExpertKey,
  _In_ PNMEVENTDATA pExpertEvent
);
```



## Parameters

<dl> <dt>

*hExpertKey* \[in\]
</dt> <dd>

Unique identifier of the expert. Network Monitor passes *hExpertKey* to the expert when it calls the [Run](run.md) function.

</dd> <dt>

*pExpertEvent* \[in\]
</dt> <dd>

A pointer to an **NMEVENTDATA** structure that describes the event condition.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value indicates the reason for the failure. If the return value is NMERR\_EXPERT\_TERMINATE, the expert immediately cleans up and returns.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




