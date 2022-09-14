---
title: CCM_DPISCALE message (Commctrl.h)
description: Enables automatic high dots per inch (dpi) scaling in Tree-View controls, List-View controls, ComboBoxEx controls, Header controls, Buttons, Toolbar controls, Animation controls, and Image Lists.
ms.assetid: 3c751f10-992c-41f8-8f0b-3dc58f0591e4
keywords:
- CCM_DPISCALE message Windows Controls
topic_type:
- apiref
api_name:
- CCM_DPISCALE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CCM\_DPISCALE message

Enables automatic high dots per inch (dpi) scaling in [Tree-View controls](tree-view-controls.md), [List-View controls](list-view-control-reference.md), [ComboBoxEx controls](comboboxex-controls.md), [Header controls](header-controls.md), [Buttons](buttons.md), [Toolbar controls](toolbar-controls-overview.md), [Animation controls](animation-control-overview.md), and [Image Lists](image-lists.md).

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Set to **TRUE**.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

The return value is not used.

## Remarks

Quick Launch and [Taskbar](/windows/desktop/shell/taskbar) should not specify a dpi scaling, because the images are already scaled.

Any control that uses an image list created with the SmallIcon metric should not scale its icons.

> [!Note]  
> To use this API, you must provide a manifest that specifies Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

