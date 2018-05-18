---
title: IVMVirtualMachine HasSSE2 property
description: The HasSSE2 property contains TRUE if the processor supports the SSE2 instruction set.
ms.assetid: '6a5a8cf8-38d2-48c1-9bde-b2fd6aa50577'
keywords: ["HasSSE2 property Virtual Server", "HasSSE2 property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , HasSSE2 property", "HasSSE2 property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , HasSSE2 property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.HasSSE2
- IVMVirtualMachine.get_HasSSE2
- VMVirtualMachine.HasSSE2
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::HasSSE2 property

The **HasSSE2** property contains **TRUE** if the processor supports the SSE2 instruction set.

This property is read-only.

## Syntax


```C++
HRESULT get_HasSSE2(
  [out] VARIANT_BOOL *sse2Enabled
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
<td><pre><code>VMVirtualMachine.HasSSE2( _
  ByRef sse2Enabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the processor supports the SSE2 instruction set.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                             |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>            |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *sse2Enabled* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>            |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>        |



## Examples

The following example displays the **HasSSE2** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "HasSSE2: " & objVM.HasSSE2
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

 

 





