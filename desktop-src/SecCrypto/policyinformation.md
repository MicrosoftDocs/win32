---
Description: Provides access to the policy information of an extension.
ms.assetid: 03d627b3-2d44-4637-97a4-85cdcaf3e4d3
title: PolicyInformation object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PolicyInformation object

\[The **PolicyInformation** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](T:System.Security.Cryptography.X509Certificates.X509Extension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to process policy information in the Certificate policies extension.\]

The **PolicyInformation** object provides access to the policy information of an extension.

## When to use

The **PolicyInformation** object is used to perform the following tasks:

-   Retrieve the policy OID.
-   Retrieve a collection of the policy's qualifiers.

## Members

The **PolicyInformation** object has these types of members:

-   [Properties](#properties)

### Properties

The **PolicyInformation** object has these properties.



| Property                                                      | Description                                                                                                 |
|:--------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**OID**](policyinformation-oid.md)<br/>               | Retrieves the policy's OID, as an [**OID**](oid.md) object. This is the default property.<br/>       |
| [**Qualifiers**](policyinformation-qualifiers.md)<br/> | Retrieves a collection of the policy's qualifiers, as a [**Qualifiers**](qualifiers.md) object.<br/> |



 

## Remarks

The **PolicyInformation** object cannot be created.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




