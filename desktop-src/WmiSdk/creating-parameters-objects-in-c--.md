---
Description: 'The IWbemServices::ExecMethod or ExecMethodAsync methods require the \_\_PARAMETERS system class as a container in pInParams if the method they are executing has any input arguments.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '17b72ceb-e730-4176-aa4d-189d0b6acc8b'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Creating Parameters Objects in C++
---

# Creating Parameters Objects in C++

The [**IWbemServices::ExecMethod**](iwbemservices-execmethod.md) or [**ExecMethodAsync**](iwbemservices-execmethodasync.md) methods require the [**\_\_PARAMETERS**](--parameters.md) system class as a container in *pInParams* if the method they are executing has any input arguments.

The following procedure describes how to create an instance of the [**\_\_PARAMETERS**](--parameters.md) system class to hold parameter information.

**To create an instance of \_\_PARAMETERS**

1.  Determine the class path for the class containing the method definition.
2.  Using the class path and the [**IWbemServices**](iwbemservices.md) pointer passed in from [**IWbemProviderInit::Initialize**](iwbemproviderinit-initialize.md), call [**IWbemClassObject::GetMethod**](iwbemclassobject-getmethod.md) to retrieve the input and output parameter classes.

    The [**GetMethod**](iwbemclassobject-getmethod.md) method returns an [**IWbemClassObject**](iwbemclassobject.md) pointer for accessing each of these classes.

3.  Using the [**IWbemClassObject**](iwbemclassobject.md) pointer for the output class, call [**IWbemClassObject::SpawnInstance**](iwbemclassobject-spawninstance.md) to create an instance of the class.
4.  Populate the class instance by setting the properties that correspond to the output values and, if there is a return value for the method, the [ReturnValue](creating-a-method.md) property.
5.  Pass the [**\_\_PARAMETERS**](--parameters.md) instance back to the caller through the [**IWbemObjectSink::Indicate**](iwbemobjectsink-indicate.md) method.

After a method provider determines that the input parameters are correct, the method pointed to by *strMethodName* might still pass or fail. Some method providers spawn a second thread to implement the method so that the method's actual success or failure ends up being reported to the caller through [**IWbemObjectSink::SetStatus**](iwbemobjectsink-setstatus.md). Note that **IWbemObjectSink::SetStatus** does not receive the return code of the provider method. However, it receives the return code of the actual call-return mechanism, and is only useful for verifying that the call occurred or that it failed for mechanical reasons.

## Related topics

<dl> <dt>

[Calling a Method](calling-a-method.md)
</dt> <dt>

[**IWbemCallResult::GetResultObject**](iwbemcallresult-getresultobject.md)
</dt> <dt>

[**IWbemServices::ExecMethodAsync**](iwbemservices-execmethodasync.md)
</dt> <dt>

[**IWbemServices::ExecMethod**](iwbemservices-execmethod.md)
</dt> </dl>

 

 



