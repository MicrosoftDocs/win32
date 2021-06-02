---
description: Provides functionality for signing executable files with an Authenticode digital signature.
ms.assetid: e6d4e694-471f-4d30-983c-6bc5d631d99e
title: SignedCode object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SignedCode
api_type: 
- COM
api_location: 
- Capicom.dll
---

# SignedCode object

\[The **SignedCode** object is available for use in the operating systems specified in the Requirements section. Instead, use Platform Invocation Services (PInvoke) to call the Win32 API [**SignerSignEx**](signersignex.md), [**SignerTimeStampEx**](signertimestampex.md), and [**WinVerifyTrust**](/windows/desktop/api/Wintrust/nf-wintrust-winverifytrust) functions to sign content with an Authenticode digital signature. For information about PInvoke, see [Platform Invoke Tutorial](https://msdn.microsoft.com/library/aa288468.aspx). The [.NET and CryptoAPI via P/Invoke: Part 1](/previous-versions/ms867087(v=msdn.10)#netcryptoapi_topic5) and [.NET and CryptoAPI via P/Invoke: Part 2](/previous-versions/ms867087(v=msdn.10)#netcryptoapi_topic6) subsections of [Extending .NET Cryptography with CAPICOM and P/Invoke](/previous-versions/ms867087(v=msdn.10)) may also be helpful.\]

The **SignedCode** object provides functionality for signing executable files with an Authenticode digital signature.

## When to use

The **SignedCode** object is used to perform the following tasks:

-   Sign executable files.
-   Time stamp executable files.
-   Determine whether the signature of the executable file is valid.
-   Set or retrieve the path to the executable file.
-   Retrieve the signer and time stamper of the executable file.
-   Retrieve a collection of the certificates for the executable file.
-   Retrieve a description or the URL to the description of the executable file.

## Members

The **SignedCode** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SignedCode** object has these methods.



| Method                                    | Description                                                                                                                                                         |
|:------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Sign**](signedcode-sign.md)           | Creates an Authenticode digital signature and signs the executable file specified in the [**SignedCode.FileName**](signedcode-filename.md) property.<br/>    |
| [**Timestamp**](signedcode-timestamp.md) | Creates an Authenticode time stamp signature on the signed executable file specified in the [**SignedCode.FileName**](signedcode-filename.md) property.<br/> |
| [**Verify**](signedcode-verify.md)       | Verifies the Authenticode signature on the signed executable file specified in the [**SignedCode.FileName**](signedcode-filename.md) property.<br/>          |



 

### Properties

The **SignedCode** object has these properties.



| Property                                                       | Access type           | Description                                                                                                                                |
|:---------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**Certificates**](signedcode-certificates.md)<br/>     | Read-only<br/>  | A [**Certificates**](certificates.md) collection that contains all the certificates in the signed executable file.<br/>             |
| [**Description**](signedcode-description.md)<br/>       | Read/write<br/> | A string that contains a description of the signed executable file.<br/>                                                             |
| [**DescriptionURL**](signedcode-descriptionurl.md)<br/> | Read/write<br/> | A string that contains the HTTP address to a description of the signed executable file.<br/>                                         |
| [**FileName**](signedcode-filename.md)<br/>             | Read/write<br/> | A string that contains the path to the content file that contains the executable file.<br/> This is the default property.<br/> |
| [**Signer**](signedcode-signer.md)<br/>                 | Read-only<br/>  | A [**Signer**](signer.md) object that provides access to the signer of the executable file.<br/>                                    |
| [**Timestamper**](signedcode-timestamper.md)<br/>       | Read-only<br/>  | A [**Signer**](signer.md) object that provides access to the time stamper of the executable file.<br/>                              |



 

## Remarks

The **SignedCode** object can be created, and is not safe for scripting. The ProgID for the **SignedCode** object is CAPICOM.SignedCode.1.

The executable file should be of a type that can be signed with Authenticode technology, for example, files that have a file name extension of .cab, .cat, .exe, .dll, .vbs, or .ocx.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
