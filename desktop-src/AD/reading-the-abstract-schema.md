---
title: Reading the Abstract Schema
description: This topic provides a code example and guidelines for reading from the abstract schema, which provides a subset of the data stored in the attributeSchema and classSchema objects in the schema container.
ms.assetid: f31fc0ae-048f-413c-9370-96367dc68df8
ms.tgt_platform: multiple
keywords:
- schema Active Directory , reading the abstract schema
ms.topic: article
ms.date: 05/31/2018
---

# Reading the Abstract Schema

This topic provides a code example and guidelines for reading from the abstract schema, which provides a subset of the data stored in the **attributeSchema** and **classSchema** objects in the schema container. To retrieve data that is unavailable in the abstract schema, read the data directly from the schema container as described in [Reading attributeSchema and classSchema Objects](reading-attributeschema-and-classschema-objects.md).

Use the "LDAP://schema" binding string to bind to an [**IADsContainer**](https://msdn.microsoft.com/library/aa705985) pointer on the abstract schema. Use this pointer to enumerate the class, attribute, and syntax entries in the abstract schema. You can also use the [**IADsContainer.GetObject**](https://msdn.microsoft.com/library/aa705989) method to retrieve individual entries.


```C++
// Bind to the abstract schema.
IADsContainer *pAbsSchema = NULL;
hr = ADsGetObject(L"LDAP://schema",
                  IID_IADsContainer,
                  (void**)&pAbsSchema);
```




```VB
' Bind to the abstract schema.
Dim adschema As IADsContainer
Set adschema = GetObject("LDAP://schema")
```



Use a similar binding string, "LDAP://schema/<object>", to bind directly to a class or attribute entry in the abstract schema. In this string, "<object>" is the **lDAPDisplayName** of a class or attribute. For classes bind to the [**IADsClass**](https://msdn.microsoft.com/library/aa705972) interface; for attributes, bind to [**IADsProperty**](https://msdn.microsoft.com/library/aa706099) interface.


```C++
// Bind to the user class entry in the abstract schema.
IADsClass *pClass;
hr = ADsGetObject(L"LDAP://schema/user",
                  IID_IADsClass,
                  (void**)&pClass);
```




```VB
Bind to the user class entry in the abstract schema.
Dim userclass As IADsClass
Set userclass = GetObject("LDAP://schema/user")
```



In addition, the [**IADs**](https://msdn.microsoft.com/library/aa705950) interface provides the [**IADs.Schema**](https://msdn.microsoft.com/library/aa746351) property. This property returns the ADsPath for the object class in abstract schema binding string format. If you have an **IADs** pointer to an object, you can bind to its class in the abstract schema using the ADsPath returned from **IADs.Schema**.

For classes, the following table lists key properties provided by the abstract schema.



| Property                                                             | Meaning                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IADsClass.Abstract**](https://msdn.microsoft.com/library/aa705973)            | Indicates whether this is an abstract class.                                                                                                                                                                                                                                            |
| [**IADsClass.Auxiliary**](https://msdn.microsoft.com/library/aa705973)           | Indicates whether this is an auxiliary class.                                                                                                                                                                                                                                           |
| [**IADsClass.AuxDerivedFrom**](https://msdn.microsoft.com/library/aa705973)      | Array of auxiliary classes this class derives from.                                                                                                                                                                                                                                     |
| [**IADsClass.Container**](https://msdn.microsoft.com/library/aa705973)           | Indicates whether objects of this class can contain other objects, which is true if any class includes this class in its list of **possibleSuperiors**.                                                                                                                                 |
| [**IADsClass.DerivedFrom**](https://msdn.microsoft.com/library/aa705973)         | Array of classes that this class is derived from.                                                                                                                                                                                                                                       |
| [**IADsClass.MandatoryProperties**](https://msdn.microsoft.com/library/aa705973) | Retrieves an array of the mandatory properties that must be set for an instance of the class. The returned list includes all the **mustContain** and **systemMustContain** values for the class and the classes from which it is derived, including superclasses and auxiliary classes. |
| [**IADsClass.OID**](https://msdn.microsoft.com/library/aa705973)                 | Retrieves the governsID of the class.                                                                                                                                                                                                                                                   |
| [**IADsClass.OptionalProperties**](https://msdn.microsoft.com/library/aa705973)  | Retrieves an array of the optional properties that might be set for an instance of the class. The returned list includes all the **mayContain** and **systemMayContain** values for the class and the classes from which it is derived, including superclasses and auxiliary classes.   |
| [**IADsClass.PossibleSuperiors**](https://msdn.microsoft.com/library/aa705973)   | Retrieves an array of the **possibleSuperiors** values for the class, which indicates the object classes that can contain objects of this class.                                                                                                                                        |



 

The abstract schema is stored in the **subSchema** object in the schema container. To get the distinguished name of the **subSchema** object, bind to rootDSE and read the **subSchemaSubEntry** attribute, as described in [Serverless Binding and RootDSE](serverless-binding-and-rootdse.md). Be aware that it is more efficient to read the abstract schema by binding to "LDAP://schema", than by binding directly to the **subSchema** object.

 

 




