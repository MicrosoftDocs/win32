---
description: Represents the certificate extension template of the certificate.
ms.assetid: '1ae9220a-f6b3-47c5-bd08-a36ffd84e1f9'
title: Template object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Template
api_type:
- COM
api_location:
- Capicom.dll
---

# Template object

\[The **Template** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509extension?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Template to retrieve the certificate extension template.\]

The **Template** object represents the certificate extension template of the certificate.

## When to use

The **Template** object is used to perform the following tasks:

-   Determine whether the template is marked critical or present.
-   Retrieve the [*object identifier*](../secgloss/o-gly.md) (OID) or name of the template.
-   Retrieve the minor or major version of the template.

## Members

The **Template** object has these types of members:

-   [Properties](#properties)

### Properties

The **Template** object has these properties.



| Property                                                 | Access type          | Description                                                                                            |
|:---------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------|
| [**IsCritical**](template-iscritical.md)<br/>     | Read-only<br/> | Retrieves a Boolean value that indicates whether the template extension is marked critical.<br/> |
| [**IsPresent**](template-ispresent.md)<br/>       | Read-only<br/> | Retrieves a Boolean value that indicates whether the template extension is present.<br/>         |
| [**MajorVersion**](template-majorversion.md)<br/> | Read-only<br/> | Retrieves the major version number of the template.<br/>                                         |
| [**MinorVersion**](template-minorversion.md)<br/> | Read-only<br/> | Retrieves the minor version number of the template.<br/>                                         |
| [**Name**](template-name.md)<br/>                 | Read-only<br/> | Retrieves a string that contains the name of the template.<br/>                                  |
| [**OID**](template-oid.md)<br/>                   | Read-only<br/> | Retrieves an [**OID**](oid.md) object that identifies the **Template** object.<br/>             |



 

## Remarks

The **Template** object cannot be created.

A **Template** object is returned by the [**Certificate.Template**](certificate-template.md) method.

CAPICOM uses two different versions of certificate templates. The following table shows the name and OID for each certificate template version.



| Version | Name                               | OID                    |
|---------|------------------------------------|------------------------|
| V1      | szOID\_ENROLL\_CERTTYPE\_EXTENSION | "1.3.6.1.4.1.311.20.2" |
| V2      | szOID\_CERTIFICATE\_TEMPLATE       | "1.3.6.1.4.1.311.21.7" |



 

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
