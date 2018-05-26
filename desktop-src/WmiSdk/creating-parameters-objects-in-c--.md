---
Description: The IWbemServicesExecMethod or ExecMethodAsync methods require the \_\_PARAMETERS system class as a container in pInParams if the method they are executing has any input arguments.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 17b72ceb-e730-4176-aa4d-189d0b6acc8b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Creating Parameters Objects in C++
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating Parameters Objects in C++

The [**IWbemServices::ExecMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethod?branch=master) or [**ExecMethodAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethodasync?branch=master) methods require the [**\_\_PARAMETERS**](--parameters.md) system class as a container in *pInParams* if the method they are executing has any input arguments.

The following procedure describes how to create an instance of the [**\_\_PARAMETERS**](--parameters.md) system class to hold parameter information.

**To create an instance of \_\_PARAMETERS**

1.  Determine the class path for the class containing the method definition.
2.  Using the class path and the [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) pointer passed in from [**IWbemProviderInit::Initialize**](/windows/win32/Wbemprov/nf-wbemprov-iwbemproviderinit-initialize?branch=master), call [**IWbemClassObject::GetMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-getmethod?branch=master) to retrieve the input and output parameter classes.

    The [**GetMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-getmethod?branch=master) method returns an [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master) pointer for accessing each of these classes.

3.  Using the [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master) pointer for the output class, call [**IWbemClassObject::SpawnInstance**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-spawninstance?branch=master) to create an instance of the class.
4.  Populate the class instance by setting the properties that correspond to the output values and, if there is a return value for the method, the [ReturnValue](creating-a-method.md) property.
5.  Pass the [**\_\_PARAMETERS**](--parameters.md) instance back to the caller through the [**IWbemObjectSink::Indicate**](/windows/win32/Wbemcli/nf-wbemcli-iwbemobjectsink-indicate?branch=master) method.

After a method provider determines that the input parameters are correct, the method pointed to by *strMethodName* might still pass or fail. Some method providers spawn a second thread to implement the method so that the method's actual success or failure ends up being reported to the caller through [**IWbemObjectSink::SetStatus**](/windows/win32/Wbemcli/nf-wbemcli-iwbemobjectsink-setstatus?branch=master). Note that **IWbemObjectSink::SetStatus** does not receive the return code of the provider method. However, it receives the return code of the actual call-return mechanism, and is only useful for verifying that the call occurred or that it failed for mechanical reasons.

## Related topics

<dl> <dt>

[Calling a Method](calling-a-method.md)
</dt> <dt>

[**IWbemCallResult::GetResultObject**](/windows/win32/Wbemcli/nf-wbemcli-iwbemcallresult-getresultobject?branch=master)
</dt> <dt>

[**IWbemServices::ExecMethodAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethodasync?branch=master)
</dt> <dt>

[**IWbemServices::ExecMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethod?branch=master)
</dt> </dl>

 

 



