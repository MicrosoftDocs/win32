---
description: Returns the ID of the device.
ms.assetid: 72a0843d-36f2-463f-8269-0e91233f1931
title: IScanProfile::GetDeviceID method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.GetDeviceID
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::GetDeviceID method

Returns the ID of the device.

## Syntax


```C++
HRESULT GetDeviceID(
  [out] BSTR *pbstrDeviceID
);
```



## Parameters

<dl> <dt>

*pbstrDeviceID* \[out\]
</dt> <dd>

Type: **BSTR\***

A pointer to the device ID.

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

 

 




