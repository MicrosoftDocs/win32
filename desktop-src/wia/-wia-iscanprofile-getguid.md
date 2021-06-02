---
description: Returns the GUID of the profile.
ms.assetid: 184456dd-515d-4744-91f3-0ef8b4d2114d
title: IScanProfile::GetGUID method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.GetGUID
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::GetGUID method

Returns the GUID of the profile.

## Syntax


```C++
HRESULT GetGUID(
  [out] GUID *retVal
);
```



## Parameters

<dl> <dt>

*retVal* \[out\]
</dt> <dd>

Type: **GUID\***

A pointer to the GUID of the profile.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The GUID for a profile is automatically generated when the profile is created with [**CreateProfile**](-wia-iscanprofilemgr-createprofile.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                        |
| Header<br/>                   | <dl> <dt>Scanprofile.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>Scanprofiles.idl</dt> </dl> |



## See also

<dl> <dt>

[**IScanProfile**](-wia-iscanprofile.md)
</dt> <dt>

[Scan Profile Schema](-wia-scan-profile-schema.md)
</dt> </dl>

 

 




