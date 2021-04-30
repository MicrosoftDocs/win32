---
description: Sets the friendly name of the profile.
ms.assetid: a0a2de8b-ab7b-49a8-b513-32af0052975f
title: IScanProfile::SetName method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.SetName
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::SetName method

Sets the friendly name of the profile.

## Syntax


```C++
HRESULT SetName(
  [in] BSTR bstrName
);
```



## Parameters

<dl> <dt>

*bstrName* \[in\]
</dt> <dd>

Type: **BSTR**

The friendly name of the profile.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is required because the GUID of a profile cannot be used to display the scan profile to a user.

A user can change the friendly name of a profile with the [**ScanProfileDialog**](-wia-iscanprofileui-scanprofiledialog.md) method.

Changes to a profile are not saved to disk until the application calls the [**IScanProfile::Save**](-wia-iscanprofile-save.md) method.

If two applications create scan profile objects from the same XML file, and each application writes changes to its object, only the changes made by the application that calls [**IScanProfile::Save**](-wia-iscanprofile-save.md) last are saved to disk.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                        |
| Header<br/>                   | <dl> <dt>Scanprofile.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>Scanprofiles.idl</dt> </dl> |



 

 




