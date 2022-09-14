---
description: The MOF ref key word describes an object path and maps to a VT\_BSTR Automation type.
ms.assetid: 9da25435-4ccc-4251-a4be-37239156e320
ms.tgt_platform: multiple
title: References (WMI)
ms.topic: article
ms.date: 05/31/2018
---

# References (WMI)

The MOF **ref** key word describes an object path and maps to a VT\_BSTR Automation type. The object path can be either a full path to a server and namespace, or a relative path to another object in the same namespace. You can use a **ref** key word to link two or more classes together. WMI supports two types of object paths, which use to define general or specific paths within WMI.

The main purpose of the **ref** key word is to reduce transport time and encoding between objects that exist entirely within the WMI repository. You can also use the **ref** key word to create an association between two classes. For more information, see [Declaring an Association Class](declaring-an-association-class.md). If the referenced item is located within the same MOF file, use an alias to initialize the **ref** value. For more information, see [Creating an Alias](creating-an-alias.md).

> [!Note]  
> When a **ref** key word is applied to a key property, you can distinguish object references by the object string value instead of by the dereferenced value.

 

MOF supports the concept of a weakly typed and strongly typed object path. A weakly typed object path points to an object of an unspecified class and uses the **ref** key word with the [OBJECT](object.md) keyword. A strongly typed object points to an object of a specific class and uses **ref** with the class name. The following example describes a weakly typed **RefToAnyClass** reference that can point to any class or class instance, and a **RefToClassX** reference that can point only to a **ClassX** class or instance:

``` syntax
class MyClass
{
    object ref RefToAnyClass;       // Weakly typed
    ClassX ref RefToClassX;         // Strongly typed
};
```

The following example describes two instances and an association object that references the previous instances:

``` syntax
#pragma namespace("\\\\.\\root")

instance of __Namespace
{
    Name = "WMI" ;
} ;

#pragma namespace("\\\\.\\root\\WMI")

Class A{
    [key] string aKey;
};

Class C{
    [key] string cKey;
};

// The following class creates an association 
// between the "A" class and the "C" class
    [Association] Class B{
    [key] A ref aRef;
    [Key, Min(1)] C ref cRef;
};

instance of a
{
    aKey = "This is the key for the A class";
};

instance of c
{
    cKey = "This is the key for the c class";
};
```

 

 



