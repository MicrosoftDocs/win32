---
title: IVMVirtualServer VMScriptsEnabled property
description: The VMScriptsEnabled property contains VARIANT\_TRUE if scripts attached to any virtual machine are allowed to run.
ms.assetid: bde32601-3a02-4d79-911b-d54ee8a08e9f
keywords:
- VMScriptsEnabled property Virtual Server
- VMScriptsEnabled property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VMScriptsEnabled property
- VMScriptsEnabled property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , VMScriptsEnabled property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VMScriptsEnabled
- IVMVirtualServer.get_VMScriptsEnabled
- IVMVirtualServer.put_VMScriptsEnabled
- VMVirtualServer.VMScriptsEnabled
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

# IVMVirtualServer::VMScriptsEnabled property

The **VMScriptsEnabled** property contains **VARIANT\_TRUE** if scripts attached to any virtual machine are allowed to run.

This property is read/write.

## Syntax


```C++
HRESULT put_VMScriptsEnabled(
  [in]  VARIANT_BOOL shouldEnable
);

HRESULT get_VMScriptsEnabled(
  [out] VARIANT_BOOL *isEnabled
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
<td><pre><code>VMVirtualServer.VMScriptsEnabled( _
  ByRef isEnabled, _
  ByVal shouldEnable _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if scripts attached to any virtual machine are allowed to run.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>          |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *isEnabled* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>      |



## Examples

The following example displays the **VMScriptsEnabled** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Virtual machine scripts enabled: " & objVS.VMScriptsEnabled
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





