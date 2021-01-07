---
description: Gets all the scan profiles available for the user in the system that your application is running under.
ms.assetid: 9787079e-283c-4f6d-b97c-cfc1349ada30
title: IScanProfileMgr::GetProfiles method (Scanprofilemgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfileMgr.GetProfiles
api_type: 
- COM
api_location: 
- Scanprofilemgr.h
---

# IScanProfileMgr::GetProfiles method

Gets all the scan profiles available for the user in the system that your application is running under.

## Syntax


```C++
HRESULT GetProfiles(
  [in, out] ULONG        *pulNumProfiles,
  [out]     IScanProfile **ppScanProfile
);
```



## Parameters

<dl> <dt>

*pulNumProfiles* \[in, out\]
</dt> <dd>

Type: **ULONG\***

When passed, a pointer to the maximum number of profiles to be returned. When returned, a pointer to the number of profiles returned.

</dd> <dt>

*ppScanProfile* \[out\]
</dt> <dd>

Type: **[**IScanProfile**](-wia-iscanprofile.md)\*\***

The address of an array of pointers to profiles.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the total number of profiles available for the user is smaller than the value passed to *pulNumProfiles*, then *pulNumProfiles* returns that total. Otherwise, it returns the same value that was passed to it.

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

 

 




