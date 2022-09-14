---
title: FastReconnect (EapType) Element
description: Learn about the FastReconnect (EapType) element. This element indicates whether to perform a fast reconnect.
ms.assetid: 075285b0-7b1b-4d3c-af27-a718f3c20394
keywords:
- FastReconnect element EAPHost
topic_type:
- apiref
api_name:
- FastReconnect
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# FastReconnect (EapType) Element

The **FastReconnect (EapType)** element indicates whether to perform a fast reconnect.

``` syntax
<xs:element name="FastReconnect"
    type="boolean"
 />
```

The **FastReconnect** element is defined by the [**EapType**](mspeapconnectionpropertiesv1schema-eaptype-element.md) element.

## Remarks

If the **FastReconnect** element is TRUE, then PEAP attempts to perform a fast reconnect; if FALSE, PEAP performs the full authentication. The **FastReconnect** element is optional.

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

 

 





