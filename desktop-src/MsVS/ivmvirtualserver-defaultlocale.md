---
title: IVMVirtualServer DefaultLocale property
description: The DefaultLocale property retrieves the default user interface locale of the Virtual Server service.
ms.assetid: ff63d164-d078-48fd-9054-47f4bcc6fe1f
keywords:
- DefaultLocale property Virtual Server
- DefaultLocale property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , DefaultLocale property
- DefaultLocale property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , DefaultLocale property
topic_type:
- apiref
api_name:
- IVMVirtualServer.DefaultLocale
- IVMVirtualServer.get_DefaultLocale
- VMVirtualServer.DefaultLocale
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

# IVMVirtualServer::DefaultLocale property

The **DefaultLocale** property retrieves the default user interface locale of the Virtual Server service.

This property is read-only.

## Syntax


```C++
HRESULT get_DefaultLocale(
  [out] ULONG *outLocale
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
<td><pre><code>VMVirtualServer.DefaultLocale( _
  ByRef outLocale _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The default Windows locale ID of the Virtual Server service.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>          |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *outLocale* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>          |



## Examples

The following example displays the **DefaultLocale** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Default Locale: " & CInt(objVS.DefaultLocale)
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
</dt> <dt>

[**Locale**](ivmvirtualserver-locale.md)
</dt> <dt>

[**QueryLocale**](ivmvirtualserver-querylocale.md)
</dt> </dl>

 

 





