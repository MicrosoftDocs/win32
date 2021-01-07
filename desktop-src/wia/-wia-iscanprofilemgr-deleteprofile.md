---
description: Deletes the specified scan profile.
ms.assetid: 31020528-3a96-492f-a3a1-e9075d4ffd14
title: IScanProfileMgr::DeleteProfile method (Scanprofilemgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfileMgr.DeleteProfile
api_type: 
- COM
api_location: 
- Scanprofilemgr.h
---

# IScanProfileMgr::DeleteProfile method

Deletes the specified scan profile.

## Syntax


```C++
HRESULT DeleteProfile(
  [in] IScanProfile *pScanProfile
);
```



## Parameters

<dl> <dt>

*pScanProfile* \[in\]
</dt> <dd>

Type: **[**IScanProfile**](-wia-iscanprofile.md)\***

A pointer to the profile.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

**IScanProfileMgr::DeleteProfile** deletes the profile from disk and destroys the profile object in memory.

Use the [**IScanProfileMgr::Refresh**](-wia-iscanprofilemgr-refresh.md) method when more than one [**IScanProfileMgr**](-wia-iscanprofilemgr.md) object might be creating or deleting profiles at the same time.

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

 

 




