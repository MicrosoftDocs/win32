---
title: IWMDRMDeviceApp QueryDeviceStatus method (WMDRMDeviceApp.h)
description: The QueryDeviceStatus method queries a device for its current DRM status and capabilities.
ms.assetid: cd5a75d5-d7f8-4077-a9fc-6e7ddd7c796b
keywords:
- QueryDeviceStatus method windows Media Device Manager
- QueryDeviceStatus method windows Media Device Manager , IWMDRMDeviceApp interface
- IWMDRMDeviceApp interface windows Media Device Manager , QueryDeviceStatus method
topic_type:
- apiref
api_name:
- IWMDRMDeviceApp.QueryDeviceStatus
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDeviceApp::QueryDeviceStatus method

The **QueryDeviceStatus** method queries a device for its current DRM status and capabilities.

## Syntax


```C++
HRESULT QueryDeviceStatus(
  [in]  IWMDMDevice *pDevice,
  [out] DWORD       *pdwStatus
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Pointer to an [**IWMDMDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice) object.

</dd> <dt>

*pdwStatus* \[out\]
</dt> <dd>

Zero or more of the following **DWORD** values describing the DRM aspects of the device, combined with a bitwise **OR**. See Remarks.



| Status                      | Description                                  |
|-----------------------------|----------------------------------------------|
| WMDRM\_DEVICE\_ISWMDRM      | The device supports Windows Media DRM.       |
| WMDRM\_DEVICE\_NEEDCLOCK    | The device does not have a secure clock.     |
| WMDRM\_DEVICE\_REVOKED      | The device has been revoked.                 |
| WMDRM\_CLIENT\_NEEDINDIV    | The DRM security needs to be individualized. |
| WMDRM\_DEVICE\_REFRESHCLOCK | The clock needs to be refreshed.             |



 

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                              | Description                                                               |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                     | The method succeeded.<br/>                                          |
| <dl> <dt>**DRM\_E\_INVALIDARG**</dt> </dl>                        | The input argument is not valid.<br/>                               |
| <dl> <dt>**NS\_E\_DRM\_INVALID\_CERTIFICATE**</dt> </dl>          | The device certificate retrieved from the device is not valid.<br/> |
| <dl> <dt>**NS\_E\_DRM\_UNABLE\_TO\_GET\_DEVICE\_CERT**</dt> </dl> | Failed to retrieve the device certificate from the device.<br/>     |



 

## Remarks

This method should be called before performing any restricted actions on DRM content, such as transferring DRM content to the device, or acquiring metering information. If the values retrieved by *pdwStatus* indicate that some action needs to be performed (such as individualization for the desktop or acquiring a clock for the device), the application should call [**AcquireDeviceData**](iwmdrmdeviceapp-acquiredevicedata.md) and pass the retrieved *pdwStatus* value from this function to the *dwFlags* parameter in **AcquireDeviceData**. If zero is returned, the device does not support Windows Media DRM 10 for Portable Devices, and no actions need be taken. See [Handling Protected Content in the Application](handling-protected-content-in-the-application.md) for more information.

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

[**IWMDRMDeviceApp Interface**](iwmdrmdeviceapp.md)
</dt> <dt>

[**IWMDRMDeviceApp2::QueryDeviceStatus2**](iwmdrmdeviceapp2-querydevicestatus2.md)
</dt> </dl>

 

 





