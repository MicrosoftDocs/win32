---
description: Gets the value of specified child properties in the <Properties> element of a scan profile.
ms.assetid: 528b51f5-51e0-4639-965d-ee318eb2187b
title: IScanProfile::GetProperty method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.GetProperty
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::GetProperty method

Gets the value of specified child properties in the `<Properties>` element of a scan profile.

## Syntax


```C++
HRESULT GetProperty(
  [in]  ULONG       num,
  [in]  PROPID      *pid,
  [out] PROPVARIANT *pvar
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

A pointer to an array of the identification numbers of the properties to be set. Each value in the array is a [WIA Property Constants](-wia-wia-property-constants.md).

</dd> <dt>

*pvar* \[out\]
</dt> <dd>

Type: **[PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)\***

A pointer to an array of values.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_FALSE if any of the property values is not available; otherwise, returns S\_OK or a standard COM error code.

## Remarks

The type of each value must be the same type that was set with the call to [**IScanProfile::SetProperty**](-wia-iscanprofile-setproperty.md).

Each value in the array that *pid* points to is one of the [WIA Property Constants](-wia-wia-property-constants.md). You can extend this identification system. See [Defining Custom Properties](-wia-defining-custom-properties.md).

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

 

 
