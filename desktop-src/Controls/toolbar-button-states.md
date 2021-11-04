---
title: Toolbar Button States (CommCtrl.h)
description: This section lists the states a toolbar button can have.
ms.assetid: 422e0d81-bd80-45dc-b843-82fc5d5c2a9a
topic_type:
- apiref
api_name:
- TBSTATE_CHECKED
- TBSTATE_ELLIPSES
- TBSTATE_ENABLED
- TBSTATE_HIDDEN
- TBSTATE_INDETERMINATE
- TBSTATE_MARKED
- TBSTATE_PRESSED
- TBSTATE_WRAP
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Toolbar Button States

This section lists the states a toolbar button can have.



| Constant                                                                                                                                                                              | Description                                                                                                                                           |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TBSTATE_CHECKED"></span><span id="tbstate_checked"></span><dl> <dt>**TBSTATE\_CHECKED**</dt> </dl>                   | The button has the [**TBSTYLE\_CHECK**](toolbar-control-and-button-styles.md) style and is being clicked.<br/>                   |
| <span id="TBSTATE_ELLIPSES"></span><span id="tbstate_ellipses"></span><dl> <dt>**TBSTATE\_ELLIPSES**</dt> </dl>                | [Version 4.70](common-control-versions.md). The button's text is cut off and an ellipsis is displayed.<br/>                                    |
| <span id="TBSTATE_ENABLED"></span><span id="tbstate_enabled"></span><dl> <dt>**TBSTATE\_ENABLED**</dt> </dl>                   | The button accepts user input. A button that does not have this state is grayed.<br/>                                                           |
| <span id="TBSTATE_HIDDEN"></span><span id="tbstate_hidden"></span><dl> <dt>**TBSTATE\_HIDDEN**</dt> </dl>                      | The button is not visible and cannot receive user input.<br/>                                                                                   |
| <span id="TBSTATE_INDETERMINATE"></span><span id="tbstate_indeterminate"></span><dl> <dt>**TBSTATE\_INDETERMINATE**</dt> </dl> | The button is grayed.<br/>                                                                                                                      |
| <span id="TBSTATE_MARKED"></span><span id="tbstate_marked"></span><dl> <dt>**TBSTATE\_MARKED**</dt> </dl>                      | [Version 4.71](common-control-versions.md). The button is marked. The interpretation of a marked item is dependent upon the application. <br/> |
| <span id="TBSTATE_PRESSED"></span><span id="tbstate_pressed"></span><dl> <dt>**TBSTATE\_PRESSED**</dt> </dl>                   | The button is being clicked.<br/>                                                                                                               |
| <span id="TBSTATE_WRAP"></span><span id="tbstate_wrap"></span><dl> <dt>**TBSTATE\_WRAP**</dt> </dl>                            | The button is followed by a line break. The button must also have the TBSTATE\_ENABLED state.<br/>                                              |



## Remarks

A toolbar may have a combination of states.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





