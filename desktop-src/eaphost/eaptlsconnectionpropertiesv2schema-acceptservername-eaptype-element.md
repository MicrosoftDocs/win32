---
title: AcceptServerName element
description: Indicates whether the server name is validated against the name string specified in the ServerNames (ServerValidationParameters) element. | AcceptServerName element
ms.assetid: 307b2d2a-1678-4aa9-82ed-46d401cf0e0f
keywords:
- AcceptServerName element EAPHost
topic_type:
- apiref
api_name:
- AcceptServerName
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# AcceptServerName element

The **AcceptServerName (EapType)** element indicates whether the server name is validated against the name string specified in the [ServerNames (ServerValidationParameters)](eaptlsconnectionpropertiesv1schema-servernames-servervalidationparameters-element.md) element.

``` xml
<xs:element name="AcceptServerName"
    type="xs:boolean"
 />
```

The **AcceptServerName** element is defined by the [EapType](eaptlsconnectionpropertiesv1schema-eaptype-element.md) element.

## Remarks

The **AcceptServerName** element is optional.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client | Windows 7 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 R2 \[desktop apps only\] |

## See also

### Definition context of element in schema

- [EapType](eaptlsconnectionpropertiesv1schema-eaptype-element.md)

### Possible immediate parent element in schema instance

- [EapType](eaptlsconnectionpropertiesv1schema-eaptype-element.md)

### Related links

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv2](eaptlsconnectionpropertiesv2schema-schema.md)
- [eaptlsconnectionpropertiesv2 Schema Elements](eaptlsconnectionpropertiesv2schema-elements.md)
- [AcceptServerName (EapType)](eaptlsconnectionpropertiesv1schema-tlsextensionstype-peapextensionstype-element.md)
