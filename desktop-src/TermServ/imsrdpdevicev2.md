---
title: IMsRdpDeviceV2 interface
description: Contains information about a device object. This is an enhancement of the IMsRdpDevice interface.
ms.assetid: 9a380a1a-d44f-4147-8917-bf1e07dbac15
ms.tgt_platform: multiple
keywords:
- IMsRdpDeviceV2 interface Remote Desktop Services
- IMsRdpDeviceV2 interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpDeviceV2
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDeviceV2 interface

Contains information about a device object. This is an enhancement of the [**IMsRdpDevice**](imsrdpdevice.md) interface.

## Members

The **IMsRdpDeviceV2** interface inherits from [**IMsRdpDevice**](imsrdpdevice.md). **IMsRdpDeviceV2** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMsRdpDeviceV2** interface has these properties.



| Property                                                                 | Access type          | Description                                                                                        |
|:-------------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------|
| [**CmClassGuid**](imsrdpdevicev2-cmclassguid.md)<br/>             | Read-only<br/> | Contains the configuration manager setup class GUID for the device.<br/>                     |
| [**CmDeviceInstance**](imsrdpdevicev2-cmdeviceinstance.md)<br/>   | Read-only<br/> | Contains the configuration manager device instance of the device.<br/>                       |
| [**DeviceText**](imsrdpdevicev2-devicetext.md)<br/>               | Read-only<br/> | Contains the device text.<br/>                                                               |
| [**DriveLetterBitmap**](imsrdpdevicev2-driveletterbitmap.md)<br/> | Read-only<br/> | Contains a bitfield that represents a map of drive letters contained within the device.<br/> |
| [**IsCompositeDevice**](imsrdpdevicev2-iscompositedevice.md)<br/> | Read-only<br/> | Specifies if the device is a composite device.<br/>                                          |
| [**IsOptionalDevice**](imsrdpdevicev2-isoptionaldevice.md)<br/>   | Read-only<br/> | Specifies if the device is optional for USB redirection.<br/>                                |
| [**IsUSBDevice**](imsrdpdevicev2-isusbdevice.md)<br/>             | Read-only<br/> | Specifies if the device is for USB redirection.<br/>                                         |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 with SP1<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2 with SP1<br/>                                             |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpDeviceV2 is defined as 5fb94466-7661-42a8-98b7-01904c11668f<br/>      |



 

 





