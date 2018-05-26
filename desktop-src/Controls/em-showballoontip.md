---
title: EM\_SHOWBALLOONTIP message
description: The EM\_SHOWBALLOONTIP message displays a balloon tip associated with an edit control.
ms.assetid: 1e6915b7-4b61-43b2-be13-b89c72378a1a
keywords:
- EM_SHOWBALLOONTIP message Windows Controls
topic_type:
- apiref
api_name:
- EM_SHOWBALLOONTIP
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

# EM\_SHOWBALLOONTIP message

The **EM\_SHOWBALLOONTIP** message displays a balloon tip associated with an edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**EDITBALLOONTIP**](/windows/win32/Commctrl/ns-commctrl-_tageditballoontip?branch=master) structure that contains information about the balloon tip to display.

</dd> </dl>

## Return value

If the message succeeds, it returns **TRUE**. Otherwise it returns **FALSE**.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EDITBALLOONTIP**](/windows/win32/Commctrl/ns-commctrl-_tageditballoontip?branch=master)
</dt> <dt>

[**Edit\_ShowBalloonTip**](/windows/win32/Commctrl/nf-commctrl-edit_showballoontip?branch=master)
</dt> </dl>

 

 





