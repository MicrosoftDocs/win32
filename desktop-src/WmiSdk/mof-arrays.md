---
description: An array is an indexed list of data values that are of the same data type, which you can reference. In addition to string and numeric arrays, MOF supports arrays of embedded objects and references.
ms.assetid: f63c222f-499d-4776-8901-65cb8b142d2b
ms.tgt_platform: multiple
title: MOF Arrays
ms.topic: article
ms.date: 05/31/2018
---

# MOF Arrays

An array is an indexed list of data values that are of the same data type, which you can reference. In addition to string and numeric arrays, MOF supports arrays of embedded objects and references.

The following rules define a MOF array:

-   Brackets used after the property identifier specify an array in a class definition.

    ``` syntax
    Class ArrayDataSample1
    {
        string strArray1[];
    };
    ```

-   All arrays must be one-dimensional.
-   Arrays can be unbounded or have an explicit size.

    ``` syntax
    Class MyClass
    {
        sint32 MyMethod1 ([in, id(0)] Win32_LogicalDisk DiskArray1[]);
        sint32 MyMethod2 ([in, id(0)] Win32_LogicalDisk DiskArray2[32]);
    };
    ```

    WMI implements bounded and unbounded arrays as **SAFEARRAY** structures, which allows WMI to vary array dimensions at run time. When you declare an array with an explicit size, WMI stores the size as a qualifier, and treats the size as the suggested maximum size. However, WMI can expand the size if necessary. Changing the explicit size has no effect on the actual data.

-   Arrays are initialized by specifying values of the appropriate type in a comma-separated list.

    ``` syntax
    Class ArrayDataSample2
    {
        [key] string s;
        string strArray2[] = {"hello", "there"};
        sint32 dwArray[] = {1,2,3};
    };
    ```

-   An array of references is declared as an array of object path strings.

    When declaring an object path string, do not place white space between the elements of the object path. The following example describes how to declare an object path reference.

    ``` syntax
    Class ClassWithRefArray
        { 
        [key] string s; 
        object ref refArray[]; 
        };

    instance of ClassWithRefArray
        {
        s = 23;
        refArray = {"Disk.Name=\"C:\"", "Disk.Name=\"E:\""};
        };
    ```

-   You can use an array as a parameter for a method, but not as a return value for an input or input-output parameter.
-   All elements in an array are created as values of the same type.

    If the elements of an array are of the **object** type, then you can place any kind of object in the array. On the other hand, if you declare a specific type of object, then WMI allows only objects of that class or subclass in the array. The following examples show array declarations that includes using the **object** type.

    ``` syntax
    Class EmbedClass
    {
        [key] sint32 PropOfClass;
    };

    Class ArrayDataClass
    {
        [key] string s;
        string strArray1[];
        string strArray2[] = {"hello", "there"};
        sint32 dwArray[] = {1,2,3};
        EmbedClass objArray[];
    };

    instance of ArrayDataClass
    { 
        s = "keyStuff";
        strArray1 = { "1.2.3.4", "1.2.3.5", "1.2.3.7"};
        strArray2 = 
            {
                "SELECT * FROM RegistryKeyChangeEvent",
                "SELECT * FROM RegistryValueChangeEvent",
                "SELECT * FROM RegistryTreeChangeEvent"
            };
        dwArray  = { 1,2,3,5,6 };
        objArray = {
                       instance of EmbedClass{PropOfClass=3;},
                       instance of EmbedClass{PropOfClass=4;}
                   };
    };
    ```

 

 



