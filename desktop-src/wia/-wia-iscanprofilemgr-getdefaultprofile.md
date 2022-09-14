---
description: Gets the default scan profile.
ms.assetid: 0e5ca06a-78ca-4d24-8dda-26babc3124b5
title: IScanProfileMgr::GetDefaultProfile method (Scanprofilemgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfileMgr.GetDefaultProfile
api_type: 
- COM
api_location: 
- Scanprofilemgr.h
---

# IScanProfileMgr::GetDefaultProfile method

Gets the default scan profile.

## Syntax


```C++
HRESULT GetDefaultProfile(
  [in]  BSTR         bstrDeviceID,
  [out] IScanProfile **ppScanProfile
);
```



## Parameters

<dl> <dt>

*bstrDeviceID* \[in\]
</dt> <dd>

Type: **BSTR**

The ID of the device.

</dd> <dt>

*ppScanProfile* \[out\]
</dt> <dd>

Type: **[**IScanProfile**](-wia-iscanprofile.md)\*\***

The address of a pointer to the device's default profile.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The default profile has a `<Default>` element.

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

 

 




