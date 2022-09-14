---
description: Retrieves an object handle for the specified object associated with the specified process.
ms.assetid: c7b371c3-02c0-4137-ad9d-dd07a74fe2a5
title: ObFindHandleForObject function (Ntosp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ObFindHandleForObject
api_type: 
- LibDef
api_location: 
- Ntoskrnl.lib
- Ntoskrnl.dll
---

# ObFindHandleForObject function

\[This function is obsolete and may be altered or unavailable in future versions of Windows. Avoid using this function.\]

Retrieves an object handle for the specified object associated with the specified process.

## Syntax


```C++
BOOLEAN WINAPI ObFindHandleForObject(
  _In_     PEPROCESS Process,
  _In_     PVOID     Object,
  _In_opt_ PVOID     Reserved1,
  _In_opt_ PVOID     Reserved2,
  _Out_    PHANDLE   Handle
);
```



## Parameters

<dl> <dt>

*Process* \[in\]
</dt> <dd>

The process. This handle is returned by the **IoGetCurrentProcess** or **PsGetCurrentProcess** function.

</dd> <dt>

*Object* \[in\]
</dt> <dd>

A pointer to the object.

</dd> <dt>

*Reserved1* \[in, optional\]
</dt> <dd>

Reserved.

</dd> <dt>

*Reserved2* \[in, optional\]
</dt> <dd>

Reserved.

</dd> <dt>

*Handle* \[out\]
</dt> <dd>

The object handle.

</dd> </dl>

## Return value

The function returns **TRUE** if a match is found and **FALSE** otherwise.

## Remarks

This function is available in Ntoskrnl.exe and can be called only from kernel mode. The corresponding import library is available through the Windows Driver Kit (WDK).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Ntosp.h</dt> </dl>      |
| Library<br/>                  | <dl> <dt>Ntoskrnl.lib</dt> </dl> |



 

 




