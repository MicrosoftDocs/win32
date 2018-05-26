---
title: HDM\_GETBITMAPMARGIN message
description: Gets the width of the bitmap margin for a header control. You can send this message explicitly or use the Header\_GetBitmapMargin macro.
ms.assetid: 67794ad4-3c22-4fad-a1d7-7a5d5cc6ad67
keywords:
- HDM_GETBITMAPMARGIN message Windows Controls
topic_type:
- apiref
api_name:
- HDM_GETBITMAPMARGIN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HDM\_GETBITMAPMARGIN message

Gets the width of the bitmap margin for a header control. You can send this message explicitly or use the [**Header\_GetBitmapMargin**](/windows/win32/Commctrl/nf-commctrl-header_getbitmapmargin?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the width of the bitmap margin in pixels. If the bitmap margin was not previously specified, the default value of 3\* [**GetSystemMetrics**](https://msdn.microsoft.com/library/windows/desktop/ms724385) (SM\_CXEDGE) is returned.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**HDM\_SETBITMAPMARGIN**](hdm-setbitmapmargin.md)
</dt> </dl>

 

 





