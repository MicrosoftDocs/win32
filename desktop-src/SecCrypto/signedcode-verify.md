---
description: Verifies the Authenticode signature on the signed code.
ms.assetid: eecd692d-6b20-4644-a3d9-fba07ee667d7
title: SignedCode.Verify method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SignedCode.Verify
api_type: 
- COM
api_location: 
- Capicom.dll
---

# SignedCode.Verify method

\[The **Verify** method is available for use in the operating systems specified in the Requirements section. Instead, use Platform Invocation Services (PInvoke) to call the Win32 API [**SignerSignEx**](signersignex.md), [**SignerTimeStampEx**](signertimestampex.md), and [**WinVerifyTrust**](/windows/desktop/api/Wintrust/nf-wintrust-winverifytrust) functions to sign content with an Authenticode digital signature. For information about PInvoke, see [Platform Invoke Tutorial](https://msdn.microsoft.com/library/aa288468.aspx). The [.NET and CryptoAPI via P/Invoke: Part 1](/previous-versions/ms867087(v=msdn.10)#netcryptoapi_topic5) and [.NET and CryptoAPI via P/Invoke: Part 2](/previous-versions/ms867087(v=msdn.10)#netcryptoapi_topic6) subsections of [Extending .NET Cryptography with CAPICOM and P/Invoke](/previous-versions/ms867087(v=msdn.10)) may also be helpful.\]

The **Verify** method verifies the Authenticode signature on the signed code.

## Syntax


```VB
SignedCode.Verify( _
  [ ByVal bUIAllowed ] _
)
```



## Parameters

<dl> <dt>

*bUIAllowed* \[in, optional\]
</dt> <dd>

A Boolean value that specifies whether a dialog box is used to verify the signature. If true, a dialog box is generated to determine whether the code is trusted. The default value is false.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**SignedCode**](signedcode.md)
</dt> </dl>

 

 
