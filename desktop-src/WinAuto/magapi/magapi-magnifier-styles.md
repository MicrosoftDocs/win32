---
title: Magnifier Styles
description: This topic describes the styles used with the magnifier control.
ms.assetid: B3C575AC-B8D3-40CF-AF09-BAC73E6C7B45
topic_type:
- apiref
api_name:
- MS_CLIPAROUNDCURSOR
- MS_INVERTCOLORS
- MS_SHOWMAGNIFIEDCURSOR
api_location:
- Magnification.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 02/07/2020
---

# Magnifier Styles

This topic describes the styles used with the magnifier control. To create a magnifier control, use the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function and specify the WC_MAGNIFIER window class, along with a combination of the following magnifier styles.

| Requirement | Value |
|:---|:---|
| MS_CLIPAROUNDCURSOR 0x0002L | Clips the area of the magnifier window that surrounds the system cursor. This style enables the user to see screen content that is behind the magnifier window. |
| MS_INVERTCOLORS 0x0004L | Displays the magnified screen content using inverted colors. |
| MS_SHOWMAGNIFIEDCURSOR 0x0001L | Displays the magnified system cursor along with the magnified screen content. |

## Requirements

| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Magnification.h</dt> </dl> |

## See also

[Constants](entry-magapi-constants.md)
