---
description: Qualifier flavors provide more information about a qualifier, such as whether a derived class or instance can override the qualifiers original value.
ms.assetid: 6a0769ac-e16c-45e1-92b6-26e4969bf23d
ms.tgt_platform: multiple
title: Qualifier Flavors
ms.topic: article
ms.date: 05/31/2018
---

# Qualifier Flavors

Qualifier flavors provide more information about a qualifier, such as whether a derived class or instance can override the qualifier's original value.

Qualifier flavors may be added to the top of the MOF file, using the following syntax, causing them to be applied throughout the definition. For example:

``` syntax
Qualifier Description : ToSubClass Amended;
```

The **ToSubClass** and **Amended** flavors applies to all the **Description** qualifiers in the MOF.

The following table lists the qualifier flavors.



| Qualifier Flavor    | Meaning                                                                                                                                                                                                                                         |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Amended**         | The qualifier is not required in the basic class definition and can be moved to the amendment to be localized.                                                                                                                                  |
| **DisableOverride** | The qualifier cannot be overridden in a derived class or instance. Note that being able to override a propagated qualifier is the default.                                                                                                      |
| **EnableOverride**  | When propagated to a derived class or instance, the value of the qualifier can be overridden. Setting **EnableOverride** is optional because being able to override the qualifier value is the default functionality for propagated qualifiers. |
| **NotToInstance**   | The qualifier is not propagated to class instances.                                                                                                                                                                                             |
| **NotToSubClass**   | The qualifier is not propagated to derived classes.                                                                                                                                                                                             |
| **Restricted**      | The qualifier is not propagated to instances or derived classes.                                                                                                                                                                                |
| **ToInstance**      | The qualifier is propagated to instances.                                                                                                                                                                                                       |
| **ToSubClass**      | The qualifier is propagated to derived classes. This flavor is only appropriate for qualifiers defined for a class and cannot be attached to a qualifier describing a class instance.                                                           |



 

 

 



