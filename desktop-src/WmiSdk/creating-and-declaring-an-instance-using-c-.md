---
Description: You can create an instance in C++ through the IWbemServices interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ee54c1ef-bc91-4771-8c11-9ee3aacd8112
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Creating and Declaring an Instance Using C++
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating and Declaring an Instance Using C++

You can create an instance in C++ through the [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) interface.

The code examples in this topic require the following \#include statement to compile correctly.


```C++
#include <wbemidl.h>
```



The following procedure describes how to create an instance of an existing class.

**To create an instance of an existing class**

1.  Retrieve the definition of the existing class by calling the [**IWbemServices::GetObject**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobject?branch=master) or [**IWbemServices::GetObjectAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobjectasync?branch=master) methods.

    The following code example shows how to use the [**GetObject**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobject?branch=master) and [**GetObjectAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobjectasync?branch=master) methods to get a pointer to the [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master) interface that provides access to the class definition.

    ```C++
    // The pSv variable is of type IWbemServices *

    IWbemClassObject *pNewInstance = 0;
    IWbemClassObject *pExampleClass = 0;
    IWbemContext *pCtx = 0;
    IWbemCallResult *pResult = 0;

    BSTR PathToClass = SysAllocString(L"Example");
    HRESULT hRes = pSvc->GetObject(PathToClass, 0, pCtx, 
                  &amp;pExampleClass, &amp;pResult);
    SysFreeString(PathToClass);
    ```

    

2.  Create the new instance by calling the [**IWbemClassObject::SpawnInstance**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-spawninstance?branch=master) method.

    The following code example shows how to create a new instance and then release the class.

    ```C++
    pExampleClass->SpawnInstance(0, &amp;pNewInstance);
    pExampleClass->Release();  // Don't need the class any more
    ```

    

3.  Set values for any properties that do not inherit the values defined for the class by calling the [**IWbemClassObject::Put**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-put?branch=master) method.

    Each instance of a class inherits all of the properties that are defined for the class. However, you can specify different property values if you choose.

    If the existing class has a key property, you should set the property either to **NULL** or a guaranteed unique value. If you set the key to **NULL** and the key is a string, then [**PutInstanceAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync?branch=master) or [**PutInstance**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putinstance?branch=master) internally generates and assigns a GUID to the key. This way, specifying **NULL** for a key property lets you create a unique instance that will not overwrite any previous instance.

    The following code example shows how to set the [**Index**](swbemrefreshableitem-index.md) property value of the example instance class.

    ```C++
    VARIANT v;
    VariantInit(&amp;v);

    V_VT(&amp;v) = VT_BSTR;
    V_BSTR(&amp;v) = SysAllocString(L"IX100");

    BSTR KeyProp = SysAllocString(L"Index");
    pNewInstance->Put(KeyProp, 0, &amp;v, 0);
    SysFreeString(KeyProp);
    VariantClear(&amp;v);
    ```

    

4.  Set the values for any relevant qualifiers through a call to [**IWbemClassObject::GetQualifierSet**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-getqualifierset?branch=master).

    The [**GetQualifierSet**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-getqualifierset?branch=master) method returns a pointer to an [**IWbemQualifierSet**](/windows/win32/Wbemcli/nn-wbemcli-iwbemqualifierset?branch=master) interface, which use to access the qualifiers for a class or instance. You can specify different values for a qualifier defined for the class if the class qualifier flavor is **EnableOverride**. You cannot modify or delete a class qualifier with the flavor set to **DisableOverride**. For more information, see [Qualifier Flavors](qualifier-flavors.md).

    As an option, you can also define additional qualifiers for your instance class. You can define additional qualifiers for the instance or instance property which do not need to appear in the class declaration.

5.  Save the instance by calling the [**IWbemServices::PutInstance**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putinstance?branch=master) or [**IWbemServices::PutInstanceAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync?branch=master) method.

    WMI saves the instance in the current WMI namespace. As such, the full path of the instance is dependent on the namespace, which is typically root\\default. For this code example, the full path name would be \\\\.\\root\\default:Example.Index="IX100".

    The following code example shows how to save an instance.

    ```C++
        hRes = pSvc->PutInstance(pNewInstance, 0, pCtx, &amp;pResult);
        pNewInstance->Release();
    ```

    

Saving the instance to WMI locks down several of the properties of the instance.

Specifically, you cannot perform any of the following operations through the WMI API after an instance exists within the WMI infrastructure:

-   Change the parent class of the class to which the instance belongs.
-   Add or remove properties.
-   Change property types.
-   Add or remove [**Key**](standard-qualifiers.md) or **Indexed** qualifiers.
-   Add or remove [**Singleton**](standard-wmi-qualifiers.md), **Dynamic**, or [**Abstract**](standard-qualifiers.md) qualifiers.

The following code example combines the code examples discussed in the previous procedure to show how to create an instance using the WMI API.


```C++
void CreateInstance (IWbemServices *pSvc)
{
    IWbemClassObject *pNewInstance = 0;
    IWbemClassObject *pExampleClass = 0;
    IWbemContext *pCtx = 0;
    IWbemCallResult *pResult = 0;

    // Get the class definition.
    BSTR PathToClass = SysAllocString(L"Example");
    HRESULT hRes = pSvc->GetObject(PathToClass, 0, pCtx, 
                 &amp;pExampleClass, &amp;pResult);
    SysFreeString(PathToClass);

    if (hRes != 0)
       return;

    // Create a new instance.
    pExampleClass->SpawnInstance(0, &amp;pNewInstance);
    pExampleClass->Release();  // Don't need the class any more

    VARIANT v;
    VariantInit(&amp;v);

    // Set the Index property (the key).
    V_VT(&amp;v) = VT_BSTR;
    V_BSTR(&amp;v) = SysAllocString(L"IX100");

    BSTR KeyProp = SysAllocString(L"Index");
    pNewInstance->Put(KeyProp, 0, &amp;v, 0);
    SysFreeString(KeyProp);
    VariantClear(&amp;v);

    // Set the IntVal property.
    V_VT(&amp;v) = VT_I4;
    V_I4(&amp;v) = 1001;  
    
    BSTR Prop = SysAllocString(L"IntVal");
    pNewInstance->Put(Prop, 0, &amp;v, 0);
    SysFreeString(Prop);
    VariantClear(&amp;v);    
    
    // Other properties acquire the 'default' value specified
    // in the class definition unless otherwise modified here.

    // Write the instance to WMI. 
    hRes = pSvc->PutInstance(pNewInstance, 0, pCtx, &amp;pResult);
    pNewInstance->Release();
}
```



 

 



