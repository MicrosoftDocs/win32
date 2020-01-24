---
title: Appendix A Supported User Interface Elements Reference
description: This appendix contains information about the system-provided UI elements exposed by Microsoft Active Accessibility in Windows 95, Windows 98, Microsoft Windows NT, Windows 2000, Windows XP, and Windows 2000 Server.
ms.assetid: 5d0a81d8-5d36-4c33-bb8c-abcb8b00166e
ms.topic: article
ms.date: 05/31/2018
---

# Appendix A: Supported User Interface Elements Reference

This appendix contains information about the system-provided UI elements exposed by Microsoft Active Accessibility in Windows 95, Windows 98, Microsoft Windows NT, Windows 2000, Windows XP, and Windows 2000 Server. This support allows client utilities to get information about system-provided UI elements in applications that do not implement Microsoft Active Accessibility.

Oleacc.dll supports controls that are defined in User32.dll, Comctl32.dll, and Windows UI elements. Specifically, it supports the following types of UI elements (listed by Windows class name).



| Windows class name                   | UI element type                                         | Windows Vista updates                                                                                                                                                                                                |
|--------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ListBox                              | List boxes                                              | None                                                                                                                                                                                                                 |
| Button                               | Push buttons, radio buttons, check buttons, group boxes | Split buttons can have zero or more children.                                                                                                                                                                        |
| Static                               | Labels                                                  | None                                                                                                                                                                                                                 |
| Edit                                 | Text boxes                                              | None                                                                                                                                                                                                                 |
| ComboBox                             | Combo boxes, drop-down lists                            | None                                                                                                                                                                                                                 |
| ScrollBar                            | Scroll bars                                             | [**EVENT\_OBJECT\_CONTENTSCROLLED**](event-constants.md) is a new event for control that have scrolling functionality but do not include a standard scroll bar as part of the control. |
| \#32768                              | USER menus                                              | None                                                                                                                                                                                                                 |
| \#32770                              | USER dialog boxes                                       | None                                                                                                                                                                                                                 |
| \#32771                              | Alt-tab window                                          | Available only in classic mode.                                                                                                                                                                                      |
| msctls\_statusbar32                  | Status bars                                             | None                                                                                                                                                                                                                 |
| msctls\_progress32                   | Progress bars                                           | New color options for progress bars are not exposed by Microsoft Active Accessibility or Microsoft UI Automation properties.                                                                                         |
| msctls\_hotkey32                     | Hot key controls                                        | None                                                                                                                                                                                                                 |
| msctls\_trackbar32                   | Trackbars, sliders                                      | None                                                                                                                                                                                                                 |
| msctls\_updown32                     | Up-down or spin controls                                | None                                                                                                                                                                                                                 |
| SysAnimate32                         | Animation control                                       | None                                                                                                                                                                                                                 |
| SysTabControl32                      | Tab control                                             | None                                                                                                                                                                                                                 |
| SysHeader32                          | List view headers                                       | None                                                                                                                                                                                                                 |
| SysListView32                        | List view controls                                      | None                                                                                                                                                                                                                 |
| SysTreeView32                        | Tree view controls                                      | None                                                                                                                                                                                                                 |
| SysDateTimePick32 (versions 5 and 6) | Date and/or time picker                                 | Version 6 of this control in Windows Vista has a native [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) implementation.                                                                                                           |
| SysIPAddress32                       | IP address controls                                     | None                                                                                                                                                                                                                 |
| tooltips\_class32                    | ToolTips                                                | None                                                                                                                                                                                                                 |
| ToolbarWindow32                      | Toolbars                                                | None                                                                                                                                                                                                                 |
| RICHEDIT, RichEdit20A, RichEdit20W   | Text fields                                             | None                                                                                                                                                                                                                 |
| SysMonthCal32 (versions 5 and 6)     | Month calendar                                          | Version 6 of this control in Windows Vista has a native [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) implementation.                                                                                                           |



 

Although some support for system-provided UI elements is provided by Microsoft Active Accessibility on Microsoft Windows NT 4.0 with service pack 4, this support is limited.

This appendix lists the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties and methods that Microsoft Active Accessibility supports for each UI element. Where applicable, the documentation also lists the [WinEvents](winevents-infrastructure.md) that the UI element triggers and includes additional information about the supported properties and methods. It also includes information about object roles and their supported **IAccessible** methods and properties.

These details can help client developers avoid making unnecessary calls to unsupported properties and methods. This information also lets server developers know which properties and methods their custom controls should support and which WinEvents their controls should trigger.

Use the information in this appendix as a guide. We strongly suggest that you use the Microsoft Active Accessibility tools to verify expected behavior for UI elements or object roles.

For more information, see the following topics:

-   [How Active Accessibility Exposes User Interface Elements](how-active-accessibility-exposes-user-interface-elements.md)
-   [User Interface Element Reference](user-interface-element-reference.md)

 

 




