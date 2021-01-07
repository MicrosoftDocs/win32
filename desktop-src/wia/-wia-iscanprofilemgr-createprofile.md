---
description: Creates an empty scan profile and associates it with a scanner or other Windows Image Acquisition (WIA) 2.0 item.
ms.assetid: daa8cd66-184b-4559-a22a-c3e6d8209a3f
title: IScanProfileMgr::CreateProfile method (Scanprofilemgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfileMgr.CreateProfile
api_type: 
- COM
api_location: 
- Scanprofilemgr.h
---

# IScanProfileMgr::CreateProfile method

Creates an empty scan profile and associates it with a scanner or other Windows Image Acquisition (WIA) 2.0 item.

## Syntax


```C++
HRESULT CreateProfile(
  [in]  BSTR         bstrDeviceID,
  [in]  BSTR         bstrName,
  [in]  GUID         guidCategory,
  [out] IScanProfile **ppScanProfile
);
```



## Parameters

<dl> <dt>

*bstrDeviceID* \[in\]
</dt> <dd>

Type: **BSTR**

The ID of the device or WIA 2.0 item.

</dd> <dt>

*bstrName* \[in\]
</dt> <dd>

Type: **BSTR**

The friendly name of the new profile.

</dd> <dt>

*guidCategory* \[in\]
</dt> <dd>

Type: **GUID**

The GUID of the category of the device or WIA 2.0 item. This must be one of the WIA\_IPA\_ITEM\_CATEGORY constants.

</dd> <dt>

*ppScanProfile* \[out\]
</dt> <dd>

Type: **[**IScanProfile**](-wia-iscanprofile.md)\*\***

The address of a pointer to the new profile.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

**IScanProfileMgr::CreateProfile** associates the specified device with the new scan profile.

**IScanProfileMgr::CreateProfile** automatically generates a GUID for the new profile. Get the GUID with [**GetGUID**](-wia-iscanprofile-getguid.md).

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

 

 




