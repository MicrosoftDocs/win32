---
title: EM_GETAUTOURLDETECT message (Richedit.h)
description: Indicates whether the auto URL detection is turned on in the rich edit control.
ms.assetid: f723f15c-bf8f-41ab-aef0-bd8f2c0b9e5d
keywords:
- EM_GETAUTOURLDETECT message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETAUTOURLDETECT
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETAUTOURLDETECT message

Indicates whether the auto URL detection is turned on in the rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

If auto-URL detection is active, the return value is 1.

If auto-URL detection is inactive, the return value is 0.

## Remarks

When auto URL detection is on, Microsoft Rich Edit is constantly checking typed text for a valid URL. Rich Edit recognizes URLs that start with these prefixes:

-   http:
-   file:
-   mailto:
-   ftp:
-   https:
-   gopher:
-   nntp:
-   prospero:
-   telnet:
-   news:
-   wais:
-   outlook:

Rich Edit also recognizes standard path names that start with \\\\. When Rich Edit locates a URL, it changes the URL text color, underlines the text, and notifies the client using [EN\_LINK](en-link.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[EN\_LINK](en-link.md)
</dt> </dl>

 

 





