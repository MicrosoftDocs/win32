---
description: Represents the basic constraints extension of a certificate.
ms.assetid: c21794f6-7654-4140-8114-0edb398d6de8
title: BasicConstraints object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BasicConstraints
api_type: 
- COM
api_location: 
- Capicom.dll
---

# BasicConstraints object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**X509BasicConstraintsExtension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509basicconstraintsextension?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/previous-versions/windows/) namespace.\]

The **BasicConstraints** object represents the basic constraints extension of a certificate.

## When to use

The **BasicConstraints** object is used to perform the following tasks:

-   Determine whether the basic constraints extension is present.
-   Determine whether the basic constraints extension is marked critical.
-   Determine whether the certificate is constrained to certificate authorities.
-   Determine whether the path length constraint is present and retrieve the path length constraint value.

## Members

The **BasicConstraints** object has these types of members:

-   [Properties](#properties)

### Properties

The **BasicConstraints** object has these properties.



| Property                                                                                     | Access type          | Description                                                                                                                                                                                                        |
|:---------------------------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IsCertificateAuthority**](basicconstraints-iscertificateauthority.md)<br/>         | Read-only<br/> | Retrieves a Boolean value that indicates whether the certificate is for a [*certification authority*](../secgloss/c-gly.md) (CA).<br/> |
| [**IsCritical**](basicconstraints-iscritical.md)<br/>                                 | Read-only<br/> | Retrieves a Boolean value that indicates whether the basic constraint extension is marked critical.<br/>                                                                                                     |
| [**IsPathLenConstraintPresent**](basicconstraints-ispathlenconstraintpresent.md)<br/> | Read-only<br/> | Retrieves a Boolean value that indicates whether the certificate's path length constraint is present.<br/>                                                                                                   |
| [**IsPresent**](basicconstraints-ispresent.md)<br/>                                   | Read-only<br/> | Retrieves a Boolean value that indicates whether the basic constraints extension is present. This is the default property.<br/>                                                                              |
| [**PathLenConstraint**](basicconstraints-pathlenconstraint.md)<br/>                   | Read-only<br/> | Retrieves the value of the path length constraint.<br/>                                                                                                                                                      |



 

## Remarks

The **BasicConstraints** object cannot be created.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[Cryptography Objects](cryptography-objects.md)
</dt> </dl>

 

 
