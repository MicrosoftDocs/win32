---
title: TB_HASACCELERATOR message (Commctrl.h)
description: Retrieves a count of toolbar buttons that have the specified accelerator character.
ms.assetid: 41167815-fb64-4203-a32c-b2a88ce7bce1
keywords:
- TB_HASACCELERATOR message Windows Controls
topic_type:
- apiref
api_name:
- TB_HASACCELERATOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_HASACCELERATOR message

\[Intended for internal use; not recommended for use in applications. This message may not be supported in future versions of Windows.\]

Retrieves a count of toolbar buttons that have the specified accelerator character.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A **WCHAR** representing the input accelerator character to test.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an **int** that receives the number of buttons that have the accelerator character.

</dd> </dl>

## Return value

The return value is not used.

## Security Considerations

Using this message might compromise the security of your program.

## Remarks

First, the system queries all toolbar buttons for matching accelerators. If no matches are found, the system sends the [TBN\_MAPACCELERATOR](tbn-mapaccelerator.md) notification to the parent window, requesting the index of the button that has the specified accelerator character. If the parent provides an index, the count is set to 1.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





