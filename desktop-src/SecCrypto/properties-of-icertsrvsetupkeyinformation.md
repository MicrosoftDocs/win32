---
Description: 'The following properties are defined by the ICertSrvSetupKeyInformation interface.'
ms.assetid: 'd805a011-8728-4687-8e4a-ad331617abe7'
title: Properties of ICertSrvSetupKeyInformation
---

# Properties of ICertSrvSetupKeyInformation

The following properties are defined by the [**ICertSrvSetupKeyInformation**](icertsrvsetupkeyinformation.md) interface.



| Property                                                                           | Description                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ContainerName**](icertsrvsetupkeyinformation-containername.md)                 | Gets or sets the name used by the [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) to generate, store, or access the key.                                                                       |
| [**Existing**](icertsrvsetupkeyinformation-existing.md)                           | Gets or sets a value that indicates whether the private key already exists.                                                                                                                                                                                                                       |
| [**ExistingCACertificate**](icertsrvsetupkeyinformation-existingcacertificate.md) | Gets or sets the binary value that has been encoded by using [*Distinguished Encoding Rules*](security.d_gly#-security-distinguished-encoding-rules-gly) (DER) and that is the binary value of the CA certificate that corresponds to an existing key. |
| [**HashAlgorithm**](icertsrvsetupkeyinformation-hashalgorithm.md)                 | Gets or sets the name of the hash algorithm used to sign or verify the CA certificate for the key.                                                                                                                                                                                                |
| [**Length**](icertsrvsetupkeyinformation-length.md)                               | Gets or sets the strength of the key to one of the values supported by the CSP.                                                                                                                                                                                                                   |
| [**ProviderName**](icertsrvsetupkeyinformation-providername.md)                   | Gets or sets the name of the CSP that is used to generate or store the private key.                                                                                                                                                                                                               |



 

 

 



