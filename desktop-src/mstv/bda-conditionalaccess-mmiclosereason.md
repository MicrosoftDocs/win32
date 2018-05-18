---
title: BDA\_CONDITIONALACCESS\_MMICLOSEREASON enumeration
description: Specifies why a media sink device (MSD) has closed a user interface (MMI) dialog box.
ms.assetid: 'd35067b3-a50b-4bc8-9139-429fe4fa25bb'
keywords: ["BDA_CONDITIONALACCESS_MMICLOSEREASON enumeration Microsoft TV Technologies"]
topic_type:
- apiref
api_name:
- BDA_CONDITIONALACCESS_MMICLOSEREASON
api_location:
- bdatypes.h
api_type:
- HeaderDef
---

# BDA\_CONDITIONALACCESS\_MMICLOSEREASON enumeration

Specifies why a media sink device (MSD) has closed a user interface (MMI) dialog box.

## Syntax


```C++
typedef enum  { 
  CONDITIONALACCESS_UNSPECIFIED                = 0,
  CONDITIONALACCESS_CLOSED_ITSELF,
  CONDITIONALACCESS_TUNER_REQUESTED_CLOSE,
  CONDITIONALACCESS_DIALOG_TIMEOUT,
  CONDITIONALACCESS_DIALOG_FOCUS_CHANGE,
  CONDITIONALACCESS_DIALOG_USER_DISMISSED,
  CONDITIONALACCESS_DIALOG_USER_NOT_AVAILABLE
} BDA_CONDITIONALACCESS_MMICLOSEREASON;
```



## Constants

<dl> <dt>

<span id="CONDITIONALACCESS_UNSPECIFIED"></span><span id="conditionalaccess_unspecified"></span>**CONDITIONALACCESS\_UNSPECIFIED**
</dt> <dd>

No reason is specified.

</dd> <dt>

<span id="CONDITIONALACCESS_CLOSED_ITSELF"></span><span id="conditionalaccess_closed_itself"></span>**CONDITIONALACCESS\_CLOSED\_ITSELF**
</dt> <dd>

The dialog box closed itself.

</dd> <dt>

<span id="CONDITIONALACCESS_TUNER_REQUESTED_CLOSE"></span><span id="conditionalaccess_tuner_requested_close"></span>**CONDITIONALACCESS\_TUNER\_REQUESTED\_CLOSE**
</dt> <dd>

The media transform device (MTD) requested the dialog box to close.

</dd> <dt>

<span id="CONDITIONALACCESS_DIALOG_TIMEOUT"></span><span id="conditionalaccess_dialog_timeout"></span>**CONDITIONALACCESS\_DIALOG\_TIMEOUT**
</dt> <dd>

The dialog box timed out.

</dd> <dt>

<span id="CONDITIONALACCESS_DIALOG_FOCUS_CHANGE"></span><span id="conditionalaccess_dialog_focus_change"></span>**CONDITIONALACCESS\_DIALOG\_FOCUS\_CHANGE**
</dt> <dd>

The focus changed.

</dd> <dt>

<span id="CONDITIONALACCESS_DIALOG_USER_DISMISSED"></span><span id="conditionalaccess_dialog_user_dismissed"></span>**CONDITIONALACCESS\_DIALOG\_USER\_DISMISSED**
</dt> <dd>

The user dismissed the dialog box.

</dd> <dt>

<span id="CONDITIONALACCESS_DIALOG_USER_NOT_AVAILABLE"></span><span id="conditionalaccess_dialog_user_not_available"></span>**CONDITIONALACCESS\_DIALOG\_USER\_NOT\_AVAILABLE**
</dt> <dd>

The destination was not reachable.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[**IBDA\_ConditionalAccessEx::CloseMmiDialog**](ibda-conditionalaccessex-closemmidialog.md)
</dt> </dl>

 

 





