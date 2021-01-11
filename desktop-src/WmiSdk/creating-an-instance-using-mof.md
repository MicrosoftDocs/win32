---
description: You can declare a basic instance of a class in the Windows Management service using Managed Object Format (MOF). You can also override the default values for an instance. For more information, see Setting an Instance Property Value.
ms.assetid: 12eda062-9614-455d-ae99-7706c685137b
ms.tgt_platform: multiple
title: Creating an Instance Using MOF
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Instance Using MOF

You can declare a basic instance of a class in the Windows Management service using Managed Object Format (MOF). You can also override the default values for an instance. For more information, see [Setting an Instance Property Value](#setting-an-instance-property-value).

The following procedure describes how to declare a basic instance of a class using MOF code.

**To declare a basic instance of a class using MOF code**

1.  Use the **Instance of** keywords followed by the class name, curly braces, and a semicolon.

    The following code example shows how to declare an instance of a class.

    ```mof
    instance of ClassName
    {
    };
    ```

    

2.  When finished, insert your MOF code into the WMI repository using the MOF compiler.

    For more information, see [Compiling MOF Files](compiling-mof-files.md).

An instance of a class includes all of the properties of the class. If the class is a derived class, instances include the properties belonging to all of the classes higher in the hierarchy. Each class that an instance is created from has one or more key properties. You cannot create an instance with more than 256 keys.

## Setting an Instance Property Value

Because WMI strongly types properties, you cannot modify property types. You can, however, set property values in instances. When a class assigns a default value to a property, WMI assigns the default value to each instance. You can override this value in your instance declaration.

The following procedure describes how to set a property value or overwrite a default value using MOF code.

**To set a property value or overwrite a default value using MOF code**

1.  Place an assignment statement between the curly braces of the instance declaration.

    The following code example shows how to set a property value.

    ``` syntax
    instance of ClassName
    {
        Prop = "value";
    };
    ```

    WMI does not require that you set any property during instance creation. The exception is any property marked with the [**Key**](key-qualifier.md) qualifier. Because WMI uses key properties to uniquely identify instances, you must set all key properties as you encounter them. In contrast, you must not set a system property in an instance declaration. Instead, WMI assigns the appropriate values to a system property when necessary.

2.  When finished, insert your MOF code into the WMI repository with a call to the MOF compiler.

    For more information, see [Compiling MOF Files](compiling-mof-files.md).

The following code examples show how an instance specifies data for properties defined by a class.

``` syntax
class MyClass 
{
    [key] string   strProp;
    sint32   dwProp1;
    uint32       dwProp2;
};

instance of MyClass 
{
    strProp = "hello";
    dwProp1 = -1;
    dwProp2 = 0xffffffff;
};
```

In the preceding example, the class defines three properties: a character string, a 32-bit signed integer, and a 32-bit unsigned integer. The instance provides data values for each of these properties.

 

 



