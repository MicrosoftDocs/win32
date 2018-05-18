---
title: IVMVirtualMachine HasMMX property
description: The HasMMX property contains TRUE if the processor supports the MMX instruction set.
ms.assetid: 'fa00f64c-77ac-430e-9b6e-f02a02d7ac9a'
keywords: ["HasMMX property Virtual Server", "HasMMX property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , HasMMX property", "HasMMX property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , HasMMX property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.HasMMX
- IVMVirtualMachine.get_HasMMX
- VMVirtualMachine.HasMMX
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::HasMMX property

The **HasMMX** property contains **TRUE** if the processor supports the MMX instruction set.

This property is read-only.

## Syntax


```C++
HRESULT get_HasMMX(
  [out] VARIANT_BOOL *mmxEnabled
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
<td><pre><code>VMVirtualMachine.HasMMX( _
  ByRef mmxEnabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the processor supports the MMX instruction set.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                            |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>           |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *mmxEnabled* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>       |



## Examples

The following example displays the **HasMMX** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "HasMMX: " & objVM.HasMMX
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

 

 





