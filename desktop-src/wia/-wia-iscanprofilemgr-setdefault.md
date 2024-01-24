---
description: Sets the specified scan profile as the default profile.
ms.assetid: c680be8b-88f0-4f7f-b1a3-e12711dba870
title: IScanProfileMgr::SetDefault method (Scanprofilemgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfileMgr.SetDefault
api_type: 
- COM
api_location: 
- Scanprofilemgr.h
---

# IScanProfileMgr::SetDefault method

Sets the specified scan profile as the default profile.

## Syntax


```C++
HRESULT SetDefault(
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

Use the **IScanProfileMgr::SetDefault** method to add a `<Default>` element to the profile or to remove that element from the device's previous default profile.

Use the [**ScanProfileDialog**](-wia-iscanprofileui-scanprofiledialog.md) method to change the default profile.

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

 

 




