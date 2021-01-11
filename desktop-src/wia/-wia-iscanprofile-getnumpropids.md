---
description: Gets the number of property IDs in a profile.
ms.assetid: fa587c8a-8d09-4dfc-938a-5ec8cc9265f5
title: IScanProfile::GetNumPropIDS method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.GetNumPropIDS
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::GetNumPropIDS method

Gets the number of property IDs in a profile.

## Syntax


```C++
HRESULT GetNumPropIDS(
  [out] ULONG *num
);
```



## Parameters

<dl> <dt>

*num* \[out\]
</dt> <dd>

Type: **ULONG\***

The number of property IDs in the profile.

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

 

 




