---
description: Creating a derived class in WMI is very similar to creating a base class. As with a base class, you must first define the derived class and then register the derived class with WMI.
ms.assetid: 8dd483b8-8bc2-4a5c-b981-6c2ffaccdb95
ms.tgt_platform: multiple
title: Creating a WMI Derived Class
ms.topic: article
ms.date: 05/31/2018
---

# Creating a WMI Derived Class

Creating a derived class in WMI is very similar to creating a base class. As with a base class, you must first define the derived class and then register the derived class with WMI. The main difference is that you must first locate the parent class from which you wish to derive. For more information, see [Writing a Class Provider](writing-a-class-provider.md) and [Writing an Instance Provider](writing-an-instance-provider.md).

The recommended way to create classes for a provider is in Managed Object Format (MOF) files. Several derived classes that are related to each other should be grouped into a MOF file, along with any base classes from which they derive properties or methods. If you place each class in a separate MOF file then each file must be compiled before the provider can work properly.

After you create your class, you must delete all instances of your class before you can perform any of the following activities on your derived class:

-   Change the parent class of your derived class.
-   Add or remove properties.
-   Change property types.
-   Add or remove [**Key**](key-qualifier.md) or **Indexed** qualifiers.
-   Add or remove [**Singleton**](standard-wmi-qualifiers.md), **Dynamic**, or [**Abstract**](standard-qualifiers.md) qualifiers.

> [!Note]  
> To add, remove, or modify a property or qualifier, call [**IWbemServices::PutClass**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putclass) or [**SWbemObject.Put\_**](swbemobject-put-.md) and set the flag parameter to "force mode". The [**Abstract**](standard-qualifiers.md) qualifier can be used only if the parent class is abstract.

 

When you declare your derived class, observe the following rules and restrictions:

-   The parent class of the derived class must already exist.

    The declaration of the parent class can appear in the same MOF file as the derived class or in a different file. If the parent class is unknown, the compiler generates a run-time error.

-   A derived class can have only a single parent class.

    WMI does not support multiple inheritance. However, a parent class can have many derived classes.

-   You can define indices for derived classes, but WMI does not use these indices.

    Therefore, specifying an index on a derived class does not improve the performance of queries for instances of the derived class. You can improve the performance of a query on a derived class by specifying indexed properties for the parent class of the derived class.

-   Derived class definitions can be more complex, and can include such features as aliases, qualifiers, and qualifier flavors.

    For more information, see [Creating an Alias](creating-an-alias.md) and [Adding a Qualifier](adding-a-qualifier.md).

-   If you wish to change a qualifier, change the default value of a base class property, or more strongly type a reference or embedded object property of a base class, you must declare the entire base class again.
-   The maximum number of properties you can define in a WMI class is 1024.

> [!Note]  
> Classes cannot be changed during execution of providers. You must stop the activity, change the class, and then restart the Windows Management service. Detecting a class change is currently not possible.

 

As with the base class, the most common use of this technique will be by client applications. However, a provider can also create a derived class. For more information, see [Creating a Base Class](creating-a-base-class.md) and [Writing a Class Provider](writing-a-class-provider.md).

The code example in this topic requires the following \#include statement to compile correctly.


```C++
#include <wbemidl.h>
```



The following procedure describes how to create a derived class using C++.

**To create a derived class using C++**

1.  Locate the base class with a call to [**IWbemServices::GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject).

    The following code example shows how to locate the Example base class.

    ```C++
    // The pSv variable is of type IWbemServices *

    IWbemClassObject *pNewDerivedClass = 0;
    IWbemClassObject *pExampleClass = 0;
    IWbemContext *pCtx = 0;
    IWbemCallResult *pResult = 0;

    BSTR PathToClass = SysAllocString(L"Example");
    HRESULT hRes = pSvc->GetObject(PathToClass, 0, pCtx, &pExampleClass, &pResult);
    SysFreeString(PathToClass);
    ```

    

