---
description: 'When creating an instance with embedded objects, perform the following tasks:'
ms.assetid: 2abf6197-8b95-4c04-b154-508aa85fe12f
ms.tgt_platform: multiple
title: Creating Embedded Objects
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Creating Embedded Objects

When creating an instance with embedded objects, perform the following tasks:

-   You must declare an embedded object as strongly typed or weakly typed.

    A strongly typed object points to an object of a specific class and uses the class name. A weakly typed object points to an object of an unspecified class and uses the **object** keyword. Both objects map to the **VT\_UNKNOWN** type.

-   You can use **NULL** for the default value of embedded objects and paths in initializations and declarations.
-   When embedding an object path, do not place white space between the elements of the embedded path. For example, the object path "Class1Index=3;" contains no space between the property name "Class1index" and the value being assigned, which is "3".

The following class declaration shows you how to declare strongly typed and weakly typed embedded objects.

``` syntax
Class MyClass
{
    EmbedClass    Object1;          // Strongly typed
    object        Object2;          // Weakly typed
};
```

The following examples describe how to declare embedded objects within a class declaration.

``` syntax
Class Class1 
{ 
     [key] sint32 Class1Index;
};

Class Class2 
{
    [key] sint32 Class2Index;
    Class1 EmbedObject1 = instance of Class1{Class1Index=3;};
};

Class Class3
{
    [key] sint32 Class3Index;
    Class2 EmbedObject2 = instance of Class2 {Class2Index=4;};
};
```

The following example describes the initialization of one property that is a strongly typed object and another property that is an array of weakly typed objects.

``` syntax
Class EmbedClass1
{
    [key] sint32 intval;
};

Class EmbedClass2
{
    [key] string sval;
};

Class ContainerClass
{
    [key] sint32 intval;
    EmbedClass1 SingleObject;
    Object ArrayObject[];
};

Instance of ContainerClass
{
    intval = 33;
    SingleObject = instance of EmbedClass1 {intval=99;};
    ArrayObject = {instance of EmbedClass2 {sval="something";},
                   instance of EmbedClass1 {intval=100;}};
};
```

 

 



