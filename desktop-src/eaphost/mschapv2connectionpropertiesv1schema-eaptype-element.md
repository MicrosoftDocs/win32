---
title: EapType Element (v2)
description: Is a derived type of the EapType element from the baseeapconnectionpropertiesv1 schema. This is the top element that appears inside the Config element of the EapHostConfig schema.
ms.assetid: dbd63387-f8ed-4308-903f-7a555f3410f7
keywords:
- EapType element EAPHost
topic_type:
- apiref
api_name:
- EapType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# EapType Element

The **EapType** element is a derived type of the [EapType](baseeapconnectionpropertiesv1schema-eaptype-element.md) element from the [baseeapconnectionpropertiesv1](baseeapconnectionpropertiesv1schema-schema.md) schema. This is the top element that appears inside the Config element of the [EapHostConfig](eaphostconfigschema-elements.md) schema

``` syntax
<xs:element name="EapType"
    substitutionGroup="EapType"
>
    <xs:complexType>
        <xs:complexContent>
            <xs:extension
                base="BaseEapTypeParameters"
            >
                <xs:sequence>
                    <xs:element name="UseWinLogonCredentials"
                        type="boolean"
                        default="true"
                        minOccurs="0"
                     />
                    <xs:any
                        processContents="lax"
                        minOccurs="0"
                        maxOccurs="unbounded"
                        namespace="##other"
                     />
                </xs:sequence>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
</xs:element>
```

## Child elements



| Element                                                                                                       | Type    | Description                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UseWinLogonCredentials**](mschapv2connectionpropertiesv1schema-usewinlogoncredentials-eaptype-element.md) | boolean | Controls use of the winlogin credentials. If TRUE, then EAP MS-CHAPv2 obtains credentials from winlogon. If FALSE, then EAP MS-CHAPv2 obtains credentials from the user. <br/> The [**UseWinLogonCredentials (EapType)**](mschapv2connectionpropertiesv1schema-usewinlogoncredentials-eaptype-element.md) element is optional.<br/> |



## Remarks

The **processContents** element enables future enhancements to the schema. The **processContents** element is optional.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[mschapv2connectionpropertiesv1 Schema](mschapv2connectionpropertiesv1schema-schema.md)
</dt> </dl>

 

 





