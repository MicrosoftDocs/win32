---
description: Sets the GUID of the category of Windows Image Acquisition (WIA) 2.0 item that the profile is associated with.
ms.assetid: e359abcb-b5d5-45a4-b650-2b278ba1ff6a
title: IScanProfile::SetItem method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.SetItem
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::SetItem method

Sets the GUID of the category of Windows Image Acquisition (WIA) 2.0 item that the profile is associated with.

## Syntax


```C++
HRESULT SetItem(
  [in] GUID guidCategory
);
```



## Parameters

<dl> <dt>

*guidCategory* \[in\]
</dt> <dd>

Type: **GUID**

The GUID of the category of the WIA 2.0 item. This must be one of the WIA\_IPA\_ITEM\_CATEGORY constants.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Users can change the category with the [**ScanProfileDialog**](-wia-iscanprofileui-scanprofiledialog.md) method.

Changes to a profile are not saved to disk until the application calls the [**IScanProfile::Save**](-wia-iscanprofile-save.md) method.

If two applications create scan profile objects from the same XML file, and each application writes changes to its object, only the changes made by the application that calls [**IScanProfile::Save**](-wia-iscanprofile-save.md) last are saved to disk.

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

 

 




