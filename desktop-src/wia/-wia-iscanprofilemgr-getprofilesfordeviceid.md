---
description: Gets all the scan profiles associated with a device.
ms.assetid: 2e509f01-9c5e-4d17-8888-b08b6b4b9fa9
title: IScanProfileMgr::GetProfilesforDeviceID method (Scanprofilemgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfileMgr.GetProfilesforDeviceID
api_type: 
- COM
api_location: 
- Scanprofilemgr.h
---

# IScanProfileMgr::GetProfilesforDeviceID method

Gets all the scan profiles associated with a device.

## Syntax


```C++
HRESULT GetProfilesforDeviceID(
  [in]      BSTR         bstrDeviceID,
  [in, out] ULONG        *pulNumProfiles,
  [out]     IScanProfile **ppScanProfile
);
```



## Parameters

<dl> <dt>

*bstrDeviceID* \[in\]
</dt> <dd>

Type: **BSTR**

The ID of the device.

</dd> <dt>

*pulNumProfiles* \[in, out\]
</dt> <dd>

Type: **ULONG\***

When passed, a pointer to the maximum number of profiles to be returned. When returned, the a pointer to the number of profiles returned.

</dd> <dt>

*ppScanProfile* \[out\]
</dt> <dd>

Type: **[**IScanProfile**](-wia-iscanprofile.md)\*\***

The address of a pointer to an array of profiles.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the total number of profiles associated with the device is smaller than the value passed to *pulNumProfiles*, then *pulNumProfiles* returns that total. Otherwise, it returns the same value that was passed to it.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                        |
| Header<br/>                   | <dl> <dt>Scanprofilemgr.h</dt> </dl> |
| IDL<br/>                      | <dl> <dt>Scanprofiles.idl</dt> </dl> |



## See also

<dl> <dt>

[**IScanProfileMgr**](-wia-iscanprofilemgr.md)
</dt> <dt>

[Scan Profile Schema](-wia-scan-profile-schema.md)
</dt> </dl>

 

 




