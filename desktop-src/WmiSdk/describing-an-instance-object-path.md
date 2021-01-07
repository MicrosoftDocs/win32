---
description: An instance object path describes the location of an instance of a given class within a specific namespace.
ms.assetid: 78a194f0-cd21-4622-9242-be7e430b96c0
ms.tgt_platform: multiple
title: Describing an Instance Object Path
ms.topic: article
ms.date: 05/31/2018
---

# Describing an Instance Object Path

An instance object path describes the location of an instance of a given class within a specific namespace.

You can have several different kinds of instance object paths:

-   Full

    A full instance object path appends the name and value of the key property for the class to a full class object path.

    The following example shows the definition of the full instance object path.

    ``` syntax
    \\Server\Namespace:Class.KeyName="KeyValue"
    ```

-   Relative

    A relative object path refers to an instance located in the current namespace on the current server. The relative path consists of the class name followed by the names and values of the key properties of this instance.

    The following example shows the definition of the relative instance object path.

    ``` syntax
    MyClass.MyProp="e:"
    ```

-   Relative with a single key

    For classes with only one property designated as the key, you can omit the name of the key property.

    The following example shows the definition of the relative instance object path with a single key.

    ``` syntax
    MyClass="e:"
    ```

-   Relative with multiple keys

    Use a comma to distinguish between the keys of an instance with multiple keys.

    The following example shows the definitions of the relative instance object path with multiple keys.

    ``` syntax
    MyOtherClass.FirstKey=1,SecondKey=2
    ```

-   Relative for a singleton class

    The relative object path for a singleton class consists of the class name followed by the "=@" notation.

    The following example shows the definition of the relative instance object path for a singleton class.

    ``` syntax
    MySingletonClass=@
    ```

The following procedure describes how to retrieve a class instance.

**To retrieve a class instance**

1.  Initialize a string that contains the object path with a call to the [**SysAllocString**](/windows/win32/api/oleauto/nf-oleauto-sysallocstring) function.
2.  Initialize an object that will receive the instance.
3.  Retrieve the object with a call to [**IWbemServices::GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) or [**IWbemServices::GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync).

    To use [**GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync), you must implement the [**IWbemSink**](swbemsink.md) interface.

The following \#include statement is required for the code that is listed later in this topic to compile correctly.


```C++
#include <wbemidl.h>
```



The following code example describes how to retrieve a class instance using an object path.


```C++
IWbemServices* pWbemSvcs = 0;

BSTR Path = SysAllocString(L"ComPort=2");    
IWbemClassObject *pComPort = 0;
pWbemSvcs->GetObject(Path, 0, 0, &pComPort, 0);
```



For instances of classes that specify multiple properties as the key, WMI requires no specific ordering of key properties in object paths. You need only specify the value of each of the properties in the object path.

The following code example describes two equivalent key descriptions.

``` syntax
MyClass.IntVal=33,StrVal="AAA"
MyClass.StrVal="AAA",IntVal=33
```

 

 
