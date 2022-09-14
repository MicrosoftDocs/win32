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
ms.date: 05/31/2018
---

# MCI Device Capabilities

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

 

 




