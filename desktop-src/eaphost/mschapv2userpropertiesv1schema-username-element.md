---
title: Username element (CHAP)
description: Learn about the Username element, which identifies the user that's being authenticated. See a syntax example and view additional available resources.
ms.assetid: 3dd12864-5e0a-492c-a2c3-28118d21a0f2
keywords:
- Username element EAPHost
topic_type:
- apiref
api_name:
- Username
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# Username element (CHAP)

The **Username** element identifies the user being authenticated.

``` syntax
<xs:element name="Username"
    substitutionGroup="Identity"
 />
```

## Remarks

If the **Username** element is not present, the user name is obtained from winlogon. This element is optional.

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[mschapv2userpropertiesv1 Schema](mschapv2userpropertiesv1schema-schema.md)
</dt> </dl>

 

 





