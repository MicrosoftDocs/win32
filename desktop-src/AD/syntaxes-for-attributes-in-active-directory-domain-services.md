---
title: Syntaxes for Attributes in Active Directory Domain Services
description: Active Directory Domain Services define a set of attribute syntaxes for specifying the type of data contained by an attribute.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '79d27d47-5d03-4ad6-bf97-c387c34fa454'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Syntaxes for Active Directory Domain Services Attributes Active Directory", "Attributes Active Directory , Syntaxes for"]
---

# Syntaxes for Attributes in Active Directory Domain Services

Active Directory Domain Services define a set of attribute syntaxes for specifying the type of data contained by an attribute. The predefined syntaxes do not actually appear in the directory, and you cannot add new syntaxes. Several methods can be used to identify the syntax of an attribute class:

-   The [**IADs.Get**](https://msdn.microsoft.com/library/aa746347), [**IADs.GetEx**](https://msdn.microsoft.com/library/aa746348), [**IADs.Put**](https://msdn.microsoft.com/library/aa746352), and [**IADs.PutEx**](https://msdn.microsoft.com/library/aa746353) methods use the [**VARIANT**](e305240e-9e11-4006-98cc-26f4932d2118) structure to get and set the values of an object's attributes. The **vt** member of this structure is a **VARTYPE** value that identifies the data type.
-   The methods of the [**IDirectoryObject**](https://msdn.microsoft.com/library/aa746355) and [**IDirectorySearch**](https://msdn.microsoft.com/library/aa746362) interfaces use a value from the [**ADSTYPEENUM**](https://msdn.microsoft.com/library/aa772240) enumeration to specify the data type.
-   To specify the syntax of a new attribute class, set the [**attributeSyntax**](https://msdn.microsoft.com/library/ms675236) and [**oMSyntax**](https://msdn.microsoft.com/library/ms679072) attributes of an [**attributeSchema**](https://msdn.microsoft.com/library/ms680969) object. If the value of **oMSyntax** is 127, you must also set the [**oMObjectClass**](https://msdn.microsoft.com/library/ms679071) attribute. For more information, see [Choosing a Syntax](choosing-a-syntax.md).

For a complete list of the syntaxes provided by Active Directory Domain Services, including each syntax's corresponding **VARTYPE** and [**ADSTYPEENUM**](https://msdn.microsoft.com/library/aa772240) value, see [Syntaxes](https://msdn.microsoft.com/library/ms684419).

 

 




