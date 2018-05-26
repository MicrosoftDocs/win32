---
title: IVMVirtualMachine ProcessorSpeed property
description: The ProcessorSpeed property contains the speed, in megahertz, of the processor.
ms.assetid: 40e72b52-4cb6-4415-b42e-661a46d68064
keywords:
- ProcessorSpeed property Virtual Server
- ProcessorSpeed property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , ProcessorSpeed property
- ProcessorSpeed property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , ProcessorSpeed property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.ProcessorSpeed
- IVMVirtualMachine.get_ProcessorSpeed
- VMVirtualMachine.ProcessorSpeed
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

# IVMVirtualMachine::ProcessorSpeed property

The **ProcessorSpeed** property contains the speed, in megahertz, of the processor.

This property is read-only.

## Syntax


```C++
HRESULT get_ProcessorSpeed(
  [out] long *processorSpeed
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
<td><pre><code>VMVirtualMachine.ProcessorSpeed( _
  ByRef processorSpeed _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The speed, in megahertz, of the processor.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>               |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *processorSpeed* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>               |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred. <br/>          |



## Examples

The following example displays the **ProcessorSpeed** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Processor speed" & objVM.ProcessorSpeed
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

 

 





