---
description: Creates an Authenticode digital signature and signs the executable file specified in the SignedCode.FileName property.
ms.assetid: db17be29-35ec-4468-b5cc-5ba64c4cf3fb
title: SignedCode.Sign method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SignedCode.Sign
api_type: 
- COM
api_location: 
- Capicom.dll
---

# SignedCode.Sign method

\[The **Sign** method is available for use in the operating systems specified in the Requirements section. Instead, use Platform Invocation Services (PInvoke) to call the Win32 API [**SignerSignEx**](signersignex.md), [**SignerTimeStampEx**](signertimestampex.md), and [**WinVerifyTrust**](/windows/desktop/api/Wintrust/nf-wintrust-winverifytrust) functions to sign content with an Authenticode digital signature. For information about PInvoke, see [Platform Invoke Tutorial](https://msdn.microsoft.com/library/aa288468.aspx). The [.NET and CryptoAPI via P/Invoke: Part 1](/previous-versions/ms867087(v=msdn.10)#netcryptoapi_topic5) and [.NET and CryptoAPI via P/Invoke: Part 2](/previous-versions/ms867087(v=msdn.10)#netcryptoapi_topic6) subsections of [Extending .NET Cryptography with CAPICOM and P/Invoke](/previous-versions/ms867087(v=msdn.10)) may also be helpful.\]

The **Sign** method creates an Authenticode digital signature and signs the executable file specified in the [**SignedCode.FileName**](signedcode-filename.md) property.

## Syntax


```VB
SignedCode.Sign( _
  [ ByVal Signer ] _
)
```



## Parameters

<dl> <dt>

*Signer* \[in, optional\]
</dt> <dd>

A [**Signer**](signer.md) object that has access to the private key of the certificate used to sign the code. The default value is **Null**.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Before the **Sign** method is called, the file that contains the code must be specified in the [**FileName**](signedcode-filename.md) property.

If the executable file is already signed, this method overwrites the existing signature.

The following results apply to the *Signer* parameter value:

-   If the *Signer* parameter is not **NULL**, this method uses the private key pointed to by the associated certificate to encrypt the signature. If the private key pointed to by the certificate is not available, the method fails.
-   If the *Signer* parameter is **NULL** and there is exactly one certificate in the CURRENT\_USER MY store that has access to a private key with code signing capability, that certificate is used to create the signature.
-   If the *Signer* parameter is **NULL**, the [**Settings.EnablePromptForCertificateUI**](settings-enablepromptforcertificateui.md) property value is true, and there is more than one certificate in the CURRENT\_USER MY store with an available private key with code signing capability, a dialog box appears that allows the user to select which certificate is used.
-   If the *Signer* parameter is **NULL** and the [**Settings.EnablePromptForCertificateUI**](settings-enablepromptforcertificateui.md) property is false, the method fails.
-   If the *Signer* parameter is **NULL** and there are no certificates in the CURRENT\_USER MY store with an available private key with code signing capability, the method fails.

This method uses the SHA-1 hashing algorithm.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
