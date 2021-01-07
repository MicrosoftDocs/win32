---
description: The ExpertGetStartupInfo function retrieves the startup configuration information for the expert.
ms.assetid: 15f080ed-50b7-40c6-b283-dbe416a2b0e9
title: ExpertGetStartupInfo function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExpertGetStartupInfo
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# ExpertGetStartupInfo function

The **ExpertGetStartupInfo** function retrieves the startup configuration information for the expert.

## Syntax


```C++
DWORD WINAPI ExpertGetStartupInfo(
  _In_  HEXPERTKEY         hExpertKey,
  _Out_ PEXPERTSTARTUPINFO pExpertStartupInfo
);
```



## Parameters

<dl> <dt>

*hExpertKey* \[in\]
</dt> <dd>

Unique expert identifier. Network Monitor passes *hExpertKey* to the expert when it calls the [Run](run.md) function.

</dd> <dt>

*pExpertStartupInfo* \[out\]
</dt> <dd>

Pointer to an [EXPERTSTARTUPINFO](expertstartupinfo.md) structure that contains startup information.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is NMERR.

## Remarks

The **ExpertGetStartupInfo** function is used if the expert must determine the startup information that is used.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




