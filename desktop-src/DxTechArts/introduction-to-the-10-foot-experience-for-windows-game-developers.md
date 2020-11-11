---
title: Introduction to the 10-Foot Experience for Windows Game Developers
description: This article introduces the 10-foot experience and explores the list of things that you should consider first about this new interaction pattern, even if you aren't expecting your game to be played this way.
ms.assetid: 126a0aae-6a7a-8cda-5748-c364e54c304e
ms.topic: article
ms.date: 05/31/2018
---

# Introduction to the 10-Foot Experience for Windows Game Developers

A growing number of people are using their personal computers in a completely new way. When you think of typical interaction with a Windows-based computer, you probably envision sitting at a desk with a monitor, and using a mouse and keyboard (or perhaps a joystick device); this is referred to as the 2-foot experience, and it's still the most common scenario for Windows gaming, but there's another trend which you'll probably start hearing more about: the 10-foot experience, which describes using your computer as an entertainment device with output to a TV. This article introduces the 10-foot experience and explores the list of things that you should consider first about this new interaction pattern, even if you aren't expecting your game to be played this way. Some portion of your customers will run your Windows-based game on a computer running Windows Media Center—it's better that you know what that experience will be like before your customers try it.

-   [What is Windows Media Center?](#what-is-windows-media-center)
-   [The 10-Foot Experience](#the-10-foot-experience)
    -   [Installation](#installation)
    -   [User Input](#user-input)
    -   [Display](#display)
-   [Aspect Ratio and Widescreen](#aspect-ratio-and-widescreen)
-   [Title-Safe Region](#title-safe-region)
-   [NTSC Suggestions](#ntsc-suggestions)
    -   [Clamp the RGB color component values between 16 and 235](#clamp-the-rgb-color-component-values-between-16-and-235)
    -   [Avoid similar colors that might appear identical](#avoid-similar-colors-that-might-appear-identical)
    -   [Avoid sharp differences in contrast](#avoid-sharp-differences-in-contrast)
-   [Conclusion](#conclusion)

## What is Windows Media Center?

Windows Media Center can act as the interface to the multimedia capabilities of the host computer. The Web site for this feature, [Windows Media Center Home](https://windows.microsoft.com/windows/products/windows-media-center/), offers a thorough introduction and shows off all the good stuff available in the latest version. Media Center is included in Windows XP Media Center Edition, Windows Vista Home Premium, Windows Vista Ultimate, and most editions of Windows 7.

In the past, the only way to get Windows Media Center was to buy a Media Center PC from a tier-1 system manufacturer, but because Windows Media Center is now included with two editions of Windows Vista, the potential marketplace is now much larger.

## The 10-Foot Experience

Windows Media Center was designed around the idea that people could use Windows for a rich living room entertainment experience, and it follows that most users prefer to interact differently with Windows Media Center differently than with traditional computer applications. For one, if the customer uses the computer in the living room for entertainment, it's likely video is displayed on something other than a conventional computer monitor: analog TVs, high-definition digital TVs, and any number of LCD displays are all likely candidates. These types of displays are usually viewed from a distance of roughly 10 feet, hence the label *10-foot experience*.

The 10-foot experience isn't confined to users of Windows Media Center; it's become common in recent years for users to connect their workstation or notebook computer to their TV and audio system. It's increasingly common for consumer display devices to expose RGB or DVI connections, the standard video output ports on computers. In addition, S-Video ports are a typical feature of high-end video cards, and they offer an easy way to output to an alternate display device.

There are some important design guidelines which should be considered for a pleasant 10-foot experience: installation, user input, and display.

### Installation

During the average 2-foot experience, the user is within reaching distance of the computer; if during startup or gameplay, the user is required to insert or switch media, the user can at least remain seated. The average 10-foot experience places the computer across the room from the user, and therefore anything that requires the user to physically interact with the computer forces the user to get up and cross the room. For this reason, developers should avoid forcing the user to change media; consider allowing a complete installation of your application to the hard drive.

### User Input

Another feature of Windows Media Center is support for a standard remote control, which is the generally preferred input device. Although the genre of your game title largely decides whether the remote control is suitable for providing game input, you still might want to allow the user to pause the game and access in-game menus by using the remote control; however, make certain that you also allow the user to control the menus by using the primary game input device. For more information about designing and developing for Windows Media Center and its devices, see [Windows Media Center Software Development Kit](/previous-versions/msdn10/bb895967(v=msdn.10)) on MSDN.

Avoid any physical interaction between the user and the computer or its peripherals. Requiring the user to change input controllers during gameplay is undesirable, since he or she is likely to be near only the primary input device.

Microsoft has created common gamepad controllers for use with both Windows and Xbox 360—the Xbox 360 Controller for Windows and the Xbox 360 Wireless Controller for Windows. Making sure that your title plays well on the common controllers will ease some of the headache associated with testing your game against potential input devices.

### Display

The wide range of potential display devices makes advice about display challenging, and each type of device has special caveats. Some of the issues surrounding specific display technologies are introduced later in this paper. Regardless of the video output device, it's important that fonts and UI graphics are sized large enough for comfortable readability at a distance of 10 feet. Also note that antialiased fonts generally offer better readability.

You should also avoid horizontal lines and static UI elements with single-pixel thickness or detail. Older televisions might not display fine detail, and even on the latest display devices, your content will flicker when running on an interlaced mode, since a single row of pixels is visible only half the time. As a replacement for small detail, realize that a 2-pixel gray line appears thinner than a 2-pixel white line. (This is essentially the same as blurring a 1-pixel white line.)

## Aspect Ratio and Widescreen

Aspect ratio describes the width and height proportion of the display. Standard TV and computer monitor displays have an aspect ratio of 4:3, meaning that for every 4 pixels running along the width of the frame buffer, there are 3 pixels along the height (sometimes also represented as 1.33).

With the advent of HDTV, an aspect ratio of 16:9—also known as wide screen—has become the standard for the future of TV, and along with enhanced-definition TV (EDTV), there are three display modes that you're likely to encounter:

<dl> <dt>

<span id="480p_EDTV"></span><span id="480p_edtv"></span><span id="480P_EDTV"></span>480p EDTV
</dt> <dd>

480 scan lines presented progressively. This mode can output either 4:3 (with a frame buffer resolution of 640×480) or 16:9 (720×480).

</dd> <dt>

<span id="720p_HDTV"></span><span id="720p_hdtv"></span><span id="720P_HDTV"></span>720p HDTV
</dt> <dd>

720 scan lines presented progressively. This mode is always 16:9 (1280×720).

</dd> <dt>

<span id="1080i_HDTV"></span><span id="1080i_hdtv"></span><span id="1080I_HDTV"></span>1080i HDTV
</dt> <dd>

1080 scan lines presented interlaced. This mode is always 16:9 (1920×1080, or 1920×540 if rendering the interlace fields separately).

</dd> </dl>

If your game is hard-coded to work in a 4:3 aspect ratio, a user who views your game on a 16:9 screen likely has three options for displaying the image, none of which are particularly satisfying:

<dl> <dt>

<span id="Stretch"></span><span id="stretch"></span><span id="STRETCH"></span>Stretch
</dt> <dd>

The 4:3 frame buffer is stretched to perfectly cover the 16:9 native resolution of the display, resulting in your scene objects appearing wider than desired. Some TVs offer additional stretch modes which attempt to preserve the aspect ratio near the center of the display and gradually increase the stretch at the image sides.

</dd> <dt>

<span id="Center"></span><span id="center"></span><span id="CENTER"></span>Center
</dt> <dd>

The 4:3 frame buffer is displayed undistorted in the center of the display, with solid color bars filling the remaining pixels on the sides.

</dd> <dt>

<span id="Zoom"></span><span id="zoom"></span><span id="ZOOM"></span>Zoom
</dt> <dd>

The 4:3 frame buffer is cropped to a 16:9 region, which then fills the native display resolution without distortion; note that the pixels above and below the clip rectangle are completely discarded, which are common regions for a game's UI elements.

</dd> </dl>

A better approach is to add support for wide screen display to your game. The most important change is to set the game camera's projection transform to use a 16:9 aspect ratio, which avoids the stretching distortion. Even if you leave the back buffer at a 4:3 resolution, switching the projection transform to use 16:9 greatly improves the perceived accuracy of the rendered image; of course the final image is filtered to upscale the 4:3 back buffer resolution to meet the 16:9 native display resolution, but this is a less noticeable artifact than the stretch distortion caused by a mismatch of aspect ratios.

The cost of rendering the scene through 16:9 camera may be higher than a 4:3 camera (even at identical resolutions), because more scene objects will be visible in the wider view frustum. You should also be aware of how the enlarged viewable area may influence gameplay; for example, a game camera with a 16:9 ratio would reveal more of your game world than a 4:3 camera.

For the best results on a 16:9 display, you should render to a 16:9 back buffer, but this will obviously require filling more pixels. The difference between 640×480 and 720×480 is almost 38,400 pixels, a gain of 12.5%. If you can afford the cost of filling this larger area, we strongly recommend doing so.

## Title-Safe Region

The image frame buffer might be partly obscured from the user, because some pixels around the border are often covered by the display's front bezel. To ensure that critical UI elements are visible on a wide variety of display hardware, you should observe the title-safe region requirements for your target display mode. For non-HDTV modes, the title-safe region is the inner 85 percent of the frame buffer, and for HDTV modes, the title-safe area is the inner 90 percent. Therefore, for the greatest compatibility across current and future display hardware, you should keep all critical UI elements and heads-up display indicators within the inner 85 percent of the frame buffer.

## NTSC Suggestions

Since NTSC is the most common video standard in the United States for consumer display hardware, it's important to know about some of the guidelines that you should follow for your output image.

### Clamp the RGB color component values between 16 and 235

Colors outside the range of 16-235 can certainly be sent to an NTSC TV, but it's likely that these out-of-range values will be interpreted as audio data. This is often called *audio buzz*, and would be most apparent if your content were presented over a solid white background. You can easily implement output color clamping within a pixel shader.

### Avoid similar colors that might appear identical

The NTSC color gamut doesn't offer the same palette as a typical computer monitor, so avoid using similar colors wherever the game requires that the player to recognize the difference.

### Avoid sharp differences in contrast

Although this guideline is not always practical to follow, you can mitigate some of the color bleeding annoyances on NTSC displays (also known as *chroma crawl*) by selecting proper colors for your UI foreground and background elements; white text on a colored background will probably give better results than contrasting colors.

## Conclusion

This article offered a look at the 10-foot experience from the perspective of a Windows game developer, but it is by no means a comprehensive survey; you should research these topics further if you're developing a Windows game title (even if it's not intended for use with Windows Media Center). The true test is to try your game on a variety of video displays to ensure that your game offers a pleasant experience on each. Based on the typical life-span of a Windows-based game and the predicted growth in use of Windows Media Center, it's almost guaranteed that a game that you release today is part of someone's 10-foot experience—whether customers can play your game from the comfort of couches or they're forced to sit at desks is largely up to you.

 

 