---
description: Specifies if this is the default profile for the device.
ms.assetid: 024ef936-ddf4-41f6-81c9-5c8a632690a0
title: IsDefault (MBNProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IsDefault
api_type: 
- Schema
---

# IsDefault (MBNProfile) Element

The **IsDefault (MBNProfile)** element specifies if this is the default profile for the device.

This is an optional element and if it is not specified then the profile will not be set as the default profile.

The default profile is used by the Mobile Broadband service for following purposes

-   The Mobile Broadband service uses connection settings from the default profile when performing automatic network connections. These settings include access point name, user name, password, etc.
-   Auto connection policy for a Mobile Broadband device is taken from it's default profile.
-   The operating system network connection UI also uses connection data from the default profile for connection operations.

Cellular service providers can provide the connection details in a profile and configure that profile as a default profile. The Mobile Broadband service will use these connection settings without prompting user for details.

``` syntax
<xs:element name="IsDefault"
    type="boolean"
 />
```

The **IsDefault** element is defined by the [**MBNProfile**](schema-mbnprofile-element.md) element.

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

 

 




