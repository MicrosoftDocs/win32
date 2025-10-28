---
title: CredentialsBlob (EapHostUserCredentials) Element
description: Learn how to use the CredentialsBlob element for binary BLOB method configurations in EAPHost, including certificate authentication with SHA-1 thumbprints.
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
ms.date: 10/28/2025
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

The **CredentialsBlob** element is defined by the [EapHostUserCredentials](eaphostusercredentialsschema-eaphostusercredentials-element.md) element.

## Remarks

The [Credentials](eaphostusercredentialsschema-credentials-eaphostusercredentials-element.md) and **CredentialsBlob** elements cannot both be used simultaneously.

For certificate-based authentication, the **CredentialsBlob** should contain the SHA-1 hash (thumbprint) of the certificate, encoded as hexBinary. This 20-byte SHA-1 hash uniquely identifies the certificate and allows EAPHost to locate it in the system's certificate store. The actual certificate must already be present in the user's or computer's certificate store.

To obtain the SHA-1 thumbprint of a certificate, open the certificate in the Certificates MMC snap-in, navigate to the **Details** tab, and copy the value from the **Thumbprint** field. The hexadecimal string should be formatted without spaces when used in the binary blob.

For more information about certificate credentials, see [EapCertificateCredential](/windows/win32/api/eaptypes/ns-eaptypes-eapcertificatecredential).

## Requirements

| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |

## Related content

**Definition context of element in schema**

[EapHostUserCredentials](eaphostusercredentialsschema-eaphostusercredentials-element.md)

**Possible immediate parent element in schema instance**

[EapHostUserCredentials](eaphostusercredentialsschema-eaphostusercredentials-element.md)

[EAPHost and Legacy Schema](eaphost-schemas.md)

[eaphostusercredentials Schema](eaphostusercredentialsschema-schema.md)
