---
description: Defines the input and output parameters for methods.
ms.assetid: d973feb5-27c4-4d8e-bf1b-0a455afa4375
ms.tgt_platform: multiple
title: '__PARAMETERS class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __PARAMETERS
api_type: 
- Schema
api_location: 
- All
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

To define a method in a user class, a WMI client creates a copy of the **\_\_PARAMETERS** class, and adds a property for each input parameter in a method. If the method contains a return value or output parameters, another copy of **\_\_PARAMETERS** must be created. If the method returns a return value, the client must add a property named **ReturnValue**. The method provider then stores the method parameters with a call to [**IWbemClassObject::PutMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-putmethod).

To invoke a method, a client calls the following in sequence:

1.  [**IWbemClassObject::GetMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-getmethod) to retrieve a copy of the **\_\_PARAMETERS** class that is stored by [**IWbemClassObject::PutMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-putmethod).
2.  [**IWbemClassObject::SpawnInstance**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-spawninstance), and then sets one property for each input parameter to the method.
3.  [**IWbemServices::ExecMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethod) or [**IWbemServices::ExecMethodAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethodasync) to execute the method.

After the method is finished executing, another **\_\_PARAMETERS** class instance may be returned if the method has output parameters or a return value.

-   If the method was invoked by using [**IWbemServices::ExecMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethod), the **\_\_PARAMETERS** instance is returned as an output argument.
-   If the method was invoked by using [**IWbemServices::ExecMethodAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethodasync), the **\_\_PARAMETERS** instance is returned as a parameter to [**IWbemObjectSink::Indicate**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjectsink-indicate).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[**IWbemServices::ExecMethodAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethodasync)
</dt> <dt>

[Calling a Method](calling-a-method.md)
</dt> </dl>

 

 




