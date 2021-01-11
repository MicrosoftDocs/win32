---
description: Saves changes to a profile to disk.
ms.assetid: e844bd4c-93c3-44a3-b7d5-0beb71c9fa17
title: IScanProfile::Save method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.Save
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::Save method

Saves changes to a profile to disk.

## Syntax


```C++
HRESULT Save();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

A saved scan profile is an XML file stored at %USERPROFILE%\\Application Data\\Microsoft\\Document Center\\UserScanProfiles.

If more than one process writes to the [**IScanProfile**](-wia-iscanprofile.md) object, the one that calls **IScanProfile::Save** last is the only process whose changes are saved.

The **IScanProfile::Save** method validates the profile before saving. The profile is always considered valid unless the category of the Windows Image Acquisition (WIA) 2.0 item associated with the profile is either WIA\_CATEGORY\_FLATBED or WIA\_CATEGORY\_FEEDER. If the category is WIA\_CATEGORY\_FLATBED or WIA\_CATEGORY\_FEEDER, the following properties must be valid for the item, if the properties are contained in the profile:

WIA\_IPS\_BRIGHTNESS

WIA\_IPS\_CONTRAST

WIA\_IPA\_DATATYPE

WIA\_IPS\_XRES

WIA\_IPA\_FORMAT

In addition, if the category is WIA\_CATEGORY\_FEEDER, the WIA\_IPS\_PAGE\_SIZE property must be valid, if it is present in the profile. For more information about these properties, see [**Scanner WIA Item Property Constants**](-wia-wiaitempropscanneritem.md).

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

 

 




