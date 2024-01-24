---
description: Gets a value that indicates whether the profile is the default scan profile of an associated IWiaItem2 device.
ms.assetid: 32ca3b9f-6235-4eec-aa94-bf20f15a9a16
title: IScanProfile::IsDefault method (Scanprofile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile.IsDefault
api_type: 
- COM
api_location: 
- Scanprofile.h
---

# IScanProfile::IsDefault method

Gets a value that indicates whether the profile is the default scan profile of an associated [**IWiaItem2**](-wia-iwiaitem2.md) device.

## Syntax


```C++
HRESULT IsDefault(
  [out] BOOL *pbDefault
);
```



## Parameters

<dl> <dt>

*pbDefault* \[out\]
</dt> <dd>

Type: **BOOL\***

A pointer to a **BOOL**.

<dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE**


</dt> <dd>

The profile is the default.

</dd> <dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE**


</dt> <dd>

The profile is not the default.

</dd> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

*pbDefault* is **TRUE** if the profile contains a `<Default>` element. It is **FALSE** if no such element is present. The element has no value.

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

 

 




