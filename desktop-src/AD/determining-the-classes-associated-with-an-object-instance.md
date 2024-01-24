---
title: Determining the Classes Associated With an Object Instance
description: Every object in Active Directory Domain Services has two attributes whose values identify the hierarchy of object classes of which the object is an instance.
ms.assetid: bb46f165-8c6e-4af1-b387-e0e30a4c6226
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Determining the Classes Associated With an Object Instance

Every object in Active Directory Domain Services has two attributes whose values identify the hierarchy of object classes of which the object is an instance.




| Attribute | Description | 
|-----------|-------------|
| <strong>structuralObjectClass</strong> | Identifies the structural and abstract classes of which the object is an instance. For example, the values for a user object can be:<ul><li><strong>top</strong></li><li><strong>person</strong></li><li><strong>organizationalPerson</strong></li><li><strong>user</strong></li></ul> | 
| <strong>objectClass</strong> | Identifies the classes included in <strong>structuralObjectClass</strong>, plus any auxiliary classes that are dynamically attached. For example, if a "vehicle" auxiliary class is attached to a user object, the values can be:<ul><li><strong>top</strong></li><li><strong>vehicle</strong></li><li><strong>person</strong></li><li><strong>organizationalPerson</strong></li><li><strong>user</strong></li></ul> | 




 

Be aware that neither of these attributes include auxiliary classes that are statically linked with the object classes of which the object is an instance. For example, the **securityPrincipal** auxiliary class is statically linked with the **user** class because it is included in the **systemAuxiliaryClass** values of the user **classSchema** object; it is not included in either the **objectClass** or **structuralObjectClass** attributes of instances of the user class.

 

 




