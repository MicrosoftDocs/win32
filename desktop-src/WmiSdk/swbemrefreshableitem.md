---
description: Represents a single item in an SWbemRefresher object.
ms.assetid: 6a12c8eb-3ef9-4292-810c-6954294fc8c7
ms.tgt_platform: multiple
title: SWbemRefreshableItem object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemRefreshableItem
- ISWbemRefreshableItem
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemRefreshableItem object

The **SWbemRefreshableItem** object represents a single item in an [**SWbemRefresher**](swbemrefresher.md) object. An **SWbemRefreshableItem** object is obtained through the [**Add**](swbemrefresher-add.md) and [**AddEnum**](swbemrefresher-addenum.md) methods of [**SWbemRefresher**](swbemrefresher.md). This object cannot be created by the VBScript [CreateObject](creating-an-object-using-vbscript.md) call.

## Members

The **SWbemRefreshableItem** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemRefreshableItem** object has these methods.



| Method                                        | Description                                                                                                             |
|:----------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**Remove**](swbemrefreshableitem-remove.md) | Removes the **SWbemRefreshableItem** object from the parent [**SWbemRefresher**](swbemrefresher.md) object.<br/> |



 

### Properties

The **SWbemRefreshableItem** object has these properties.



| Property                                                       | Access type           | Description                                                                                                                          |
|:---------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| [**Index**](swbemrefreshableitem-index.md)<br/>         | Read/write<br/> | Index of the item in its parent [**SWbemRefresher**](swbemrefresher.md) object.<br/>                                          |
| [**IsSet**](swbemrefreshableitem-isset.md)<br/>         | Read/write<br/> | Indicates whether the **SWbemRefreshableItem** object represents a single object or an object set.<br/>                        |
| [**Object**](swbemrefreshableitem-object.md)<br/>       | Read/write<br/> | Represents a single [**SWbemObject**](swbemobject.md) object that is refreshed.<br/>                                          |
| [**ObjectSet**](swbemrefreshableitem-objectset.md)<br/> | Read/write<br/> | Represents the object set to be refreshed.<br/>                                                                                |
| [**Refresher**](swbemrefreshableitem-refresher.md)<br/> | Read-only<br/>  | Represents the parent [**SWbemRefresher**](swbemrefresher.md) object which contains the **SWbemRefreshableItem** object.<br/> |



 

## Remarks

The VBScript method [**GetObject**](https://msdn.microsoft.com/library/ebdktb00(v=VS.71).aspx) cannot be used to create **SWbemRefreshableItem** objects directly.

## Examples

The following script illustrates the creation of an [**SWbemRefresher**](swbemrefresher.md) object and the addition of single object and enumerator **SWbemRefreshableItem** to it.


```VB
' Get some namespace connections
set cimv2 = GetObject("winmgmts:root\cimv2")
set default = GetObject("winmgmts:root\default")    

' Create a refresher
set refresher = CreateObject("WbemScripting.SWbemRefresher")

' Add a single object to the refresher.
' The @ is used because this is a singleton 
' system class so only one instance exists.
set item1 = refresher.Add (default, "__CIMOMIdentification=@").Object
MsgBox "WMI Version " item1
' Add an enumerator to the refresher.
' Note that the SWbemRefreshableItem.ObjectSet 
' property must be used to designate
' this as an object set rather than a single object.
set item2 = refresher.AddEnum (cimv2, "Win32_Process").ObjectSet

' Loop three times, refreshing the items

For I= 1 To 3
MsgBox "Refresh number " & I
refresher.Refresh

' Iterate through the collection of
' processes in item2 with name of wscript
    For each process in item2
        If process.name = "wscript.exe" then
        MsgBox "Process " & process.Name & _
           " Page Faults " & process.PageFaults
        End If
    Next 
Next

' Clear out the refresher
refresher.DeleteAll 

' The following should return 0
MsgBox "Number of items in Refresher after DeleteAll " _
    & refresher.Count
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemRefreshableItem<br/>                                                  |
| IID<br/>                      | IID\_ISWbemRefreshableItem<br/>                                                   |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




