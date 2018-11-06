---
title: Automating Playback
description: Automating Playback
ms.assetid: 3aa05a54-58d7-4d14-93ee-459aa860b20e
keywords:
- MCIWndCreate macro
- MCIWndPlay macro
ms.topic: article
ms.date: 05/31/2018
---

# Automating Playback

You can automate playback in your application by using [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea) and the [**MCIWndPlay**](/windows/desktop/api/Vfw/nf-vfw-mciwndplay) macro, along with either the [**MCIWndDestroy**](/windows/desktop/api/Vfw/nf-vfw-mciwnddestroy) or the [**MCIWndClose**](/windows/desktop/api/Vfw/nf-vfw-mciwndclose) macro. To automate playback, specify the MCIWNDF\_NOPLAYBAR and MCIWNDF\_NOTIFYMODE styles in the **MCIWndCreate***dwStyle* parameter. Specify the MCIWNDF\_NOPLAYBAR style to hide the toolbar, and the MCIWNDF\_NOTIFYMODE style to issue an appropriate notification message when the device stops playing.

You can play the device or file specified in **MCIWndCreate** by using **MCIWndPlay**. The MCIWndPlay macro starts playing the content from its current playback position and continues to its end.

You can destroy or close an MCIWnd window by using the [**MCIWndDestroy**](/windows/desktop/api/Vfw/nf-vfw-mciwnddestroy) or [**MCIWndClose**](/windows/desktop/api/Vfw/nf-vfw-mciwndclose) macro. The **MCIWndDestroy** macro closes the device or file and destroys the MCIWnd window by invalidating its handle. If your application can reuse the MCIWnd window, use **MCIWndClose** to close the device without destroying the window.

Your application can detect when the device stops playing and automatically close the window. To do this, specify the MCIWNDF\_NOTIFYMODE style for the *dwStyle* parameter of [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea). This causes the device to send a [**MCIWNDM\_NOTIFYMODE**](mciwndm-notifymode.md) message whenever it changes modes. Your application can trap this message to determine whether the device has stopped playing. When the device stops playing, the application closes the window.

 

 




