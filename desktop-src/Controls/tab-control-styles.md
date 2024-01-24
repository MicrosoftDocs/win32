---
title: Tab Control Styles (CommCtrl.h)
description: This section lists supported tab control styles.
ms.assetid: a01a6609-b02e-4ada-afa0-ed5ad8dde0d6
topic_type:
- apiref
api_name:
- TCS_BOTTOM
- TCS_BUTTONS
- TCS_FIXEDWIDTH
- TCS_FLATBUTTONS
- TCS_FOCUSNEVER
- TCS_FOCUSONBUTTONDOWN
- TCS_FORCEICONLEFT
- TCS_FORCELABELLEFT
- TCS_HOTTRACK
- TCS_MULTILINE
- TCS_MULTISELECT
- TCS_OWNERDRAWFIXED
- TCS_RAGGEDRIGHT
- TCS_RIGHT
- TCS_RIGHTJUSTIFY
- TCS_SCROLLOPPOSITE
- TCS_SINGLELINE
- TCS_TABS
- TCS_TOOLTIPS
- TCS_VERTICAL
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Tab Control Styles

This section lists supported tab control styles.



| Constant                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                    |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TCS_BOTTOM"></span><span id="tcs_bottom"></span><dl> <dt>**TCS\_BOTTOM**</dt> </dl>                                  | [Version 4.70](common-control-versions.md). Tabs appear at the bottom of the control. This value equals TCS\_RIGHT. This style is not supported if you use ComCtl32.dll version 6.<br/>                                                                                                                                                                 |
| <span id="TCS_BUTTONS"></span><span id="tcs_buttons"></span><dl> <dt>**TCS\_BUTTONS**</dt> </dl>                               | Tabs appear as buttons, and no border is drawn around the display area.<br/>                                                                                                                                                                                                                                                                             |
| <span id="TCS_FIXEDWIDTH"></span><span id="tcs_fixedwidth"></span><dl> <dt>**TCS\_FIXEDWIDTH**</dt> </dl>                      | All tabs are the same width. This style cannot be combined with the TCS\_RIGHTJUSTIFY style.<br/>                                                                                                                                                                                                                                                        |
| <span id="TCS_FLATBUTTONS"></span><span id="tcs_flatbuttons"></span><dl> <dt>**TCS\_FLATBUTTONS**</dt> </dl>                   | [Version 4.71](common-control-versions.md). Selected tabs appear as being indented into the background while other tabs appear as being on the same plane as the background. This style only affects tab controls with the TCS\_BUTTONS style.<br/>                                                                                                     |
| <span id="TCS_FOCUSNEVER"></span><span id="tcs_focusnever"></span><dl> <dt>**TCS\_FOCUSNEVER**</dt> </dl>                      | The tab control does not receive the input focus when clicked.<br/>                                                                                                                                                                                                                                                                                      |
| <span id="TCS_FOCUSONBUTTONDOWN"></span><span id="tcs_focusonbuttondown"></span><dl> <dt>**TCS\_FOCUSONBUTTONDOWN**</dt> </dl> | The tab control receives the input focus when clicked.<br/>                                                                                                                                                                                                                                                                                              |
| <span id="TCS_FORCEICONLEFT"></span><span id="tcs_forceiconleft"></span><dl> <dt>**TCS\_FORCEICONLEFT**</dt> </dl>             | Icons are aligned with the left edge of each fixed-width tab. This style can only be used with the TCS\_FIXEDWIDTH style.<br/>                                                                                                                                                                                                                           |
| <span id="TCS_FORCELABELLEFT"></span><span id="tcs_forcelabelleft"></span><dl> <dt>**TCS\_FORCELABELLEFT**</dt> </dl>          | Labels are aligned with the left edge of each fixed-width tab; that is, the label is displayed immediately to the right of the icon instead of being centered. This style can only be used with the TCS\_FIXEDWIDTH style, and it implies the TCS\_FORCEICONLEFT style.<br/>                                                                             |
| <span id="TCS_HOTTRACK"></span><span id="tcs_hottrack"></span><dl> <dt>**TCS\_HOTTRACK**</dt> </dl>                            | [Version 4.70](common-control-versions.md). Items under the pointer are automatically highlighted. You can check whether hot tracking is enabled by calling [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa). <br/>                                                                                                                              |
| <span id="TCS_MULTILINE"></span><span id="tcs_multiline"></span><dl> <dt>**TCS\_MULTILINE**</dt> </dl>                         | Multiple rows of tabs are displayed, if necessary, so all tabs are visible at once.<br/>                                                                                                                                                                                                                                                                 |
| <span id="TCS_MULTISELECT"></span><span id="tcs_multiselect"></span><dl> <dt>**TCS\_MULTISELECT**</dt> </dl>                   | [Version 4.70](common-control-versions.md). Multiple tabs can be selected by holding down the CTRL key when clicking. This style must be used with the TCS\_BUTTONS style.<br/>                                                                                                                                                                         |
| <span id="TCS_OWNERDRAWFIXED"></span><span id="tcs_ownerdrawfixed"></span><dl> <dt>**TCS\_OWNERDRAWFIXED**</dt> </dl>          | The parent window is responsible for drawing tabs.<br/>                                                                                                                                                                                                                                                                                                  |
| <span id="TCS_RAGGEDRIGHT"></span><span id="tcs_raggedright"></span><dl> <dt>**TCS\_RAGGEDRIGHT**</dt> </dl>                   | Rows of tabs will not be stretched to fill the entire width of the control. This style is the default.<br/>                                                                                                                                                                                                                                              |
| <span id="TCS_RIGHT"></span><span id="tcs_right"></span><dl> <dt>**TCS\_RIGHT**</dt> </dl>                                     | [Version 4.70](common-control-versions.md). Tabs appear vertically on the right side of controls that use the TCS\_VERTICAL style. This value equals TCS\_BOTTOM. This style is not supported if you use visual styles.<br/>                                                                                                                            |
| <span id="TCS_RIGHTJUSTIFY"></span><span id="tcs_rightjustify"></span><dl> <dt>**TCS\_RIGHTJUSTIFY**</dt> </dl>                | The width of each tab is increased, if necessary, so that each row of tabs fills the entire width of the tab control. This window style is ignored unless the TCS\_MULTILINE style is also specified.<br/>                                                                                                                                               |
| <span id="TCS_SCROLLOPPOSITE"></span><span id="tcs_scrollopposite"></span><dl> <dt>**TCS\_SCROLLOPPOSITE**</dt> </dl>          | [Version 4.70](common-control-versions.md). Unneeded tabs scroll to the opposite side of the control when a tab is selected.<br/>                                                                                                                                                                                                                       |
| <span id="TCS_SINGLELINE"></span><span id="tcs_singleline"></span><dl> <dt>**TCS\_SINGLELINE**</dt> </dl>                      | Only one row of tabs is displayed. The user can scroll to see more tabs, if necessary. This style is the default.<br/>                                                                                                                                                                                                                                   |
| <span id="TCS_TABS"></span><span id="tcs_tabs"></span><dl> <dt>**TCS\_TABS**</dt> </dl>                                        | Tabs appear as tabs, and a border is drawn around the display area. This style is the default.<br/>                                                                                                                                                                                                                                                      |
| <span id="TCS_TOOLTIPS"></span><span id="tcs_tooltips"></span><dl> <dt>**TCS\_TOOLTIPS**</dt> </dl>                            | The tab control has a tooltip control associated with it. <br/>                                                                                                                                                                                                                                                                                          |
| <span id="TCS_VERTICAL"></span><span id="tcs_vertical"></span><dl> <dt>**TCS\_VERTICAL**</dt> </dl>                            | [Version 4.70](common-control-versions.md). Tabs appear at the left side of the control, with tab text displayed vertically. This style is valid only when used with the TCS\_MULTILINE style. To make tabs appear on the right side of the control, also use the TCS\_RIGHT style. This style is not supported if you use ComCtl32.dll version 6.<br/> |



## Remarks

The following styles can be modified after the control is created.

-   TCS\_BOTTOM
-   TCS\_BUTTONS
-   TCS\_FIXEDWIDTH
-   TCS\_FLATBUTTONS
-   TCS\_FORCEICONLEFT
-   TCS\_FORCELABELLEFT
-   TCS\_MULTILINE
-   TCS\_OWNERDRAWFIXED
-   TCS\_RAGGEDRIGHT
-   TCS\_RIGHT
-   TCS\_VERTICAL

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

