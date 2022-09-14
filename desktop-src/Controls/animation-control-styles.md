---
title: Animation Control Styles (CommCtrl.h)
description: This section lists the window styles used with animation controls.
ms.assetid: ad4fc4fd-166d-4871-9f60-5133a48681aa
topic_type:
- apiref
api_name:
- ACS_AUTOPLAY
- ACS_CENTER
- ACS_TIMER
- ACS_TRANSPARENT
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Animation Control Styles

This section lists the window styles used with animation controls.




| Constant | Description | 
|----------|-------------|
| <span id="ACS_AUTOPLAY"></span><span id="acs_autoplay"></span><dl><dt><strong>ACS_AUTOPLAY</strong></dt></dl> | Starts playing the animation as soon as the AVI clip is opened. <br /> | 
| <span id="ACS_CENTER"></span><span id="acs_center"></span><dl><dt><strong>ACS_CENTER</strong></dt></dl> | Centers the animation in the animation control's window. <br /> | 
| <span id="ACS_TIMER"></span><span id="acs_timer"></span><dl><dt><strong>ACS_TIMER</strong></dt></dl> | By default, the control creates a thread to play the AVI clip. If you set this flag, the control plays the clip without creating a thread; internally the control uses a Win32 timer to synchronize playback. <br /><strong>Comctl32.dll version 6 and later:</strong> This style is not supported. By default, the control plays the AVI clip without creating a thread.<br /><blockquote>[!Note]<br />Comctl32.dll version 6 is not redistributable. To use Comctl32.dll version 6, specify it in a manifest. For more information on manifests, see <a href="cookbook-overview.md">Enabling Visual Styles</a>.</blockquote><br /> | 
| <span id="ACS_TRANSPARENT"></span><span id="acs_transparent"></span><dl><dt><strong>ACS_TRANSPARENT</strong></dt></dl> | Allows you to match an animation's background color to that of the underlying window, creating a "transparent" background. The parent of the animation control must not have the WS_CLIPCHILDREN style (see <a href="/windows/desktop/winmsg/window-styles">Window Styles</a>). The control sends a <a href="wm-ctlcolorstatic.md"><strong>WM_CTLCOLORSTATIC</strong></a> message to its parent. Use <a href="/windows/desktop/api/wingdi/nf-wingdi-setbkcolor"><strong>SetBkColor</strong></a> to set the background color for the device context to an appropriate value. The control interprets the upper-left pixel of the first frame as the animation's default background color. It will remap all pixels with that color to the value you supplied in response to WM_CTLCOLORSTATIC. <br /> | 




## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



