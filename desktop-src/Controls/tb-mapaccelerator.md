---
title: TB_MAPACCELERATOR message (Commctrl.h)
description: Determines the ID of the button that corresponds to the specified accelerator character.
ms.assetid: 724b593d-39af-4301-b721-0332844677b1
keywords:
- TB_MAPACCELERATOR message Windows Controls
topic_type:
- apiref
api_name:
- TB_MAPACCELERATOR
- TB_MAPACCELERATORA
- TB_MAPACCELERATORW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_MAPACCELERATOR message

Determines the ID of the button that corresponds to the specified accelerator character.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

The accelerator character.

</dd> <dt>

*lParam* \[out\]
</dt> <dd>

Pointer to a **UINT**. On return, if successful, this parameter will hold the id of the button that has *wParam* as its accelerator character.

</dd> </dl>

## Return value

Returns a nonzero value if one of the buttons has *wParam* as its accelerator character, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TB\_MAPACCELERATORW** (Unicode) and **TB\_MAPACCELERATORA** (ANSI)<br/>       |



 

 





