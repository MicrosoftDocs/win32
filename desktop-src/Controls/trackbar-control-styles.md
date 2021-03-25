---
title: Trackbar Control Styles (CommCtrl.h)
description: This section contains information about the styles used with trackbar controls.
ms.assetid: ac2f59c6-85a2-4f41-aace-4132971d3559
topic_type:
- apiref
api_name:
- TBS_AUTOTICKS
- TBS_VERT
- TBS_HORZ
- TBS_TOP
- TBS_BOTTOM
- TBS_LEFT
- TBS_RIGHT
- TBS_BOTH
- TBS_NOTICKS
- TBS_ENABLESELRANGE
- TBS_FIXEDLENGTH
- TBS_NOTHUMB
- TBS_TOOLTIPS
- TBS_REVERSED
- TBS_DOWNISLEFT
- TBS_NOTIFYBEFOREMOVE
- TBS_TRANSPARENTBKGND
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Trackbar Control Styles

This section contains information about the styles used with trackbar controls.



| Constant                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                           |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TBS_AUTOTICKS"></span><span id="tbs_autoticks"></span><dl> <dt>**TBS\_AUTOTICKS**</dt> </dl>                      | The trackbar control has a tick mark for each increment in its range of values. <br/>                                                                                                                                                                                                                                                                           |
| <span id="TBS_VERT"></span><span id="tbs_vert"></span><dl> <dt>**TBS\_VERT**</dt> </dl>                                     | The trackbar control is oriented vertically.<br/>                                                                                                                                                                                                                                                                                                               |
| <span id="TBS_HORZ"></span><span id="tbs_horz"></span><dl> <dt>**TBS\_HORZ**</dt> </dl>                                     | The trackbar control is oriented horizontally. This is the default orientation. <br/>                                                                                                                                                                                                                                                                           |
| <span id="TBS_TOP"></span><span id="tbs_top"></span><dl> <dt>**TBS\_TOP**</dt> </dl>                                        | The trackbar control displays tick marks above the control. This style is valid only with TBS\_HORZ. <br/>                                                                                                                                                                                                                                                      |
| <span id="TBS_BOTTOM"></span><span id="tbs_bottom"></span><dl> <dt>**TBS\_BOTTOM**</dt> </dl>                               | The trackbar control displays tick marks below the control. This style is valid only with TBS\_HORZ. <br/>                                                                                                                                                                                                                                                      |
| <span id="TBS_LEFT"></span><span id="tbs_left"></span><dl> <dt>**TBS\_LEFT**</dt> </dl>                                     | The trackbar control displays tick marks to the left of the control. This style is valid only with TBS\_VERT. <br/>                                                                                                                                                                                                                                             |
| <span id="TBS_RIGHT"></span><span id="tbs_right"></span><dl> <dt>**TBS\_RIGHT**</dt> </dl>                                  | The trackbar control displays tick marks to the right of the control. This style is valid only with TBS\_VERT. <br/>                                                                                                                                                                                                                                            |
| <span id="TBS_BOTH"></span><span id="tbs_both"></span><dl> <dt>**TBS\_BOTH**</dt> </dl>                                     | The trackbar control displays tick marks on both sides of the control. This will be both top and bottom when used with TBS\_HORZ or both left and right if used with TBS\_VERT. <br/>                                                                                                                                                                           |
| <span id="TBS_NOTICKS"></span><span id="tbs_noticks"></span><dl> <dt>**TBS\_NOTICKS**</dt> </dl>                            | The trackbar control does not display any tick marks. <br/>                                                                                                                                                                                                                                                                                                     |
| <span id="TBS_ENABLESELRANGE"></span><span id="tbs_enableselrange"></span><dl> <dt>**TBS\_ENABLESELRANGE**</dt> </dl>       | The trackbar control displays a selection range only. The tick marks at the starting and ending positions of a selection range are displayed as triangles (instead of vertical dashes), and the selection range is highlighted. <br/>                                                                                                                           |
| <span id="TBS_FIXEDLENGTH"></span><span id="tbs_fixedlength"></span><dl> <dt>**TBS\_FIXEDLENGTH**</dt> </dl>                | The trackbar control allows the size of the slider to be changed with the [**TBM\_SETTHUMBLENGTH**](tbm-setthumblength.md) message. <br/>                                                                                                                                                                                                                      |
| <span id="TBS_NOTHUMB"></span><span id="tbs_nothumb"></span><dl> <dt>**TBS\_NOTHUMB**</dt> </dl>                            | The trackbar control does not display a slider. <br/>                                                                                                                                                                                                                                                                                                           |
| <span id="TBS_TOOLTIPS"></span><span id="tbs_tooltips"></span><dl> <dt>**TBS\_TOOLTIPS**</dt> </dl>                         | [Version 4.70](common-control-versions.md). The trackbar control supports tooltips. When a trackbar control is created using this style, it automatically creates a default tooltip control that displays the slider's current position. You can change where the tooltips are displayed by using the [**TBM\_SETTIPSIDE**](tbm-settipside.md) message. <br/> |
| <span id="TBS_REVERSED"></span><span id="tbs_reversed"></span><dl> <dt>**TBS\_REVERSED**</dt> </dl>                         | [Version 5.80.](common-control-versions.md)This style bit is used for "reversed" trackbars, where a smaller number indicates "higher" and a larger number indicates "lower." It has no effect on the control; it is simply a label that can be checked to determine whether a trackbar is normal or reversed.<br/>                                             |
| <span id="TBS_DOWNISLEFT"></span><span id="tbs_downisleft"></span><dl> <dt>**TBS\_DOWNISLEFT**</dt> </dl>                   | By default, the trackbar control uses down equal to right and up equal to left. Use the TBS\_DOWNISLEFT style to reverse the default, making down equal left and up equal right. <br/>                                                                                                                                                                          |
| <span id="TBS_NOTIFYBEFOREMOVE"></span><span id="tbs_notifybeforemove"></span><dl> <dt>**TBS\_NOTIFYBEFOREMOVE**</dt> </dl> | [Version 6.00](common-control-versions.md) and **Windows Vista.** Trackbar should notify parent before repositioning the slider due to user action (enables snapping). <br/>                                                                                                                                                                                   |
| <span id="TBS_TRANSPARENTBKGND"></span><span id="tbs_transparentbkgnd"></span><dl> <dt>**TBS\_TRANSPARENTBKGND**</dt> </dl> | [Version 6.00](common-control-versions.md) and **Windows Vista.** Background is painted by the parent via the WM\_PRINTCLIENT message. <br/>                                                                                                                                                                                                                   |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





