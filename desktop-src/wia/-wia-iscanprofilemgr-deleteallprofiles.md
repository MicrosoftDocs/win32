---
description: Deletes all the scan profiles associated with the specified device.
ms.assetid: 5abf101b-0442-47fc-8159-95db63f0af78
title: IScanProfileMgr::DeleteAllProfiles method (Scanprofilemgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfileMgr.DeleteAllProfiles
api_type: 
- COM
api_location: 
- Scanprofilemgr.h
---

# IScanProfileMgr::DeleteAllProfiles method

Deletes all the scan profiles associated with the specified device.

## Syntax


```C++
HRESULT DeleteAllProfiles(
  [in] BSTR bstrDeviceID
);
```



## Parameters

<dl> <dt>

*bstrDeviceID* \[in\]
</dt> <dd>

Type: **BSTR**

The ID of the device.

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

 

 




