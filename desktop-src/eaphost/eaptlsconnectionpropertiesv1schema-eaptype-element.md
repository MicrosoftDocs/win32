---
title: EapType Element
description: Is a derived type of the EapType element from the BaseEapConnectionProperties schema. | EapType Element
ms.assetid: cf92d500-f815-48e2-a7d5-1364cb13a1f0
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

The **EapType** element is a derived type of the [**EapType**](baseeapconnectionpropertiesv1schema-eaptype-element.md) element from the [BaseEapConnectionProperties](baseeapconnectionpropertiesv1schema-schema.md) schema.

This derived **EapType** element contains the following elements: [**CredentialsSource**](eaptlsconnectionpropertiesv1schema-credentialssource-eaptype-element.md), [**ServerValidation**](eaptlsconnectionpropertiesv1schema-servervalidation-eaptype-element.md), [**DifferentUsername**](eaptlsconnectionpropertiesv1schema-differentusername-eaptype-element.md), [**PerformServerValidation**](eaptlsconnectionpropertiesv1schema-performservervalidation-peapextensionstype-element.md), [**AcceptServerName**](eaptlsconnectionpropertiesv1schema-tlsextensionstype-peapextensionstype-element.md), and[**TLSExtensions**](eaptlsconnectionpropertiesv1schema-acceptservername-peapextensionstype-element.md).

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
                    <xs:element name="CredentialsSource"
                        type="CredentialsSourceParameters"
                        minOccurs="0"
                     />
                    <xs:element name="ServerValidation"
                        type="ServerValidationParameters"
                        minOccurs="0"
                     />
                    <xs:element name="DifferentUsername"
                        type="boolean"
                        minOccurs="0"
                     />
                    <xs:element
                        minOccurs="0"
                        maxOccurs="1"
                        ref="extendedTLS: PerformServerValidation"
                     />
                    <xs:element
                        minOccurs="0"
                        maxOccurs="1"
                        ref="extendedTLS: AcceptServerName"
                     />
                    <xs:element
                        minOccurs="0"
                        maxOccurs="1"
                        ref="extendedTLS: TLSExtensions"
                     />
                </xs:sequence>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
</xs:element>
```

## Child elements



| Element                                                                                                                               | Type                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**extendedTLS: PerformServerValidation**](eaptlsconnectionpropertiesv1schema-performservervalidation-peapextensionstype-element.md) |                                                                                                                   | Windows 7 and later: indicates whether server validation is performed.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**extendedTLS: AcceptServerName**](eaptlsconnectionpropertiesv1schema-tlsextensionstype-peapextensionstype-element.md)              |                                                                                                                   | Windows 7 and later: indicates whether the name of a server is read.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**extendedTLS: TLSExtensions**](eaptlsconnectionpropertiesv1schema-acceptservername-peapextensionstype-element.md)                  |                                                                                                                   | Windows 7 and later: enables future enhancements to the schema.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**CredentialsSource**](eaptlsconnectionpropertiesv1schema-credentialssource-eaptype-element.md)                                     | [**CredentialsSourceParameters**](eaptlsconnectionpropertiesv1schema-credentialssourceparameters-complextype.md) | Contains information about the location of the EAP Transport Level Security (EAP-TLS) certificate. <br/> The [**CredentialsSource**](eaptlsconnectionpropertiesv1schema-credentialssource-eaptype-element.md) element is optional.<br/>                                                                                                                                                                                                                                                                                                                                                                     |
| [**DifferentUsername**](eaptlsconnectionpropertiesv1schema-differentusername-eaptype-element.md)                                     | boolean                                                                                                           | Determines which user name EAP-TLS is to use. <br/> If the [**DifferentUsername**](eaptlsconnectionpropertiesv1schema-differentusername-eaptype-element.md) element is **TRUE**, EAP-TLS should use a user name other than the name that appears on the certificate. If the [**DifferentUsername**](eaptlsconnectionpropertiesv1schema-differentusername-eaptype-element.md) element is **FALSE**, EAP-TLS uses the user name that appears on the certificate.<br/> The [**DifferentUsername**](eaptlsconnectionpropertiesv1schema-differentusername-eaptype-element.md) element is optional. <br/> |
| [**ServerValidation**](eaptlsconnectionpropertiesv1schema-servervalidation-eaptype-element.md)                                       | [**ServerValidationParameters**](eaptlsconnectionpropertiesv1schema-servervalidationparameters-complextype.md)   | Contains information about how to perform server validation. The [**ServerValidation**](eaptlsconnectionpropertiesv1schema-servervalidation-eaptype-element.md) element is optional. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                        |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema](eaptlsconnectionpropertiesv1schema-schema.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema Elements](eaptlsconnectionpropertiesv1schema-elements.md)
</dt> </dl>

 

 





