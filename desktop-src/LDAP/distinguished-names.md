---
title: Distinguished Names
description: The LDAP API references an LDAP object by its distinguished name (DN). A DN is a sequence of relative distinguished names (RDN) connected by commas.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'bb936c24-9a1b-4588-bc31-18aaf2b541b3'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["Distinguished Names LDAP"]
---

# Distinguished Names

The LDAP API references an LDAP object by its distinguished name (**DN**). A **DN** is a sequence of relative distinguished names (RDN) connected by commas.

An **RDN** is an attribute with an associated value in the form **attribute**=*value*; normally expressed in a UTF-8 string format. The following table lists typical RDN attribute types.



| String     | Attribute type         |
|------------|------------------------|
| **DC**     | domainComponent        |
| **CN**     | commonName             |
| **OU**     | organizationalUnitName |
| **O**      | organizationName       |
| **STREET** | streetAddress          |
| **L**      | localityName           |
| **ST**     | stateOrProvinceName    |
| **C**      | countryName            |
| **UID**    | userid                 |



 

The following are examples of distinguished names.

``` syntax
CN=Jeff Smith,OU=Sales,DC=Fabrikam,DC=COM
```

``` syntax
CN=Karen Berge,CN=admin,DC=corp,DC=Fabrikam,DC=COM
```

The following table lists reserved characters that cannot be used in an attribute value without being escaped.

> [!Note]  
> See the guidance below the table about using the escape character with these reserved characters.

 



| Reserved character | Description                                                       | Hex value |
|--------------------|-------------------------------------------------------------------|-----------|
|                    | space or **\#** character at the beginning of a string<br/> |           |
|                    | space character at the end of a string<br/>                 |           |
| **,**              | comma<br/>                                                  | 0x2C      |
| **+**              | plus sign<br/>                                              | 0x2B      |
| **"**              | double quote<br/>                                           | 0x22      |
| **\\**             | backslash<br/>                                              | 0x5C      |
| **&lt;**           | left angle bracket<br/>                                     | 0x3C      |
| **&gt;**           | right angle bracket<br/>                                    | 0x3E      |
| **;**              | semicolon<br/>                                              | 0x3B      |
| **LF**             | line feed<br/>                                              | 0x0A      |
| **CR**             | carriage return<br/>                                        | 0x0D      |
| **=**              | equals sign<br/>                                            | 0x3D      |
| **/**              | forwards slash<br/>                                         | 0x2F      |



 

If a reserved character is part of an attribute value, it must be escaped by prefixing it with a backslash (**\\**) in the attribute string. If an attribute value contains other reserved characters, such as the equals sign (**=**) or non-printable characters, it must be encoded in hexadecimal by replacing the character with a backslash followed by two hex digits.

The following are examples of some distinguished names that include escaped characters. The first example is an organizational unit name with an embedded comma; the second example is a value containing a carriage return.

``` syntax
CN=Litware,OU=Docs\, Adatum,DC=Fabrikam,DC=COM
```

``` syntax
CN=Before\0DAfter,OU=Test,DC=North America,DC=Fabrikam,DC=COM
```

## LDAP ADsPath

For more information about using distinguished names via the ADSI LDAP provider, see [LDAP ADsPath](https://msdn.microsoft.com/library/aa746384).

## Related topics

<dl> <dt>

[RFC 2253](http://go.microsoft.com/fwlink/p/?linkid=84036)
</dt> </dl>

 

 





