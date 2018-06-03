---
Description: Returns a Boolean value that indicates whether the EKU extension is present. This is the default property.
ms.assetid: d7568525-1054-47e1-a176-f154792f9589
title: ExtendedKeyUsage.IsPresent property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ExtendedKeyUsage.IsPresent property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509EnhancedKeyUsageExtension Class**](https://www.bing.com/search?q=**X509EnhancedKeyUsageExtension Class**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace.\]

The **IsPresent** property returns a Boolean value that indicates whether the EKU extension is present. This is the default property.

## Syntax


```VB
ExtendedKeyUsage.IsPresent As Boolean
```



## Property value

If **true**, the EKU extension is present.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExtendedKeyUsage**](extendedkeyusage.md)
</dt> </dl>

 

 




