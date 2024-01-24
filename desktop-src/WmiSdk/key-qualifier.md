---
description: The Key qualifier indicates whether the property is part of the namespace handle.
ms.assetid: 838d295f-e812-4e46-99a4-d2714a0ae8dc
ms.tgt_platform: multiple
title: Key Qualifier
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Key
api_type: 
- NA
api_location: 
---

# Key Qualifier

The **Key** qualifier indicates whether the property is part of the namespace handle. If more than one property has the **Key** qualifier, then all such properties collectively form the key (a compound key). When taken together, the key properties must supply a unique reference for each class instance. If this qualifier is placed on a property, only the value **TRUE** is allowed.

You can use any property type except for the following:

-   Arrays
-   Real and floating-point numbers
-   Embedded objects
-   Characters lower than ASCII 32 (that is, white space characters)
-   Character strings of type **char16** or character strings that are defined as keys must contain values greater than U+0020. This is because WMI uses key values in object paths, and you cannot use nonprinting characters in an object path.

When a parent class specifies a key, all classes derived from the parent class inherit that key. The derived classes cannot alter the inherited key or define any new key property. However, when you derive a subclass from an abstract class without a key, you can introduce a key in the subclass.

All classes that define more than one instance must specify a key. Because abstract classes do not define any instances, they do not need to specify keys. Because singleton classes define only one instance, they cannot specify keys.

Keys are written one time at object instantiation and must not be modified later. It does not make sense to apply a default value to a key-qualified property.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



 

 




