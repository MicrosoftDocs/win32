---
title: PSM_SETHEADERTITLE message (Prsht.h)
description: Sets the title text for the header of a wizard's interior page. You can send this message explicitly or use the PropSheet\_SetHeaderTitle macro.
ms.assetid: 19d4badf-d99d-4a28-92d4-33bcf5d23944
keywords:
- PSM_SETHEADERTITLE message Windows Controls
topic_type:
- apiref
api_name:
- PSM_SETHEADERTITLE
- PSM_SETHEADERTITLEA
- PSM_SETHEADERTITLEW
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_SETHEADERTITLE message

Sets the title text for the header of a wizard's interior page. You can send this message explicitly or use the [**PropSheet\_SetHeaderTitle**](/windows/desktop/api/Prsht/nf-prsht-propsheet_setheadertitle) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the wizard's page.

</dd> <dt>

*lParam* 
</dt> <dd>

New header subtitle.

</dd> </dl>

## Return value

No return value.

## Remarks

If you specify the current page, it will immediately be repainted to display the new title.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **PSM\_SETHEADERTITLEW** (Unicode) and **PSM\_SETHEADERTITLEA** (ANSI)<br/>  |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**PSM\_HWNDTOINDEX**](psm-hwndtoindex.md)
</dt> <dt>

[**PSM\_IDTOINDEX**](psm-idtoindex.md)
</dt> <dt>

[**PSM\_PAGETOINDEX**](psm-pagetoindex.md)
</dt> </dl>

 

 





