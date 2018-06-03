---
title: WiaDeviceType enumeration
description: Specifies the type of device attached to a user's computer. Use Type (DeviceInfo) or Type (Device) to obtain these values from the device.
ms.assetid: 79d53e0f-515f-4f8a-b7a3-d16dfc3822d9
keywords:
- WiaDeviceType enumeration WIA Automation
topic_type:
- apiref
api_name:
- WiaDeviceType
api_location:
- Wiaaut.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# WiaDeviceType enumeration

Specifies the type of device attached to a user's computer. Use [**Type (DeviceInfo)**](-wiaaut-ideviceinfo-type.md) or [**Type (Device)**](-wiaaut-idevice-type.md) to obtain these values from the device.

## Members



| Member                    | Description                                     | Value |
|---------------------------|-------------------------------------------------|-------|
| **UnspecifiedDeviceType** | The device type is unknown.<br/>          | 0     |
| **ScannerDeviceType**     | The device is a scanner.<br/>             | 1     |
| **CameraDeviceType**      | The device is a camera.<br/>              | 2     |
| **VideoDeviceType**       | The device provides streaming video.<br/> | 3     |



## Remarks

The value of the [**Type (Device)**](-wiaaut-idevice-type.md) property on a [**Device**](-wiaaut-device.md) object can return one of the members of the **WiaDeviceType** enumeration. This provides more information about exactly what kind of imaging device the **Device** object is connected to.

For example code, see [Determine if the Selected Device is a Camera](https://www.bing.com/search?q=Determine if the Selected Device is a Camera) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md)
</dt> <dt>

[**ShowSelectDevice**](-wiaaut-icommondialog-showselectdevice.md)
</dt> </dl>

 

 





