---
title: TTM_SETWINDOWTHEME message (Commctrl.h)
description: Sets the visual style of a tooltip control.
ms.assetid: eeddb91e-8eb8-4480-9ab2-5efa9e3ef48a
keywords:
- TTM_SETWINDOWTHEME message Windows Controls
topic_type:
- apiref
api_name:
- TTM_SETWINDOWTHEME
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_SETWINDOWTHEME message

Sets the visual style of a tooltip control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a Unicode string that contains the tooltip visual style to set.

</dd> </dl>

## Return value

The return value is not used.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





