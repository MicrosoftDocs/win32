---
title: HH\_SYNC command
description: Locates and selects the contents entry for the help topic that is open in the Topic pane of the HTML Help Viewer.
ms.assetid: EC3655CF-24F9-43b2-85CA-B1C356152ED2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HH\_SYNC command

Locates and selects the contents entry for the help topic that is open in the Topic pane of the HTML Help Viewer.



| *pszFile*                                                                                                                                                                                                                                                                                                         | *dwData*                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Specifies the name of the window type that you want to sync and the name of the compiled help (.chm) file in which the window type is defined. The window type name must begin with a greater-than (&gt;) character and must be preceded by the name of the compiled help file in which it is defined.<br/> | Specifies a pointer to a topic within a compiled help file. This value is the topic file to which the contents will synchronize. |



 

## Example


```
HtmlHelp(
         hwndCaller,
         "..\\MyHelpFile.chm>wintype",
         HH_SYNC,
         "MyHelpFile.chm::/html/MyTopic.htm") ;
```



## Remarks

-   This command requires that you specify a window type.
-   Calling this command is equivalent to clicking the Locate button on the toolbar of the Help Viewer.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 





