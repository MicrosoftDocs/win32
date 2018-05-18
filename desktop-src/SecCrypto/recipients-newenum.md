---
Description: 'The \_NewEnum property of Recipients retrieves an IEnumVARIANT interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).'
ms.assetid: 'affdc695-b78c-48b5-b66d-5f94e1a86ff2'
title: 'Recipients.\_NewEnum property'
---

# Recipients.\_NewEnum property

\[The **\_NewEnum** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**CmsRecipientCollection Class**](T:System.Security.Cryptography.Pkcs.CmsRecipientCollection) in the [**System.Security.Cryptography.Pkcs**](frlrfSystemSecurityCryptographyPkcs) namespace.\]

The **\_NewEnum** property retrieves an [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).

## Syntax


```VB
Recipients._NewEnum As IUnknown
```



## Property value

An [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface on an object that can be used to enumerate the collection.

## Remarks

This property is automatically used internally when you use the `For Each In` construct in Visual Basic Scripting Edition (VBScript).

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Recipients**](recipients.md)
</dt> </dl>

 

 




