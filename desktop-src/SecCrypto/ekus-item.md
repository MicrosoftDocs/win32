---
Description: 'Retrieves the EKU object that represents the indexed extended key usage (EKU) property.'
ms.assetid: 'b8c12a7a-e836-48c2-958c-937b3723f85b'
title: 'IEKUs::Item property'
---

# IEKUs::Item property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ExtensionCollection Class**](T:System.Security.Cryptography.X509Certificates.X509ExtensionCollection) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **Item** property retrieves the [**EKU**](eku.md) object that represents the indexed extended key usage (EKU) property.

This property is read-only.

## Syntax


```VB
EKUs.Item( _
  ByVal Index _
) As Variant
```



## Property value

An [**EKU**](eku.md) object that represents the indexed extended key usage (EKU) property.

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

 

 




