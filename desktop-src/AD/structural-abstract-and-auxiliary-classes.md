---
title: Structural, Abstract, and Auxiliary Classes
description: The objectClassCategory attribute of a classSchema object can have a value, as listed in the following table, that indicates whether the class is structural, abstract, or auxiliary.
ms.assetid: 5af740cb-b292-4d80-abe5-3e3d194758f3
ms.tgt_platform: multiple
keywords:
- Structural, Abstract, and Auxiliary Classes AD
ms.topic: article
ms.date: 05/31/2018
---

# Structural, Abstract, and Auxiliary Classes

The **objectClassCategory** attribute of a **classSchema** object can have a value, as listed in the following table, that indicates whether the class is structural, abstract, or auxiliary.



| Value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | A structural class, which is the only type of class that can have instances in Active Directory Domain Services. A structural class can be a subclass of an abstract or structural class. A structural class can include any number of auxiliary classes in its definition.                                                                                                                                                                                                                                           |
| 2     | An abstract class, which is a template used to derive new abstract, auxiliary, and structural classes. An abstract class can only be a subclass of an abstract class. Abstract classes cannot be instantiated in Active Directory Domain Services. An abstract class can include any number of auxiliary classes in its definition.                                                                                                                                                                                   |
| 3     | An auxiliary class, which can be included in the definition of a structural, abstract, or auxiliary class, in which case, the **mustContain**, **systemMustContain**, **mayContain**, and **systemMayContain** values of the auxiliary class are added to those of the class. An auxiliary class can be a subclass of an abstract or auxiliary class. Auxiliary classes cannot be instantiated in Active Directory Domain Services. An auxiliary class can include any number of auxiliary classes in its definition. |



 

Do not confuse the **objectClassCategory** with an [object category](object-class-and-object-category.md).

 

 




