---
title: IWMDRMDevice IsWMDRMDevice method
description: The IsWMDRMDevice method determines whether the device supports Windows Media DRM 10 for Portable Devices.
ms.assetid: 247e7a77-e805-4848-893f-f5522c161232
keywords:
- IsWMDRMDevice method windows Media Device Manager
- IsWMDRMDevice method windows Media Device Manager , IWMDRMDevice interface
- IWMDRMDevice interface windows Media Device Manager , IsWMDRMDevice method
topic_type:
- apiref
api_name:
- IWMDRMDevice.IsWMDRMDevice
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDevice::IsWMDRMDevice method

The **IsWMDRMDevice** method determines whether the device supports Windows Media DRM 10 for Portable Devices.

## Syntax


```C++
HRESULT IsWMDRMDevice(
  [out] DWORD *pdwVersion
);
```



## Parameters

<dl> <dt>

*pdwVersion* \[out\]
</dt> <dd>

Version of Windows Media DRM 10 for Portable Devices, which has value of 0x00010000.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMDDRMSP.idl</dt> </dl> |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMDevice Interface**](iwmdrmdevice.md)
</dt> </dl>

 

 





