---
title: Class Inheritance in the Active Directory Schema
description: All object classes in an Active Directory directory service schema are derived from the special class top.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 26e5107f-8204-4f64-bd07-b5b4f16103f4
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Class Inheritance in the Active Directory Schema

All object classes in an Active Directory directory service schema are derived from the special class [**top**](https://msdn.microsoft.com/library/ms683975). With the exception of **top**, all object classes are subclasses of another object class. For example, [**contact**](https://msdn.microsoft.com/library/ms680995) is a subclass of [**organizationalPerson**](https://msdn.microsoft.com/library/ms683883); **organizationalPerson** is a subclass of [**person**](https://msdn.microsoft.com/library/ms683895); and **person** is a subclass of **top**. The [**subClassOf**](https://msdn.microsoft.com/library/ms679891) attribute of a [**classSchema**](https://msdn.microsoft.com/library/ms680982) object is a single-valued property that indicates the immediate superclass of the class.

Some of the attribute values that define a class are inherited from its superclasses. So the [**contact**](https://msdn.microsoft.com/library/ms680995) class inherits values from its superclasses, which are the [**organizationalPerson**](https://msdn.microsoft.com/library/ms683883), [**person**](https://msdn.microsoft.com/library/ms683895), and [**top**](https://msdn.microsoft.com/library/ms683975) classes. A class inherits the following data from its superclasses:

-   Possible attributes: The values of the [**mustContain**](https://msdn.microsoft.com/library/ms678696), [**mayContain**](https://msdn.microsoft.com/library/ms677072), [**systemMustContain**](https://msdn.microsoft.com/library/ms680024), and [**systemMayContain**](https://msdn.microsoft.com/library/ms680023) attributes of a [**classSchema**](https://msdn.microsoft.com/library/ms680982) object define a complete list of the attributes that can be set on an instance of the object class. For each object class, the values of these attributes include all of the values that are inherited from its superclasses, as well as any values that are set explicitly for the object class itself. Thus, the [**mustContain**](https://msdn.microsoft.com/library/ms678696) attribute of the [**organizationalPerson**](https://msdn.microsoft.com/library/ms683883) class includes all the **mustContain** values that are inherited from the [**person**](https://msdn.microsoft.com/library/ms683895) and [**top**](https://msdn.microsoft.com/library/ms683975) classes as well as any **mustContain** values that are set explicitly on the **organizationalPerson** class.
-   Possible parents in the directory hierarchy: The values of the [**possSuperiors**](https://msdn.microsoft.com/library/ms679133) and [**systemPossSuperiors**](https://msdn.microsoft.com/library/ms680026) attributes of a [**classSchema**](https://msdn.microsoft.com/library/ms680982) object define a complete list of the object classes that can contain an instance of the object class. For each object class, the values include those inherited from its superclasses, as well as those set explicitly for the object class itself.

Be aware that object class can also have many auxiliary classes, which are specified in the [**auxiliaryClass**](https://msdn.microsoft.com/library/ms675242) and [**systemAuxiliaryClass**](https://msdn.microsoft.com/library/ms680020) attributes of a **classSchema** object. An object class inherits [**mustContain**](https://msdn.microsoft.com/library/ms678696), [**mayContain**](https://msdn.microsoft.com/library/ms677072), [**systemMustContain**](https://msdn.microsoft.com/library/ms680024), and [**systemMayContain**](https://msdn.microsoft.com/library/ms680023) values from its auxiliary classes.

 

 




