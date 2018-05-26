---
title: IVMVirtualMachine ChassisAssetTag property
description: The ChassisAssetTag property contains the chassis asset tag.
ms.assetid: 2858ff38-e5d6-4164-b934-4491234d472d
keywords:
- ChassisAssetTag property Virtual Server
- ChassisAssetTag property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , ChassisAssetTag property
- ChassisAssetTag property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , ChassisAssetTag property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.ChassisAssetTag
- IVMVirtualMachine.get_ChassisAssetTag
- IVMVirtualMachine.put_ChassisAssetTag
- VMVirtualMachine.ChassisAssetTag
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMVirtualMachine::ChassisAssetTag property

The **ChassisAssetTag** property contains the chassis asset tag.

This property is read/write.

## Syntax


```C++
HRESULT put_ChassisAssetTag(
  [in]  BSTR chassisAssetTag
);

HRESULT get_ChassisAssetTag(
  [out] BSTR *chassisAssetTag
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMVirtualMachine.ChassisAssetTag( _
  ByRef chassisAssetTag, _
  ByVal chassisAssetTag _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The chassis asset tag.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                                 |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *chassisAssetTag* parameter is **NULL**.<br/>                                                  |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *chassisAssetTag* parameter is greater than 32 characters, an empty string, or not valid.<br/> |
| <dl> <dt>VM\_E\_VM\_RUNNING</dt> </dl> | The asset tag cannot be set while the virtual machine is running.<br/>                             |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                                                 |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                                                             |



## Remarks

This property will not contain valid information until after the virtual machine has started up for the first time. An empty string will be returned if it is read before the initial startup.

## Examples

The following example displays the **ChassisAssetTag** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
If objVM.ChassisAssetTag = "" Then
  WScript.Echo "Chassis asset tag: [null]"
Else
  WScript.Echo "Chassis asset tag: " & objVM.ChassisAssetTag
End If
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





