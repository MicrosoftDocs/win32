---
title: Username element (TLS)
description: Learn about the Username element. This element captures the user name to be sent in the EAP-Identity response.
ms.assetid: dda4a7dd-36ba-418d-9b26-2818ef20854d
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

# Username element (TLS)

The **Username** element captures the user name to be sent in the EAP-Identity response.

If the **Username** element is absent, then EAP-TLS uses the name in the certificate referred to in the [**UserCert**](eaptlsuserpropertiesv1schema-usercert-eaptype-element.md) element.

``` syntax
<xs:element name="Username"
    substitutionGroup="Identity"
 />
```

## Requirements



| Role | Minimum supported OS versions |
|------|-------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eaptlsuserpropertiesv1 Schema](eaptlsuserpropertiesv1schema-schema.md)
</dt> </dl>

 

 





