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

-   The [**IADs.Get**](/windows/desktop/api/iads/nf-iads-iads-get), [**IADs.GetEx**](/windows/desktop/api/iads/nf-iads-iads-getex), [**IADs.Put**](/windows/desktop/api/iads/nf-iads-iads-put), and [**IADs.PutEx**](/windows/desktop/api/iads/nf-iads-iads-putex) methods use the [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) structure to get and set the values of an object's attributes. The **vt** member of this structure is a **VARTYPE** value that identifies the data type.
-   The methods of the [**IDirectoryObject**](/windows/desktop/api/iads/nn-iads-idirectoryobject) and [**IDirectorySearch**](/windows/desktop/api/iads/nn-iads-idirectorysearch) interfaces use a value from the [**ADSTYPEENUM**](/windows/win32/api/iads/ne-iads-adstypeenum) enumeration to specify the data type.
-   To specify the syntax of a new attribute class, set the [**attributeSyntax**](/windows/desktop/ADSchema/a-attributesyntax) and [**oMSyntax**](/windows/desktop/ADSchema/a-omsyntax) attributes of an [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) object. If the value of **oMSyntax** is 127, you must also set the [**oMObjectClass**](/windows/desktop/ADSchema/a-omobjectclass) attribute. For more information, see [Choosing a Syntax](choosing-a-syntax.md).

For a complete list of the syntaxes provided by Active Directory Domain Services, including each syntax's corresponding **VARTYPE** and [**ADSTYPEENUM**](/windows/win32/api/iads/ne-iads-adstypeenum) value, see [Syntaxes](/windows/desktop/ADSchema/syntaxes).

 

 