---
title: IVMVirtualServer VMRCEnabled property
description: The VMRCEnabled property enables or disables server administration using Virtual Machine Remote Control (VMRC).
ms.assetid: 58ae0e3a-a8bd-478a-b9ed-972decf29205
keywords:
- VMRCEnabled property Virtual Server
- VMRCEnabled property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VMRCEnabled property
- VMRCEnabled property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , VMRCEnabled property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VMRCEnabled
- IVMVirtualServer.get_VMRCEnabled
- IVMVirtualServer.put_VMRCEnabled
- VMVirtualServer.VMRCEnabled
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

# IVMVirtualServer::VMRCEnabled property

The **VMRCEnabled** property enables or disables server administration using Virtual Machine Remote Control (VMRC).

This property is read/write.

## Syntax


```C++
HRESULT put_VMRCEnabled(
  [in]  VARIANT_BOOL shouldEnable
);

HRESULT get_VMRCEnabled(
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
<td><pre><code>VMVirtualServer.VMRCEnabled( _
  ByRef isEnabled, _
  ByVal shouldEnable _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if server administration using VMRC is enabled, **vbFalse** otherwise.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                  |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *isEnabled* referenced **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                  |



## Remarks

The **VMRCEnabled** property contains **TRUE** if server administration using Virtual Machine Remote Control (VMRC) is enabled.

## Examples

The following example displays the **VMRCEnabled** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

Wscript.Echo "VMRC enabled: " & objVS.VMRCEnabled
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

 

 





