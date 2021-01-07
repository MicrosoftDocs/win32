---
description: Gets the number of scan profiles created for the user in the system that your application is running under.
ms.assetid: 0667a885-d61f-4c44-b988-a42242c2678e
title: IScanProfileMgr::GetNumProfiles method (Scanprofilemgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfileMgr.GetNumProfiles
api_type: 
- COM
api_location: 
- Scanprofilemgr.h
---

# IScanProfileMgr::GetNumProfiles method

Gets the number of scan profiles created for the user in the system that your application is running under.

## Syntax


```C++
HRESULT GetNumProfiles(
  [out] ULONG *pulNumProfiles
);
```



## Parameters

<dl> <dt>

*pulNumProfiles* \[out\]
</dt> <dd>

Type: **ULONG\***

A pointer to the number of profiles created for the user.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

 




