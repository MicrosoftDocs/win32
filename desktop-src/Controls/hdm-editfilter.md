---
title: HDM_EDITFILTER message (Commctrl.h)
description: Moves the input focus to the edit box when a filter button has the focus.
ms.assetid: 580f7872-4056-4d7d-8e69-274b4b4b5545
keywords:
- HDM_EDITFILTER message Windows Controls
topic_type:
- apiref
api_name:
- HDM_EDITFILTER
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDM\_EDITFILTER message

Moves the input focus to the edit box when a filter button has the focus.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A value specifying the column to edit.

</dd> <dt>

*lParam* 
</dt> <dd>

A flag that specifies how to handle the user's editing changes. Use this flag to specify what to do if the user is in the process of editing the filter when the message is sent.



| Value                                                                                                                                      | Meaning                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt></dt> <dt>**TRUE**</dt> </dl>  | Discard the changes made by the user. <br/> |
| <dl> <dt></dt> <dt>**FALSE**</dt> </dl> | Accept the changes made by the user. <br/>  |



 

</dd> </dl>

## Return value

Returns an integer. The **LRESULT** is cast to an integer that indicates **TRUE**(1) or **FALSE**(0).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**HDM\_CLEARFILTER**](hdm-clearfilter.md)
</dt> </dl>

 

 





