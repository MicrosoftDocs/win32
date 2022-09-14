---
description: Opens a scan profile that has been saved to disk as an XML file.
ms.assetid: 2b45280e-a1b6-4db9-af8c-09faff34b067
title: IScanProfileMgr::OpenProfile method (Scanprofilemgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfileMgr.OpenProfile
api_type: 
- COM
api_location: 
- Scanprofilemgr.h
---

# IScanProfileMgr::OpenProfile method

Opens a scan profile that has been saved to disk as an XML file.

## Syntax


```C++
HRESULT OpenProfile(
  [in]  GUID         guid,
  [out] IScanProfile **ppScanProfile
);
```



## Parameters

<dl> <dt>

*guid* \[in\]
</dt> <dd>

Type: **GUID**

The GUID of the profile.

</dd> <dt>

*ppScanProfile* \[out\]
</dt> <dd>

Type: **[**IScanProfile**](-wia-iscanprofile.md)\*\***

The address of a pointer to the profile.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If a scan profile is saved using the [**Save**](-wia-iscanprofile-save.md) method, it is stored as an XML file at %USERPROFILE%\\Application Data\\Microsoft\\Document Center\\UserScanProfiles.

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

 

 




