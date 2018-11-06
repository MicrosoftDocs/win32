---
Description: The main purpose of WMI is to provide access to classes and instances that represent objects on your network.
ms.assetid: 8d559eee-3dbf-4132-b1c0-a6925b8feb56
ms.tgt_platform: multiple
title: Calling a WMI Method
ms.topic: article
ms.date: 05/31/2018
---

# Calling a WMI Method

The main purpose of WMI is to provide access to classes and instances that represent objects on your network. These classes and instances are supported by providers. For example, all of the instances that represent standard hardware devices on your enterprise, such as [**Win32\_PhysicalMemory**](https://msdn.microsoft.com/library/aa394347) or [**Win32\_Printer**](https://msdn.microsoft.com/library/aa394363), are supported by the Win32 provider. Similarly, you can access the event log through the Event Log provider, and the registry through the Registry provider.

The methods that WMI implements in interfaces such as [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) or scripting objects such as [**SWbemServices**](swbemservices.md), are primarily for generically obtaining and manipulating data supplied by any provider. For example, use [**SWbemServices.InstancesOf**](swbemservices-instancesof.md) to obtain all the instances of [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) in a subset of enterprise computers. You can then call the Win32 provider method [**GetOwnerSid**](https://msdn.microsoft.com/library/aa390459) on each **Win32\_Process** object.

In the following example, the [**GetOwnerSid**](https://msdn.microsoft.com/library/aa390459) method is called as an automation method on the Process object. A WMI method, such as the [**Path\_**](swbemobject-path-.md) method defined for [**SWbemObject**](swbemobject.md) could also be called on the **Process** object.


```VB
Set ProcessCollection = _
    GetObject("WinMgmts:").InstancesOf("Win32_Process")

For Each Process In ProcessCollection
    SID = Process.GetOwnerSid
Next
```



The actual process of using the WMI methods is identical to using any other Windows COM or automation interface. For more information, see [COM](https://msdn.microsoft.com/en-us/library/ms685978(v=VS.85).aspx) and [Creating a WMI Application or Script](creating-a-wmi-application-or-script.md). For more information about the interfaces that WMI supports, see [COM API for WMI](com-api-for-wmi.md) and [Scripting API for WMI](scripting-api-for-wmi.md).

For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

## Related topics

<dl> <dt>

[Calling a Method](calling-a-method.md)
</dt> </dl>

 

 



