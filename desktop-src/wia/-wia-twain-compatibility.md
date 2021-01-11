---
description: WIA provides a TWAIN compatibility layer that allows TWAIN-aware applications to communicate with Windows Image Acquisition (WIA) devices.
ms.assetid: 8e5673b9-c234-4722-b244-41aae015ac0c
title: TWAIN Compatibility
ms.topic: article
ms.date: 05/31/2018
---

# TWAIN Compatibility

WIA provides a TWAIN compatibility layer that allows TWAIN-aware applications to communicate with Windows Image Acquisition (WIA) devices. TWAIN-aware applications do not have full access to WIA functionality. For example, an application cannot suppress the user interface using the TWAIN compatibility layer.

WIA devices appear twice to an application that is aware of both WIA and TWAIN: once through normal WIA communication, and once through the TWAIN compatibility layer. To avoid listing a WIA device twice, an application that is aware of both WIA and TWAIN must filter out the WIA devices that come through the TWAIN compatibility layer. All WIA devices that come through the TWAIN compatibility layer have "WIA-" as a prefix, so it is easy to filter them.

 

 



