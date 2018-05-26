---
Description: Sets or retrieves the description of the signed executable file.
ms.assetid: 39ce37bd-fe3e-4195-a132-93f3743f7370
title: SignedCode.Description property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SignedCode.Description property

\[The **Description** property is available for use in the operating systems specified in the Requirements section. Instead, use Platform Invocation Services (PInvoke) to call the Win32 API [**SignerSignEx**](signersignex.md), [**SignerTimeStampEx**](signertimestampex.md), and [**WinVerifyTrust**](/windows/win32/Wintrust/nf-wintrust-winverifytrust?branch=master) functions to sign content with an Authenticode digital signature. For information about PInvoke, see [Platform Invoke Tutorial](http://go.microsoft.com/fwlink/p/?linkid=119531). The [.NET and CryptoAPI via P/Invoke: Part 1](http://go.microsoft.com/fwlink/p/?linkid=119533) and [.NET and CryptoAPI via P/Invoke: Part 2](http://go.microsoft.com/fwlink/p/?linkid=119534) subsections of [Extending .NET Cryptography with CAPICOM and P/Invoke](http://go.microsoft.com/fwlink/p/?linkid=119532) may also be helpful.\]

The **Description** property sets or retrieves the description of the signed executable file.

## Syntax


```VB
SignedCode.Description As String
```



## Property value

The description of the signed executable file.

## Remarks

The description is the text that appears in the Authenticode verification dialog box. The text should describe the signed executable file. If this property is **NULL**, the dialog box displays the name of the executable file.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**SignedCode**](signedcode.md)
</dt> </dl>

 

 




