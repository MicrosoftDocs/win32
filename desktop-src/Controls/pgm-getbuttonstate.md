---
title: PGM_GETBUTTONSTATE message (Commctrl.h)
description: Retrieves the state of the specified button in a pager control. You can send this message explicitly or use the Pager\_GetButtonState macro.
ms.assetid: 58f99b67-fef7-4695-86e2-0579a2f6de2f
keywords:
- PGM_GETBUTTONSTATE message Windows Controls
topic_type:
- apiref
api_name:
- PGM_GETBUTTONSTATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGM\_GETBUTTONSTATE message

Retrieves the state of the specified button in a pager control. You can send this message explicitly or use the [**Pager\_GetButtonState**](/windows/desktop/api/Commctrl/nf-commctrl-pager_getbuttonstate) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Indicates which button to retrieve the state for. This can be one of the following values:



| Value                                                                                                                                                                     | Meaning                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PGB_TOPORLEFT"></span><span id="pgb_toporleft"></span><dl> <dt>**PGB\_TOPORLEFT**</dt> </dl>             | Indicates the top button in a [**PGS\_VERT**](pager-control-styles.md) pager control or the left button in a [**PGS\_HORZ**](pager-control-styles.md) pager control. <br/>     |
| <span id="PGB_BOTTOMORRIGHT"></span><span id="pgb_bottomorright"></span><dl> <dt>**PGB\_BOTTOMORRIGHT**</dt> </dl> | Indicates the bottom button in a [**PGS\_VERT**](pager-control-styles.md) pager control or the right button in a [**PGS\_HORZ**](pager-control-styles.md) pager control. <br/> |



 

</dd> </dl>

## Return value

Returns the state of the button specified in *lParam*. This will be one or more of the following values (if more then one value is returned they will be combined using a bitwise OR):



| Return code                                                                                   | Description                                 |
|-----------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>**PGF\_INVISIBLE**</dt> </dl> | The button is not visible. <br/>      |
| <dl> <dt>**PGF\_NORMAL**</dt> </dl>    | The button is in normal state. <br/>  |
| <dl> <dt>**PGF\_GRAYED**</dt> </dl>    | The button is in grayed state. <br/>  |
| <dl> <dt>**PGF\_DEPRESSED**</dt> </dl> | The button is in pressed state. <br/> |
| <dl> <dt>**PGF\_HOT**</dt> </dl>       | The button is in hot state. <br/>     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





