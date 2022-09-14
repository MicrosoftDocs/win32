---
description: An association class is a special type of class that defines a relationship between two other classes.
ms.assetid: 21fd6e39-5dd3-41b8-a2f5-0135a6637ce8
ms.tgt_platform: multiple
title: Declaring an Association Class
ms.topic: article
ms.date: 05/31/2018
---

# Declaring an Association Class

An association class is a special type of class that defines a relationship between two other classes.

The following procedure describes how to create an association class using MOF code.

**To create an association class using MOF code**

1.  Assign the **Association** qualifier to your class.

    Although it is possible to create a class with references to objects or classes, using the **Association** qualifier not only makes it clear that your class is an association class, but, as a best practice, ensures that your class fully functions as an association class.

2.  Create two references within the class describing the two object instances you wish to associate together using the **ref** type.

    The references bind the two objects in the association by containing paths to the objects. Although not required, use the reference properties as key properties as well.

    Although you can create fully qualified or namespace-relative references, WMI has only limited support for cross-namespace references. Specifically, only statically defined objects can reference each other across namespace boundaries; dynamically supported objects cannot reference each other.

    If necessary, use the **HasClassRef** and **Classref** qualifiers in conjunction with the **object ref** type to reference a class.

    WMI supports having one **ref** reference point to an instance, and the other **object** reference point to a class. In this case, your association class would describe an association that binds instances to classes.

    The following code example describes the syntax for using **HasClassRef** and **Classref** with an **object** type.

    ``` syntax
    [HasClassRefs, Association]
    class SomeAssocClass
    {
         [key, classref{ "MyEndpoint", "OtherContainer" }]
         object ref ep1;
         [key] object ref ep2;
    }; 
    ```

    In the previous example, the **ep1** reference can point to the class definitions for either the **MyEndpoint** class or the **OtherContainer** class. Note that while you must weakly type the reference class, you cannot weakly type the **Classref** qualifier itself; doing so would severely reduce the efficiency of the WMI query engine. Weak typing is creating a reference that can contain any data type by using the **object** keyword and **ref** data type. To successfully use **HasClassRef**, you must set the relevant qualifier flavors to propagate to all instances and subclasses.

3.  Create any other properties as necessary.

    The following code example shows that WMI does not currently support association classes having less or more than two reference properties.

    ``` syntax
    [Association : ToInstance] 
    class MyAssocClass
    {
        ClassX ref PathToClassX ;
        ClassY ref PathToClassY ;
    };
    ```

4.  When finished, compile your MOF code with the MOF compiler.

    For more information, see [Compiling MOF Files](compiling-mof-files.md).

The code example in Step 3 defines the **MyAssocClass** association class. The **MyAssocClass** class defines a relationship between **ClassX** and **ClassY**. The **PathToClassX** and **PathToClassY** properties contain object paths to the instances of the classes to be associated. The keyword **ToInstance** is one of several flavor flags that WMI defines to provide information about the use of a qualifier. The **ToInstance** keyword indicates that WMI should propagate the **Association** qualifier to all instances of the association class. By checking this instance qualifier, the client software can determine that an instance belongs to an association class, without having to retrieve the class definition to look for the **Association** qualifier. For more information, see [Describing a Qualifier With a Qualifier Flavor](describing-a-qualifier-with-a-qualifier-flavor.md) and [References](references.md).

## Related topics

<dl> <dt>

[Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md)
</dt> </dl>

 

 