2.  Create a derived object from the base class with a call to [**IWbemClassObject::SpawnDerivedClass**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-spawnderivedclass).

    The following code example shows how to create a derived class object.

    ```C++
    pExampleClass->SpawnDerivedClass(0, &pNewDerivedClass);
    pExampleClass->Release();  // Don't need the parent class any more
    ```

    

3.  Establish a name for the class by setting the **\_\_CLASS** system property with a call to the [**IWbemClassObject::Put**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-put) method.

    The following code example shows how to assign a name to the derived class.

    ```C++
    VARIANT v;
    VariantInit(&v);

    V_VT(&v) = VT_BSTR;
    V_BSTR(&v) = SysAllocString(L"Example2");
    BSTR Class = SysAllocString(L"__CLASS");
    pNewDerivedClass->Put(Class, 0, &v, 0);
    SysFreeString(Class);
    VariantClear(&v);
    ```

    

4.  Create additional properties with [**IWbemClassObject::Put**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-put).

    The following code example shows how to create additional properties.

    ```C++
    BSTR OtherProp = SysAllocString(L"OtherInfo2");
    pNewDerivedClass->Put(OtherProp, 0, NULL, CIM_STRING); 
    SysFreeString(OtherProp);
    ```

    

5.  Save the new class by calling [**IWbemServices::PutClass**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putclass).

    The following code example shows how to save the new derived class.

    ```C++
    hRes = pSvc->PutClass(pNewDerivedClass, 0, pCtx, &pResult);
    pNewDerivedClass->Release();
    ```

    

The following code example combines the code examples discussed in the previous procedure to describe how to create a derived class using the WMI API.


```C++
void CreateDerivedClass(IWbemServices *pSvc)
{
  IWbemClassObject *pNewDerivedClass = 0;
  IWbemClassObject *pExampleClass = 0;
  IWbemContext *pCtx = 0;
  IWbemCallResult *pResult = 0;

  BSTR PathToClass = SysAllocString(L"Example");
  HRESULT hRes = pSvc->GetObject(PathToClass, 0, pCtx, 
    &pExampleClass, &pResult);
  SysFreeString(PathToClass);

  if (hRes != 0)
    return;

  pExampleClass->SpawnDerivedClass(0, &pNewDerivedClass);
  pExampleClass->Release();  // The parent class is no longer needed

  VARIANT v;
  VariantInit(&v);

  // Create the class name.
  // =====================

  V_VT(&v) = VT_BSTR;
  V_BSTR(&v) = SysAllocString(L"Example2");
  BSTR Class = SysAllocString(L"__CLASS");
  pNewDerivedClass->Put(Class, 0, &v, 0);
  SysFreeString(Class);
  VariantClear(&v);

  // Create another property.
  // =======================
  BSTR OtherProp = SysAllocString(L"OtherInfo2");
  // No default value
  pNewDerivedClass->Put(OtherProp, 0, NULL, CIM_STRING); 
  SysFreeString(OtherProp);
  
  // Register the class with WMI. 
  // ============================
  hRes = pSvc->PutClass(pNewDerivedClass, 0, pCtx, &pResult);
  pNewDerivedClass->Release();
}
```



The following procedure describes how to define a derived class using MOF code.

**To define a derived class using MOF code**

1.  Define your derived class with the **Class** keyword, followed by the name of your derived class, and the name of the parent class separated by a colon.

    The following code example describes an implementation of a derived class.

    ``` syntax
    class MyClass 
    {
        [key] string   strProp;
        sint32   dwProp1;
        uint32       dwProp2;
    };

    class MyDerivedClass : MyClass
    {
        string   strDerivedProp;
        sint32   dwDerivedProp;
    };
    ```

2.  When complete, compile your MOF code with the MOF compiler.

    For more information, see [Compiling MOF Files](compiling-mof-files.md).

## Related topics

<dl> <dt>

[Creating a Class](creating-a-class.md)
</dt> </dl>

 

 



