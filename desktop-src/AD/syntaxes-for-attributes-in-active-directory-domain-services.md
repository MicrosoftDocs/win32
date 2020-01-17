---
title: Syntaxes for Attributes in Active Directory Domain Services
description: Active Directory Domain Services define a set of attribute syntaxes for specifying the type of data contained by an attribute.
ms.assetid: 79d27d47-5d03-4ad6-bf97-c387c34fa454
ms.tgt_platform: multiple
keywords:
- Syntaxes for Active Directory Domain Services Attributes Active Directory
- Attributes Active Directory , Syntaxes for
ms.topic: article
ms.date: 05/31/2018
---

# Syntaxes for Attributes in Active Directory Domain Services

Active Directory Domain Services define a set of attribute syntaxes for specifying the type of data contained by an attribute. The predefined syntaxes do not actually appear in the directory, and you cannot add new syntaxes. Several methods can be used to identify the syntax of an attribute class:

-   The [**IADs.Get**](https://docs.microsoft.com/windows/desktop/api/iads/nf-iads-iads-get), [**IADs.GetEx**](https://docs.microsoft.com/windows/desktop/api/iads/nf-iads-iads-getex), [**IADs.Put**](https://docs.microsoft.com/windows/desktop/api/iads/nf-iads-iads-put), and [**IADs.PutEx**](https://docs.microsoft.com/windows/desktop/api/iads/nf-iads-iads-putex) methods use the [**VARIANT**](https://msdn.microsoft.com/library/ms221627(v=VS.71).aspx) structure to get and set the values of an object's attributes. The **vt** member of this structure is a **VARTYPE** value that identifies the data type.
-   The methods of the [**IDirectoryObject**](https://docs.microsoft.com/windows/desktop/api/iads/nn-iads-idirectoryobject) and [**IDirectorySearch**](https://docs.microsoft.com/windows/desktop/api/iads/nn-iads-idirectorysearch) interfaces use a value from the [**ADSTYPEENUM**](https://docs.microsoft.com/windows/win32/api/iads/ne-iads-adstypeenum) enumeration to specify the data type.
-   To specify the syntax of a new attribute class, set the [**attributeSyntax**](https://docs.microsoft.com/windows/desktop/ADSchema/a-attributesyntax) and [**oMSyntax**](https://docs.microsoft.com/windows/desktop/ADSchema/a-omsyntax) attributes of an [**attributeSchema**](https://docs.microsoft.com/windows/desktop/ADSchema/c-attributeschema) object. If the value of **oMSyntax** is 127, you must also set the [**oMObjectClass**](https://docs.microsoft.com/windows/desktop/ADSchema/a-omobjectclass) attribute. For more information, see [Choosing a Syntax](choosing-a-syntax.md).

For a complete list of the syntaxes provided by Active Directory Domain Services, including each syntax's corresponding **VARTYPE** and [**ADSTYPEENUM**](https://docs.microsoft.com/windows/win32/api/iads/ne-iads-adstypeenum) value, see [Syntaxes](https://docs.microsoft.com/windows/desktop/ADSchema/syntaxes).

 

 




