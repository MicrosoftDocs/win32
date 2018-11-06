---
title: Finding Devices
description: The UPnP architecture is a dynamic network architecture that allows devices to join and leave the network at any time.
ms.assetid: b89d9ec3-ce1a-4162-bf82-b08a49207d7d
ms.topic: article
ms.date: 05/31/2018
---

# Finding Devices

The UPnP architecture is a dynamic network architecture that allows devices to join and leave the network at any time. Because of this dynamic architecture, applications cannot rely on specific UPnP-based devices to be available at any given time. For this reason, applications (or control points) search the network to find devices that most closely match specified criteria. Applications also wait for device advertisement messages that indicate new devices have been added to the network.

The following are valid search criteria for UPnP-based devices:

-   Device type
-   Service type
-   Unique device name (UDN)
-   All root devices

The device type and service type searches are typically used to find a class of devices with common characteristics. The UDN search is used to find a specific device.

To search for devices, an application must first instantiate the Device Finder object. This object exposes the [**IUPnPDeviceFinder**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevicefinder) interface; its methods perform the previously described searches.

The following sections describe the process of finding devices:

-   [Creating the Device Finder](creating-the-device-finder.md)
-   [Asynchronous Searching](asynchronous-searching.md)
-   [Synchronous Searching](synchronous-searching.md)
-   [Device Collections Returned By Synchronous Searches](device-collections-returned-by-synchronous-searches.md)

 

 




