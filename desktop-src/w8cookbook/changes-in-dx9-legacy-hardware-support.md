---
title: Changes in DX9 legacy hardware support
description: Changes in DX9 legacy hardware support
ms.assetid: 25C7DFC7-58F4-4F6D-8D26-6DBA92424A0B
ms.topic: article
ms.date: 05/31/2018
---

# Changes in DX9 legacy hardware support

## Platform

**Clients** – Windows 8 


## Description

Intel and AMD/ATI no longer support their DX9 graphics parts and will not be updating drivers for these devices for Windows 8. Furthermore, these devices are not covered in-box for Windows 8. The last drivers for these devices are those available on WU and on the OEM/IHV’s websites; many date from Vista, and many of these final version drivers exhibit problems on Windows 8. In addition, nVidia has recently stated that they will not support their DX9 (Vista and older) mobile (notebook) parts for Windows 8. They continue to support their desktop DX9 parts.

All of these driver/part combinations are on the Internet Explorer 9 software fallback list. This means that for either performance or stability reasons, Internet Explorer 9 uses software rendering on these devices. This is a good indication that the experience with Windows Store apps will not be satisfactory on these drivers and parts.

## Manifestation

As there is no in-box support for these devices, many users with these parts will wind up running on the Microsoft Basic Display Driver. This is a WARP-based WDDM 1.2 software GPU, and is actually faster than some of the parts in this class, for example, the Intel GMA500 series). It supports aero-glass and DWM, and can run Windows Store apps.

However, it has some important limitations:

-   It doesn’t support multiple monitors or projection
-   It doesn’t support sleep, though it does support hibernation
-   It often will not allow changing screen resolution

## Mitigation

If after testing, you find that the user experience is not acceptable, you may choose to set hardware requirements for their products that exclude these older DX9 Intel and AMD parts. You may also choose to alert your customers that they may have an unacceptable experience on these parts.

## Tests

Evaluate the performance and experience on these devices:

-   What is the experience like on the final driver version available?
-   What is the experience like on the MSBDD?

 

 




