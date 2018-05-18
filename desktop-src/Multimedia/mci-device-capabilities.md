---
title: MCI Device Capabilities
description: MCI Device Capabilities
ms.assetid: 'ac79fbe6-23ea-44ce-ada1-abea1fd07394'
keywords: ["MCIWndCanConfig macro", "MCIWndCanEject macro", "MCIWndCanPlay macro", "MCIWndCanRecord macro", "MCIWndCanSave macro", "MCIWndCanWindow macro"]
---

# MCI Device Capabilities

MCIWnd includes the following macros to let you query MCI devices for their capabilities.



| Macro                                      | Description                                                                                                                                 |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**MCIWndCanConfig**](mciwndcanconfig.md) | Determines whether a device has a configuration dialog box to support multiple configurations, such as the MCIAVI device.                   |
| [**MCIWndCanEject**](mciwndcaneject.md)   | Determines whether a device has a software-controlled eject function.                                                                       |
| [**MCIWndCanPlay**](mciwndcanplay.md)     | Determines whether a device can play the existing content.                                                                                  |
| [**MCIWndCanRecord**](mciwndcanrecord.md) | Determines whether a device can record.                                                                                                     |
| [**MCIWndCanSave**](mciwndcansave.md)     | Determines whether a device can store data.                                                                                                 |
| [**MCIWndCanWindow**](mciwndcanwindow.md) | Determines whether a device supports MCI window commands (such as [**window**](window.md), [**put**](put.md) and [**where**](where.md)). |



 

These macros return **TRUE** if the device supports the specific capability, or **FALSE** otherwise.

 

 




