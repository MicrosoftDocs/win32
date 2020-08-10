---
title: User Element
description: Learn about the User element. This element is not used when using legacy methods via the EAPHost APIs.
ms.assetid: d35fb4ba-5f48-431d-b2bf-738043f5d1ff
keywords:
- User element EAPHost
topic_type:
- apiref
api_name:
- User
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# User Element

The **User** element is not used when using legacy methods via the EAPHost APIs.

``` syntax
<xs:element name="User">
    <xs:complexType>
        <xs:sequence>
            <xs:element
                maxOccurs="unbounded"
                ref="Eap"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Child elements



| Element                                                  | Type | Description                                                                     |
|----------------------------------------------------------|------|---------------------------------------------------------------------------------|
| [**Eap**](baseeapuserpropertiesv1schema-eap-element.md) |      | Captures the method type and method specific credential information.<br/> |



## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eapuserpropertiesv1 Schema](eapuserpropertiesv1schema-schema.md)
</dt> </dl>

 

 





