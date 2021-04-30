---
description: An imaging device is represented in Windows Image Acquisition (WIA) as a hierarchical tree of WIA item objects (IWiaItem interfaces).
ms.assetid: 5f3e56aa-8616-4574-882c-619caf54ca04
title: Using WIA Device Objects
ms.topic: article
ms.date: 05/31/2018
---

# Using WIA Device Objects

An imaging device is represented in Windows Image Acquisition (WIA) as a hierarchical tree of WIA item objects ([**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) interfaces). Typically, the root of this item tree represents the device itself, while the other items on the tree represent images, for a camera, or scanning regions, for a scanner.

Applications use the WIA device manager to create and enumerate WIA devices. The following sections explain how to create and use WIA devices:

-   [Selecting a Device](-wia-selecting-a-device.md)
-   [WIA Camera Devices](-wia-wia-camera-devices.md)
-   [WIA Scanner Devices](-wia-wia-scanner-devices.md)

 

 



