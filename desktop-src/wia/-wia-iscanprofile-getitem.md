---
description: Gets the GUID of the category of the Windows Image Acquisition (WIA) 2.0 item that the profile is associated with.
ms.assetid: 2c816789-ad66-4b06-9160-7a86289ff373
title: IScanProfile::GetItem method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.GetItem
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::GetItem method

Gets the GUID of the category of the Windows Image Acquisition (WIA) 2.0 item that the profile is associated with.

## Syntax


```C++
HRESULT GetItem(
  [out] GUID *pguidCategory
);
```



## Parameters

<dl> <dt>

*pguidCategory* \[out\]
</dt> <dd>

Type: **GUID\***

A pointer to the GUID of the category of the WIA 2.0 item. This is always one of the WIA\_IPA\_ITEM\_CATEGORY constants.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

 




