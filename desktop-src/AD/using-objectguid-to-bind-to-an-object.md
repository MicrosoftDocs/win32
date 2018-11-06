---
title: Using objectGUID to Bind to an Object
description: An object distinguished name changes if the object is renamed or moved, therefore the distinguished name is not a reliable object identifier.
ms.assetid: 6c038005-3ecb-4c00-b1a3-a231d3aea64e
ms.tgt_platform: multiple
keywords:
- Using objectGUID to Bind to an Object AD
- objectGUID AD
- objectGUID AD , using to bind to an object
- Active Directory, using, binding, using objectGUID to bind to object
ms.topic: article
ms.date: 05/31/2018
---

# Using objectGUID to Bind to an Object

An object distinguished name changes if the object is renamed or moved, therefore the distinguished name is not a reliable object identifier. In Active Directory Domain Services, an object's **objectGUID** property never changes, even if the object is renamed or moved. For more information about **objectGUID** and identifiers, see [Object Names and Identities](object-names-and-identities.md).

The Active Directory LDAP provider provides a method to bind to an object using the object GUID. The binding string format is as follows:


```C++
LDAP://servername/<GUID=XXXXX>
```



In this example, "servername" is the name of the directory server and "XXXXX" is the string representation of the hexadecimal value of the GUID. The "servername" is optional. The GUID string is specified in the "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" form. The GUID string can also take the form "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", which is the same form as the string produced by the [**StringFromGUID2**](https://msdn.microsoft.com/en-us/library/ms683893(v=VS.85).aspx) function, without the surrounding braces "{}". For more information and a code example that shows how to create a bindable string from a GUID, see [Example Code for Creating a Bindable String Representation of a GUID](example-code-for-creating-a-bindable-string-representation-of-a-guid.md). The [**IADs.GUID**](https://msdn.microsoft.com/library/aa746351) property can be used to retrieve the proper string form of the GUID.

When binding using the object GUID, some [**IADs**](https://msdn.microsoft.com/library/aa705950) and [**IADsContainer**](https://msdn.microsoft.com/library/aa705985) methods and properties are not supported. The following **IADs** properties are not supported by objects obtained by binding using the object GUID:

-   [**ADsPath**](https://msdn.microsoft.com/library/aa746351)
-   [**Name**](https://msdn.microsoft.com/library/aa746351)
-   [**Parent**](https://msdn.microsoft.com/library/aa746351)

The following **IADsContainer** methods are not supported by objects obtained by binding using the object GUID:

-   [**GetObject**](https://msdn.microsoft.com/library/aa705989)
-   [**Create**](https://msdn.microsoft.com/library/aa705987)
-   [**Delete**](https://msdn.microsoft.com/library/aa705988)
-   [**CopyHere**](https://msdn.microsoft.com/library/aa705986)
-   [**MoveHere**](https://msdn.microsoft.com/library/aa705991)

To use these methods and properties after binding to an object using the object GUID, use the [**IADs.Get**](https://msdn.microsoft.com/library/aa746347) method to retrieve the object distinguished name and then use the distinguished name to bind to the object again.

If an application stores or caches identifiers or references to objects stored in Active Directory Domain Services, the object GUID is the best identifier to use for several reasons:

-   The **objectGUID** property of on object never changes even if the object is renamed or moved.
-   It is easy to bind to the object using the object GUID.
-   If the object is renamed or moved, the **objectGUID** property provides a single identifier that can be used to quickly find and identify the object rather than having to compose a query that has conditions for all properties that would identify that object.

 

 




