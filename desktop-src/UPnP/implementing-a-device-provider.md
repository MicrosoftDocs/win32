---
title: Implementing a Device Provider
description: To implement a device provider, create an object that exposes the IUPnPDeviceProvider interface.
ms.assetid: 3ba1200d-68d4-4f03-805c-7fff2d76b16f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing a Device Provider

To implement a device provider, create an object that exposes the [**IUPnPDeviceProvider**](/windows/win32/Upnphost/nn-upnphost-iupnpdeviceprovider?branch=master) interface. This object must be registered with the device host using the [**IUPnPRegistrar::RegisterDeviceProvider**](/windows/win32/Upnphost/nf-upnphost-iupnpregistrar-registerdeviceprovider?branch=master) method. This method takes the following parameters:

-   The name of the provider, which must be unique on the computer.
-   The ProgID of the class that implements the device provider.
-   An initialization string that is passed to the device provider when it is started.
-   A container ID. A container ID is a string that identifies the group to which the device belongs. All devices with the same container identifier are hosted in the same process.

 

 




