---
title: MCI Device Capabilities
description: MCI Device Capabilities
ms.assetid: ac79fbe6-23ea-44ce-ada1-abea1fd07394
keywords:
- MCIWndCanConfig macro
- MCIWndCanEject macro
- MCIWndCanPlay macro
- MCIWndCanRecord macro
- MCIWndCanSave macro
- MCIWndCanWindow macro
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MCI Device Capabilities

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

MCIWnd includes the following macros to let you query MCI devices for their capabilities.



| Macro                                      | Description                                                                                                                                 |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**MCIWndCanConfig**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanconfig) | Determines whether a device has a configuration dialog box to support multiple configurations, such as the MCIAVI device.                   |
| [**MCIWndCanEject**](/windows/desktop/api/Vfw/nf-vfw-mciwndcaneject)   | Determines whether a device has a software-controlled eject function.                                                                       |
| [**MCIWndCanPlay**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanplay)     | Determines whether a device can play the existing content.                                                                                  |
| [**MCIWndCanRecord**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanrecord) | Determines whether a device can record.                                                                                                     |
| [**MCIWndCanSave**](/windows/desktop/api/Vfw/nf-vfw-mciwndcansave)     | Determines whether a device can store data.                                                                                                 |
| [**MCIWndCanWindow**](/windows/desktop/api/Vfw/nf-vfw-mciwndcanwindow) | Determines whether a device supports MCI window commands (such as [**window**](window.md), [**put**](put.md) and [**where**](where.md)). |



 

These macros return **TRUE** if the device supports the specific capability, or **FALSE** otherwise.

 

 




