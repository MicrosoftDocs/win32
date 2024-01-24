---
title: ServerValidationParameters complex type (PEAP)
description: Learn about the ServerValidationParameters complex type. This type contains information about how to perform server validation. | ServerValidationParameters complex type (PEAP)
ms.assetid: 65b3199c-9462-447b-b560-0713348f9130
keywords:
- ServerValidationParameters complex type EAPHost
topic_type:
- apiref
api_name:
- ServerValidationParameters
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# ServerValidationParameters complex type (PEAP)

The **ServerValidationParameters** complex type contains information about how to perform server validation.

``` syntax
<xs:complexType name="ServerValidationParameters">
    <xs:sequence>
        <xs:element name="DisableUserPromptForServerValidation"
            type="boolean"
            minOccurs="0"
         />
        <xs:element name="ServerNames"
            type="complextype"
            minOccurs="0"
         />
        <xs:element name="TrustedRootCA"
            type="hexBinary"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
    <xs:attribute name="PerformServerValidation"
        type="boolean"
     />
</xs:complexType>
```

## Child elements



| Element                                                                                                                                                    | Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DisableUserPromptForServerValidation**](mspeapconnectionpropertiesv1schema-disableuserpromptforservervalidation-servervalidationparameters-element.md) | boolean     | Indicates whether the user should be asked for server validation. <br/> If [**DisableUserPromptForServerValidation**](mspeapconnectionpropertiesv1schema-disableuserpromptforservervalidation-servervalidationparameters-element.md) is TRUE, then PEAP performs the server validation without user input; if the validation fails, PEAP fails the authentication.<br/> If [**DisableUserPromptForServerValidation**](mspeapconnectionpropertiesv1schema-disableuserpromptforservervalidation-servervalidationparameters-element.md) is FALSE, the user is prompted for a validated server certificate or name, or root certification authority (CA).<br/> The [**DisableUserPromptForServerValidation**](mspeapconnectionpropertiesv1schema-disableuserpromptforservervalidation-servervalidationparameters-element.md) element is optional.<br/> |
| [**ServerNames**](mspeapconnectionpropertiesv1schema-servernames-servervalidationparameters-element.md)                                                   | complextype | Represents a list of servers the client trusts. Each server name is delimited by semicolons, and can be represented by regular expressions. <br/> The [**ServerNames**](mspeapconnectionpropertiesv1schema-servernames-servervalidationparameters-element.md) element is optional.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**TrustedRootCA**](mspeapconnectionpropertiesv1schema-trustedrootca-servervalidationparameters-element.md)                                               | hexBinary   | Captures the thumb print of root certificate authorities (CAs) that are trusted by the client. <br/> The thumb print is a hexadecimal string that contains the SHA-1 hash of the certificate<br/> The [**TrustedRootCA**](mspeapconnectionpropertiesv1schema-trustedrootca-servervalidationparameters-element.md) element is optional.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |



## Attributes



| Name                    | Type    | Description                                                                                                                                                                                                                  |
|-------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PerformServerValidation | boolean | Windows 7 or later: Indicates whether server validation is performed. The [**PerformServerValidation**](mspeapconnectionpropertiesv2-performservervalidation-peapextensionstype-element.md) element is optional.<br/> |



## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[mspeapconnectionpropertiesv1 Schema](mspeapconnectionpropertiesv1schema-schema.md)
</dt> <dt>

[mspeapconnectionpropertiesv1 Schema Complex Types](mspeapconnectionpropertiesv1schema-complex-types.md)
</dt> <dt>

[**AcceptServerName**](mspeapconnectionpropertiesv1schema-acceptservername-peapextensionstype-element.md)
</dt> </dl>

 

 





