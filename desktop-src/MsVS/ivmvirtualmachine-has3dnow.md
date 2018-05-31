---
title: IVMVirtualMachine Has3DNow property
description: The Has3DNow property contains TRUE if the processor supports the 3DNow instruction set.
ms.assetid: ea9bf1a9-f084-4a0f-af21-0d01d17c1d08
keywords:
- Has3DNow property Virtual Server
- Has3DNow property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , Has3DNow property
- Has3DNow property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , Has3DNow property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Has3DNow
- IVMVirtualMachine.get_Has3DNow
- VMVirtualMachine.Has3DNow
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

# IVMVirtualMachine::Has3DNow property

The **Has3DNow** property contains **TRUE** if the processor supports the 3DNow instruction set.

This property is read-only.

## Syntax


```C++
HRESULT get_Has3DNow(
  [out] VARIANT_BOOL *threeDNowEnabled
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
<td><pre><code>VMVirtualMachine.Has3DNow( _
  ByRef threeDNowEnabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the processor supports the 3DNow instruction set.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                 |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *threeDNowEnabled* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                 |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>             |



## Examples

The following example displays the **Has3DNow** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Has3DNow: " & objVM.Has3DNow
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

 

 





