---
Description: Establishes the signer of a SignedData or SignedCode object.
ms.assetid: 380c9cf3-27a2-4354-b1c8-97cec33f4e44
title: Signer object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Signer object

\[The **Signer** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**CmsSigner Class**](https://www.bing.com/search?q=**CmsSigner+Class**) in the [**System.Security.Cryptography.Pkcs**](https://www.bing.com/search?q=**System.Security.Cryptography.Pkcs**) namespace.\]

The **Signer** object establishes the signer of a [**SignedData**](signeddata.md) or [**SignedCode**](signedcode.md) object. The [**Certificate**](certificate.md) of the **Signer** object must have an available private key that can be used to sign data.

## Members

The **Signer** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Signer** object has these methods.



| Method                      | Description                                                       |
|:----------------------------|:------------------------------------------------------------------|
| [**Load**](signer-load.md) | Loads a signing certificate from a specified PFX file.<br/> |



 

### Properties

The **Signer** object has these properties.



| Property                                                                     | Access type           | Description                                                                                                                                                                                                                                                                                                                                 |
|:-----------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AuthenticatedAttributes**](signer-authenticatedattributes.md)<br/> | Read-only<br/>  | The collection of authenticated attributes.<br/>                                                                                                                                                                                                                                                                                      |
| [**Certificate**](signer-certificate.md)<br/>                         | Read/write<br/> | The [**Certificate**](certificate.md) object that represents the certificate of a signer of the data.<br/> When the value of this property is reset, directly or indirectly, the whole [*state*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) of the object is reset.<br/> This is the default property.<br/> |
| [**Chain**](signer-chain.md)<br/>                                     | Read-only<br/>  | The chain of the signer.<br/>                                                                                                                                                                                                                                                                                                         |
| [**Options**](signer-options.md)<br/>                                 | Read/write<br/> | Sets or retrieves the signer's certificate option.<br/>                                                                                                                                                                                                                                                                               |



 

## Remarks

The **Signer** object can be created, and it is safe for scripting. The ProgID for the **Signer** object is CAPICOM.Signer.2.

**CAPICOM 1.*x*:** The ProgID for the **Signer** object is CAPICOM.Signer.1.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 




