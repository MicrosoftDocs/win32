---
title: IWMDRMDeviceApp AcquireDeviceData method (WMDRMDeviceApp.h)
description: The AcquireDeviceData method initializes or resets a device secure clock.
ms.assetid: 2f1cfdb9-0f07-4bee-94aa-b33b039453d0
keywords:
- AcquireDeviceData method windows Media Device Manager
- AcquireDeviceData method windows Media Device Manager , IWMDRMDeviceApp interface
- IWMDRMDeviceApp interface windows Media Device Manager , AcquireDeviceData method
topic_type:
- apiref
api_name:
- IWMDRMDeviceApp.AcquireDeviceData
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDeviceApp::AcquireDeviceData method

The **AcquireDeviceData** method initializes or resets a device secure clock.

## Syntax


```C++
HRESULT AcquireDeviceData(
  [in]  IWMDMDevice    *pDevice,
  [in]  IWMDMProgress3 *pProgressCallback,
  [in]  DWORD          dwFlags,
  [out] DWORD          *pdwStatus
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Pointer to an [**IWMDMDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice) interface for the device that will report metering data.

</dd> <dt>

*pProgressCallback* \[in\]
</dt> <dd>

Progress callback through which the application can track the progress of the event, or cancel the event. The progress is identified by the *EventId* parameter of [**IWMDMProgress3**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmprogress3) methods.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

A logical **OR** of one or both of the following flags, specifying what action to perform. This value is retrieved from the *pdwStatus* parameter of [**IWMDRMDeviceApp::QueryDeviceStatus**](iwmdrmdeviceapp-querydevicestatus.md) or [**IWMDRMDeviceApp2::QueryDeviceStatus2**](iwmdrmdeviceapp2-querydevicestatus2.md). You can use the *pdwStatus* flag directly.



| Flag                        | Description                                   |
|-----------------------------|-----------------------------------------------|
| WMDRM\_DEVICE\_NEEDCLOCK    | Acquire a clock from a secure clock server.   |
| WMDRM\_DEVICE\_REFRESHCLOCK | Refresh the clock from a secure clock server. |



 

</dd> <dt>

*pdwStatus* \[out\]
</dt> <dd>

One of the following **DWORD** values specifying the status returned by the device.



| Status | Description                                                     |
|--------|-----------------------------------------------------------------|
| 0      | The action is not supported.                                    |
| 1      | The device secure clock could not be acquired from the service. |
| 2      | The device's secure clock could not be set.                     |
| 3      | The device's secure clock was set.                              |



 

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                                             | Description                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                                    | The method succeeded.<br/>                                                                                                    |
| <dl> <dt>**DRM\_E\_INVALIDARG**</dt> </dl>                                       | One or more arguments are not valid.<br/>                                                                                     |
| <dl> <dt>**NS\_E\_DEVICE\_NOT\_WMDRM\_DEVICE**</dt> </dl>                        | The specified device is not a Windows Media DRM compatible device.<br/>                                                       |
| <dl> <dt>**NS\_E\_DRM\_UNABLE\_TO\_GET\_SECURE\_CLOCK**</dt> </dl>               | Failed to retrieve secure clock challenge from the device or unable to retrieve the secure clock URL from the challenge.<br/> |
| <dl> <dt>**NS\_E\_DRM\_UNABLE\_TO\_GET\_SECURE\_CLOCK\_FROM\_SERVER**</dt> </dl> | Failed to retrieve the secure clock response from the secure clock server.<br/>                                               |
| <dl> <dt>**NS\_E\_DRM\_UNABLE\_TO\_SET\_SECURE\_CLOCK**</dt> </dl>               | Failed to send the secure clock challenge to the device, or the device failed to set the clock.<br/>                          |



 

## Remarks

This is an asynchronous method; the device must await the [**IWMDMProgress::End**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmprogress-end) callback for this operation before attempting to play any licensed content.

An application can learn if the device must have its clock reset or updated by calling [**IWMDRMDeviceApp::QueryDeviceStatus**](iwmdrmdeviceapp-querydevicestatus.md) or [**IWMDRMDeviceApp2::QueryDeviceStatus2**](iwmdrmdeviceapp2-querydevicestatus2.md).

Your application must have an Internet connection to enable it to acquire or reset a secure clock.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMDRMDeviceApp.h (also requires Wmdrmdeviceapp\_i.c, built from WMDRMDeviceApp.idl)</dt> </dl> |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl>                                                                        |



## See also

<dl> <dt>

[**Handling Protected Content in the Application**](handling-protected-content-in-the-application.md)
</dt> <dt>

[**IWMDMDevice Interface**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice)
</dt> <dt>

[**IWMDMProgress3 Interface**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmprogress3)
</dt> <dt>

[**IWMDRMDeviceApp Interface**](iwmdrmdeviceapp.md)
</dt> </dl>

 

 





