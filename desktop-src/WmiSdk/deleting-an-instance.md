---
description: Deleting an instance is the most common delete command you are likely to perform in WMI.
ms.assetid: 95ba3e9c-1397-41fe-a080-c03a98aafd42
ms.tgt_platform: multiple
title: Deleting an Instance
ms.topic: article
ms.date: 05/31/2018
---

# Deleting an Instance

Deleting an instance is the most common delete command you are likely to perform in WMI. Like deleting a class, the actual command is fairly simple. However, WMI performs quite differently depending on the type of instance you are deleting. If the instance is static, WMI simply deletes the instance from the WMI repository. For information about removing classes and instances from the WMI repository, see the [**pragma deleteclass**](pragma-deleteclass.md) preprocessor command.

If the instance is dynamic, WMI must call [**IWbemServices::DeleteInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstanceasync) on the providers that are responsible for the following classes:

-   The class that owns the instance.
-   Every parent class of the class that owns the instance.
-   Every subclass of the class that owns the instance.

The success of the deletion depends on the topmost nonabstract class for the original instance. If the provider for any topmost nonabstract class succeeds in completing the deletion, the operation succeeds. For more information, see the Remarks section of [**IWbemServices::DeleteInstance**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstance).

The [COM API for WMI](com-api-for-wmi.md) has different methods for deleting an instance and deleting an object.

The following procedure describes how to use C++ to delete an instance of a base class or derived class.

**To delete an instance of a base class or derived class using C++**

-   Call either the [**IWbemServices::DeleteInstance**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstance) or [**IWbemServices::DeleteInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstanceasync) methods.

    As the name suggests, [**DeleteInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstanceasync) deletes an instance asynchronously while [**DeleteInstance**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstance) deletes an instance synchronously. To use **DeleteInstanceAsync**, you must also implement an [**IWbemObjectSink**](iwbemobjectsink.md) object.

> [!Note]  
> Because the callback to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

The [Scripting API for WMI](scripting-api-for-wmi.md) uses the same methods to delete either a class object or an instance.

The following procedure describes how to use VBScript to delete an instance of a base class or derived class.

**To delete an instance of a base class or derived class using VBScript**

-   Call either the [**SWbemObject.Delete\_**](swbemobject-delete-.md) or [**SWbemObject.DeleteAsync\_**](swbemobject-deleteasync-.md) methods.

    As the name suggests, [**Delete\_**](swbemobject-delete-.md) deletes an instance synchronously while [**DeleteAsync\_**](swbemobject-deleteasync-.md) deletes an instance asynchronously. For more information about deleting an instance asynchronously, see [Calling a Method](calling-a-method.md).

    The following example describes how to delete an instance using VBScript.

    ```VB
    Dim service

    Set service = GetObject("winmgmts:{impersonationLevel=impersonate}") 

    Set objwbemobject= service.get("")

    objwbemobject.Path_.Class = "MyNewClass" 
    objwbemobject.put_
    service.delete  "MyNewClass"
    ```

    

> [!Note]  
> Because the callback to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

 

 



