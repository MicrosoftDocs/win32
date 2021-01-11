---
description: Use the Count property of the SWbemObjectSet object to determine how many items are in an SWbemObjectSet collection. This property is read-only.
ms.assetid: ad3d1265-a11e-4962-b1f3-60092d2f79ef
ms.tgt_platform: multiple
title: SWbemObjectSet.Count property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObjectSet.Count
- ISWbemObjectSet.Count
- ISWbemObjectSet.get_Count
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObjectSet.Count property

Use the **Count** property of the [**SWbemObjectSet**](swbemobjectset.md) object to determine how many items are in an **SWbemObjectSet** collection. This property is read-only.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemObjectSet.Count As Integer
```



## Property value

## Remarks

One thing to be careful of when using Count is that WMI does not keep a running tally of the number of items in a collection. If you request Count for a collection, WMI cannot instantly respond with a number; instead, it must literally count the items, enumerating the entire collection. For a collection that has relatively few items, such as services, this enumeration likely takes less than a second. Counting the number of events in an event log collection, however, can take considerably longer.

And then suppose you want to display the property values for every event in the collection. If so, WMI will have to enumerate the entire collection a second time.

> [!Note]  
> If you attempt to get this property from an [**SWbemObjectSet**](swbemobjectset.md) object that is returned from a method where the specified flags are included the wbemFlagForwardOnly flag, you will get an wbemErrFailed error.

 

## Examples

For the most part, the only thing you will ever do with an SWbemObjectSet is enumerate all the objects contained within the collection itself. However, the Count Count that can be useful in system administration scripting. As the name implies, Count tells you the number of items in the collection. For example, this script retrieves a collection of all the services installed on a computer and then echoes the total number of services found:


```VB
strComputer = "."
Set objSWbemServices = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
Set colSWbemObjectSet = objSWbemServices.InstancesOf("Win32_Service")
Wscript.Echo "Services installed on target computer: " & colSWbemObjectSet.Count

```



What makes Count useful is that it can tell you whether a specific instance is available on a computer. For example, this script retrieves a collection of all the services on a computer that have the Name W3SVC. If the Count is 0 (and it is valid for collections to have no instances), that means the W3SVC service is not installed on the computer.


```VB
strComputer = "."
Set objSWbemServices = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
Set colSWbemObjectSet = objSWbemServices.ExecQuery _
    ("SELECT * FROM Win32_Service WHERE Name='w3svc'")
If colSWbemObjectSet.Count = 0 Then
    Wscript.Echo "W3SVC service is not installed on target computer."
Else
    For Each objSWbemObject In colSWbemObjectSet
        ' Perform task on World Wide Web Publishing service.
    Next
End If
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemObjectSet<br/>                                                        |
| IID<br/>                      | IID\_ISWbemObjectSet<br/>                                                         |



 

 




