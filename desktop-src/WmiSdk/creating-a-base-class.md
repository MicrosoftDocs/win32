---
Description: The recommended way to create a new WMI base class for a WMI provider is in a Managed Object Format (MOF) file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d46060aa-77c3-4f51-b4a7-2c3612f2bc5c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Creating a WMI Base Class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating a WMI Base Class

The recommended way to create a new WMI base class for a WMI provider is in a Managed Object Format (MOF) file. You can also create a base class using the [COM API for WMI](com-api-for-wmi.md). While you can create a base or derived class in script, without a provider supplying data to the class and its subclasses, the class is not useful.

The following sections are discussed in this topic:

-   [Creating a Base Class Using MOF](#creating-a-base-class-using-mof)
-   [Creating a Base Class with C++](#creating-a-base-class-with-c)
-   [Related topics](#related-topics)

## Creating a Base Class Using MOF

WMI classes usually rely on inheritance. Before creating a base class, check the Common Information Model (CIM) classes available from the Distributed Management Task Force ([DMTF](Http://go.microsoft.com/fwlink/p/?linkid=84401)).

If many derived classes will use the same properties, put these properties and methods in your base class. The maximum number of properties you can define in a WMI class is 1024.

When creating a base class, observe the following list of guidelines for class names:

-   Use both uppercase and lowercase letters.
-   Begin a class name with a letter.
-   Do not use either a leading or trailing underscore.
-   Define all remaining characters as letters, digits, or underscores.
-   Use a consistent naming convention.

    While not necessary, a good naming convention for a class is two components joined by an underscore. When possible, a vendor name should make up the first half of the name, and a descriptive class name should be the second part.

> [!Note]  
> Classes cannot be changed during execution of providers. You must stop the activity, change the class, and then restart the Windows Management service. Detecting a class change is currently not possible.

 

In MOF, create a base class by naming it with the **class** keyword, but not indicating a parent class.

**To create a base class using MOF code**

1.  Use the **class** keyword with the name of the new class, followed by a pair of curly braces and a semicolon. Add properties and methods for the class between the curly braces. The following code example is provided.

    The following code example shows how a base class should be defined.

    ``` syntax
    class MyClass_BaseDisk
    {
    };
    ```

    The following code example shows an incorrect definition of a base class.

    ``` syntax
    class MyClass_BaseDisk : CIM_LogicalDisk
    {
    };
    ```

2.  Add any class [*qualifiers*](gloss-q.md#wmi-gloss-qualifier) before the class keyword to modify the way the class is used. Place the qualifiers between square brackets. For more information about qualifiers for modifying classes, see [WMI Qualifiers](wmi-qualifiers.md). Use the **Abstract** qualifier to indicate that you cannot create an instance of this class directly. Abstract classes are often used to define properties or methods that will be used by several derived classes. For more information, see [Creating a Derived Class](creating-a-derived-class.md).

    The following code example defines the class as abstract and defines the provider that will supply the data. The **ToSubClass** qualifier [*flavor*](gloss-f.md#wmi-gloss-flavor) indicates that the information in the **Provider** qualifier is inherited by derived classes.

    ``` syntax
    [Abstract, Provider("MyProvider") : ToSubClass]
    class MyClass_BaseDisk
    {
    };
    ```

3.  Add the properties and methods for the class inside square brackets before the property or method name. For more information, see [Adding a Property](adding-a-property.md) and [Creating a Method](creating-a-method.md). You can modify these properties and methods using MOF qualifiers. For more information, see [Adding a Qualifier](adding-a-qualifier.md).

    The following code example shows how to modify properties and methods with MOF qualifiers.

    ``` syntax
    [read : ToSubClass, key : ToSubClass ] string DeviceID;
      [read : ToSubClass] uint32 State;
      [read : ToSubclass, write : ToSubClass] uint64 LimitUsers;
    ```

4.  Save the MOF file with an extension of .mof.
5.  Register the class with WMI by running [**Mofcomp.exe**](mofcomp.md) on the file.

    **mofcomp.exe** *newmof.mof*

    If you do not use the **-N** switch or the preprocessor command \#[**pragma namespace**](pragma-namespace.md) to specify a namespace, the compiled MOF classes will be stored in the root\\default namespace in the repository. For more information, see [**mofcomp**](mofcomp.md).

The following code example combines the MOF code examples discussed in the previous procedure and shows how to create a base class in the root\\cimv2 namespace using MOF.

``` syntax
#pragma namespace("\\\\.\\Root\\cimv2")

[Abstract, Provider("MyProvider") : ToSubClass]
class MyClass_BaseDisk
{
  [read : ToSubClass, key : ToSubClass ] string DeviceID;
  [read : ToSubClass] uint32 State;
  [read : ToSubClass, write : ToSubClass] uint64 LimitUsers;
};
```

For more information, see [Creating a Derived Class](creating-a-derived-class.md) for an example of a dynamic class derived from this base class.

## Creating a Base Class with C++

Creating a base class using the WMI API is mainly a series of Put commands that define the class and register the class with WMI. The main purpose of this API is to enable client applications to create base classes. However, you can also have a provider use this API to create a base class. For example, if you believe that the MOF code for your provider will not be installed properly, you can instruct your provider to automatically create the correct classes in the WMI repository. For more information about providers, see [Writing a Class Provider](writing-a-class-provider.md).

> [!Note]  
> Classes cannot be changed during execution of providers. You must stop the activity, change the class, and then restart the Windows Management service. Detecting a class change is currently not possible.

 

The code requires the following reference to compile correctly.


```C++
#include <wbemidl.h>
```



You can create a new base class programmatically using the [COM API for WMI](com-api-for-wmi.md).

**To create a new base class with the WMI API**

1.  Retrieve a definition for the new class by calling the [**IWbemServices::GetObject**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobject?branch=master) method with the *strObjectPath* parameter set to a **null** value.

    The following code example shows how to retrieve a definition for a new class.

    ```C++
    IWbemServices* pSvc = 0;
    IWbemContext* pCtx = 0;
    IWbemClassObject* pNewClass = 0;
    IWbemCallResult* pResult = 0;
    HRESULT hRes = pSvc->GetObject(0, 0, pCtx, &amp;pNewClass, &amp;pResult);
    ```

    

2.  Establish a name for the class by setting the **\_\_CLASS** system property with a call to the [**IWbemClassObject::Put**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-put?branch=master) method.

    The following code example shows how to name the class by setting the **\_\_CLASS** system property.

    ```C++
    VARIANT v;
    VariantInit(&amp;v);
    V_VT(&amp;v) = VT_BSTR;

    V_BSTR(&amp;v) = SysAllocString(L"Example");
    BSTR Class = SysAllocString(L"__CLASS");
    pNewClass->Put(Class, 0, &amp;v, 0);
    SysFreeString(Class);
    VariantClear(&amp;v);
    ```

    

3.  Create the key property or properties by calling [**IWbemClassObject::Put**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-put?branch=master).

    The following code example describes how to create the [**Index**](swbemrefreshableitem-index.md) property, which is labeled as a key property in Step 4.

    ```C++
      BSTR KeyProp = SysAllocString(L"Index");
      pNewClass->Put(KeyProp, 0, NULL, CIM_STRING);
    ```

    

4.  Attach the [**Key**](standard-qualifiers.md) standard qualifier to the key property by first calling the [**IWbemClassObject::GetPropertyQualifierSet**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-getpropertyqualifierset?branch=master) method and then the [**IWbemQualifierSet::Put**](/windows/win32/Wbemcli/nf-wbemcli-iwbemqualifierset-put?branch=master) method.

    The following code example shows how to attach the [**Key**](standard-qualifiers.md) standard qualifier to the key property.

    ```C++
      IWbemQualifierSet *pQual = 0;
      pNewClass->GetPropertyQualifierSet(KeyProp, &amp;pQual);
      SysFreeString(KeyProp);

      V_VT(&amp;v) = VT_BOOL;
      V_BOOL(&amp;v) = VARIANT_TRUE;
      BSTR Key = SysAllocString(L"Key");

      pQual->Put(Key, &amp;v, 0);   // Flavors not required for Key 
      SysFreeString(Key);

      // No longer need the qualifier set for "Index"
      pQual->Release();   
      VariantClear(&amp;v);
    ```

    

5.  Create other properties of the class with [**IWbemClassObject::Put**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-put?branch=master).

    The following code example describes how to create additional properties.

    ```C++
      V_VT(&amp;v) = VT_BSTR;
      V_BSTR(&amp;v) = SysAllocString(L"<default>");
      BSTR OtherProp = SysAllocString(L"OtherInfo");
      pNewClass->Put(OtherProp, 0, &amp;v, CIM_STRING);
      SysFreeString(OtherProp);
      VariantClear(&amp;v);

      OtherProp = SysAllocString(L"IntVal");
      pNewClass->Put(OtherProp, 0, NULL, CIM_SINT32); // NULL is default
      SysFreeString(OtherProp);
    ```

    

6.  Register the new class by calling [**IWbemServices::PutClass**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putclass?branch=master).

    Because you cannot define keys and indices after you register a new class, ensure that you have defined all of your properties before calling [**PutClass**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putclass?branch=master).

    The following code example describes how to register a new class.

    ```C++
      hRes = pSvc->PutClass(pNewClass, 0, pCtx, &amp;pResult);
      pNewClass->Release();
    ```

    

The following code example combines the code examples discussed in the previous procedure and shows how to create a base class using the WMI API.


```C++
void CreateClass(IWbemServices *pSvc)
{
  IWbemClassObject *pNewClass = 0;
  IWbemContext *pCtx = 0;
  IWbemCallResult *pResult = 0;

  // Get a class definition. 
  // ============================
  HRESULT hRes = pSvc->GetObject(0, 0, pCtx, &amp;pNewClass, &amp;pResult);
  VARIANT v;
  VariantInit(&amp;v);

  // Create the class name.
  // ============================
  V_VT(&amp;v) = VT_BSTR;
  V_BSTR(&amp;v) = SysAllocString(L"Example");
  BSTR Class = SysAllocString(L"__CLASS");
  pNewClass->Put(Class, 0, &amp;v, 0);
  SysFreeString(Class);
  VariantClear(&amp;v);

  // Create the key property. 
  // ============================
  BSTR KeyProp = SysAllocString(L"Index");
  pNewClass->Put(KeyProp, 0, NULL, CIM_STRING);

  // Attach Key qualifier to mark the "Index" property as the key.
  // ============================
  IWbemQualifierSet *pQual = 0;
  pNewClass->GetPropertyQualifierSet(KeyProp, &amp;pQual);
  SysFreeString(KeyProp);

  V_VT(&amp;v) = VT_BOOL;
  V_BOOL(&amp;v) = VARIANT_TRUE;
  BSTR Key = SysAllocString(L"Key");

  pQual->Put(Key, &amp;v, 0);   // Flavors not required for Key 
  SysFreeString(Key);

  // No longer need the qualifier set for "Index"
  pQual->Release();     
  VariantClear(&amp;v);

  // Create other properties.
  // ============================
  V_VT(&amp;v) = VT_BSTR;
  V_BSTR(&amp;v) = SysAllocString(L"<default>");
  BSTR OtherProp = SysAllocString(L"OtherInfo");
  pNewClass->Put(OtherProp, 0, &amp;v, CIM_STRING);
  SysFreeString(OtherProp);
  VariantClear(&amp;v);

  OtherProp = SysAllocString(L"IntVal");
  pNewClass->Put(OtherProp, 0, NULL, CIM_SINT32); // NULL is default
  SysFreeString(OtherProp);
  
  // Register the class with WMI
  // ============================
  hRes = pSvc->PutClass(pNewClass, 0, pCtx, &amp;pResult);
  pNewClass->Release();
}
```



## Related topics

<dl> <dt>

[Creating a Class](creating-a-class.md)
</dt> </dl>

 

 



