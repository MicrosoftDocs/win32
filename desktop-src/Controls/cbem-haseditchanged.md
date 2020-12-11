---
title: CBEM_HASEDITCHANGED message (Commctrl.h)
description: Determines whether the user has changed the text of a ComboBoxEx edit control.
ms.assetid: 8bf8c40a-e1ab-4748-899b-a9ed27767884
keywords:
- CBEM_HASEDITCHANGED message Windows Controls
topic_type:
- apiref
api_name:
- CBEM_HASEDITCHANGED
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CBEM\_HASEDITCHANGED message

Determines whether the user has changed the text of a ComboBoxEx edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns **TRUE** if the text in the control's edit box has been changed, or **FALSE** otherwise.

## Remarks

A ComboBoxEx control uses an edit box control when it is set to the [**CBS\_DROPDOWN**](combo-box-styles.md) style. You can retrieve the edit box control's window handle by sending a [**CBEM\_GETEDITCONTROL**](cbem-geteditcontrol.md) message.

When the user begins editing, you will receive a [CBEN\_BEGINEDIT](cben-beginedit.md) notification. When editing is complete, or the focus changes, you will receive a [CBEN\_ENDEDIT](cben-endedit.md) notification. The **CBEM\_HASEDITCHANGED** message is only useful for determining whether the text has been changed if it is sent before the CBEN\_ENDEDIT notification. If the message is sent afterward, it will return **FALSE**. For example, suppose the user starts to edit the text in the edit box but changes focus, generating a CBEN\_ENDEDIT notification. If you then send a **CBEM\_HASEDITCHANGED** message, it will return **FALSE**, even though the text has been changed.

The [**CBS\_SIMPLE**](combo-box-styles.md) style does not work correctly with **CBEM\_HASEDITCHANGED**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





