---
title: MCIAVI
description: MCIAVI
ms.assetid: 68639f35-bc20-457d-b937-760af8323dce
keywords:
- MCI devices,MCIAVI driver
- MCI commands,MCIAVI driver
- MCIAVI driver
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MCIAVI

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

An AVI file can contain more than two streams — for example, a video sequence, an English soundtrack, and a French soundtrack. Your application can use a stream independently of the other streams in the file.

The **digitalvideo** device type controls video files. For a list of the MCI commands recognized by digital-video devices, see [Digital-Video Command Set](digital-video-command-set.md).

The MCIAVI driver plays video sequences and other data streams under the control of MCI commands. Data streams can contain images, audio, and palettes. The image data can consist of images with either color palettes or true-color information.

Audio is synchronized with the video within one-thirtieth of a second. If audio hardware is not available, however, the driver plays only the video stream. The MCIAVI driver can drop video frames, if necessary, to play a stream without audio interruption.

Your application can use the MCIWnd window class services instead of the MCI command interface to control any MCI driver. This window class handles many of the details of managing the window supporting the MCI device and simplifies the programming required to send the MCI commands. Your application can use the MCIWnd library services directly to control the MCI device, or it can have MCIWnd display a toolbar, scroll bar, and menus that let the user control the device. For more information about the MCIWnd window class, see [MCIWnd Window Class](mciwnd-window-class.md).

 

 




