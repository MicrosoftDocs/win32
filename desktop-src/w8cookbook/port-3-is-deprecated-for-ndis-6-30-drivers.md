---
title: Port 3 is deprecated for NDIS 6.30 drivers
description: Port 3 is deprecated for NDIS 6.30 drivers
ms.assetid: 900BD08D-3EAF-43F3-A74A-359815474FAD
ms.topic: article
ms.date: 05/31/2018
---

# Port 3 is deprecated for NDIS 6.30 drivers

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

Windows 8 removes platform support for NDIS miniport WLAN drivers to create or start up the IHV extensibility port (also known as 3rd port). This feature was introduced in Windows 7 as a stopgap measure while the Wi-Fi Alliance (WFA) developed the Wi-Fi Direct specification. The specification is now finished, products using Wi-Fi Direct are being certified, and Windows 8 introduces a native Wi-Fi Direct stack.

## Manifestation

Nothing, as third port is a platform capability that WLAN miniport drivers start up if they need this functionality.

## Solution

We are keeping the extensibility port feature available for existing drivers that do not report NDIS 6.30 to maintain device compatibility. However, new WLAN drivers that report NDIS 6.30 will not be able to start this port; instead, developers of these drivers should use Wi-Fi Direct.

 

 




