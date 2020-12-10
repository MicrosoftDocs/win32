---
title: PSM_SETTITLE message (Prsht.h)
description: Sets the title of a property sheet. You can send this message explicitly or by using the PropSheet\_SetTitle macro.
ms.assetid: 53ce8e20-4554-41f4-bad9-fb24c2c93c34
keywords:
- PSM_SETTITLE message Windows Controls
topic_type:
- apiref
api_name:
- PSM_SETTITLE
- PSM_SETTITLEA
- PSM_SETTITLEW
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_SETTITLE message

Sets the title of a property sheet. You can send this message explicitly or by using the [**PropSheet\_SetTitle**](/windows/desktop/api/Prsht/nf-prsht-propsheet_settitle) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Flag that indicates whether to include the prefix "Properties for" or the suffix "Properties" (depending on the version) with the specified title string. If this value is PSH\_PROPTITLE, the prefix or suffix is included.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a buffer that contains the title string. If the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) of this parameter is **NULL**, the property sheet loads the string resource specified in the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)).

</dd> </dl>

## Return value

No return value.

## Remarks

In an Aero Wizard, this message can be used to change the title of an interior page dynamically; for example, when handling the [PSN\_SETACTIVE](psn-setactive.md) notification.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **PSM\_SETTITLEW** (Unicode) and **PSM\_SETTITLEA** (ANSI)<br/>              |



 

