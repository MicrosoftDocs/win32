---
Description: The \_NewEnum property of EKUs retrieves an IEnumVARIANT interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).
ms.assetid: c7d038c0-416f-47f7-94ba-74ca877da7ba
title: EKUs._NewEnum property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- EKUs._NewEnum
api_type:
- COM
api_location:
- Capicom.dll
---

# EKUs.\_NewEnum property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ExtensionCollection Class**](https://msdn.microsoft.com/library/bs5ba18k(v=VS.90).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **\_NewEnum** property retrieves an [**IEnumVARIANT**](https://msdn.microsoft.com/en-us/library/ms221053(v=VS.71).aspx) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).

## Syntax


```VB
EKUs._NewEnum As IUnknown
```



## Property value

An [**IEnumVARIANT**](https://msdn.microsoft.com/en-us/library/ms221053(v=VS.71).aspx) interface on an object that can be used to enumerate the collection.

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

 

 




