---
title: RB\_GETTEXTCOLOR message
description: Retrieves a rebar controls default text color.
ms.assetid: fc9c731d-c606-4845-a119-737267301b29
keywords:
- RB_GETTEXTCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- RB_GETTEXTCOLOR
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

# RB\_GETTEXTCOLOR message

Retrieves a rebar control's default text color.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a [**COLORREF**](https://msdn.microsoft.com/library/windows/desktop/dd183449) value that represent the current default text color.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**RB\_SETTEXTCOLOR**](rb-settextcolor.md)
</dt> </dl>

 

 





