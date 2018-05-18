---
title: About the HTML Help Viewer
description: About the HTML Help Viewer
ms.assetid: '9865D3D7-351D-4df6-B1BC-DAF2D725D298'
---

# About the HTML Help Viewer

The HTML Help Viewer is the standard three-pane help window in which a compiled help (.chm) file appears. Each pane of the Help Viewer can be manipulated through an [**HH\_WINTYPE**](hh-wintype-structure.md) structure.

The Help Viewer is shown below:

![](images/hh-viewer.gif)



| Pane                               | Description                                                                            |
|------------------------------------|----------------------------------------------------------------------------------------|
| Navigation Pane (*hwndNavigation*) | Contains all navigational elements, such as a Contents tab, Index tab, and Search tab. |
| Toolbar Pane (*hwndToolbar*)       | Contains one or more navigation buttons, such as Home, Refresh, and Stop.              |
| Topic Pane (*hwndHTML*)            | Displays the selected help topic, or the default help topic.                           |



 

> [!Note]  
> The parent help window (*hwndHelp*) can be used to manipulate the entire Help Viewer and all of its panes.

 

## Related topics

<dl> <dt>

[About Window Types](window-types.md)
</dt> </dl>

 

 




