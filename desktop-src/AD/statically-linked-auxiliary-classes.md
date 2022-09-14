---
title: Statically Linked Auxiliary Classes
description: A statically linked auxiliary class is one that is included in the auxiliaryClass or systemAuxiliaryClass attribute of an object class's classSchema definition in the schema.
ms.assetid: 24765001-7a60-4654-a23a-bf0326b59096
ms.tgt_platform: multiple
keywords:
- Statically Linked Auxiliary Classes AD
ms.topic: article
ms.date: 05/31/2018
---

# Statically Linked Auxiliary Classes

A statically linked auxiliary class is one that is included in the **auxiliaryClass** or **systemAuxiliaryClass** attribute of an object class's **classSchema** definition in the schema. This means that the auxiliary class is part of every instance of the class with which it is associated.

An auxiliary class can be statically linked to an object class when the class is defined, that is, when its **classSchema** object is added to the schema container. This is the only time that the **systemAuxiliaryClass** can be used; after a **classSchema** object is created, its **systemAuxiliaryClass** attribute cannot be modified. An auxiliary class that is statically linked at this time can have mandatory (**mustHave**) and/or optional (**mayHave**) attributes.

A privileged user with the permissions required to extend the schema can add or remove auxiliary classes from the **systemAuxiliaryClass** attribute of an existing **classSchema** object. Doing so adds or removes the auxiliary class from every existing instance of the object class. An auxiliary class that is statically linked at this time can have optional attributes, but cannot have mandatory attributes. This is because there may be existing instances of the object class, in which case, adding a new mandatory attribute would create problems. A privileged user can subsequently remove an auxiliary class from the **auxiliaryClass** attribute of a **classSchema** object.

 

 




