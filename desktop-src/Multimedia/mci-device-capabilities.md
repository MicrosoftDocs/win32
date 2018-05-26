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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MCI Device Capabilities

MCIWnd includes the following macros to let you query MCI devices for their capabilities.



| Macro                                      | Description                                                                                                                                 |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**MCIWndCanConfig**](/windows/win32/Vfw/nf-vfw-mciwndcanconfig?branch=master) | Determines whether a device has a configuration dialog box to support multiple configurations, such as the MCIAVI device.                   |
| [**MCIWndCanEject**](/windows/win32/Vfw/nf-vfw-mciwndcaneject?branch=master)   | Determines whether a device has a software-controlled eject function.                                                                       |
| [**MCIWndCanPlay**](/windows/win32/Vfw/nf-vfw-mciwndcanplay?branch=master)     | Determines whether a device can play the existing content.                                                                                  |
| [**MCIWndCanRecord**](/windows/win32/Vfw/nf-vfw-mciwndcanrecord?branch=master) | Determines whether a device can record.                                                                                                     |
| [**MCIWndCanSave**](/windows/win32/Vfw/nf-vfw-mciwndcansave?branch=master)     | Determines whether a device can store data.                                                                                                 |
| [**MCIWndCanWindow**](/windows/win32/Vfw/nf-vfw-mciwndcanwindow?branch=master) | Determines whether a device supports MCI window commands (such as [**window**](window.md), [**put**](put.md) and [**where**](where.md)). |



 

These macros return **TRUE** if the device supports the specific capability, or **FALSE** otherwise.

 

 




