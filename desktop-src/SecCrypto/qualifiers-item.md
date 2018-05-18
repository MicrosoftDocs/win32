---
Description: 'Retrieves a qualifier based on a specified index.'
ms.assetid: '4d54358d-99de-4a1c-b843-41006f47a279'
title: 'Qualifiers.Item property'
---

# Qualifiers.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](T:System.Security.Cryptography.X509Certificates.X509Extension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to process qualifiers that are part of the policy information in the Certificate Policies extension.\]

The **Item** property retrieves a qualifier based on a specified index. This is the default property.

## Syntax


```VB
Qualifiers.Item( _
  ByVal Index _
) As Variant
```



## Property value

A [**Qualifier**](qualifier.md) object that represents the indexed qualifier of the collection.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Qualifiers**](qualifiers.md)
</dt> </dl>

 

 




