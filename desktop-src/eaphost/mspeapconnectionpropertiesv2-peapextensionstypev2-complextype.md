---
title: PeapExtensionsTypeV2 Complex Type
description: Learn about the PeapExtensionsTypeV2 complex type. This type enables future enhancements to the schema.
ms.assetid: cb011182-afec-4813-bd56-add894c74c9c
ms.topic: article
ms.date: 05/31/2018
---

# PeapExtensionsTypeV2 Complex Type

The **PeapExtensionsTypeV2** complex type enables future enhancements to the schema.


```XML
<xs:complexType name="PeapExtensionsTypeV2">
    <xs:sequence>
        <xs:any processContents="lax" 
            minOccurs="0" 
            maxOccurs="unbounded" 
            namespace="##other"
        />
    <xs:sequence>
</xs:complexType>

```



## Remarks

The **PeapExtensionsTypeV2** element is optional.

## Related topics

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[mspeapconnectionpropertiesv2 Schema](mspeapconnectionpropertiesv2schema-schema.md)
</dt> <dt>

[mspeapconnectionpropertiesv2 Complex Types](mspeapconnectionpropertiesv2schema-complex-types.md)
</dt> <dt>

[**PeapExtensionsType**](mspeapconnectionpropertiesv1schema-peapextensionstype-complextype.md)
</dt> </dl>

 

 




