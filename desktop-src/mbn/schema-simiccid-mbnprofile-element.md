---
description: Identifies the SIM Identification number for GSM devices.
ms.assetid: 980afba4-fc31-4da0-ba01-6eb8e3db0ac8
title: SimIccID (MBNProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SimIccID
api_type: 
- Schema
---

# SimIccID (MBNProfile) Element

The **SimIccID (MBNProfile)** element identifies the SIM Identification number for GSM devices.

This element is optional and is set by the Mobile Broadband service for internal use. An application should not set this field while creating or updating a profile.

``` syntax
<xs:element name="SimIccID"
    type="simIccIDType"
 />
```

The **SimIccID** element is defined by the [**MBNProfile**](schema-mbnprofile-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**MBNProfile**](schema-mbnprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**MBNProfile**](schema-mbnprofile-element.md)
</dt> </dl>

 

 




