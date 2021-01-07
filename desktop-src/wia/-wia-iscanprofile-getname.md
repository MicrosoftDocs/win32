---
description: Gets the friendly name of the profile.
ms.assetid: db2f8229-ce43-4608-af3f-a06011b4fac0
title: IScanProfile::GetName method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.GetName
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::GetName method

Gets the friendly name of the profile.

## Syntax


```C++
HRESULT GetName(
  [out] BSTR *pbstrName
);
```



## Parameters

<dl> <dt>

*pbstrName* \[out\]
</dt> <dd>

Type: **BSTR\***

The friendly name of the profile.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is required because the GUID of a profile cannot be used to display the scan profile to a user.

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

 

 




