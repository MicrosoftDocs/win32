---
Description: Sets or retrieves the value of the attribute.
ms.assetid: aaf0c07c-756f-48c8-b4cd-def40f7cb1a3
title: Attribute.Value property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Attribute.Value
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Attribute.Value property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**CryptographicAttributeObject Class**](https://msdn.microsoft.com/library/ms147976(v=VS.90).aspx) in the [**System.Security.Cryptography**](https://msdn.microsoft.com/library/9eat8fht(v=VS.96).aspx) namespace.\]

The **Value** property sets or retrieves the value of the attribute.

This property is read/write.

## Syntax


```VB
Attribute.Value As Variant
```



## Property value

A **Variant** variable that contains the value of the attribute. For **CAPICOM\_AUTHENTICATED\_ATTRIBUTE\_SIGNING\_TIME** attributes, the data type is **DATE**. For all other attributes, the property value is a string.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




