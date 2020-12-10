---
title: LVM_SETICONSPACING message (Commctrl.h)
description: Sets the spacing between icons in list-view controls that have the LVS\_ICON style. You can send this message explicitly or by using the ListView\_SetIconSpacing macro.
ms.assetid: 2dd3d9df-5b0d-445e-9201-d766fa218f90
keywords:
- LVM_SETICONSPACING message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETICONSPACING
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETICONSPACING message

Sets the spacing between icons in list-view controls that have the [**LVS\_ICON**](list-view-window-styles.md) style. You can send this message explicitly or by using the [**ListView\_SetIconSpacing**](/windows/desktop/api/Commctrl/nf-commctrl-listview_seticonspacing) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the distance, in pixels, to set between icons on the x-axis. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the distance, in pixels, to set between icons on the y-axis. See Remarks.

</dd> </dl>

## Return value

Returns a **DWORD** value that contains the previous x-axis distance in the low word, and the previous y-axis distance in the high word.

## Remarks

Values for *lParam* are relative to the upper-left corner of an icon bitmap. Therefore, to set spacing between icons that do not overlap, the *lParam* values must include the size of the icon, plus the amount of empty space desired between icons. Values that do not include the width of the icon will result in overlaps.

When defining the icon spacing, the *lParam* values must set to 4 or larger. Smaller values will not yield the desired layout. To reset the icons to the default spacing, set the *lParam* values to -1.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

