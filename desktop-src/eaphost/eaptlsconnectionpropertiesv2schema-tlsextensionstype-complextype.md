---
title: TLSExtensionsType Complex Type
description: Learn about the TLSExtensionsType complex type. This type enables future enhancements to the schema.
ms.assetid: 5e4f8ef8-1adb-4683-8001-ba7d2d392523
ms.topic: article
ms.date: 05/31/2018
---

# TLSExtensionsType Complex Type

The **TLSExtensionsType** complex type enables future enhancements to the schema.


```XML
<xs:complexType name="TLSExtensionsType">
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

The **TLSExtensionsType** element is optional.

## Related topics

<dl> <dt>


</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eaptlsconnectionpropertiesv2](eaptlsconnectionpropertiesv2schema-schema.md)
</dt> <dt>

[eaptlsconnectionpropertiesv2 Complex Types](eaptlsconnectionpropertiesv2schema-complex-types.md)
</dt> <dt>

[**TLSExtensions (TLSExtensionsType)**](eaptlsconnectionpropertiesv2schema-performservervalidation-eaptype-element.md)
</dt> </dl>

 

 




