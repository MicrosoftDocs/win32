---
description: Using Custom Properties.
ms.assetid: 09b30c95-0ce2-401c-a4ae-99c801a2048a
title: Using Custom Properties
ms.topic: article
ms.date: 05/31/2018
---

# Using Custom Properties

**Using Custom Properties**.

A Windows Image Acquisition (WIA) driver can define its own custom properties. Callers can manipulate custom properties just as they would normal WIA properties. However, only your application or custom UI module can access these custom properties.

WIA drivers should define the custom properties to have property identifiers that are offset by WIA\_PRIVATE\_DEVPROP for device properties, and use WIA\_PRIVATE\_ITEMPROP for normal item properties, such as inside [IWiaMiniDrv::drvInitItemProperties](https://msdn.microsoft.com/library/ms794131.aspx). For more information, see [Defining Custom Properties](-wia-defining-custom-properties.md).

There are two ways to pass custom parameters to WIA drivers.

The first option is to use the **IWiaItemExtras::Escape** method (described in the Platform SDK documentation). This is similar to the [IStiUSD::Escape](https://msdn.microsoft.com/library/ms794396.aspx) method, but it allows callers to use WIA directly, instead of using STI methods. Using **IWiaItemExtras::Escape**, you can pass any information to the driver, and the driver can pass any information back. The WIA service manages only those buffers passed between the caller and the driver.

The second option is to use custom properties. Using the **IWiaItemExtras::Escape** method is more flexible than using custom WIA properties, but custom WIA properties allow you to store information in the item's property stream so that the driver can read the information at another time.

 

 



