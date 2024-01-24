---
title: Tab Control Extended Styles (CommCtrl.h)
description: The tab control now supports extended styles. These styles are manipulated using the TCM\_GETEXTENDEDSTYLE and TCM\_SETEXTENDEDSTYLE messages and should not be confused with extended window styles that are passed to CreateWindowEx.
ms.assetid: 24294037-598c-4fcd-8a7c-8647ccfb1d81
topic_type:
- apiref
api_name:
- TCS_EX_FLATSEPARATORS
- TCS_EX_REGISTERDROP
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Tab Control Extended Styles

The tab control now supports extended styles. These styles are manipulated using the [**TCM\_GETEXTENDEDSTYLE**](tcm-getextendedstyle.md) and [**TCM\_SETEXTENDEDSTYLE**](tcm-setextendedstyle.md) messages and should not be confused with extended window styles that are passed to [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa).



| Constant                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TCS_EX_FLATSEPARATORS"></span><span id="tcs_ex_flatseparators"></span><dl> <dt>**TCS\_EX\_FLATSEPARATORS**</dt> </dl> | [Version 4.71](common-control-versions.md). The tab control will draw separators between the tab items. This extended style only affects tab controls that have the [**TCS\_BUTTONS**](tab-control-styles.md) and [**TCS\_FLATBUTTONS**](tab-control-styles.md) styles. By default, creating the tab control with the **TCS\_FLATBUTTONS** style sets this extended style. If you do not require separators, you should remove this extended style after creating the control.<br/> |
| <span id="TCS_EX_REGISTERDROP"></span><span id="tcs_ex_registerdrop"></span><dl> <dt>**TCS\_EX\_REGISTERDROP**</dt> </dl>       | [Version 4.71](common-control-versions.md). The tab control generates [TCN\_GETOBJECT](tcn-getobject.md) notification codes to request a drop target object when an object is dragged over the tab items in the control. The application must call [**CoInitialize**](/windows/desktop/api/objbase/nf-objbase-coinitialize) or [**OleInitialize**](/windows/desktop/api/ole2/nf-ole2-oleinitialize) before setting this style. <br/>                                                                                                                                               |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

