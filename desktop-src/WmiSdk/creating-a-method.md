---
description: To create a WMI method, define the input and output parameters for the method.
ms.assetid: 71cbecde-33c4-4bf1-9793-bef6d823dcac
ms.tgt_platform: multiple
title: Creating a WMI Method
ms.topic: article
ms.date: 05/31/2018
---

# Creating a WMI Method

To create a WMI method, define the input and output parameters for the method. The input and output parameters are represented by a special WMI system class [**\_\_PARAMETERS**](--parameters.md). For more information, see [Calling a Method](calling-a-method.md) and [Writing a Method Provider](writing-a-method-provider.md).

The following sections are discussed in this topic:

-   [Creating a WMI Class Method in MOF](#creating-a-wmi-class-method-in-mof)
-   [Creating a WMI Class Method in C++](#creating-a-wmi-class-method-in-c)
-   [Related topics](#related-topics)

## Creating a WMI Class Method in MOF

In WMI, provider methods are generally distinct actions related to the object that the class represents. Rather than change the value of a property to execute an action, a method should be created. For example, you can enable or disable a network information center (NIC) that is represented by [**Win32\_NetworkAdapter**](/windows/desktop/CIMWin32Prov/win32-networkadapter) by using the [**Enable**](/windows/desktop/CIMWin32Prov/enable-method-in-class-win32-networkadapter) and [**Disable**](/windows/desktop/CIMWin32Prov/disable-method-in-class-win32-networkadapter) methods. While these actions can be represented as a read/write property, the recommended design is to create a method. Alternatively, if you want to make a state or value visible for the class, then the recommended approach is to create a read/write property rather than a method. In **Win32\_NetworkAdapter**, the **NetEnabled** property makes the state of the adapter visible but changes between states are executed by the **Enable** or **Disable** methods.

Class declarations can include the declaration of one or more methods. You can either choose to inherit the methods of a parent class, or implement your own. If you choose to implement your own methods, you must declare the method and mark the method with specific qualifier tags.

The following procedure describes how to declare a method in a class that does not inherit from a base class.

**To declare a method**

1.  Define the name of your method between the curly braces of a class declaration, followed by any qualifiers.

    The following code example describes the syntax for a method.

    ``` syntax
    [Dynamic, Provider ("ProviderName")]
    class ClassName
    {
        [Implemented] <ReturnType> <MethodName>
            ([ParameterDirection, IDQualifier] 
            <ParameterType> <ParameterName>);
    };
    ```

2.  When finished, insert your Managed Object Format (MOF) code into the WMI repository with a call to the MOF compiler.

    For more information, see [Compiling MOF Files](compiling-mof-files.md).

The following list defines the elements of the method declaration.

<dl> <dt>

<span id="Provider"></span><span id="provider"></span><span id="PROVIDER"></span>[**Provider**](/windows/desktop/api/Provider/nl-provider-provider)
</dt> <dd>

Links a specific provider to your class description. The value of the [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifier is the name of the provider, which tells WMI where the code that supports your method resides. A provider should also mark with the **Dynamic** qualifier any class that has dynamic instances. In contrast, do not use the **Dynamic** qualifier to mark a class that contains a static instance with **Implemented** methods.

</dd> <dt>

<span id="Implemented"></span><span id="implemented"></span><span id="IMPLEMENTED"></span>**Implemented**
</dt> <dd>

Declares that you will implement a method, rather than inherit the method implementation from the parent class. By default, WMI propagates the implementation of the parent class to a derived class unless the derived class provides an implementation. Omitting the **Implemented** qualifier indicates that the method has no implementation in that class. If you redeclare a method without the **Implemented** qualifier, WMI still assumes that you are not going to implement that method, and invokes the parent class method implementation when called. As such, redeclaring a method in a derived class without attaching the **Implemented** qualifier is useful only when you add or remove a qualifier to or from the method.

</dd> <dt>

<span id="ReturnType"></span><span id="returntype"></span><span id="RETURNTYPE"></span>ReturnType
</dt> <dd>

Describes what value the method returns. The return value for a method must be a Boolean, numeric, **CHAR**, **STRING**, [DATETIME](datetime.md), or schema object. You can also declare the return type as [VOID](void.md), indicating that the method returns nothing. However, you cannot declare an array as a return value type.

</dd> <dt>

<span id="MethodName"></span><span id="methodname"></span><span id="METHODNAME"></span>MethodName
</dt> <dd>

Defines the name of the method. Every method must have a unique name. WMI does not allow two methods with the same name and different signatures to exist in one class or within a class hierarchy. As such, you also cannot overload a method.

</dd> <dt>

<span id="ParameterDirection"></span><span id="parameterdirection"></span><span id="PARAMETERDIRECTION"></span>ParameterDirection
</dt> <dd>

Contains qualifiers that describe if a parameter is an input parameter, output parameter, or both. Do not use the same parameter name more than one time as an input parameter or more than one time as an output parameter. If the same parameter name appears with both the [**In**](standard-qualifiers.md) and an **Out** qualifiers, the functionality is conceptually the same as using the **In**, **Out** qualifiers on a single parameter. However, when using separate declarations, the input and output parameters must be exactly the same in all other respects, including the number and type of [**ID**](standard-wmi-qualifiers.md) qualifiers, and the qualifier must be the same and explicitly declared for both. It is strongly recommended to use the **In**, **Out** qualifiers within a single parameter declaration.

</dd> <dt>

<span id="IDQualifier"></span><span id="idqualifier"></span><span id="IDQUALIFIER"></span>**IDQualifier**
</dt> <dd>

Contains the [**ID**](standard-wmi-qualifiers.md) qualifier that uniquely identifies the position of each parameter within the sequence of parameters in the method. By default, the MOF compiler automatically marks parameters with an **ID** qualifier. The compiler marks the first parameter with a value of 0 (zero), the second parameter a value of 1 (one), and so on. If necessary, you can explicitly state the ID sequence in your MOF code.

</dd> <dt>

<span id="ParameterType"></span><span id="parametertype"></span><span id="PARAMETERTYPE"></span>ParameterType
</dt> <dd>

Describes what data type the method can accept. You can define a parameter type as any MOF data value, including an array, schema object, or reference. When using an array as a parameter, use the array as unbound or with an explicit size.

</dd> <dt>

<span id="ParameterName"></span><span id="parametername"></span><span id="PARAMETERNAME"></span>ParameterName
</dt> <dd>

Contains the name of the parameter. You can also choose to define the default value of the parameter at this point. Parameters lacking initial values remain unassigned.

</dd> </dl>

The following code example describes parameter listing and qualifiers.

``` syntax
[Dynamic, Provider ("ProviderX")]
class MyClass
{
    [Implemented] 
    sint32 MyMethod1 ([in, id(0)] sint32 InParam);
    [Implemented] 
    void MyMethod2 ([in, id(0)] sint32 InParam, 
       [out, id(1)] sint32 OutParam);
    [Implemented] 
    sint32 MyMethod3 ([in, out, id(0)] sint32 InOutParam);
};
```

The following code example describes how to use an array in a MOF parameter.

``` syntax
[Dynamic, Provider ("ProviderX")]
class MyClass
{
    [Implemented] 
    sint32 MyMethod1 ([in, id(0)] Win32_LogicalDisk DiskParam[]);
    [Implemented] 
    sint32 MyMethod2 ([in, id(0)] Win32_LogicalDisk DiskParam[32]);
};
```

The following code example describes using a schema object as both a parameter and return value.

``` syntax
[Dynamic, Provider ("ProviderX")]
class MyClass
{
    [Implemented] sint32 MyMethod1 ([in, id(0)] Win32_LogicalDisk 
        DiskParam);
    [Implemented] 
    Win32_LogicalDisk MyMethod2 ([in, id(0)] string DiskVolLabel);
};
```

The following code example describes how to include two references: one to an instance of the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class and the other to an instance of an unknown object type.

``` syntax
[Dynamic, Provider("ProviderX")]
class MyClass
{
    [Implemented] 
    sint32 MyMethod1 ([in, id(0)] Win32_LogicalDisk ref DiskRef);
    [Implemented] 
    sint32 MyMethod2 ([in, id(0)] object ref AnyObject);
};
```

## Creating a WMI Class Method in C++

The following procedure describes how to create a WMI class method programmatically.

**To create a WMI class method programmatically**

1.  Create the class to which the method will belong.

    You must first have a class to place the method in before you create the method.

2.  Retrieve two child classes of the [**\_\_PARAMETERS**](--parameters.md) system class using either [**IWbemServices::GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) or [**GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync).

    Use the first child class to describe the in-parameters, and the second to describe the out-parameters. If necessary, you can perform a single retrieval followed by a call to the [**IWbemClassObject::Clone**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-clone) method.

3.  Write the in-parameters to the first class, and the out-parameters to the second class, using one or more calls to [**IWbemClassObject::Put**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-put).

    When describing parameters to a method, observe the following rules and restrictions:

    -   Treat the \[in, out\] parameters as separate entries, one in the object that contains the in-parameters and one in the object that contains the out-parameters.
    -   Other than the \[in, out\] qualifiers, the remaining qualifiers must be exactly the same.
    -   Specify the [**ID**](standard-wmi-qualifiers.md) qualifiers, starting at 0 (zero), one for each parameter.

        The order of the input or output parameters is established by the value of the [**ID**](standard-wmi-qualifiers.md) qualifier on each parameter. All input arguments must precede any output arguments. Changing the order of method input and output parameters when updating an existing method provider can cause applications that call the method to fail. Add new input parameters at the end of the existing parameters rather than inserting them in the sequence that is already established.

        Make sure to leave no gaps in the [**ID**](standard-wmi-qualifiers.md) qualifier sequence.

    -   Place the return value in the out-parameters class as a property named **ReturnValue**.

        This identifies the property as the return value of the method. The CIM type of this property is the return type of the method. If the method has a return type of void, then do not have a **ReturnValue** property at all. Also, the **ReturnValue** property cannot have an [**ID**](standard-wmi-qualifiers.md) qualifier like the arguments of the method. Assigning an **ID** qualifier to the **ReturnValue** property produces a WMI error.

    -   Express any default parameter values for the property in the class.

4.  Place both [**\_\_PARAMETERS**](--parameters.md) objects into the parent class with a call to [**IWbemClassObject::PutMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-putmethod).

    A single call to [**PutMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-putmethod) can place both [**\_\_PARAMETERS**](--parameters.md) objects into the class.

## Related topics

<dl> <dt>

[Creating a Class](creating-a-class.md)
</dt> </dl>

 

 
