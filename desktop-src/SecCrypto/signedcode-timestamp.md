---
Description: Creates an Authenticode time stamp signature on the signed executable file specified in the SignedCode.FileName property.
ms.assetid: 8f4c9901-b509-4e4c-82f9-a802b0896a11
title: SignedCode.Timestamp method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SignedCode.Timestamp method

\[The **Timestamp** method is available for use in the operating systems specified in the Requirements section. Instead, use Platform Invocation Services (PInvoke) to call the Win32 API [**SignerSignEx**](signersignex.md), [**SignerTimeStampEx**](signertimestampex.md), and [**WinVerifyTrust**](/windows/win32/Wintrust/nf-wintrust-winverifytrust?branch=master) functions to sign content with an Authenticode digital signature. For information about PInvoke, see [Platform Invoke Tutorial](http://go.microsoft.com/fwlink/p/?linkid=119531). The [.NET and CryptoAPI via P/Invoke: Part 1](http://go.microsoft.com/fwlink/p/?linkid=119533) and [.NET and CryptoAPI via P/Invoke: Part 2](http://go.microsoft.com/fwlink/p/?linkid=119534) subsections of [Extending .NET Cryptography with CAPICOM and P/Invoke](http://go.microsoft.com/fwlink/p/?linkid=119532) may also be helpful.\]

The **Timestamp** method creates an Authenticode time stamp signature on the signed executable file specified in the **SignedCode.FileName** property. This time stamp is a counter signature on the signed executable file that is performed by a time stamp authority.

## Syntax


```VB
SignedCode.Timestamp( _
  ByVal URL _
)
```



## Parameters

<dl> <dt>

*URL* \[in\]
</dt> <dd>

A string that contains the URL of the time stamp server.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

A time stamp extends the validity of a certificate by verifying that the executable file was signed at the time that it was time stamped.

Before this method can be called, the signed executable file to be time stamped must be specified in the **SignedCode.FileName** property, and the [**SignedCode.Sign**](signedcode-sign.md) method must be called to sign the executable file.

If the signed executable file is already time stamped, this method overwrites the existing time stamp.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**SignedCode**](signedcode.md)
</dt> </dl>

 

 




