---
title: Error Messages and Notifications
description: Error Messages and Notifications
ms.assetid: 7f804364-d8be-4e52-ab0e-fba05bcf76ce
keywords:
- MCIWndGetError macro
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Error Messages and Notifications

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

MCIWnd uses MCI to control the devices that play and record multimedia data. In general, MCIWnd displays MCI errors in an error dialog box. An MCI error is generated whenever an MCI command fails. For example, if your application tries to resume paused playback by using the [**MCIWndResume**](/windows/desktop/api/Vfw/nf-vfw-mciwndresume) macro and the current device does not support resume, an error is reported to the user.

MCIWnd allows you two choices for handling error messages:

-   You can prevent error messages from reaching the user. To prevent the display of MCI error messages, specify the MCIWNDF\_NOERRORDLG window style when you create an instance of an MCIWnd window by using the [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea) or [CreateWindowEx](/windows/win32/api/winuser/nf-winuser-createwindowexa) function.
-   You can redirect them to your application for display. To redirect MCI error messages to your application, specify the MCIWNDF\_NOTIFYERROR window style when you create an instance of an MCIWnd window by using **MCIWndCreate** or **CreateWindowEx**.

When error notification is enabled, MCIWnd sends each notification message ([**MCIWNDM\_NOTIFYERROR**](mciwndm-notifyerror.md)) to the main message handler of the parent of the MCIWnd window. Your application must have a message handler to process the notification messages it receives.

You can obtain a textual description of the most recent MCI error message by using the [**MCIWndGetError**](/windows/desktop/api/Vfw/nf-vfw-mciwndgeterror) macro. This macro returns the text in an application-defined buffer. If the error string is longer than the buffer, MCIWnd truncates the string.

You can route all notifications to another window by using the [**MCIWndSetOwner**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetowner) macro.

 

 