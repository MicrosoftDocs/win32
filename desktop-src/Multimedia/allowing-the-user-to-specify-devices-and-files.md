---
title: Allowing the User to Specify Devices and Files
description: Allowing the User to Specify Devices and Files
ms.assetid: cc542b56-c66e-4622-b2d1-505d31aab25b
keywords:
- MCIWndOpenDialog macro
- MCIWndOpen macro
- MCIWndOpenInterface macro
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Allowing the User to Specify Devices and Files

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can associate a device or file with an existing MCIWnd window by using the [**MCIWndOpenDialog**](/windows/desktop/api/Vfw/nf-vfw-mciwndopendialog), [**MCIWndOpen**](/windows/desktop/api/Vfw/nf-vfw-mciwndopen), and [**MCIWndOpenInterface**](/windows/desktop/api/Vfw/nf-vfw-mciwndopeninterface) macros, and the [**GetOpenFileNamePreview**](/windows/desktop/api/Vfw/nf-vfw-getopenfilenamepreviewa) function.

To let a user of your application select a file to play, use **MCIWndOpenDialog**. This macro displays the **Open** dialog box (shown in the following screen shot) for choosing a file and associates the selected file with the current MCIWnd window.

![mciwnd window image](images/mciwnd3.gif)

You can let a user of your application select a file to associate with an MCIWnd window and preview that file by using [**GetOpenFileNamePreview**](/windows/desktop/api/Vfw/nf-vfw-getopenfilenamepreviewa) and [**MCIWndOpen**](/windows/desktop/api/Vfw/nf-vfw-mciwndopen). The **GetOpenFileNamePreview** function displays the **Open** dialog box for choosing a file and lets the user preview (play) its contents. When the name of an existing file is specified in the dialog box, **GetOpenFileNamePreview** provides a small control to let the user preview the contents of the file. You can associate a specified file, selected with **GetOpenFileNamePreview** or specified in another manner, with an MCIWnd window by using **MCIWndOpen**.

You can also use **MCIWndOpen** to specify a device to associate with an MCIWnd window. For example, you can use a device name, such as "CDAudio".

To associate an MCIWnd window with a file interface or data-stream interface to multimedia data, use the [**MCIWndOpenInterface**](/windows/desktop/api/Vfw/nf-vfw-mciwndopeninterface) macro. For more information about file and data-stream interfaces, see [AVIFile Functions and Macros](avifile-functions-and-macros.md).

> [!Note]  
> Before associating a new file or device with an MCIWnd window, [**MCIWndOpenDialog**](/windows/desktop/api/Vfw/nf-vfw-mciwndopendialog) and [**MCIWndOpen**](/windows/desktop/api/Vfw/nf-vfw-mciwndopen) close any device currently associated with the window. Your application does not need to close any open devices before using these macros.

 

 

 




