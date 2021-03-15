---
title: EapType Element
description: Is a derived type of the EapType element from the baseeapuserpropertiesv1 schema. | EapType Element
ms.assetid: 7bd8fb5b-ceff-4d82-a979-b01229f8863a
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

The **EapType** element is a derived type of the [**EapType**](baseeapuserpropertiesv1schema-eaptype-element.md) element from the [baseeapuserpropertiesv1](baseeapuserpropertiesv1schema-schema.md) schema.

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
                    <xs:element
                        minOccurs="0"
                        ref="Username"
                     />
                    <xs:element name="Password"
                        type="string"
                        minOccurs="0"
                     />
                    <xs:element name="LogonDomain"
                        type="string"
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



| Element                                                                           | Type   | Description                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Username**](mschapv2userpropertiesv1schema-username-element.md)               |        | Identifies the user being authenticated. If this element is not present, the user name is obtained from winlogon. The [**Username**](mschapv2userpropertiesv1schema-username-element.md) element is optional.<br/>                                        |
| [**LogonDomain**](mschapv2userpropertiesv1schema-logondomain-eaptype-element.md) | string | Identifies the domain of the user or machine being authenticated. If this element is not present, the domain from winlogon is used. The [**LogonDomain**](mschapv2userpropertiesv1schema-logondomain-eaptype-element.md) element is optional.<br/>        |
| [**Password**](mschapv2userpropertiesv1schema-password-eaptype-element.md)       | string | Identifies the password of the user or machine being authenticated. If this element is not present, the password hash is obtained from winlogon. The [**Password**](mschapv2userpropertiesv1schema-password-eaptype-element.md) element is optional.<br/> |



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

[mschapv2userpropertiesv1 Schema](mschapv2userpropertiesv1schema-schema.md)
</dt> </dl>

 

 





