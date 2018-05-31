---
title: IVMVirtualServer Version property
description: The Version property contains the version of this instance of Virtual Server.
ms.assetid: f4f90fda-d74c-401c-8eea-947cd6060498
keywords:
- Version property Virtual Server
- Version property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , Version property
- Version property Virtual Server , VMVirtualServer object
- VMVirtualServer object Virtual Server , Version property
topic_type:
- apiref
api_name:
- IVMVirtualServer.Version
- IVMVirtualServer.get_Version
- VMVirtualServer.Version
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

# IVMVirtualServer::Version property

The **Version** property contains the version of this instance of Virtual Server.

This property is read-only.

## Syntax


```C++
HRESULT get_Version(
  [out] BSTR *version
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
<td><pre><code>VMVirtualServer.Version( _
  ByRef version _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The version of this instance of Virtual Server.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>         | *version* is **NULL**.<br/>        |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



## Remarks

The Virtual Server version information is returned as a string value with the following format:

*v***.***s***.***bbb***.***t* *ee*

Where *v* is the major version number, *s* is the minor version number, *bbb* is the build number, *t* is the build type (0 = release build), and *ee* is the server edition (SE = Standard Edition, EE = Enterprise Edition).

## Examples

The following example displays the **Version** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Version: " & objVS.Version
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

 

 





