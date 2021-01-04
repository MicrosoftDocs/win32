---
title: PSM_SETHEADERSUBTITLE message (Prsht.h)
description: Sets the subtitle text for the header of a wizard's interior page. You can send this message explicitly or use the PropSheet\_SetHeaderSubTitle macro.
ms.assetid: 6ef3017b-8a20-4d62-a604-135410d8bdf7
keywords:
- PSM_SETHEADERSUBTITLE message Windows Controls
topic_type:
- apiref
api_name:
- PSM_SETHEADERSUBTITLE
- PSM_SETHEADERSUBTITLEA
- PSM_SETHEADERSUBTITLEW
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_SETHEADERSUBTITLE message

Sets the subtitle text for the header of a wizard's interior page. You can send this message explicitly or use the [**PropSheet\_SetHeaderSubTitle**](/windows/desktop/api/Prsht/nf-prsht-propsheet_setheadersubtitle) macro.

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

If you specify the current page, it will immediately be repainted to display the new subtitle.

> [!Note]  
> This message is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2)).

 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl>      |
| Unicode and ANSI names<br/>   | **PSM\_SETHEADERSUBTITLEW** (Unicode) and **PSM\_SETHEADERSUBTITLEA** (ANSI)<br/> |



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

 

 





