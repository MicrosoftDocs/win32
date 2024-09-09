---
title: LM_GETIDEALSIZE message (Commctrl.h)
description: LM_GETIDEALSIZE message - Retrieves the preferred height of a link for the control's current width.
ms.assetid: 63aad7eb-26ee-41d2-90d4-65fdcf0f182a
keywords:
- LM_GETIDEALSIZE message Windows Controls
topic_type:
- apiref
api_name:
- LM_GETIDEALSIZE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LM\_GETIDEALSIZE message

Retrieves the preferred height of a link for the control's current width.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Maximum width of the link, in pixels.</dd> <dt>

*lParam* \[out\]
</dt> <dd>When this message returns, contains a pointer to a <a href="/windows/win32/api/windef/ns-windef-size">**SIZE**</a> structure. The **cy** member of this structure indicates the ideal height of the control for the given width. It adjusts the **cx** member to the amount of space actually needed.</dd> </dl>

## Return value

Integer that represents the preferred height of the link text, in pixels.

## Remarks

> [!Note]  
> To use this API, you must provide a manifest that specifies Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

