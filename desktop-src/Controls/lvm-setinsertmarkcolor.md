---
title: LVM_SETINSERTMARKCOLOR message (Commctrl.h)
description: Sets the color of the insertion point.
ms.assetid: dce2c266-672b-4682-ba23-51d9a8e1102b
keywords:
- LVM_SETINSERTMARKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETINSERTMARKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETINSERTMARKCOLOR message

Sets the color of the insertion point.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>**COLORREF** structure that specifies the color to set the insertion point.</dd> </dl>

## Return value

Returns **COLORREF** structure set to the previous color.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





