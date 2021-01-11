---
description: WMI supplies methods in the COM API and the scripting API to obtain information or manipulate objects in an enterprise system.
ms.assetid: 7a1eda93-014e-4067-b6d0-361a3d2fd1df
ms.tgt_platform: multiple
title: Calling a WMI Method
ms.topic: article
ms.date: 05/31/2018
---

# Calling a WMI Method

WMI supplies methods in the [COM API](com-api-for-wmi.md) and the [scripting API](scripting-api-for-wmi.md) to obtain information or manipulate objects in an enterprise system. For example, the WMI scripting method [**SWbemServices.ExecQuery**](swbemservices-execquery.md) queries for data. Providers also have methods defined in the classes they register. Examples are the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) methods [**Chkdsk**](/windows/desktop/CIMWin32Prov/chkdsk-method-in-class-win32-logicaldisk) and [**ScheduleAutoChk**](/windows/desktop/CIMWin32Prov/scheduleautochk-method-in-class-win32-logicaldisk) supplied by the [Win32 provider](/windows/desktop/CIMWin32Prov/win32-provider).

The following sections are discussed in this topic:

-   [WMI Methods Compared to Provider Methods](#wmi-methods-compared-to-provider-methods)
-   [Method-Calling Modes in WMI](#method-calling-modes-in-wmi)
    -   [Synchronous Mode](#synchronous-mode)
    -   [Asynchronous Mode](#asynchronous-mode)
    -   [Semisynchronous Mode](#semisynchronous-mode)
-   [Related topics](#related-topics)

## WMI Methods Compared to Provider Methods

By using [*WMI method*](gloss-w.md) calls combined with [*provider method*](gloss-p.md) calls, you can retrieve and manipulate information about your enterprise. For more information, see [Calling a WMI Method](calling-a-wmi-method.md) and [Calling a Provider Method](calling-a-provider-method.md).

The methods of the WMI scripting object [**SWbemObject**](swbemobject.md) have a special status because they can apply to any WMI data class. For more information, see [Scripting with SWbemObject](scripting-with-swbemobject.md).

The following code example calls both WMI and provider methods.

The following WMI and provider methods are located in the [Scripting API for WMI](scripting-api-for-wmi.md):

-   **objWMIService.ExecQuery** calls the WMI scripting method [**SWbemServices.ExecQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execquery)
-   **objService.StopService()** calls the provider method [**Win32\_Service.StopService**](/windows/desktop/CIMWin32Prov/stopservice-method-in-class-win32-service)

You can look up the code that may appear in "Return" in the Return Codes section for [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service).


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")

Set colServices = objWMIService.ExecQuery ("Select * from Win32_Service where Name='Alerter'")
For Each objService in colServices
    Return = objService.StopService()
    If Return <> 0 Then
        Wscript.Echo "Failed " &VBNewLine & "Error code = " & Return 
    Else
       WScript.Echo "Succeeded"
    End If
Next
```


```PowerShell

$colServices= Get-WmiObject -Class Win32_Service -Filter 'Name = &quot;Alerter&quot;'
foreach ($objService in $colServices)
{
    $objService.StopService()
}
```





## Method-Calling Modes in WMI

The semisynchronous calling mode usually provides the best balance between security and performance.

For more information about each of the possible modes, see the following:

-   [Synchronous](#synchronous-mode)
-   [Asynchronous](#asynchronous-mode)
-   [Semisynchronous](#semisynchronous-mode)

### Synchronous Mode

Synchronous mode occurs when the program or scripts pauses until the method call returns a [**SWbemObjectSet**](swbemobjectset.md) collection object. WMI builds this collection in memory before returning the collection object to the calling program or script.

Synchronous mode can have an adverse effect of program or script performance on the computer running the program or script. For example, synchronously retrieving thousands of events from the event log can take a long time and use a lot of memory because WMI creates an object from each event and then puts those objects into a collection before passing the collection to the method.

You should only call methods that do not return large data sets in synchronous mode. The following [**SWbemServices**](swbemservices.md) methods can be safely called in synchronous mode:

-   [**SWbemServices.Delete**](swbemservices-delete.md)
-   [**SWbemServices.ExecMethod**](swbemservices-execmethod.md)
-   [**SWbemServices.Get**](swbemservices-get.md)

Any [**SWbemServices**](swbemservices.md) methods without the word, "Async" in the name can be called in synchronous mode by setting the **wbemFlagReturnWhenComplete** value in the *iFlags* parameter.

### Asynchronous Mode

Asynchronous mode occurs when the program or script continues to run after calling the method. WMI returns all objects from the method to a [**SWbemSink**](swbemsink.md) object as each object is created. The calling program or script must have an **SWbemSink** object and an [**SWbemSink.OnObjectReady**](swbemsink-onobjectready.md) event handler to process the returned objects. For more information about creating an event handler for asynchronous mode, see [Receiving a WMI Event](receiving-a-wmi-event.md).

While this mode does not have the performance and resource penalty of synchronous mode, asynchronous mode can create serious security risks because the results stored in the [**SWbemSink**](swbemsink.md) object may not come from the calling program or script. WMI lowers the authentication level on the **SWbemSink** object until the method succeeds. For more information about how to mitigate these security risks, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

Methods appended with the word Async are methods for asynchronous mode. The following methods are asynchronous calls:

-   [**SWbemServices.AssociatorsOfAsync**](swbemservices-associatorsofasync.md)
-   [**SWbemServices.DeleteAsync**](swbemservices-deleteasync.md)
-   [**SWbemServices.ExecMethodAsync**](swbemservices-execmethodasync.md)
-   [**SWbemServices.ExecNotificationQueryAsync**](swbemservices-execnotificationqueryasync.md)
-   [**SWbemServices.ExecQueryAsync**](swbemservices-execqueryasync.md)
-   [**SWbemServices.InstancesOfAsync**](swbemservices-instancesofasync.md)
-   [**SWbemServices.ReferencesToAsync**](swbemservices-referencesto.md)
-   [**SWbemServices.SubclassesOfAsync**](swbemservices-subclassesofasync.md)

For more information about asynchronous mode, see:

-   [Making an Asynchronous Call with C++](making-an-asynchronous-call-with-c--.md)
-   [Making an Asynchronous Call with VBScript](making-an-asynchronous-call-with-vbscript.md)

### Semisynchronous Mode

Semisynchronous mode is similar to asynchronous mode in that the program or script continues to run after calling the method. In semisynchronous mode, WMI retrieves the objects in the background as your script or program continues to run. WMI returns each object returned to the calling method right after the object is created.

Because WMI manages the object, semisynchronous mode is more secure than asynchronous mode. However, if you use semisynchronous mode with more than 1,000 instances, instance retrieval can monopolize the available resources, which can degrade the performance of the program or script and the computer using the program or script. Each object takes up the necessary resources until the memory is released.

To work around this condition, you can call the method with the *iFlags* parameter set with the **wbemFlagForwardOnly** and **wbemFlagReturnImmediately** flags to instruct WMI to return a forward-only [**SWbemObjectSet**](swbemobjectset.md). A forward-only **SWbemObjectSet** eliminates the performance problem caused by a large data set by releasing the memory after the object is enumerated.

Any [**SWbemServices**](swbemservices.md) method that cannot be called in either synchronous or asynchronous mode is called in semisynchronous mode.

The following methods are called in semisynchronous mode:

-   [**SWbemServices.AssociatorsOf**](swbemservices-associatorsof.md)
-   [**SWbemServices.Delete**](swbemservices-delete.md)
-   [**SWbemServices.ExecMethod**](swbemservices-execmethod.md)
-   [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md)
-   [**SWbemServices.ExecQuery**](swbemservices-execquery.md)
-   [**SWbemServices.Get**](swbemservices-get.md)
-   [**SWbemServices.InstancesOf**](swbemservices-instancesof.md)
-   [**SWbemServices.ReferencesTo**](swbemservices-referencesto.md)
-   [**SWbemServices.SubclassesOf**](swbemservices-subclassesof.md)
-   [**SWbemServices.Put**](swbemservicesex-put.md)

For more information about semisynchronous mode, see [Making a Semisynchronous Call with C++](making-a-semisynchronous-call-with-c--.md) and [Making a Semisynchronous Call with VBScript](making-a-semisynchronous-call-with-vbscript.md).

## Related topics

<dl> <dt>

[Improving Enumeration Performance](improving-enumeration-performance.md)
</dt> <dt>

[Scripting with SWbemObject](scripting-with-swbemobject.md)
</dt> <dt>

[**WbemFlagEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemflagenum)
</dt> </dl>

 

 
