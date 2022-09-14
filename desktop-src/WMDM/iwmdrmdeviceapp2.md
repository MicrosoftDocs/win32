---
title: IWMDRMDeviceApp2 interface
description: The IWMDRMDeviceApp2 interface extends IWMDRMDeviceApp by providing a new version of the QueryDeviceStatus method.
ms.assetid: a7e28d5a-041f-4102-97db-0c77ca146e26
keywords:
- IWMDRMDeviceApp2 interface windows Media Device Manager
- IWMDRMDeviceApp2 interface windows Media Device Manager , described
topic_type:
- apiref
api_name:
- IWMDRMDeviceApp2
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IWMDRMDeviceApp2 interface

The **IWMDRMDeviceApp2** interface extends [**IWMDRMDeviceApp**](iwmdrmdeviceapp.md) by providing a new version of the [**QueryDeviceStatus**](iwmdrmdeviceapp-querydevicestatus.md) method. **QueryDeviceStatus2** enables the caller to query for a specific DRM requirement.

To get this interface, call **CoCreateInstance** and pass in CLSID\_WMDRMDeviceApp.

> [!Note]  
> This interface is defined in the header file built from WMDRMDeviceApp.idl. This header **\#includes** "wmdm.h". You might need to change this file name to match the header built from WMDM.idl.

 

## Members

The **IWMDRMDeviceApp2** interface inherits from [**IWMDRMDeviceApp**](iwmdrmdeviceapp.md). **IWMDRMDeviceApp2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMDeviceApp2** interface has these methods.



| Method                                                            | Description                                                          |
|:------------------------------------------------------------------|:---------------------------------------------------------------------|
| [**QueryDeviceStatus2**](iwmdrmdeviceapp2-querydevicestatus2.md) | Queries a device for a specific DRM status or capability.<br/> |



 

## See also

<dl> <dt>

[**IWMDRMDeviceApp**](iwmdrmdeviceapp.md)
</dt> <dt>

[**Handling Protected Content in the Application**](handling-protected-content-in-the-application.md)
</dt> <dt>

[**Interfaces for Applications**](interfaces-for-applications.md)
</dt> <dt>

[**Metering Content Usage**](metering-content-usage.md)
</dt> </dl>

 

 





