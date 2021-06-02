---
description: The SWbemRefresher object is a container object that can refresh the data for all the objects added to it. The set of added objects, each item represented by an SWbemRefreshableItem instance can be treated as a collection and enumerated.
ms.assetid: cc5872a1-932b-4b68-9f5e-a91d35c8e117
ms.tgt_platform: multiple
title: SWbemRefresher object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemRefresher
- ISWbemRefresher
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemRefresher object

The **SWbemRefresher** object is a container object that can refresh the data for all the objects that are added to it. Single instances and instance enumerators can be added or removed from the container. The set of added objects, each item represented by an [**SWbemRefreshableItem**](swbemrefreshableitem.md) instance, can be treated as a collection and enumerated. WMI instances from any class can be added to the **SWbemRefresher** object. Even if the provider for the instance data is not a high-performance provider, the refresher object can still update the data on the [**Refresh**](swbemrefresher-refresh.md) call. If the data is supplied through a high-performance provider and the [**AutoReconnect**](swbemrefresher-autoreconnect.md) property is **TRUE**, then the **SWbemRefresher** object attempts to reestablish a broken connection to the data provider. This object can be created by the VBScript **CreateObject** call.

The refresh operation can be carried out by calling either the [**SWbemRefresher.Refresh**](swbemrefresher-refresh.md) method or the [**SWbemObjectEx.Refresh\_**](swbemobjectex-refresh-.md) method.

## Members

The **SWbemRefresher** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemRefresher** object has these methods.



| Method                                        | Description                                                                                           |
|:----------------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**Add**](swbemrefresher-add.md)             | Adds a new refreshable object to the collection in the refresher object.<br/>                   |
| [**AddEnum**](swbemrefresher-addenum.md)     | Adds a new enumerator to the refresher object.<br/>                                             |
| [**DeleteAll**](swbemrefresher-deleteall.md) | Removes all items from the collection in the refresher object.<br/>                             |
| [**Item**](swbemrefresher-item.md)           | Returns a specified refresher item from the collection.<br/>                                    |
| [**Refresh**](swbemrefresher-refresh.md)     | Updates all the items that are contained in the refresher object.<br/>                          |
| [**Remove**](swbemrefresher-remove.md)       | Removes the refresher item object or object set with a specified index from the refresher.<br/> |



 

### Properties

The **SWbemRefresher** object has these properties.



| Property                                                         | Access type          | Description                                                                                                           |
|:-----------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**AutoReconnect**](swbemrefresher-autoreconnect.md)<br/> | Read-only<br/> | Indicates whether the refresher automatically reconnects to a remote provider if the connection is broken.<br/> |
| [**Count**](swbemrefresher-count.md)<br/>                 | Read-only<br/> | Contains the number of items in the refresher object.<br/>                                                      |



 

## Examples

The following example illustrates creating an **SWbemRefresher** object, using the [**Add**](swbemrefresher-add.md) and [**AddEnum**](swbemrefresher-addenum.md) methods to store a single instance and an enumeration instance, the refreshing of the data, and using the Item property to obtain the [**SWbemRefreshableItem**](swbemrefreshableitem.md) objects.


```VB
' Get namespace connections
set objServicesCimv2 = GetObject("winmgmts:root\cimv2")
set objServicesDefault = GetObject("winmgmts:root\default")

' Create a refresher object
set objRefresher = CreateObject("WbemScripting.SWbemRefresher")

' Add a single object (SWbemObjectEx) to the refresher. The "@"
' is used because _CIMOMIdentification is a singleton class- only 
' one instance exists. Note that the
' SWbemRefreshableItem.Object property must 
' be specified or the SWbemRefresher.Refresh call will fail.

set objRefreshableItem1 = objRefresher. _
    Add (objServicesDefault, "__CIMOMIdentification=@").Object

' Add an enumerator (SWbemObjectSet object)
' to the refresher. Note that the
' SWbemRefreshableItem.ObjectSet property
' must be specified or the SWbemRefresher.Refresh call will fail. 
set objRefreshableItem2 = objRefresher. _
    AddEnum (objServicesCimv2, "Win32_Process").ObjectSet

' Display number of items in refresher and update the data.
MsgBox "Number of items in refresher = " & objRefresher.Count
objRefresher.Refresh

' Iterate through the refresher. SWbemRefreshable
' Item.IsSet checks for whether the item is an enumerator.
for each RefreshableItem in objRefresher
 if RefreshableItem.IsSet then  
    MsgBox "Item with index " & RefreshableItem.Index &_
    " is an enumerator containing "_
    & RefreshableItem.ObjectSet.Count & " processes"
 else  
      MsgBox "Item with index " & RefreshableItem.Index _
          & " is a single object containing WMI version "_
          &  objRefreshableItem1.VersionCurrentlyRunning
 end if
next
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemRefresher<br/>                                                        |
| IID<br/>                      | IID\_ISWbemRefresher<br/>                                                         |



## See also

<dl> <dt>

[**SWbemRefreshableItem**](swbemrefreshableitem.md)
</dt> <dt>

[**SWbemObjectEx**](swbemobjectex.md)
</dt> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




