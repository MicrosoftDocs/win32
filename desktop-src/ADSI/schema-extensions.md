---
title: Schema Extensions
description: The architecture of the ADSI schema provides that new schema classes can be added to the schema class container and new properties to an existing schema class object at run time.
ms.assetid: 935d39ca-cfb9-4aa3-aa0e-b614f7b359f2
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Schema Extensions

The architecture of the ADSI schema provides that new schema classes can be added to the schema class container and new properties to an existing schema class object at run time. The latter ability requires no new code. This is an important feature for namespaces that allow extensible directory services. The provider component must allow for this extensibility and know where to access and store the class instance and the values of its properties. In a typical extensible directory service, this information is stored in the directory service database in the same manner as any other schema class and property definitions.

> [!Note]  
> In COM interface terminology, only properties can be added to an existing schema class, not methods. Adding a new method would require adding a new implementation of that method and thus require additional code.

 

For an example of a specific provider schema, see [Schema Management](schema-management.md).

 

 




