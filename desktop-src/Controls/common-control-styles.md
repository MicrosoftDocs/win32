---
title: Common Control Styles (CommCtrl.h)
description: This section lists common control styles. Except where noted, these styles apply to rebar controls, toolbar controls, and status windows.
ms.assetid: aab0cd68-ede7-474b-8695-c75805669716
topic_type:
- apiref
api_name:
- CCS_ADJUSTABLE
- CCS_BOTTOM
- CCS_LEFT
- CCS_NODIVIDER
- CCS_NOMOVEX
- CCS_NOMOVEY
- CCS_NOPARENTALIGN
- CCS_NORESIZE
- CCS_RIGHT
- CCS_TOP
- CCS_VERT
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Common Control Styles

This section lists common control styles. Except where noted, these styles apply to rebar controls, toolbar controls, and status windows.



| Constant                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                           |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CCS_ADJUSTABLE"></span><span id="ccs_adjustable"></span><dl> <dt>**CCS\_ADJUSTABLE**</dt> </dl>          | Enables a toolbar's built-in customization features, which let the user to drag a button to a new position or to remove a button by dragging it off the toolbar. In addition, the user can double-click the toolbar to display the **Customize Toolbar** dialog box, which enables the user to add, delete, and rearrange toolbar buttons.<br/> |
| <span id="CCS_BOTTOM"></span><span id="ccs_bottom"></span><dl> <dt>**CCS\_BOTTOM**</dt> </dl>                      | Causes the control to position itself at the bottom of the parent window's client area and sets the width to be the same as the parent window's width. Status windows have this style by default.<br/>                                                                                                                                          |
| <span id="CCS_LEFT"></span><span id="ccs_left"></span><dl> <dt>**CCS\_LEFT**</dt> </dl>                            | [Version 4.70](common-controls-intro.md). Causes the control to be displayed vertically on the left side of the parent window.<br/>                                                                                                                                                                                                            |
| <span id="CCS_NODIVIDER"></span><span id="ccs_nodivider"></span><dl> <dt>**CCS\_NODIVIDER**</dt> </dl>             | Prevents a two-pixel highlight from being drawn at the top of the control. <br/>                                                                                                                                                                                                                                                                |
| <span id="CCS_NOMOVEX"></span><span id="ccs_nomovex"></span><dl> <dt>**CCS\_NOMOVEX**</dt> </dl>                   | [Version 4.70](common-controls-intro.md). Causes the control to resize and move itself vertically, but not horizontally, in response to a [**WM\_SIZE**](/windows/desktop/winmsg/wm-size) message. If CCS\_NORESIZE is used, this style does not apply.<br/>                                                                                                    |
| <span id="CCS_NOMOVEY"></span><span id="ccs_nomovey"></span><dl> <dt>**CCS\_NOMOVEY**</dt> </dl>                   | Causes the control to resize and move itself horizontally, but not vertically, in response to a [**WM\_SIZE**](/windows/desktop/winmsg/wm-size) message. If CCS\_NORESIZE is used, this style does not apply. Header windows have this style by default.<br/>                                                                                                    |
| <span id="CCS_NOPARENTALIGN"></span><span id="ccs_noparentalign"></span><dl> <dt>**CCS\_NOPARENTALIGN**</dt> </dl> | Prevents the control from automatically moving to the top or bottom of the parent window. Instead, the control keeps its position within the parent window despite changes to the size of the parent. If CCS\_TOP or CCS\_BOTTOM is also used, the height is adjusted to the default, but the position and width remain unchanged. <br/>        |
| <span id="CCS_NORESIZE"></span><span id="ccs_noresize"></span><dl> <dt>**CCS\_NORESIZE**</dt> </dl>                | Prevents the control from using the default width and height when setting its initial size or a new size. Instead, the control uses the width and height specified in the request for creation or sizing. <br/>                                                                                                                                 |
| <span id="CCS_RIGHT"></span><span id="ccs_right"></span><dl> <dt>**CCS\_RIGHT**</dt> </dl>                         | [Version 4.70](common-controls-intro.md). Causes the control to be displayed vertically on the right side of the parent window.<br/>                                                                                                                                                                                                           |
| <span id="CCS_TOP"></span><span id="ccs_top"></span><dl> <dt>**CCS\_TOP**</dt> </dl>                               | Causes the control to position itself at the top of the parent window's client area and sets the width to be the same as the parent window's width. Toolbars have this style by default. <br/>                                                                                                                                                  |
| <span id="CCS_VERT"></span><span id="ccs_vert"></span><dl> <dt>**CCS\_VERT**</dt> </dl>                            | [Version 4.70](common-controls-intro.md). Causes the control to be displayed vertically.<br/>                                                                                                                                                                                                                                                  |



## Remarks

The following topics describe additional control styles:

-   [**Animation Control Styles**](animation-control-styles.md)
-   [**Button Styles**](button-styles.md)
-   [**Combo Box Styles**](combo-box-styles.md)
-   [**ComboBoxEx Control Extended Styles**](comboboxex-control-extended-styles.md)
-   [**Date and Time Picker Control Styles**](date-and-time-picker-control-styles.md)
-   [**Edit Control Styles**](edit-control-styles.md)
-   [**Header Control Styles**](header-control-styles.md)
-   [**List Box Styles**](list-box-styles.md)
-   [**List-View Window Styles**](list-view-window-styles.md)
-   [**Month Calendar Control Styles**](month-calendar-control-styles.md)
-   [**Pager Control Styles**](pager-control-styles.md)
-   [**Progress Bar Control Styles**](progress-bar-control-styles.md)
-   [**Rebar Control Styles**](rebar-control-styles.md)
-   [**Rich Edit Control Styles**](rich-edit-control-styles.md)
-   [**Scroll Bar Control Styles**](scroll-bar-control-styles.md)
-   [Static Control Styles](static-control-styles.md)
-   [**Status Bar Styles**](status-bar-styles.md)
-   [**SysLink Control Styles**](syslink-control-styles.md)
-   [**Tab Control Styles**](tab-control-styles.md)
-   [**Toolbar Control and Button Styles**](toolbar-control-and-button-styles.md)
-   [**Tooltip Styles**](tooltip-styles.md)
-   [**Trackbar Control Styles**](trackbar-control-styles.md)
-   [**Tree-View Control Window Styles**](tree-view-control-window-styles.md)
-   [**Up-Down Control Styles**](up-down-control-styles.md)

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

