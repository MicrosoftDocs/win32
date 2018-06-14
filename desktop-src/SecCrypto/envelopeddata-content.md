---
Description: Sets or retrieves the plaintext content of a message to be enveloped. This is the default property.
ms.assetid: 7927321f-fbda-45e0-9b9f-c10ecd3a98b1
title: EnvelopedData.Content property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EnvelopedData.Content property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**EnvelopedCms Class**](https://www.bing.com/search?q=**EnvelopedCms+Class**) in the [**System.Security.Cryptography.Pkcs**](https://www.bing.com/search?q=**System.Security.Cryptography.Pkcs**) namespace.\]

The **Content** property sets or retrieves the plaintext content of a message to be enveloped. This is the default property.

## Syntax


```VB
EnvelopedData.Content As String
```



## Property value

The plaintext content of a message to be enveloped.

## Remarks

Setting this property must be done before the [**Encrypt**](envelopeddata-encrypt.md) method is called. When the value of this property is reset, directly or indirectly, the whole [*state*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) of the object is reset, and any encrypted content in the object is lost.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**EnvelopedData**](envelopeddata.md)
</dt> </dl>

 

 




