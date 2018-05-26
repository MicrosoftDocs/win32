---
title: Menus and Buttons
description: Menus and Buttons
ms.assetid: ab2bb143-6b55-4628-aa05-1bd7c5b4018e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Menus and Buttons

This topic applies to Windows XP Service Pack 1 or later.

Menus are the full-page navigational splash screens designed by the DVD author that occur at the beginning of the DVD, and may appear elsewhere in the disc. Buttons are the selection items on the menu screens, rather than the buttons in the hosting form or Web page.

The **MSVidWebDVD** object automatically handles menu commands when the user clicks on the on-screen buttons with the mouse. An application does not need to do anything to implement basic mouse support. But an application can override this automatic mouse handling at any time in order to cause additional actions to take place when a user clicks on a menu button. For example, you could cause certain text or images to be displayed on a Web page depending on which button the user clicks. To implement custom mouse handling, use the **MSVidWebDVD** menu-related methods such as [**SelectAndActivateButton**](mstv-msvidwebdvd_selectandactivatebutton_method) and [**ButtonAtPosition**](mstv-msvidwebdvd_buttonatposition_property).

The **MSVidWebDVD** also offers a set of methods (for example, [**SelectUpperButton**](mstv-msvidwebdvd_selectupperbutton_method)) which allow you to display an image map on your form representing a DVD remote control, with buttons that move the current button selection up, down, right and left. These buttons are referred to as "directional" or "relative" buttons in the documentation.

## Related topics

<dl> <dt>

[DVD Applications in Visual Basic (Video Control)](dvd-applications-in-visual-basic--video-control.md)
</dt> </dl>

 

 




