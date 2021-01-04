---
title: TBN_DUPACCELERATOR notification code (Commctrl.h)
description: Ascertains whether an accelerator key can be used on two or more active toolbars. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 98068d1a-1460-4be3-8575-9294b82ce903
keywords:
- TBN_DUPACCELERATOR notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_DUPACCELERATOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBN\_DUPACCELERATOR notification code

Ascertains whether an accelerator key can be used on two or more active toolbars. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_DUPACCELERATOR

    lpnmtb = (NMTBDUPACCELERATOR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to a structure that provides an accelerator and that receives a value specifying whether multiple toolbars respond to the same character.

</dd> </dl>

## Return value

Returns **TRUE** if successful, otherwise **FALSE**.

## Remarks

The application must declare the **NMTBDUPACCELERATOR** structure as follows:

``` syntax
typedef struct tagNMTBDUPACCELERATOR
{
    NMHDR hdr;
    UINT ch;   // The accelerator.
    BOOL fDup; // TRUE if multiple toolbars respond to the accelerator.
} NMTBDUPACCELERATOR, *LPNMTBDUPACCELERATOR;
```

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





