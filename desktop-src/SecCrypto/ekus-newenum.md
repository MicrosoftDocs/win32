---
Description: The \_NewEnum property of EKUs retrieves an IEnumVARIANT interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).
ms.assetid: c7d038c0-416f-47f7-94ba-74ca877da7ba
title: EKUs.\_NewEnum property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EKUs.\_NewEnum property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ExtensionCollection Class**](T:System.Security.Cryptography.X509Certificates.X509ExtensionCollection) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **\_NewEnum** property retrieves an [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).

## Syntax


```VB
EKUs._NewEnum As IUnknown
```



## Property value

An [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface on an object that can be used to enumerate the collection.

## Remarks

This property is automatically used internally when you use the `For Each In` construct in Visual Basic Scripting Edition (VBScript).

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**EKUs**](ekus.md)
</dt> </dl>

 

 




