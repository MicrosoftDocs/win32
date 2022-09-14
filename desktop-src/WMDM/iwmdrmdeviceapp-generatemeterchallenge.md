---
title: IWMDRMDeviceApp GenerateMeterChallenge method (WMDRMDeviceApp.h)
description: The GenerateMeterChallenge method acquires metering data from a device.
ms.assetid: 2457cab7-bd45-49a7-ba69-74ae022207ce
keywords:
- GenerateMeterChallenge method windows Media Device Manager
- GenerateMeterChallenge method windows Media Device Manager , IWMDRMDeviceApp interface
- IWMDRMDeviceApp interface windows Media Device Manager , GenerateMeterChallenge method
topic_type:
- apiref
api_name:
- IWMDRMDeviceApp.GenerateMeterChallenge
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDeviceApp::GenerateMeterChallenge method

The **GenerateMeterChallenge** method acquires metering data from a device.

## Syntax


```C++
HRESULT GenerateMeterChallenge(
  [in]  IWMDMDevice *pDevice,
  [in]  BSTR        bstrMeterCert,
  [out] BSTR        *pbstrMeterURL,
  [out] BSTR        *pbstrMeterData
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Pointer to an [**IWMDMDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice) interface. If the application passes in **NULL**, metering information stored on the computer is used instead of metering information from a connected device.

</dd> <dt>

*bstrMeterCert* \[in\]
</dt> <dd>

The application's metering certificate, as a **BSTR**. This is a signed certificate received from Microsoft.

</dd> <dt>

*pbstrMeterURL* \[out\]
</dt> <dd>

The URL where metering data should be sent. This is allocated by Windows Media Device Manager, and must be free by the caller using **SysFreeString**.

</dd> <dt>

*pbstrMeterData* \[out\]
</dt> <dd>

Metering data to send to the metering service. This is allocated by Windows Media Device Manager, and must be free by the caller using **SysFreeString**.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                      | Description                                                                   |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                             | The method succeeded.<br/>                                              |
| <dl> <dt>**DRM\_E\_INVALIDARG**</dt> </dl>                | One or more arguments are not valid.<br/>                               |
| <dl> <dt>**DRM\_E\_INVALIDXMLTAG**</dt> </dl>             | XML is improperly formed.<br/>                                          |
| <dl> <dt>**DRM\_E\_NOXMLCLOSETAG**</dt> </dl>             | XML is improperly formed.<br/>                                          |
| <dl> <dt>**DRM\_E\_NOXMLOPENTAG**</dt> </dl>              | XML is improperly formed.<br/>                                          |
| <dl> <dt>**DRM\_E\_XMLNOTFOUND**</dt> </dl>               | Failed to find a required XML tag.<br/>                                 |
| <dl> <dt>**Errors from the device**</dt> </dl>            | Any of a number of device errors.<br/>                                  |
| <dl> <dt>**Errors from the DRM Client**</dt> </dl>        | Any of a number of internal DRM client errors.<br/>                     |
| <dl> <dt>**NS\_E\_DEVICE\_NOT\_WMDRM\_DEVICE**</dt> </dl> | The specified device is not a Windows Media DRM compatible device.<br/> |



 

## Remarks

Before calling this method, the application should call [**IWMDRMDeviceApp::QueryDeviceStatus**](iwmdrmdeviceapp-querydevicestatus.md) or [**IWMDRMDeviceApp2::QueryDeviceStatus2**](iwmdrmdeviceapp2-querydevicestatus2.md) to verify that all the device's DRM components are up to date. This method can only be called on a device that supports Windows Media DRM 10 for Portable Devices.

The retrieved data *pbstrMeterData* should be sent to the URL specified by *pbstrMeterURL*. Be sure to URL-encode the retrieved data so that it does not get modified during transfer.

See [Handling Protected Content in the Application](handling-protected-content-in-the-application.md) for more information.

## Examples

The following C++ code example creates a **WMDRMDeviceApp** object, verifies that the device is a Windows Media DRM 10 device, that its clock is accurate, and then requests the metering data.


```C++
HRESULT hr = S_OK;
// Create the WMDRMDeviceApp object.
CComPtr<IWMDRMDeviceApp> pDRM;
hr = pDRM.CoCreateInstance(CLSID_WMDRMDeviceApp, 0, CLSCTX_ALL);

// Find out first if the device is a WMDRM 10 device, and if it requires
// any clock updates.
DWORD status = 0;
hr = pDRM->QueryDeviceStatus(pDevice, &status);

if (!(WMDRM_DEVICE_ISWMDRM & status)) // Device is not WMDRM 10. Nothing can be updated,
    return E_FAIL;                   // and metering cannot be performed.
else if (status & WMDRM_DEVICE_REVOKED) // Device is revoked.
    return E_FAIL;
else if (status & WMDRM_DEVICE_NEEDCLOCK || 
    status & WMDRM_CLIENT_NEEDINDIV ||
    status & WMDRM_DEVICE_REFRESHCLOCK)
{
    // Need to update device clock. 
    // Using custom function, which is synchronous.
    hr = myAcquireDeviceData(pDRM, pDevice, this, status, &result);
    if (hr != S_OK || result != 0)    // Couldn't perform the updates.
        return E_FAIL;    
}

// Any updates have been performed. Now get the metering information from the device.
CComBSTR meterCert(METERCERT);
CComBSTR URL;
CComBSTR rawdata;
CComBSTR data;
hr = pDRM->GenerateMeterChallenge(pDevice, meterCert, &URL, &rawdata);
if (hr == S_OK)
    ..... Send to URL...
```



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

 

 





