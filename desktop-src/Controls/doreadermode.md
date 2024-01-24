---
title: DoReaderMode function
description: Enables reader mode in a window.
ms.assetid: 8f898cdd-c907-430a-8287-15d88390c756
keywords:
- DoReaderMode function Windows Controls
topic_type:
- apiref
api_name:
- DoReaderMode
api_location:
- Comctl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DoReaderMode function

\[**DoReaderMode** is available through Windows XP with Service Pack 2 (SP2). It may be unavailable in subsequent versions.\]

Enables reader mode in a window.

## Syntax


```C++
void WINAPI DoReaderMode(
  _In_ PREADERMODEINFO prmi
);
```



## Parameters

<dl> <dt>

*prmi* \[in\]
</dt> <dd>

Type: **PREADERMODEINFO**

A pointer to a [**READERMODEINFO**](readermodeinfo.md) structure that contains initialization information for the reader mode.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Reader mode is activated through supported devices by a mouse click, typically using a third mouse button or scroll wheel. Subsequent mouse movement in a specified area scrolls that area's contents rather than moving a pointer. Outside of that area, the mouse pointer is displayed and operates normally. A second click of the button or scroll wheel releases the device from reader mode.

> [!Note]  
> This function is not declared in any public header. To use it, you must access it as ordinal 383 from Comctl32.dll.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows Vista \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                            |
| DLL<br/>                      | <dl> <dt>Comctl32.dll (version 4.72 or later)</dt> </dl> |



 

 





