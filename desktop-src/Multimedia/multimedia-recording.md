---
title: Multimedia Recording
description: Multimedia Recording
ms.assetid: e37aaac2-be89-4907-b1a8-f2c64ab2f39e
keywords:
- MCIWndCreate function
- MCIWndNew macro
ms.topic: article
ms.date: 05/31/2018
---

# Multimedia Recording

You can implement recording capabilities in your application by using the user interface built into MCIWnd. You can use the [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea) function and the [**MCIWndNew**](/windows/desktop/api/Vfw/nf-vfw-mciwndnew) macro to provide controls for starting and stopping recording and for saving the recorded information. Using **MCIWndCreate**, you can specify window styles to display an MCIWnd window and to include the **Record** button on the toolbar. Using **MCIWndNew**, you can specify the device type that is being recorded and specify that the information is to be captured in a new file.

If your application requires more sophistication, you can automate and customize the recording by using the [**MCIWndRecord**](/windows/desktop/api/Vfw/nf-vfw-mciwndrecord) macro. For more information, see [Customizing the Recording Process](customizing-the-recording-process.md).

> [!Note]  
> Some devices, such as CD audio and MCIAVI, are used for playback only. Other devices, such as waveform-audio devices, can be used for recording. If you specify a device that cannot record, MCIWnd omits the **Record** button from the toolbar.

 

 

 




