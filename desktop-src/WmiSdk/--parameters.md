---
Description: Defines the input and output parameters for methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d973feb5-27c4-4d8e-bf1b-0a455afa4375
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: '\_\_PARAMETERS class'
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# \_\_PARAMETERS class

The **\_\_PARAMETERS** system class is an abstract class that defines the input and output parameters for methods. It is also used to pass input and output parameter values between a WMI client and a method provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract]
class __PARAMETERS
{
};
```

## Members

The **\_\_PARAMETERS** class does not define any members.

## Remarks

To define a method in a user class, a WMI client creates a copy of the **\_\_PARAMETERS** class, and adds a property for each input parameter in a method. If the method contains a return value or output parameters, another copy of **\_\_PARAMETERS** must be created. If the method returns a return value, the client must add a property named **ReturnValue**. The method provider then stores the method parameters with a call to [**IWbemClassObject::PutMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-putmethod?branch=master).

To invoke a method, a client calls the following in sequence:

1.  [**IWbemClassObject::GetMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-getmethod?branch=master) to retrieve a copy of the **\_\_PARAMETERS** class that is stored by [**IWbemClassObject::PutMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-putmethod?branch=master).
2.  [**IWbemClassObject::SpawnInstance**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-spawninstance?branch=master), and then sets one property for each input parameter to the method.
3.  [**IWbemServices::ExecMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethod?branch=master) or [**IWbemServices::ExecMethodAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethodasync?branch=master) to execute the method.

After the method is finished executing, another **\_\_PARAMETERS** class instance may be returned if the method has output parameters or a return value.

-   If the method was invoked by using [**IWbemServices::ExecMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethod?branch=master), the **\_\_PARAMETERS** instance is returned as an output argument.
-   If the method was invoked by using [**IWbemServices::ExecMethodAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethodasync?branch=master), the **\_\_PARAMETERS** instance is returned as a parameter to [**IWbemObjectSink::Indicate**](/windows/win32/Wbemcli/nf-wbemcli-iwbemobjectsink-indicate?branch=master).

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[**IWbemServices::ExecMethodAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethodasync?branch=master)
</dt> <dt>

[Calling a Method](calling-a-method.md)
</dt> </dl>

 

 




