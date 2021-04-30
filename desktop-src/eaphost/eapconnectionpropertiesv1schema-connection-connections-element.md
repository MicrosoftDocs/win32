---
title: Connection (Connections) Element
description: Defines each configuration setting and associates it with a name. The Connection element is optional.
ms.assetid: 913263ab-0e0e-4213-947b-7bca9ba0697e
keywords:
- Connection element EAPHost
topic_type:
- apiref
api_name:
- Connection
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# Connection (Connections) Element

The **Connection (Connections)** element defines each configuration setting and associates it with a name. The **Connection** element is optional.

``` syntax
<xs:element name="Connection">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="Name"
                type="string"
             />
            <xs:element
                maxOccurs="unbounded"
                ref="Eap"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The **Connection** element is defined by the [**Connections**](eapconnectionpropertiesv1schema-connections-element.md) element.

## Child elements



| Element                                                                 | Type   | Description                                                                                                             |
|-------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------|
| [**Eap**](baseeapconnectionpropertiesv1schema-eap-element.md)          |        | Identifies the EAP configuration element.<br/>                                                                    |
| [**Name**](eapconnectionpropertiesv1schema-name-connection-element.md) | string | Captures the name of the connection being defined, assisting in the identification of multiple connections. <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**Connections**](eapconnectionpropertiesv1schema-connections-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**Connections**](eapconnectionpropertiesv1schema-connections-element.md)
</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eapconnectionpropertiesv1 Schema](eapconnectionpropertiesv1schema-schema.md)
</dt> </dl>

 

 





