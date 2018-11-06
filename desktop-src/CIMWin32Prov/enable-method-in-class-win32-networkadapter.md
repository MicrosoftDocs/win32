---
Description: Enables the network adapter.
ms.assetid: ceb71e1b-5107-420f-a677-814307340469
ms.tgt_platform: multiple
title: Enable method of the Win32_NetworkAdapter class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkAdapter.Enable
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Enable method of the Win32\_NetworkAdapter class

The **Enable** method enables the network adapter.

## Syntax


```mof
uint32 Enable();
```



## Parameters

This method has no parameters.

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

You may experience difficulty using this method if your application does not administrator access privilidges.

## Examples

The following Visual Basic Script example enables the first network adapter and shows the status of the **NetEnabled** property. For more information, see [**SWbemObjectSet.ItemIndex**](https://msdn.microsoft.com/library/aa826600).


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:\\" & _
    strComputer & "\root\cimv2")

set colAdapters = _
    objWMIService.Execquery_
        ("Select * from Win32_NetworkAdapter Where NetEnabled=False")
For Each Adapter in colAdapters
    WScript.Echo Adapter.DeviceId & "    " & Adapter.Name
Next
errReturn = colAdapters.ItemIndex(0).Enable()
If errReturn <> 0 Then
    WScript.Echo "Enable Network adapter failed for adapter= "_
        & colAdapters.ItemIndex(0).DeviceId
Else 
    WScript.Echo "Enable Network adapter succeeded for adapter= "_
        & colAdapters.ItemIndex(0).DeviceId 
End If 
WScript.Echo "NetEnabled= " & colAdapters.ItemIndex(0).NetEnabled
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_NetworkAdapter**](win32-networkadapter.md)
</dt> <dt>

[WMI Tasks: Networking](https://msdn.microsoft.com/library/aa394595)
</dt> <dt>

[IPv6 and IPv4 Support in WMI](https://msdn.microsoft.com/library/aa822883)
</dt> </dl>

 

 




