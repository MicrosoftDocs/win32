---
title: IWMDRMDeviceApp SynchronizeLicenses method (WMDRMDeviceApp.h)
description: The SynchronizeLicenses method updates licenses on a device when they are close to expiring.
ms.assetid: 352378c1-7432-476c-98e9-d811165c020e
keywords:
- SynchronizeLicenses method windows Media Device Manager
- SynchronizeLicenses method windows Media Device Manager , IWMDRMDeviceApp interface
- IWMDRMDeviceApp interface windows Media Device Manager , SynchronizeLicenses method
topic_type:
- apiref
api_name:
- IWMDRMDeviceApp.SynchronizeLicenses
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDeviceApp::SynchronizeLicenses method

The **SynchronizeLicenses** method updates licenses on a device when they are close to expiring.

## Syntax


```C++
HRESULT SynchronizeLicenses(
  [in] IWMDMDevice    *pDevice,
  [in] IWMDMProgress3 *pProgressCallback,
  [in] DWORD          cMinCountThreshold,
  [in] DWORD          cMinHoursThreshold
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Pointer to an [**IWMDMDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice) object.

</dd> <dt>

*pProgressCallback* \[in\]
</dt> <dd>

Progress callback that will receive progress of any steps that it might need to carry out. The step is identified by the *EventId* parameter of the [**IWMDMProgress3**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmprogress3) method called.

</dd> <dt>

*cMinCountThreshold* \[in\]
</dt> <dd>

Optional minimum remaining play count on a device license.

</dd> <dt>

*cMinHoursThreshold* \[in\]
</dt> <dd>

Optional minimum remaining hours on a device license.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                         | Description                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                | The method succeeded.<br/>                                                                                                                            |
| <dl> <dt>**DRM\_E\_INVALIDARG**</dt> </dl>                   | One or more arguments are not valid.<br/>                                                                                                             |
| <dl> <dt>**DRM\_E\_INVALIDXMLTAG**</dt> </dl>                | XML is improperly formed.<br/>                                                                                                                        |
| <dl> <dt>**DRM\_E\_NOTIMPL**</dt> </dl>                      | This functionality is not currently implemented. (SyncLicenses w/ *pDevice* =NULL)<br/>                                                               |
| <dl> <dt>**DRM\_E\_NOXMLCLOSETAG**</dt> </dl>                | The license XML was improperly formed.<br/>                                                                                                           |
| <dl> <dt>**DRM\_E\_NOXMLOPENTAG**</dt> </dl>                 | The license XML was improperly formed.<br/>                                                                                                           |
| <dl> <dt>**DRM\_E\_OUTOFMEMORY**</dt> </dl>                  | Out of memory.<br/>                                                                                                                                   |
| <dl> <dt>**DRM\_E\_XMLNOTFOUND**</dt> </dl>                  | Failed to find a required XML tag in the license.<br/>                                                                                                |
| <dl> <dt>**NS\_E\_DEVICE\_NOT\_WMDRM\_DEVICE**</dt> </dl>    | The specified device is not a Windows Media DRM-compatible device.<br/>                                                                               |
| <dl> <dt>**NS\_E\_DRM\_NEEDS\_INDIVIDUALIZATION**</dt> </dl> | The DRM requires an individualized black box to perform this function. In other words, the Windows Media Format SDK requires a security upgrade.<br/> |



 

## Remarks

This call can only be made on a device that supports Windows Media DRM 10 for Portable Devices. You must specify at least one threshold parameter.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMDRMDeviceApp.h (also requires Wmdrmdeviceapp\_i.c, built from WMDRMDeviceApp.idl)</dt> </dl> |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl>                                                                        |



## See also

<dl> <dt>

[**Handling Protected Content in the Application**](handling-protected-content-in-the-application.md)
</dt> <dt>

[**IWMDMProgress3 Interface**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmprogress3)
</dt> <dt>

[**IWMDRMDeviceApp Interface**](iwmdrmdeviceapp.md)
</dt> </dl>

 

 





