---
description: Gets the number of scan profiles for the device.
ms.assetid: fb1f8884-28ef-460e-a8c4-b9608cc89dc6
title: IScanProfileMgr::GetNumProfilesforDeviceID method (Scanprofilemgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfileMgr.GetNumProfilesforDeviceID
api_type: 
- COM
api_location: 
- Scanprofilemgr.h
---

# IScanProfileMgr::GetNumProfilesforDeviceID method

Gets the number of scan profiles for the device.

## Syntax


```C++
HRESULT GetNumProfilesforDeviceID(
  [in]  BSTR  bstrDeviceID,
  [out] ULONG *pulNumProfiles
);
```



## Parameters

<dl> <dt>

*bstrDeviceID* \[in\]
</dt> <dd>

Type: **BSTR**

The ID of the device.

</dd> <dt>

*pulNumProfiles* \[out\]
</dt> <dd>

Type: **ULONG\***

A pointer to the number of profiles available for the device.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

 




