---
title: IVMVirtualMachine ParallelPorts property
description: The ParallelPorts property contains an enumerable collection of parallel ports.
ms.assetid: '551c52b2-5baf-4abc-a5a3-923e0481cfb0'
keywords: ["ParallelPorts property Virtual Server", "ParallelPorts property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , ParallelPorts property", "ParallelPorts property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , ParallelPorts property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.ParallelPorts
- IVMVirtualMachine.get_ParallelPorts
- VMVirtualMachine.ParallelPorts
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::ParallelPorts property

The **ParallelPorts** property contains an enumerable collection of parallel ports.

This property is read-only.

## Syntax


```C++
HRESULT get_ParallelPorts(
  [out] IVMParallelPortCollection **parallelPortCollection
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
<td><pre><code>VMVirtualMachine.ParallelPorts( _
  ByRef parallelPortCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMParallelPortCollection**](ivmparallelportcollection.md) object associated with this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                        |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                       |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *parallelPortCollection* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                       |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                   |



## Examples

The following example displays the number of parallel ports attached to a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set colPars = objVM.ParallelPorts

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Parallel Ports: " & colPars.Count
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





