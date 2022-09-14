---
title: Adjusting Speed, Volume, and Zoom
description: Adjusting Speed, Volume, and Zoom
ms.assetid: 16cfbf86-911e-4cf3-9640-69fffc09c1ed
keywords:
- MCIWndSetSpeed macro
- MCIWndGetSpeed macro
- MCIWndSetVolume macro
- MCIWndGetVolume macro
- MCIWndSetZoom macro
- MCIWndGetZoom macro
ms.topic: article
ms.date: 05/31/2018
---

# Adjusting Speed, Volume, and Zoom

The speed, volume, and zoom macros provide the functionality of the **View**, **Volume**, and **Speed** commands on the MCIWnd menu. The macros described in this section are generally used with video and other devices that display images during playback.

Some devices support multiple playback speed changes. You can set the playback speed for these devices by using the [**MCIWndSetSpeed**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetspeed) macro. This macro defines the playback speed as 1000. Higher values indicate faster speeds. Lower values indicate slower speeds.

You can retrieve the current playback speed by using the [**MCIWndGetSpeed**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetspeed) macro. This macro uses the same values and range as those used by **MCIWndSetSpeed**.

Some devices support volume changes. You can adjust or set the volume by using the [**MCIWndSetVolume**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetvolume) macro. This macro defines the normal volume level as 1000. Higher values indicate louder volumes. Lower values indicate quieter volumes.

You can retrieve the current volume level by using the [**MCIWndGetVolume**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetvolume) macro. This macro uses the same numerical values and range as those used by **MCIWndSetVolume**.

For devices that use a playback window, MCIWnd supports a zoom feature that sets the size of the playback image. You can set the playback image size by using the [**MCIWndSetZoom**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetzoom) macro. The macro redefines the playback image size while maintaining a constant aspect ratio for the image. The zoom value is defined as a percentage of the original image size. Thus, 100 represents the original image size, 50 indicates the image shown is half its original size, and 200 indicates that the image shown is twice its original size.

You can retrieve the current zoom value by using the [**MCIWndGetZoom**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetzoom) macro. This macro uses the same values and range as those used by **MCIWndSetZoom**.

> [!Note]  
> The standard MCI CD audio and waveform-audio drivers do not support volume or speed changes.

 

 

 




