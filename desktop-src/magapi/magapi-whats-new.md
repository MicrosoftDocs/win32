---
title: Whats New
description: This topic summarizes the changes that were made to the Magnification API for Windows 8.
ms.assetid: 62ADB373-1B5A-4B68-A376-DB5CE8813EBE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**MagGetFullscreenColorEffect**](/windows/previous-versions/Magnification/nf-magnification-maggetfullscreencoloreffect?branch=master)<br/> | Retrieves the color transformation matrix associated with the full-screen magnifier.<br/> |
| [**MagGetFullscreenTransform**](/windows/previous-versions/Magnification/nf-magnification-maggetfullscreentransform?branch=master)<br/>     | Retrieves the magnification settings for the full-screen magnifier.<br/>                  |
| [**MagSetFullscreenColorEffect**](/windows/previous-versions/Magnification/nf-magnification-magsetfullscreencoloreffect?branch=master)<br/> | Changes the color transformation matrix associated with the full-screen magnifier.<br/>   |
| [**MagSetFullscreenTransform**](/windows/previous-versions/Magnification/nf-magnification-magsetfullscreentransform?branch=master)<br/>     | Changes the magnification settings for the full-screen magnifier.<br/>                    |



 

## Input Transformations

An input transformation maps the coordinate space of the magnified screen content to the actual (unmagnified) screen coordinate space. This mapping ensures that pen and touch input in magnified screen content is mapped to the appropriate coordinates of the unmagnified screen. The following functions were added to support input transformations.



| Topic                                                                  | Description                                            |
|------------------------------------------------------------------------|--------------------------------------------------------|
| [**MagGetInputTransform**](/windows/previous-versions/Magnification/nf-magnification-maggetinputtransform?branch=master)<br/> | Retrieves the current input transformation.<br/> |
| [**MagSetInputTransform**](/windows/previous-versions/Magnification/nf-magnification-magsetinputtransform?branch=master)<br/> | Sets the input transformation.<br/>              |



 

## Visibility of the System Cursor

The following function was added to enable showing or hiding the system cursor.



| Topic                                                                | Description                                  |
|----------------------------------------------------------------------|----------------------------------------------|
| [**MagShowSystemCursor**](/windows/previous-versions/Magnification/nf-magnification-magshowsystemcursor?branch=master)<br/> | Shows or hides the system cursor.<br/> |



 

## Updated Magnifier Sample Application

The magnifier sample application was updated to demonstrate the full-screen and cursor hiding capabilities of the new API functions. For more information, see [Magnification API Sample](http://go.microsoft.com/fwlink/p/?linkid=230729).

## Related topics

<dl> <dt>

[Magnification API](entry-magapi-sdk.md)
</dt> </dl>

 

 





