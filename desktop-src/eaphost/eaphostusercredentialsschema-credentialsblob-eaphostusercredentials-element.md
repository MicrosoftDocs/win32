---
title: CredentialsBlob (EapHostUserCredentials) Element
description: Is used when the method configuration is a binary BLOB instead of in XML text format.
ms.assetid: 9d03374b-74f6-428e-8d3e-f8dccf51884e
keywords:
- CredentialsBlob element EAPHost
topic_type:
- apiref
api_name:
- CredentialsBlob
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# CredentialsBlob (EapHostUserCredentials) Element

The **CredentialsBlob (EapHostUserCredentials)** element is used when the method configuration is a binary BLOB instead of in XML text format.

``` syntax
<xs:element name="CredentialsBlob"
    type="hexBinary"
 />
```

The **CredentialsBlob** element is defined by the [**EapHostUserCredentials**](eaphostusercredentialsschema-eaphostusercredentials-element.md) element.

## Remarks

The [**Credentials**](eaphostusercredentialsschema-credentials-eaphostusercredentials-element.md) and **CredentialsBlob** elements cannot both be used simultaneously.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**EapHostUserCredentials**](eaphostusercredentialsschema-eaphostusercredentials-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**EapHostUserCredentials**](eaphostusercredentialsschema-eaphostusercredentials-element.md)
</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eaphostusercredentials Schema](eaphostusercredentialsschema-schema.md)
</dt> </dl>

 

 





