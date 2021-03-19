---
title: IWMDRMDeviceApp ProcessMeterResponse method (WMDRMDeviceApp.h)
description: The ProcessMeterResponse method resets some or all of the metering counts on a device, after data from the device has been sent to and processed by the server.
ms.assetid: bafc4bb2-aa3c-4b2a-a818-1a78577cefc5
keywords:
- ProcessMeterResponse method windows Media Device Manager
- ProcessMeterResponse method windows Media Device Manager , IWMDRMDeviceApp interface
- IWMDRMDeviceApp interface windows Media Device Manager , ProcessMeterResponse method
topic_type:
- apiref
api_name:
- IWMDRMDeviceApp.ProcessMeterResponse
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDeviceApp::ProcessMeterResponse method

The **ProcessMeterResponse** method resets some or all of the metering counts on a device, after data from the device has been sent to and processed by the server.

## Syntax


```C++
HRESULT ProcessMeterResponse(
  [in]  IWMDMDevice *pDevice,
  [in]  BYTE        *pbResponse,
  [in]  DWORD       cbResponse,
  [out] DWORD       *pdwFlags
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Pointer to an [**IWMDMDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice) object.

</dd> <dt>

*pbResponse* \[in\]
</dt> <dd>

Response received from a metering server, after sending data generated using [**GenerateMeterChallenge**](iwmdrmdeviceapp-generatemeterchallenge.md).

</dd> <dt>

*cbResponse* \[in\]
</dt> <dd>

Size of *pbResponse*, in bytes.

</dd> <dt>

*pdwFlags* \[out\]
</dt> <dd>

A **DWORD** from the following table indicating whether there is more metering data on the device that needs to be processed.



| Flag                            | Description                                     |
|---------------------------------|-------------------------------------------------|
| WMDRM\_METER\_RESPONSE\_ALL     | All metering data has been processed.           |
| WMDRM\_METER\_RESPONSE\_PARTIAL | Additional metering data needs to be processed. |



 

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                      | Description                                                                   |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                             | The method succeeded.<br/>                                              |
| <dl> <dt>**DRM\_E\_INVALIDARG**</dt> </dl>                | One or more arguments are not valid.<br/>                               |
| <dl> <dt>**Errors from the device**</dt> </dl>            | Any of a number of device errors.<br/>                                  |
| <dl> <dt>**Errors from the DRM Client**</dt> </dl>        | Any of a number of internal DRM client errors.<br/>                     |
| <dl> <dt>**NS\_E\_DEVICE\_NOT\_WMDRM\_DEVICE**</dt> </dl> | The specified device is not a Windows Media DRM compatible device.<br/> |



 

## Remarks

More information on metering, including code examples, can be found in the whitepaper [Metering the Use of Digital Media Content with Windows Media DRM 10](/previous-versions//bb614723(v=vs.85)) on the MSDN Web site.

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

[**IWMDRMDeviceApp Interface**](iwmdrmdeviceapp.md)
</dt> </dl>

 

