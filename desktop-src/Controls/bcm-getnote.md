---
title: BCM_GETNOTE message (Commctrl.h)
description: Gets the text of the note associated with a command link button. You can send this message explicitly or use the Button\_GetNote macro.
ms.assetid: ddaf4227-1316-49b5-abf0-00215472c46c
keywords:
- BCM_GETNOTE message Windows Controls
topic_type:
- apiref
api_name:
- BCM_GETNOTE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BCM\_GETNOTE message

Gets the text of the note associated with a command link button. You can send this message explicitly or use the [**Button\_GetNote**](/windows/desktop/api/Commctrl/nf-commctrl-button_getnote) macro.

## Parameters

<dl> <dt>

*wParam* \[in, out\]
</dt> <dd>

A **DWORD** that specifies the size of the buffer pointed to by *lParam*, in characters.

</dd> <dt>

*lParam* \[out\]
</dt> <dd>

The string buffer to receive the text. The buffer must be large enough to accommodate the terminating NULL character.

</dd> </dl>

## Return value

If the message succeeds, it returns **TRUE**. Otherwise it returns **FALSE**.

## Remarks

The **BCM\_GETNOTE** message works only with buttons that have the [**BS\_COMMANDLINK**](button-styles.md) or [**BS\_DEFCOMMANDLINK**](button-styles.md) button style.

[**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) will contain:

-   ERROR\_NOT\_SUPPORTED, if the button does not have the [**BS\_DEFCOMMANDLINK**](button-styles.md) or [**BS\_COMMANDLINK**](button-styles.md) style.
-   ERROR\_INSUFFICIENT\_BUFFER, if the *lParam* buffer is too small. The *wParam* parameter will contain the required buffer size, in characters.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[Button Styles](button-styles.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Button Types](button-types-and-styles.md)
</dt> </dl>

 

