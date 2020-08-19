---
title: Class Inheritance in the Active Directory Schema
description: All object classes in an Active Directory directory service schema are derived from the special class top.
ms.assetid: 26e5107f-8204-4f64-bd07-b5b4f16103f4
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Class Inheritance in the Active Directory Schema

All object classes in an Active Directory directory service schema are derived from the special class [**top**](/windows/desktop/ADSchema/c-top). With the exception of **top**, all object classes are subclasses of another object class. For example, [**contact**](/windows/desktop/ADSchema/c-contact) is a subclass of [**organizationalPerson**](/windows/desktop/ADSchema/c-organizationalperson); **organizationalPerson** is a subclass of [**person**](/windows/desktop/ADSchema/c-person); and **person** is a subclass of **top**. The [**subClassOf**](/windows/desktop/ADSchema/a-subclassof) attribute of a [**classSchema**](/windows/desktop/ADSchema/c-classschema) object is a single-valued property that indicates the immediate superclass of the class.

Some of the attribute values that define a class are inherited from its superclasses. So the [**contact**](/windows/desktop/ADSchema/c-contact) class inherits values from its superclasses, which are the [**organizationalPerson**](/windows/desktop/ADSchema/c-organizationalperson), [**person**](/windows/desktop/ADSchema/c-person), and [**top**](/windows/desktop/ADSchema/c-top) classes. A class inherits the following data from its superclasses:

-   Possible attributes: The values of the [**mustContain**](/windows/desktop/ADSchema/a-mustcontain), [**mayContain**](/windows/desktop/ADSchema/a-maycontain), [**systemMustContain**](/windows/desktop/ADSchema/a-systemmustcontain), and [**systemMayContain**](/windows/desktop/ADSchema/a-systemmaycontain) attributes of a [**classSchema**](/windows/desktop/ADSchema/c-classschema) object define a complete list of the attributes that can be set on an instance of the object class. For each object class, the values of these attributes include all of the values that are inherited from its superclasses, as well as any values that are set explicitly for the object class itself. Thus, the [**mustContain**](/windows/desktop/ADSchema/a-mustcontain) attribute of the [**organizationalPerson**](/windows/desktop/ADSchema/c-organizationalperson) class includes all the **mustContain** values that are inherited from the [**person**](/windows/desktop/ADSchema/c-person) and [**top**](/windows/desktop/ADSchema/c-top) classes as well as any **mustContain** values that are set explicitly on the **organizationalPerson** class.
-   Possible parents in the directory hierarchy: The values of the [**possSuperiors**](/windows/desktop/ADSchema/a-posssuperiors) and [**systemPossSuperiors**](/windows/desktop/ADSchema/a-systemposssuperiors) attributes of a [**classSchema**](/windows/desktop/ADSchema/c-classschema) object define a complete list of the object classes that can contain an instance of the object class. For each object class, the values include those inherited from its superclasses, as well as those set explicitly for the object class itself.

Be aware that object class can also have many auxiliary classes, which are specified in the [**auxiliaryClass**](/windows/desktop/ADSchema/a-auxiliaryclass) and [**systemAuxiliaryClass**](/windows/desktop/ADSchema/a-systemauxiliaryclass) attributes of a **classSchema** object. An object class inherits [**mustContain**](/windows/desktop/ADSchema/a-mustcontain), [**mayContain**](/windows/desktop/ADSchema/a-maycontain), [**systemMustContain**](/windows/desktop/ADSchema/a-systemmustcontain), and [**systemMayContain**](/windows/desktop/ADSchema/a-systemmaycontain) values from its auxiliary classes.

 

 