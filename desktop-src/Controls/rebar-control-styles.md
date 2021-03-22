---
title: Rebar Control Styles (CommCtrl.h)
description: Rebar controls support a variety of control styles in addition to standard window styles.
ms.assetid: 9690a4bd-51bd-4df9-8988-7da3ece7899f
topic_type:
- apiref
api_name:
- RBS_AUTOSIZE
- RBS_BANDBORDERS
- RBS_DBLCLKTOGGLE
- RBS_FIXEDORDER
- RBS_REGISTERDROP
- RBS_TOOLTIPS
- RBS_VARHEIGHT
- RBS_VERTICALGRIPPER
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Rebar Control Styles

Rebar controls support a variety of control styles in addition to standard window styles.



| Constant                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RBS_AUTOSIZE"></span><span id="rbs_autosize"></span><dl> <dt>**RBS\_AUTOSIZE**</dt> </dl>                      | [Version 4.71](common-control-versions.md). The rebar control will automatically change the layout of the bands when the size or position of the control changes. An [RBN\_AUTOSIZE](rbn-autosize.md) notification will be sent when this occurs.<br/>                                                                                              |
| <span id="RBS_BANDBORDERS"></span><span id="rbs_bandborders"></span><dl> <dt>**RBS\_BANDBORDERS**</dt> </dl>             | [Version 4.71](common-control-versions.md). The rebar control displays narrow lines to separate adjacent bands.<br/>                                                                                                                                                                                                                                 |
| <span id="RBS_DBLCLKTOGGLE"></span><span id="rbs_dblclktoggle"></span><dl> <dt>**RBS\_DBLCLKTOGGLE**</dt> </dl>          | [Version 4.71](common-control-versions.md). The rebar band will toggle its maximized or minimized state when the user double-clicks the band. Without this style, the maximized or minimized state is toggled when the user single-clicks on the band.<br/>                                                                                          |
| <span id="RBS_FIXEDORDER"></span><span id="rbs_fixedorder"></span><dl> <dt>**RBS\_FIXEDORDER**</dt> </dl>                | [Version 4.70](common-control-versions.md). The rebar control always displays bands in the same order. You can move bands to different rows, but the band order is static.<br/>                                                                                                                                                                      |
| <span id="RBS_REGISTERDROP"></span><span id="rbs_registerdrop"></span><dl> <dt>**RBS\_REGISTERDROP**</dt> </dl>          | [Version 4.71](common-control-versions.md). The rebar control generates [RBN\_GETOBJECT](rbn-getobject.md) notification codes when an object is dragged over a band in the control. To receive the RBN\_GETOBJECT notifications, initialize OLE with a call to [**OleInitialize**](/windows/desktop/api/ole2/nf-ole2-oleinitialize) or [**CoInitialize**](/windows/desktop/api/objbase/nf-objbase-coinitialize).<br/> |
| <span id="RBS_TOOLTIPS"></span><span id="rbs_tooltips"></span><dl> <dt>**RBS\_TOOLTIPS**</dt> </dl>                      | [Version 4.71](common-control-versions.md). Not yet supported.<br/>                                                                                                                                                                                                                                                                                  |
| <span id="RBS_VARHEIGHT"></span><span id="rbs_varheight"></span><dl> <dt>**RBS\_VARHEIGHT**</dt> </dl>                   | [Version 4.71](common-control-versions.md). The rebar control displays bands at the minimum required height, when possible. Without this style, the rebar control displays all bands at the same height, using the height of the tallest visible band to determine the height of other bands.<br/>                                                   |
| <span id="RBS_VERTICALGRIPPER"></span><span id="rbs_verticalgripper"></span><dl> <dt>**RBS\_VERTICALGRIPPER**</dt> </dl> | [Version 4.71](common-control-versions.md). The size grip will be displayed vertically instead of horizontally in a vertical rebar control. This style is ignored for rebar controls that do not have the [**CCS\_VERT**](common-control-styles.md) style.<br/>                                                                            |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

