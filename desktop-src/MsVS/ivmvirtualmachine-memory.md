---
title: IVMVirtualMachine Memory property
description: The Memory property contains the quantity, in megabytes, of physical RAM in the virtual machine.
ms.assetid: f215b0d3-866a-433e-b14e-44d12eb92396
keywords:
- Memory property Virtual Server
- Memory property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , Memory property
- Memory property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , Memory property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Memory
- IVMVirtualMachine.get_Memory
- IVMVirtualMachine.put_Memory
- VMVirtualMachine.Memory
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualMachine::Memory property

The **Memory** property contains the quantity, in megabytes, of physical RAM in the virtual machine.

This property is read/write.

## Syntax


```C++
HRESULT put_Memory(
  [in]  long megabytesOfMemory
);

HRESULT get_Memory(
  [out] long *megabytesOfMemory
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
<td><pre><code>VMVirtualMachine.Memory( _
  ByRef megabytesOfMemory, _
  ByVal megabytesOfMemory _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The quantity, in megabytes, of physical RAM in the virtual machine.

This property value is read/write.

## Error codes



| Name                                                                                               | Meaning                                                                       |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                   | The operation was successful.<br/>                                      |
| <dl> <dt>E\_POINTER</dt> </dl>              | The *megabytesOfMemory* parameter is **NULL**.<br/>                     |
| <dl> <dt>E\_INVALIDARG</dt> </dl>           | The *megabytesOfMemory* parameter is not valid or is out of range.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>      | The configuration is unknown.<br/>                                      |
| <dl> <dt>VM\_E\_PREF\_NOT\_FOUND</dt> </dl> | The preference was not found.<br/>                                      |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>      | An unexpected error has occurred.<br/>                                  |



## Remarks

The amount of physical RAM in a virtual machine must be at least 4 MB. The upper limit on memory depends on the host configuration, but can be at most 3,712 MB.

You cannot set this property if the virtual machine is running or saved.

## Examples

The following example displays the **Memory** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Memory: " & objVM.Memory
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

 

 





