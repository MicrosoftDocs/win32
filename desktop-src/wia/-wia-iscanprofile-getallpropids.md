---
description: Gets all available property IDs in a profile.
ms.assetid: 9ef2abdd-0b33-4be3-a124-7795f42d5e55
title: IScanProfile::GetAllPropIDs method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.GetAllPropIDs
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::GetAllPropIDs method

Gets all available property IDs in a profile.

## Syntax


```C++
HRESULT GetAllPropIDs(
  [in, out] ULONG  *num,
  [out]     PROPID *ppid
);
```



## Parameters

<dl> <dt>

*num* \[in, out\]
</dt> <dd>

Type: **ULONG\***

The number of property IDs requested or returned.

</dd> <dt>

*ppid* \[out\]
</dt> <dd>

Type: **PROPID\***

A pointer to an array of property IDs.

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

 

 




