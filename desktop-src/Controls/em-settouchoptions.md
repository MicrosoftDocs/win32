---
title: EM_SETTOUCHOPTIONS message (Richedit.h)
description: Sets the touch options associated with a rich edit control.
ms.assetid: C15036D6-B74F-414D-B731-F1587B616644
keywords:
- EM_SETTOUCHOPTIONS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETTOUCHOPTIONS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETTOUCHOPTIONS message

Sets the touch options associated with a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The touch option to set. This parameter can be one of the following values.



| Value                                                                                                                                                                        | Meaning                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RTO_SHOWHANDLES"></span><span id="rto_showhandles"></span><dl> <dt>**RTO\_SHOWHANDLES**</dt> </dl>          | Show or hide the touch gripper handles, depending on the value of *lParam*.<br/>                                                                                                                                                       |
| <span id="RTO_DISABLEHANDLES"></span><span id="rto_disablehandles"></span><dl> <dt>**RTO\_DISABLEHANDLES**</dt> </dl> | Enable or disable the touch gripper handles, depending on the value of *lParam*. When handles are disabled, they are hidden if they are visible and remain hidden until an **EM\_SETTOUCHOPTIONS** message changes their status. <br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Set to **TRUE** to show/enable the touch selection handles, or **FALSE** to hide/disable the touch selection handles.

</dd> </dl>

## Return value

This message returns zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETTOUCHOPTIONS**](em-settouchoptions.md)
</dt> </dl>

 

 





