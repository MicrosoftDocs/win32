---
title: PSM_SETNEXTTEXT message (Prsht.h)
description: Sets the text of the Next button in a wizard. You can send this message explicitly or by using the PropSheet\_SetNextText macro.
ms.assetid: 4608425e-1724-4d0b-b0f6-9fec147a85f6
keywords:
- PSM_SETNEXTTEXT message Windows Controls
topic_type:
- apiref
api_name:
- PSM_SETNEXTTEXT
- PSM_SETNEXTTEXTW
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_SETNEXTTEXT message

Sets the text of the **Next** button in a wizard. You can send this message explicitly or by using the [**PropSheet\_SetNextText**](/windows/desktop/api/Prsht/nf-prsht-propsheet_setnexttext) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a buffer that contains the text.

</dd> </dl>

## Return value

No meaningful return value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **PSM\_SETNEXTTEXTW** (Unicode)<br/>                                         |



 

 





