---
Description: Retrieves a Boolean value that indicates whether the basic constraint extension is marked critical.
ms.assetid: 4e84ea58-397b-491c-bdab-b5b4d46e070e
title: BasicConstraints.IsCritical property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BasicConstraints.IsCritical
api_type: 
- COM
api_location: 
- Capicom.dll
---

# BasicConstraints.IsCritical property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**X509BasicConstraintsExtension Class**](https://msdn.microsoft.com/library/z0k9d993(v=VS.90).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/ztkw6e67(v=VS.96).aspx) namespace.\]

The **IsCritical** property retrieves a Boolean value that indicates whether the basic constraint extension is marked critical.

This property is read-only.

## Syntax


```VB
BasicConstraints.IsCritical As Boolean
```



## Property value

If **true**, the basic constraint extension is marked critical.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




