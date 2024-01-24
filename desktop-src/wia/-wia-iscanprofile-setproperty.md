---
description: Sets the value of specified child properties in the <Properties> element of a scan profile.
ms.assetid: 3cf7b723-4004-49e5-b3bd-49a84432ede3
title: IScanProfile::SetProperty method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.SetProperty
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::SetProperty method

Sets the value of specified child properties in the `<Properties>` element of a scan profile.

## Syntax


```C++
HRESULT SetProperty(
  [in] ULONG       num,
  [in] PROPID      *pid,
  [in] PROPVARIANT *pvar
);
```



## Parameters

<dl> <dt>

*num* \[in\]
</dt> <dd>

Type: **ULONG**

The number of entries in the arrays that are pointed to by *pid* and *pvar*.

</dd> <dt>

*pid* \[in\]
</dt> <dd>

Type: **PROPID\***

A pointer to an array of identification numbers of the properties to be set. Each value in the array is a [WIA Property Constants](-wia-wia-property-constants.md).

</dd> <dt>

*pvar* \[in\]
</dt> <dd>

Type: **[PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)\***

A pointer to an array of values to be assigned to the properties.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Each value in the array that *pid* points to is one of the [WIA Property Constants](-wia-wia-property-constants.md). You can extend this identification system. See [Defining Custom Properties](-wia-defining-custom-properties.md).

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

**Conceptual**
</dt> <dt>

[Scan Profile Schema](-wia-scan-profile-schema.md)
</dt> <dt>

[WIA Property Constants](-wia-wia-property-constants.md)
</dt> <dt>

[Defining Custom Properties](-wia-defining-custom-properties.md)
</dt> </dl>

 

 
