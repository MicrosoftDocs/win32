---
description: The following properties are defined by the ICertSrvSetupKeyInformation interface.
ms.assetid: d805a011-8728-4687-8e4a-ad331617abe7
title: Properties of ICertSrvSetupKeyInformation
ms.topic: article
ms.date: 05/31/2018
---

# Properties of ICertSrvSetupKeyInformation

The following properties are defined by the [**ICertSrvSetupKeyInformation**](/windows/desktop/api/Casetup/nn-casetup-icertsrvsetupkeyinformation) interface.



| Property                                                                           | Description                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ContainerName**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_containername)                 | Gets or sets the name used by the [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) to generate, store, or access the key.                                                                       |
| [**Existing**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_existing)                           | Gets or sets a value that indicates whether the private key already exists.                                                                                                                                                                                                                       |
| [**ExistingCACertificate**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_existingcacertificate) | Gets or sets the binary value that has been encoded by using [*Distinguished Encoding Rules*](../secgloss/d-gly.md) (DER) and that is the binary value of the CA certificate that corresponds to an existing key. |
| [**HashAlgorithm**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_hashalgorithm)                 | Gets or sets the name of the hash algorithm used to sign or verify the CA certificate for the key.                                                                                                                                                                                                |
| [**Length**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_length)                               | Gets or sets the strength of the key to one of the values supported by the CSP.                                                                                                                                                                                                                   |
| [**ProviderName**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_providername)                   | Gets or sets the name of the CSP that is used to generate or store the private key.                                                                                                                                                                                                               |



 

 

 
