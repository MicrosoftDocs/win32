---
title: BaseEapMethodUserCredentials Complex Type
description: Learn about the BaseEapMethodUserCredentials complex type. This type is a placeholder element for method credential data.
ms.assetid: ebbf813d-657a-4ff2-acf2-c18ce694b564
keywords:
- BaseEapMethodUserCredentials complex type EAPHost
topic_type:
- apiref
api_name:
- BaseEapMethodUserCredentials
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# BaseEapMethodUserCredentials Complex Type

The **BaseEapMethodUserCredentials** complex type is a placeholder element for method credential data.

``` syntax
<xs:complexType name="BaseEapMethodUserCredentials">
    <xs:sequence>
        <xs:any
            processContents="lax"
            minOccurs="0"
            maxOccurs="unbounded"
            namespace="##any"
         />
    </xs:sequence>
</xs:complexType>
```

## Remarks

The EAP method performs schema validation on the contents of **BaseEapMethodUserCredentials**.

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[baseeapmethodusercredentials Schema](baseeapmethodusercredentialsschema-schema.md)
</dt> </dl>

 

 





