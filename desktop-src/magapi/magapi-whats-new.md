---
title: What's New
description: This topic summarizes the changes that were made to the Magnification API for Windows 8.
ms.assetid: 62ADB373-1B5A-4B68-A376-DB5CE8813EBE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New

This topic summarizes the changes that were made to the Magnification API for Windows 8. The following sections describe the changes:

-   [Full-Screen Magnifiers](#full-screen-magnifiers)
-   [Input Transformations](#input-transformations)
-   [Visibility of the System Cursor](#visibility-of-the-system-cursor)
-   [Updated Magnifier Sample Application](#updated-magnifier-sample-application)
-   [Related topics](#related-topics)

## Full-Screen Magnifiers

The following functions were added to support a full-screen magnifier, and to apply color effects to the magnified screen content.



| Topic                                                                                | Description                                                                                     |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**MagGetFullscreenColorEffect**](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetfullscreencoloreffect)<br/> | Retrieves the color transformation matrix associated with the full-screen magnifier.<br/> |
| [**MagGetFullscreenTransform**](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetfullscreentransform)<br/>     | Retrieves the magnification settings for the full-screen magnifier.<br/>                  |
| [**MagSetFullscreenColorEffect**](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetfullscreencoloreffect)<br/> | Changes the color transformation matrix associated with the full-screen magnifier.<br/>   |
| [**MagSetFullscreenTransform**](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetfullscreentransform)<br/>     | Changes the magnification settings for the full-screen magnifier.<br/>                    |



 

## Input Transformations

An input transformation maps the coordinate space of the magnified screen content to the actual (unmagnified) screen coordinate space. This mapping ensures that pen and touch input in magnified screen content is mapped to the appropriate coordinates of the unmagnified screen. The following functions were added to support input transformations.



| Topic                                                                  | Description                                            |
|------------------------------------------------------------------------|--------------------------------------------------------|
| [**MagGetInputTransform**](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetinputtransform)<br/> | Retrieves the current input transformation.<br/> |
| [**MagSetInputTransform**](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetinputtransform)<br/> | Sets the input transformation.<br/>              |



 

## Visibility of the System Cursor

The following function was added to enable showing or hiding the system cursor.



| Topic                                                                | Description                                  |
|----------------------------------------------------------------------|----------------------------------------------|
| [**MagShowSystemCursor**](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magshowsystemcursor)<br/> | Shows or hides the system cursor.<br/> |



 

## Updated Magnifier Sample Application

The magnifier sample application was updated to demonstrate the full-screen and cursor hiding capabilities of the new API functions. For more information, see [Magnification API Sample](http://go.microsoft.com/fwlink/p/?linkid=230729).

## Related topics

<dl> <dt>

[Magnification API](entry-magapi-sdk.md)
</dt> </dl>

 

 





