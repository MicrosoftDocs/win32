---
title: Using Enhanced Storage
description: The following sections outline the steps required to accomplish common Enhanced Storage tasks
ms.assetid: d35c335e-a974-4a8b-93d7-50597a03003a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Enhanced Storage

The following sections outline the steps required to accomplish common Enhanced Storage tasks:

-   [Discover and Enumerate Enhanced Storage Devices, ACTs, and Silos](#discover-and-enumerate-enhanced-storage-devices-acts-and-silos)
-   [Invoke an Enhanced Storage Portable Device Command](#invoke-an-enhanced-storage-portable-device-command)
-   [Related topics](#related-topics)

## Discover and Enumerate Enhanced Storage Devices, ACTs, and Silos

Before calling any of the following methods for device, ACT, and silo enumeration, an [**IEnumEnhancedStorageACT**](/windows/previous-versions/EhStorAPI/nn-ehstorapi-ienumenhancedstorageact?branch=master) interface must be created. Once initialized, the following methods should be called in the following order for complete enumeration:



|       | Method                                                                      | Description                                            |
|-------|-----------------------------------------------------------------------------|--------------------------------------------------------|
| **1** | [**IEnumEnhancedStorageACT::GetACTs**](/windows/previous-versions/EhStorAPI/nf-ehstorapi-ienumenhancedstorageact-getacts?branch=master) | Enumerate all ACTs.                                    |
| **2** | [**IEnhancedStorageACT::GetSilos**](/windows/previous-versions/EhStorAPI/nf-ehstorapi-ienhancedstorageact-getsilos?branch=master)       | Enumerate all silos associated with an ACT.            |
| **3** | [**IEnhancedStorageSilo::GetInfo**](/windows/previous-versions/EhStorAPI/nf-ehstorapi-ienhancedstoragesilo-getinfo?branch=master)       | Retrieve descriptive information from a specific silo. |



 

## Invoke an Enhanced Storage Portable Device Command

Once enumerated, silo specific operations are supported through the [**IEnhancedStorageSilo**](/windows/previous-versions/EhStorAPI/nn-ehstorapi-ienhancedstoragesilo?branch=master) interface. More specifically, this interface allows raw silo commands to be sent to a portable device. The following table outlines the steps required to configure and send commands after the desired silo has been discovered:



|       | Operation                                                                                 | Description                                                                            |
|-------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **1** | [**IEnhancedStorageSilo::GetPortableDevice**](/windows/previous-versions/EhStorAPI/nf-ehstorapi-ienhancedstoragesilo-getportabledevice?branch=master) | Retrieve [IPortableDevice](http://go.microsoft.com/fwlink/p/?linkid=134792) interface. |
| **2** | [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=185195)                  | Set command parameters.                                                                |
| **3** | [IPortableDevice::SendCommand](http://go.microsoft.com/fwlink/p/?linkid=185194)           | Invoke the Enhanced Storage Portable Device command.                                   |
| **4** | [IPortableDevice](http://go.microsoft.com/fwlink/p/?linkid=134792)                        | Use 'get' methods to check status and retrieve return values.                          |



 

A complete Enhanced Storage enumeration tool is provided as a sample in the [Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=147890). The **EnStorEnumerator** sample demonstrates how to discover an Enhanced Storage device and send Portable Device commands to the IEEE 1667 certificate and password silo drivers.

## Related topics

<dl> <dt>

[About Enhanced Storage](about-enhanced-storage.md)
</dt> <dt>

[Enhanced Storage Reference](enhanced-storage-reference.md)
</dt> </dl>

 

 




