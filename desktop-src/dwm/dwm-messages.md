---
title: DWM Messages
description: This section contains information about the Desktop Window Manager (DWM) messages.
ms.assetid: FF251CDA-7D68-4dd0-A54B-50B07E11C7C1
keywords:
- Desktop Window Manager (DWM),reference
- DWM (Desktop Window Manager),reference
- Desktop Window Manager (DWM),messages
- DWM (Desktop Window Manager),messages
ms.topic: article
ms.date: 05/31/2018
---

# DWM Messages

This section contains information about the Desktop Window Manager (DWM) messages.

## In this section




| Topic | Description | 
|-------|-------------|
| <a href="wm-dwmcolorizationcolorchanged.md"><strong>WM_DWMCOLORIZATIONCOLORCHANGED</strong></a><br /> | Informs all top-level windows that the colorization color has changed.<br /> | 
| <a href="wm-dwmcompositionchanged.md"><strong>WM_DWMCOMPOSITIONCHANGED</strong></a><br /> | Informs all top-level windows that DWM composition has been enabled or disabled. <br /><blockquote>[!Note]<br />As of Windows 8, DWM composition is always enabled, so this message is not sent regardless of video mode changes.</blockquote><br /> | 
| <a href="wm-dwmncrenderingchanged.md"><strong>WM_DWMNCRENDERINGCHANGED</strong></a><br /> | Sent when the non-client area rendering policy has changed.<br /> | 
| <a href="wm-dwmsendiconiclivepreviewbitmap.md"><strong>WM_DWMSENDICONICLIVEPREVIEWBITMAP</strong></a><br /> | Instructs a window to provide a static bitmap to use as a <em>live preview</em> (also known as a <em>Peek preview</em>) of that window.<br /> | 
| <a href="wm-dwmsendiconicthumbnail.md"><strong>WM_DWMSENDICONICTHUMBNAIL</strong></a><br /> | Instructs a window to provide a static bitmap to use as a thumbnail representation of that window.<br /> | 
| <a href="wm-dwmwindowmaximizedchange.md"><strong>WM_DWMWINDOWMAXIMIZEDCHANGE</strong></a><br /> | Sent when a DWM composed window is maximized.<br /> | 




 

 

 





