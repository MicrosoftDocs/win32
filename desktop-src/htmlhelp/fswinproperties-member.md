---
title: fsWinProperties Member
description: fsWinProperties Member
ms.assetid: F76EE396-E147-4795-BB6A-78DBC4201118
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# fsWinProperties Member

The *fsWinProperties* member is used to define various properties for a help window, and is also used to control how the window is created.

This member can be a combination of one or more of the following values.



| Value                        | Description                                                                                                                                                                                                                                                                      |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HHWIN\_PROP\_AUTO\_SYNC      | Locates and selects the contents or index entry (depending on whether the Contents or Index tab is selected in the Navigation pane) for the help topic that appears in the Help Viewer. If the topic cannot be located in the Navigation pane, no action is taken.<br/>    |
| HHWIN\_PROP\_CHANGE\_TITLE   | Changes the title bar of the Help Viewer to match the title of the topic that appears in the Topic pane.                                                                                                                                                                         |
| HHWIN\_PROP\_NAV\_ONLY\_WIN  | Specifies that the window only contain a Navigation pane and toolbar. No topics can appear in this Help Viewer.                                                                                                                                                                  |
| HHWIN\_PROP\_NODEF\_EXSTYLES | Specifies that the window use no default extended styles when it is created. If used in combination with the HHWIN\_PROP\_ONTOP flag, the HHWIN\_PROP\_ONTOP flag is ignored.                                                                                                    |
| HHWIN\_PROP\_NODEF\_STYLES   | Specifies that the window not use default styles when it is created. If this flag is not specified, the window is created with the following default styles: WS\_THICKFRAME \| WS\_OVERLAPPED \| WS\_VISIBLE <br/>                                                         |
| HHWIN\_PROP\_NOTB\_TEXT      | Specifies that the buttons on the toolbar of the Help Viewer not contain text below the icon.                                                                                                                                                                                    |
| HHWIN\_PROP\_NOTITLEBAR      | Creates a window without a title bar.                                                                                                                                                                                                                                            |
| HHWIN\_PROP\_NO\_TOOLBAR     | Creates a window without a toolbar.                                                                                                                                                                                                                                              |
| HHWIN\_PROP\_ONTOP           | Creates a window that stays on top of all windows on the desktop rather than staying on top of only the calling window.                                                                                                                                                          |
| HHWIN\_PROP\_TAB\_ADVSEARCH  | Creates a window whose Navigation pane includes a full-text Search tab. If HHWIN\_PROP\_TAB\_SEARCH is not specified as a value for *fsWinProperties*, no Search tab will appear, whether or not the compiled help (.chm) file includes full-text search information.<br/> |
| HHWIN\_PROP\_TAB\_FAVORITES  | Creates a window whose Navigation pane includes a Favorites tab.                                                                                                                                                                                                                 |
| HHWIN\_PROP\_TAB\_SEARCH     | Creates a window whose Navigation pane includes a Search tab.                                                                                                                                                                                                                    |
| HHWIN\_PROP\_TRACKING        | Enables HTML Help notification messages to be sent to the window specified in *hwndCaller*.                                                                                                                                                                                      |
| HHWIN\_PROP\_TRI\_PANE       | Creates the HTML Help Viewer (with a Topic pane, Navigation pane, and toolbar). After a window has been created, this flag cannot be used to modify the existing window.<br/>                                                                                              |
| HHWIN\_PROP\_USER\_POS       | If the user resizes or repositions the help window, this size/position will be used when the compiled help file is opened again. Without this setting, the window always appears in the same size/position.                                                                      |



 

## Related topics

<dl> <dt>

[**Back to HH\_WINTYPE**](/previous-versions/windows/desktop/api/HtmlHelp/ns-htmlhelp-taghh_wintype)
</dt> </dl>

 

 





