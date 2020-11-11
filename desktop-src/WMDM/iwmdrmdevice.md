---
title: IWMDRMDevice interface
description: This interface is not intended to be implemented by a service provider, but is provided for purposes of complete documentation.The IWMDRMDevice interface enables a secure content provider to communicate with devices that use Windows Media DRM 10 for Portable Devices.
ms.assetid: ebad4acd-16cc-433f-a5e0-fcae59030f55
keywords:
- IWMDRMDevice interface windows Media Device Manager
- IWMDRMDevice interface windows Media Device Manager , described
topic_type:
- apiref
api_name:
- IWMDRMDevice
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IWMDRMDevice interface

This interface is not intended to be implemented by a service provider, but is provided for purposes of complete documentation.

The **IWMDRMDevice** interface enables a secure content provider to communicate with devices that use Windows Media DRM 10 for Portable Devices.

## Members

The **IWMDRMDevice** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMDRMDevice** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMDevice** interface has these methods.



| Method                                                                  | Description                                                                                  |
|:------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**CleanDataStore**](iwmdrmdevice-cleandatastore.md)                   | Starts the process of cleaning the DRM data store on the device.<br/>                  |
| [**GetDeviceCertificate**](iwmdrmdevice-getdevicecertificate.md)       | Retrieves the device certificate.<br/>                                                 |
| [**GetMeterChallenge**](iwmdrmdevice-getmeterchallenge.md)             | Retrieves the metering challenge.<br/>                                                 |
| [**GetSecureClock**](iwmdrmdevice-getsecureclock.md)                   | Retrieves the secure clock.<br/>                                                       |
| [**GetSecureClockChallenge**](iwmdrmdevice-getsecureclockchallenge.md) | Retrieves the secure clock challenge.<br/>                                             |
| [**GetSyncList**](iwmdrmdevice-getsynclist.md)                         | Retrieves the license synchronization list.<br/>                                       |
| [**IsWMDRMDevice**](iwmdrmdevice-iswmdrmdevice.md)                     | Determines whether the device supports Windows Media DRM 10 for Portable Devices.<br/> |
| [**SetLicenseResponse**](iwmdrmdevice-setlicenseresponse.md)           | Sets the license response.<br/>                                                        |
| [**SetMeterResponse**](iwmdrmdevice-setmeterresponse.md)               | Sets the metering response.<br/>                                                       |
| [**SetSecureClockResponse**](iwmdrmdevice-setsecureclockresponse.md)   | Sets the secure clock response.<br/>                                                   |



 

## See also

<dl> <dt>

[**Interfaces for Service Providers**](interfaces-for-service-providers.md)
</dt> </dl>

 

