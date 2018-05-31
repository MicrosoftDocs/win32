---
title: DVD Applications in Visual Basic (Video Control)
description: DVD Applications in Visual Basic (Video Control)
ms.assetid: 2330ddf5-4188-4aee-837e-814e83f39cbb
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DVD Applications in Visual Basic (Video Control)

This topic applies to Windows XP Service Pack 1 or later.

Microsoft® DirectShow® provides several objects to control DVD playback. These include the **MSWebDVD** object, the **MSVidWebDVD** object, and the [DVD Navigator](https://msdn.microsoft.com/library/windows/desktop/dd388609) filter. The recommended object is the MSVidWebDVD object, which provides all the capabilities of the **MSWebDVD** object, but is used in tandem with the Video Control which provides a range of additional abilities.

All DVD control objects actually use the DVD Navigator filter behind the scenes to access and control the DVD player. But unlike DVD Navigator filter, the **MSVidWebDVD** object handles mouse clicks and automates graph building. And unlike **MSWebDVD**, **MSVidWebDVD** is associated with the Video Control, to allow digital and analog television tuning as well as broadcast IP data services, all in the same screen space. This document describes the Microsoft Visual Basic® control of this object.

The **MSVidWebDVD** object operates in tandem with the **MSVidCtl** Microsoft ActiveX® control (also called the Video Control), and together they provide analog and digital television tuning, broadcast IP data services, file playback, and DVD playback for video or karaoke discs. **MSVidCtl** and **MSVidWebDVD** can be embedded in a Windows form or Web page, and can be controlled with Visual Basic, HTML scripting, or C++ in Microsoft Foundation Class or ATL forms.

To create the **MSVidWebDVD** object, you need Microsoft Windows XP and a DVD decoder installed on your computer. Currently, most codecs are suitable for either DVD play or digital television tuning, but not both. You cannot simultaneously register multiple codecs to handle both, so you may have to unregister existing codecs to register a DVD-capable codec that works with the Video Mixing Renderer. Although there is not now a method to determine if your codec is correct, a good rule of thumb is to use only Windows Hardware Quality Labs (WHQL) certified codecs. If you register a new video codec, be sure to uninstall the older codec by using **regsvr32** with the **/u** command line switch.

This section contains the following topics:

-   [Creating the MSVidWebDVD Object](creating-the-msvidwebdvd-object.md)
-   [Controlling Playback](controlling-playback.md)
-   [Menus and Buttons](menus-and-buttons.md)
-   [Audio Streams: Controlling Spoken Language](audio-streams--controlling-spoken-language.md)
-   [Subpicture Streams: Controlling Subtitles](subpicture-streams--controlling-subtitles.md)
-   [Angle Blocks](angle-blocks.md)
-   [Parental Management](parental-management.md)
-   [Text Strings](text-strings.md)
-   [DVD Error Handling](dvd-error-handling.md)

## Related topics

<dl> <dt>

[DVD Basics](https://msdn.microsoft.com/library/windows/desktop/dd388582)
</dt> <dt>

[Using the Video Control](using-the-video-control.md)
</dt> </dl>

 

 




