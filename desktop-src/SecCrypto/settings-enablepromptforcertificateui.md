---
description: Sets or retrieves a Boolean value that specifies whether user interface prompts for a signer or sender's identity can be used.
ms.assetid: b9765de4-0b94-4006-aaa8-9ad6858da1f4
title: Settings.EnablePromptForCertificateUI property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Settings.EnablePromptForCertificateUI
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Settings.EnablePromptForCertificateUI property

\[The **EnablePromptForCertificateUI** property is available for use in the operating systems specified in the Requirements section.\]

The **EnablePromptForCertificateUI** property sets or retrieves a Boolean value that specifies whether user interface prompts for a signer or sender's identity can be used.

## Syntax


```VB
Settings.EnablePromptForCertificateUI As Boolean
```



## Property value

If **true**, user interface prompts for a signer or sender's identity can be used. The default value is **false**.

> [!Note]  
> Setting this property does not disable warnings that are generated before any private key usage is done from a web-based application.

 

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Settings**](settings.md)
</dt> </dl>

 

 




