---
Description: The following properties are defined by the ICertSrvSetupKeyInformation interface.
ms.assetid: d805a011-8728-4687-8e4a-ad331617abe7
title: Properties of ICertSrvSetupKeyInformation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Properties of ICertSrvSetupKeyInformation

The following properties are defined by the [**ICertSrvSetupKeyInformation**](/windows/win32/Casetup/nn-casetup-icertsrvsetupkeyinformation?branch=master) interface.



| Property                                                                           | Description                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ContainerName**](/windows/win32/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_containername?branch=master)                 | Gets or sets the name used by the [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) to generate, store, or access the key.                                                                       |
| [**Existing**](/windows/win32/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_existing?branch=master)                           | Gets or sets a value that indicates whether the private key already exists.                                                                                                                                                                                                                       |
| [**ExistingCACertificate**](/windows/win32/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_existingcacertificate?branch=master) | Gets or sets the binary value that has been encoded by using [*Distinguished Encoding Rules*](security.d_gly#-security-distinguished-encoding-rules-gly) (DER) and that is the binary value of the CA certificate that corresponds to an existing key. |
| [**HashAlgorithm**](/windows/win32/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_hashalgorithm?branch=master)                 | Gets or sets the name of the hash algorithm used to sign or verify the CA certificate for the key.                                                                                                                                                                                                |
| [**Length**](/windows/win32/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_length?branch=master)                               | Gets or sets the strength of the key to one of the values supported by the CSP.                                                                                                                                                                                                                   |
| [**ProviderName**](/windows/win32/Casetup/nf-casetup-icertsrvsetupkeyinformation-get_providername?branch=master)                   | Gets or sets the name of the CSP that is used to generate or store the private key.                                                                                                                                                                                                               |



 

 

 



