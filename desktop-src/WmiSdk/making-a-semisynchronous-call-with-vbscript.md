---
description: Provides semisynchronous access functionality and a code example for making a semisynchronous method call.
ms.assetid: 3eae38e8-6a63-45c0-99b0-94e25ddbc5a8
ms.tgt_platform: multiple
title: Making a Semisynchronous Call with VBScript
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Making a Semisynchronous Call with VBScript

Some WMI methods can return large collections, causing scripts to stop responding. In script, semisynchronous access is the default, and Windows Management Instrumentation (WMI) sets **wbemFlagReturnImmediately** for calls that can return large object collections such as the following [**SWbemServices**](swbemservices.md) methods: [**InstancesOf**](swbemservices-instancesof.md), [**SubclassesOf**](swbemservices-subclassesof.md), [**ExecQuery**](swbemservices-execquery.md), [**AssociatorsOf**](swbemservices-associatorsof.md), and [**ReferencesTo**](swbemservices-referencesto.md).

Semisynchronous access that uses **wbemFlagReturnImmediately** set in the *IFlags* parameter is also the default for calls that can return large object sets for the following [**SWbemObject**](swbemobject.md) methods: [**Instances\_**](swbemobject-instances-.md), [**Subclasses\_**](swbemobject-subclasses-.md), [**Associators\_**](swbemobject-associators-.md), and [**References\_**](swbemobject-references-.md).

To reduce the WMI memory resource usage when processing a large collection of objects, include the value of **wbemFlagForwardOnly** in the *IFlags* parameter. Using **wbemFlagForwardOnly** causes WMI to create a forward-only enumerator that does not allow rewinding the collection and accessing items again.

WMI eliminates the memory for each object as the **For Each** statement processes an object. You cannot call the **Count** method for a collection when the **wbemFlagForwardOnly** flag was set on the call that obtained the collection. Note that the *IFlags* parameter has **wbemFlagReturnImmediately** and **wbemFlagForwardOnly** set by default for the [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md) method.

The following procedure describes how to use VBScript to make a semisynchronous call.

**To make a semisynchronous call in VBScript**

1.  Set the *IFlags* parameter to the value of [wbemFlagReturnImmediately](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemflagenum).
2.  Make the normal synchronous call for [**SWbemServices.ExecQuery**](swbemservices-execquery.md) or [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md) with the *iFlags* value.
3.  If you want to treat the objects returned by the call as a collection, use an enumeration syntax such as VBScript **For Each**. As each object is returned, it is processed as the next item in the collection.
4.  Create a forward-only enumerator by combining the value of **wbemFlagReturnImmediately** with the value of **wbemFlagForwardOnly**. The decimal value of this OR operation is 48. These constants are defined in the wbemdisp.tlb type library for Visual Basic. Most scripting languages use the numeric value or define a constant. For more information, see [WbemFlagEnum](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemflagenum).

The following code example shows how to make a semisynchronous method call. For more information, see [Calling a Method](calling-a-method.md).


```VB
wbemFlagReturnImmediately = 16
wbemFlagForwardOnly = 32
IFlags = wbemFlagReturnImmediately + wbemFlagForwardOnly
WScript.Echo IFlags
Set objWMIService = GetObject("winmgmts:root\cimv2")
' Query for all the Win32_Process objects on the 
'     local computer and use forward-only enumerator
Set colProcesses = objWMIService.ExecQuery("SELECT Name FROM Win32_Process",,IFlags)
' Receive each object as it arrives
For Each objProcess in colProcesses
    WScript.Echo objProcess.Name
Next
```



## Related topics

<dl> <dt>

[Calling a Method](calling-a-method.md)
</dt> </dl>

 

 



