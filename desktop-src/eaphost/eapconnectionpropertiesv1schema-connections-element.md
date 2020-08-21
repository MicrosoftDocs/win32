---
title: Connections Element
description: Learn about the Connections element. This element collects and contains zero or more Connection elements.
ms.assetid: 2c199338-892f-4d8c-bf33-4a19f362de3e
keywords:
- Connections element EAPHost
topic_type:
- apiref
api_name:
- Connections
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# Connections Element

The **Connections** element collects and contains zero or more [**Connection**](eapconnectionpropertiesv1schema-connection-connections-element.md) elements.

``` syntax
<xs:element name="Connections">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="Connection"
                minOccurs="0"
                maxOccurs="unbounded"
            >
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
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Child elements



| Element                                                                              | Type   | Description                                                                                                                                                                                |
|--------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Eap**](baseeapconnectionpropertiesv1schema-eap-element.md)                       |        | Identifies the EAP configuration element.<br/>                                                                                                                                       |
| [**Connection**](eapconnectionpropertiesv1schema-connection-connections-element.md) |        | Defines each configuration setting and associates it with a name. The [**Connection**](eapconnectionpropertiesv1schema-connection-connections-element.md) element is optional.<br/> |
| [**Name**](eapconnectionpropertiesv1schema-name-connection-element.md)              | string | Captures the name of the connection being defined, assisting in the identification of multiple connections.<br/>                                                                     |



## Remarks

The **Connections** element is not used with legacy methods via the EAPHost APIs.

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eapconnectionpropertiesv1 Schema](eapconnectionpropertiesv1schema-schema.md)
</dt> </dl>

 

 





