---
title: IVMVirtualServer VSScriptsEnabled property
description: The VSScriptsEnabled property indicates whether scripts attached to Virtual Server events are allowed to run.
ms.assetid: 28174d06-b597-433e-ab45-2fb89d7aef3d
keywords:
- VSScriptsEnabled property Virtual Server
- VSScriptsEnabled property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VSScriptsEnabled property
- VSScriptsEnabled property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , VSScriptsEnabled property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VSScriptsEnabled
- IVMVirtualServer.get_VSScriptsEnabled
- IVMVirtualServer.put_VSScriptsEnabled
- VMVirtualServer.VSScriptsEnabled
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

# IVMVirtualServer::VSScriptsEnabled property

The **VSScriptsEnabled** property indicates whether scripts attached to Virtual Server events are allowed to run.

This property is read/write.

## Syntax


```C++
HRESULT put_VSScriptsEnabled(
  [in]  VARIANT_BOOL shouldEnable
);

HRESULT get_VSScriptsEnabled(
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
<td><pre><code>VMVirtualServer.VSScriptsEnabled( _
  ByRef isEnabled, _
  ByVal shouldEnable _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if scripts attached to Virtual Server events are allowed to run.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>          |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *isEnabled* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>      |



## Examples

The following example displays the **VSScriptsEnabled** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Virtual server event scripts enabled: " & objVS.VSScriptsEnabled
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

 

 





