---
title: EM\_SHOWBALLOONTIP message
description: The EM\_SHOWBALLOONTIP message displays a balloon tip associated with an edit control.
ms.assetid: '1e6915b7-4b61-43b2-be13-b89c72378a1a'
keywords: ["EM_SHOWBALLOONTIP message Windows Controls"]
topic_type:
- apiref
api_name:
- EM_SHOWBALLOONTIP
api_location:
- Commctrl.h
api_type:
- HeaderDef
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

A pointer to an [**EDITBALLOONTIP**](editballoontip.md) structure that contains information about the balloon tip to display.

</dd> </dl>

## Return value

If the message succeeds, it returns **TRUE**. Otherwise it returns **FALSE**.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EDITBALLOONTIP**](editballoontip.md)
</dt> <dt>

[**Edit\_ShowBalloonTip**](edit-showballoontip.md)
</dt> </dl>

 

 





