---
title: UI Automation Support for Standard Controls
description: This topic identifies the standard Windows controls that are supported by Microsoft UI Automation. Full support is provided only for controls from version 6 of ComCtrl32.dll (available with Windows XP and later).
ms.assetid: 4821684c-8a90-413c-8ddc-699926e3bb09
keywords:
- clients,UI Automation support for standard controls
- clients,standard control support
- clients,Win32 controls
- UI Automation,support for standard controls
- UI Automation,standard control support
- UI Automation,Win32 controls
- support for standard controls
- standard control support
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation Support for Standard Controls

This topic identifies the standard Windows controls that are supported by Microsoft UI Automation. Full support is provided only for controls from version 6 of ComCtrl32.dll (available with Windows XP and later).

> [!Note]  
> The RichEdit control is supported only for versions shipped with Windows Vista (in RichEd20.dll version 3.1 and later, and MsftEdit.dll version 4.1 and later).

 

The following table lists the class names of the supported standard controls, along with the corresponding UI Automation control types.



| Class Name          | Control Type        |
|---------------------|---------------------|
| Button              | Button              |
| Button              | RadioButton         |
| Button              | Group               |
| Button              | CheckBox            |
| Button              | Hyperlink           |
| Button              | SplitButton         |
| Button              | CheckBox            |
| ComboBoxEx32        | ComboBox            |
| ComboBox            | ComboBox            |
| Edit                | Document            |
| Edit                | Edit                |
| SysLink             | Hyperlink           |
| Static              | Text                |
| Static              | Image               |
| SysIPAddress32      | Custom              |
| SysHeader32         | Header/HeaderItem   |
| SysListView32       | DataGrid            |
| SysListView32       | List                |
| ListBox             | List                |
| ListBox             | ListItem            |
| \#32768             | Menu                |
| \#32768             | MenuItem            |
| msctls\_progress32  | ProgressBar         |
| RichEdit            | Document. See note. |
| RichEdit20A         | Document            |
| RichEdit20W         | Document            |
| RichEdit50W         | Document            |
| ScrollBar           | Slider              |
| msctls\_trackbar32  | Slider              |
| msctls\_updown32    | Spinner             |
| msctls\_statusbar32 | StatusBar           |
| SysTabControl32     | Tab                 |
| SysTabControl32     | TabItem             |
| ToolbarWindow32     | ToolBar             |
| ToolbarWindow32     | MenuItem            |
| ToolbarWindow32     | Button              |
| ToolbarWindow32     | CheckBox            |
| ToolbarWindow32     | RadioButton         |
| ToolbarWindow32     | Separator           |
| tooltips\_class32   | ToolTip             |
| \#32774             | ToolTip             |
| ReBarWindow32       | Toolbar             |
| SysTreeView32       | Tree                |
| SysTreeView32       | TreeItem            |



 

The controls listed in the following table are not supported.



| Class Name                                    | Control Type |
|-----------------------------------------------|--------------|
| SysAnimate32                                  | Image        |
| SysPager                                      | Spinner      |
| SysDateTimePick32                             | Custom       |
| SysMonthCal32                                 | Calendar     |
| MS\_WINNOTE                                   | Tooltip      |
| VBBubble                                      | Tooltip      |
| ScrollBar (when used as a standalone control) | Slider       |
| SuperGrid                                     | Custom       |



 

## Related topics

<dl> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> </dl>

 

 




