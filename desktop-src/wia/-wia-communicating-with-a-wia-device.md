---
description: When a thread is actively communicating with a Windows Image Acquisition (WIA) device (for example, transferring data or writing device properties) WIA &\#0034;locks&\#0034; the device.
ms.assetid: 59533937-284a-4732-a73b-d2e0b5a9a370
title: Communicating with a WIA Device in Multiple Threads or Applications
ms.topic: article
ms.date: 05/31/2018
---

# Communicating with a WIA Device in Multiple Threads or Applications

When a thread is actively communicating with a Windows Image Acquisition (WIA) device (for example, transferring data or writing device properties) WIA "locks" the device. When a device is locked, no other threads or processes can actively communicate with that device.

WIA does not prohibit multiple threads or processes from maintaining connections to a single device. That is, a device is locked only during the actual communication, and two or more applications can simultaneously have a single device selected.

WIA creates a separate item tree each time any thread or application calls [**IWiaDevMgr::CreateDevice**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-createdevice) or [**IWiaDevMgr2::CreateDevice**](-wia-iwiadevmgr2-createdevice.md) to create an instance of that device. WIA maintains separate state information for each item tree. For example, if a thread creates two instances of a particular scanner, it can set different scan resolutions for the two instances. When [**IWiaDataTransfer::idtGetData**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadatatransfer-idtgetdata) is called on a particular instance, WIA loads the properties associated with that instance to the device before the actual scan takes place. This does not affect the state of the other instance of the device.

If a thread currently has a device locked (it is actively communicating with that device) and another thread attempts to call a method that actively communicates with the device, the method returns a WIA\_ERROR\_BUSY error.

Typically, reading and writing device properties takes so little time that these operations rarely cause a conflict. Transferring data, however, usually takes longer, and therefore is more likely to create device access conflicts. It is sound programming to avoid lengthy device operations (data transfers) concurrently in separate threads within an application.

An application should never assume that it is the only application that is communicating with a WIA device when it starts.

 

 



