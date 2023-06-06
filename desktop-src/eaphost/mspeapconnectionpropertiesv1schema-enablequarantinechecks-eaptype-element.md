---
title: EnableQuarantineChecks (EapType) Element
description: Learn about the EnableQuarantineChecks (EapType) element. This element indicates whether to perform Network Access Protection (NAP) checks.
ms.assetid: bd5c7efc-f857-4e21-9cd8-0a1cbe5a87d8
keywords:
- EnableQuarantineChecks element EAPHost
topic_type:
- apiref
api_name:
- EnableQuarantineChecks
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# EnableQuarantineChecks (EapType) Element

> [!Note]  
> Starting with Windows 10/Windows Server 2016, the **EnableQuarantineChecks** element can be included in the profile but will do nothing, as the **Network Access Protection (NAP)** platform is not available.

The **EnableQuarantineChecks (EapType)** element indicates whether to perform Network Access Protection (NAP) checks.

``` syntax
<xs:element name="EnableQuarantineChecks"
    type="boolean"
 />
```

The **EnableQuarantineChecks** element is defined by the [**EapType**](mspeapconnectionpropertiesv1schema-eaptype-element.md) element.

## Remarks

If the **EnableQuarantineChecks** element is TRUE, then PEAP will perform NAP checks; if FALSE, PEAP will not perform NAP checks. The **EnableQuarantineChecks** element is optional.

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**EapType**](mspeapconnectionpropertiesv1schema-eaptype-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**EapType**](mspeapconnectionpropertiesv1schema-eaptype-element.md)
</dt> <dt>


</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[mspeapconnectionpropertiesv1 Schema](mspeapconnectionpropertiesv1schema-schema.md)
</dt> <dt>

[mspeapconnectionpropertiesv1 Schema Elements](mspeapconnectionpropertiesv1schema-elements.md)
</dt> </dl>

 

 





