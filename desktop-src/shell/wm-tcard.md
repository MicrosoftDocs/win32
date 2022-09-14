---
description: Sent to an application that has initiated a training card with Windows Help.
title: WM_TCARD message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: fdde7603-9913-4e80-9502-2142ef8a511c
api_name: 
 - WM_TCARD
api_type: 
 - HeaderDef
api_location: 
 - Winuser.h
topic_type: 
 - APIRef
 - kbSyntax

---

# WM\_TCARD message

Sent to an application that has initiated a training card with Windows Help. The message informs the application when the user clicks an authorable button. An application initiates a training card by specifying the HELP\_TCARD command in a call to the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function.

## Parameters

<dl> <dt>

*idAction* 
</dt> <dd>

A value that indicates the action the user has taken. This can be one of the following values.

<dt>

<span id="IDABORT"></span><span id="idabort"></span>

<span id="IDABORT"></span><span id="idabort"></span>**IDABORT**


</dt> <dd>

The user clicked an authorable **Abort** button.

</dd> <dt>

<span id="IDCANCEL"></span><span id="idcancel"></span>

<span id="IDCANCEL"></span><span id="idcancel"></span>**IDCANCEL**


</dt> <dd>

The user clicked an authorable **Cancel** button.

</dd> <dt>

<span id="IDCLOSE"></span><span id="idclose"></span>

<span id="IDCLOSE"></span><span id="idclose"></span>**IDCLOSE**


</dt> <dd>

The user closed the training card.

</dd> <dt>

<span id="IDHELP"></span><span id="idhelp"></span>

<span id="IDHELP"></span><span id="idhelp"></span>**IDHELP**


</dt> <dd>

The user clicked an authorable Windows **Help** button.

</dd> <dt>

<span id="IDIGNORE"></span><span id="idignore"></span>

<span id="IDIGNORE"></span><span id="idignore"></span>**IDIGNORE**


</dt> <dd>

The user clicked an authorable **Ignore** button.

</dd> <dt>

<span id="IDOK"></span><span id="idok"></span>

<span id="IDOK"></span><span id="idok"></span>**IDOK**


</dt> <dd>

The user clicked an authorable **OK** button.

</dd> <dt>

<span id="IDNO"></span><span id="idno"></span>

<span id="IDNO"></span><span id="idno"></span>**IDNO**


</dt> <dd>

The user clicked an authorable **No** button.

</dd> <dt>

<span id="IDRETRY"></span><span id="idretry"></span>

<span id="IDRETRY"></span><span id="idretry"></span>**IDRETRY**


</dt> <dd>

The user clicked an authorable **Retry** button.

</dd> <dt>

<span id="HELP_TCARD_DATA"></span><span id="help_tcard_data"></span>

<span id="HELP_TCARD_DATA"></span><span id="help_tcard_data"></span>**HELP\_TCARD\_DATA**


</dt> <dd>

The user clicked an authorable button. The *dwActionData* parameter contains a long integer specified by the Help author.

</dd> <dt>

<span id="HELP_TCARD_OTHER_CALLER"></span><span id="help_tcard_other_caller"></span>

<span id="HELP_TCARD_OTHER_CALLER"></span><span id="help_tcard_other_caller"></span>**HELP\_TCARD\_OTHER\_CALLER**


</dt> <dd>

Another application has requested training cards.

</dd> <dt>

<span id="IDYES"></span><span id="idyes"></span>

<span id="IDYES"></span><span id="idyes"></span>**IDYES**


</dt> <dd>

The user clicked an authorable **Yes** button.

</dd> </dl> </dd> <dt>

*dwActionData* 
</dt> <dd>

If *idAction* specifies HELP\_TCARD\_DATA, this parameter is a **long** specified by the Help author. Otherwise, this parameter is zero.

</dd> </dl>

## Return value

The return value is ignored; use zero.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



 

 




