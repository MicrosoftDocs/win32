---
description: Provides read-only access to key usage properties of a certificate.
ms.assetid: '8b8e9076-1a4f-4383-ac4b-1322d52949f0'
title: KeyUsage object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- KeyUsage
api_type:
- COM
api_location:
- Capicom.dll
---

# KeyUsage object

\[The **KeyUsage** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509enhancedkeyusageextension?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **KeyUsage** object provides read-only access to key usage properties of a certificate.

## Members

The **KeyUsage** object has these types of members:

-   [Properties](#properties)

### Properties

The **KeyUsage** object has these properties.



| Property                                                                           | Access type          | Description                                                                                                                                 |
|:-----------------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| [**IsCritical**](keyusage-iscritical.md)<br/>                               | Read-only<br/> | Retrieves a Boolean value that indicates whether the **KeyUsage** extension is marked critical.<br/>                                  |
| [**IsCRLSignEnabled**](keyusage-iscrlsignenabled.md)<br/>                   | Read-only<br/> | Retrieves a Boolean value that indicates whether the CRLSign bit is set.<br/>                                                         |
| [**IsDataEnciphermentEnabled**](keyusage-isdataenciphermentenabled.md)<br/> | Read-only<br/> | Retrieves a Boolean value that indicates whether the dataEncipherment bit is set.<br/>                                                |
| [**IsDecipherOnlyEnabled**](keyusage-isdecipheronlyenabled.md)<br/>         | Read-only<br/> | Retrieves a Boolean value that indicates whether the decipherOnly bit is set.<br/>                                                    |
| [**IsDigitalSignatureEnabled**](keyusage-isdigitalsignatureenabled.md)<br/> | Read-only<br/> | Retrieves a Boolean value that indicates whether the digitalSignature bit is set.<br/>                                                |
| [**IsEncipherOnlyEnabled**](keyusage-isencipheronlyenabled.md)<br/>         | Read-only<br/> | Retrieves a Boolean value that indicates whether the encipherOnly bit is set.<br/>                                                    |
| [**IsKeyAgreementEnabled**](keyusage-iskeyagreementenabled.md)<br/>         | Read-only<br/> | Retrieves a Boolean value that indicates whether the keyAgreement bit is set.<br/>                                                    |
| [**IsKeyCertSignEnabled**](keyusage-iskeycertsignenabled.md)<br/>           | Read-only<br/> | Retrieves a Boolean value that indicates whether the keyCertSign bit is set.<br/>                                                     |
| [**IsKeyEnciphermentEnabled**](keyusage-iskeyenciphermentenabled.md)<br/>   | Read-only<br/> | Retrieves a Boolean value that indicates whether the keyEncipherment bit is set.<br/>                                                 |
| [**IsNonRepudiationEnabled**](keyusage-isnonrepudiationenabled.md)<br/>     | Read-only<br/> | Retrieves a Boolean value that indicates whether the nonRepudiationEnabled bit is set.<br/>                                           |
| [**IsPresent**](keyusage-ispresent.md)<br/>                                 | Read-only<br/> | Retrieves a Boolean value that indicates whether the **KeyUsage** extension is present.<br/> This is the default property.<br/> |



 

## Remarks

The **KeyUsage** object cannot be created.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 
