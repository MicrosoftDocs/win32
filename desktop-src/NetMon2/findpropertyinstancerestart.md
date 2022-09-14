---
description: Finds the next instance of the property specified by the hProperty parameter.
ms.assetid: f77cb92b-5936-4349-bf66-643c16e9e0df
title: FindPropertyInstanceRestart function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FindPropertyInstanceRestart
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# FindPropertyInstanceRestart function

The **FindPropertyInstanceRestart** function finds the next instance of the property specified by the *hProperty* parameter.

## Syntax


```C++
LPPROPERTYINST WINAPI FindPropertyInstanceRestart(
  _In_ HFRAME         hFrame,
  _In_ HPROPERTY      hProperty,
  _In_ LPPROPERTYINST *lpRestartKey,
  _In_ BOOL           DirForward
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

A handle to the frame. The frame handle can be retrieved by a call to the [GetFrame](getframe.md) function.

</dd> <dt>

*hProperty* \[in\]
</dt> <dd>

A handle to the property to find. The property handle can be retrieved by a call to the [GetProperty](getproperty.md) function.

</dd> <dt>

*lpRestartKey* \[in\]
</dt> <dd>

A pointer to the property instance used as the starting point of the search. If the *lpRestartKey* parameter is set to **NULL**, the search begins at beginning of the frame, or the end of the frame, depending on the value of the *DirForward* parameter.

If *lpRestartKey* points to **NULL**, the search begins at the beginning of the frame if *DirForward* is **TRUE** or the at end of the frame if the parameter is **FALSE**.

</dd> <dt>

*DirForward* \[in\]
</dt> <dd>

An indicator of the search direction. If the value is **TRUE**, the search moves from the current location to the end of the frame. If the value is **FALSE**, the search moves from the current location to the beginning of the frame.

</dd> </dl>

## Return value

If the function is successful, the return value is the next valid **LPPROPERTYINST**.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **FindPropertyInstanceRestart** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[GetFrame](getframe.md)
</dt> <dt>

[GetProperty](getproperty.md)
</dt> </dl>

 

 




