---
description: Identifies the name of Home provider for the given SIM/Device.
ms.assetid: 05d65091-5a1d-427a-8f51-1e1b9d189571
title: HomeProviderName (MBNProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- HomeProviderName
api_type: 
- Schema
---

# HomeProviderName (MBNProfile) Element

The **HomeProviderName (MBNProfile)** element identifies the name of Home provider for the given SIM/Device.

This element is optional and is set by the Mobile Broadband service for internal use. An application should not set this field while creating or updating a profile.

``` syntax
<xs:element name="HomeProviderName"
    type="providerNameType"
 />
```

The **HomeProviderName** element is defined by the [**MBNProfile**](schema-mbnprofile-element.md) element.

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

 

 




