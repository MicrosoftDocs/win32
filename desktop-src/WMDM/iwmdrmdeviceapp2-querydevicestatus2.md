---
title: IWMDRMDeviceApp2 QueryDeviceStatus2 method (WMDRMDeviceApp.h)
description: The QueryDeviceStatus2 method queries a device for a specific DRM status or capability.
ms.assetid: f7e95fb7-5929-4a70-8580-a443e152e6d1
keywords:
- QueryDeviceStatus2 method windows Media Device Manager
- QueryDeviceStatus2 method windows Media Device Manager , IWMDRMDeviceApp2 interface
- IWMDRMDeviceApp2 interface windows Media Device Manager , QueryDeviceStatus2 method
topic_type:
- apiref
api_name:
- IWMDRMDeviceApp2.QueryDeviceStatus2
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDeviceApp2::QueryDeviceStatus2 method

The **QueryDeviceStatus2** method queries a device for a specific DRM status or capability.

## Syntax


```C++
HRESULT QueryDeviceStatus2(
  [in]  IWMDMDevice *pDevice,
  [in]  DWORD       dwFlags,
  [out] DWORD       *pdwStatus
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Pointer to an [**IWMDMDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice) object.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

One or more of the following **DWORD** values specifying which capabilities to request, combined with a bitwise **OR**.



| Flag                              | Description                                                                  |
|-----------------------------------|------------------------------------------------------------------------------|
| WMDRM\_QUERY\_CLIENT\_INDIVSTATUS | Query whether the computer's DRM components need to be individualized.       |
| WMDRM\_QUERY\_DEVICE\_CLOCKSTATUS | Query whether the device's secure clock needs to be added or updated.        |
| WMDRM\_QUERY\_DEVICE\_ISREVOKED   | Query whether the device is revoked.                                         |
| WMDRM\_QUERY\_DEVICE\_ISWMDRM     | Query whether the device supports Windows Media DRM 10 for Portable Devices. |



 

</dd> <dt>

*pdwStatus* \[out\]
</dt> <dd>

Zero or more of the following **DWORD** values specifying the requested device status, combined with a bitwise **OR**.



| Status                      | Description                                              |
|-----------------------------|----------------------------------------------------------|
| WMDRM\_DEVICE\_ISWMDRM      | The device supports Windows Media DRM.                   |
| WMDRM\_DEVICE\_NEEDCLOCK    | The device does not have a secure clock.                 |
| WMDRM\_DEVICE\_REVOKED      | The device has been revoked.                             |
| WMDRM\_CLIENT\_NEEDINDIV    | The computer's DRM components need to be individualized. |
| WMDRM\_DEVICE\_REFRESHCLOCK | The clock needs to be refreshed.                         |



 

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                              | Description                                                               |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                     | The method succeeded.<br/>                                          |
| <dl> <dt>**DRM\_E\_INVALIDARG**</dt> </dl>                        | One or more arguments are not valid.<br/>                           |
| <dl> <dt>**NS\_E\_DRM\_INVALID\_CERTIFICATE**</dt> </dl>          | The device certificate retrieved from the device is not valid.<br/> |
| <dl> <dt>**NS\_E\_DRM\_UNABLE\_TO\_GET\_DEVICE\_CERT**</dt> </dl> | Failed to retrieve the device certificate from the device.<br/>     |



 

## Remarks

This method should be called before performing any restricted actions on DRM content, such as transferring DRM content to the device, or acquiring metering information. If the values retrieved by *pdwStatus* indicate that some action needs to be performed (such as individualization for the desktop or acquiring a clock for the device), the application should call [**IWMDRMDeviceApp::AcquireDeviceData**](iwmdrmdeviceapp-acquiredevicedata.md) and pass in the retrieved *pdwStatus* value from this function to the *dwFlags* parameter in **AcquireDeviceData**. If zero is returned, the device does not support Windows Media DRM 10 for Portable Devices, and no actions need be taken. See [Handling Protected Content in the Application](handling-protected-content-in-the-application.md) for more information.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMDRMDeviceApp.h (also requires Wmdrmdeviceapp\_i.c, built from WMDRMDeviceApp.idl)</dt> </dl> |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl>                                                                        |



## See also

<dl> <dt>

[**Handling Protected Content in the Application**](handling-protected-content-in-the-application.md)
</dt> <dt>

[**IWMDRMDeviceApp::QueryDeviceStatus**](iwmdrmdeviceapp-querydevicestatus.md)
</dt> <dt>

[**IWMDRMDeviceApp2 Interface**](iwmdrmdeviceapp2.md)
</dt> </dl>

 

 





