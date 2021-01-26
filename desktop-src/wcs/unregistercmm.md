---
title: UnregisterCMM function
description: The UnregisterCMM function dissociates a specified ID value from a given color management module dynamic-link library (CMM DLL).
ms.assetid: b965db49-6131-4146-b298-77455b80972d
keywords:
- UnregisterCMM function Windows Color System
topic_type:
- apiref
api_name:
- UnregisterCMM
- UnregisterCMMA
- UnregisterCMMW
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# UnregisterCMM function

The **UnregisterCMM** function dissociates a specified ID value from a given color management module dynamic-link library (CMM DLL).

## Syntax


```C++
BOOL WINAPI UnregisterCMM(
   PCTSTR pMachineName,
   DWORD  cmmID
);
```



## Parameters

<dl> <dt>

*pMachineName* 
</dt> <dd>

Reserved; must currently be set to **NULL**, until non-local registration is supported. This parameter is intended to point to the name of the computer on which a CMM DLLs registration should be removed. A **NULL** pointer indicates the local computer.

</dd> <dt>

*cmmID* 
</dt> <dd>

Specifies the ID value identifying the CMM whose registration is to be removed. This is the signature of the CMM registered with the International Color Consortium (ICC).

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

If the profile for creating a transform later specifies this ID, the Windows default CMM will be used rather than this CMM DLL.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **UnregisterCMMW** (Unicode) and **UnregisterCMMA** (ANSI)<br/>                |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





