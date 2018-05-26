---
title: IVMVirtualServer DefaultVNConfigurationPath property
description: The DefaultVNConfigurationPath property contains the default directory searched by the web application to create lists of available virtual network configuration files.
ms.assetid: e7cbb039-f0fe-490d-a306-71923ec9ba08
keywords:
- DefaultVNConfigurationPath property Virtual Server
- DefaultVNConfigurationPath property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , DefaultVNConfigurationPath property
- DefaultVNConfigurationPath property Virtual Server , VMVirtualServer interface
- VMVirtualServer interface Virtual Server , DefaultVNConfigurationPath property
topic_type:
- apiref
api_name:
- IVMVirtualServer.DefaultVNConfigurationPath
- IVMVirtualServer.get_DefaultVNConfigurationPath
- VMVirtualServer.DefaultVNConfigurationPath
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

# IVMVirtualServer::DefaultVNConfigurationPath property

The **DefaultVNConfigurationPath** property contains the default directory searched by the web application to create lists of available virtual network configuration files.

This property is read-only.

## Syntax


```C++
HRESULT get_DefaultVNConfigurationPath(
  [out] BSTR *configurationPath
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
<td><pre><code>VMVirtualServer.DefaultVNConfigurationPath( _
  ByRef configurationPath _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The default virtual network configurations directory path. In the path string, a backslash (\) may appear immediately before the terminating null character.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                  |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *configurationPath* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                  |



## Remarks

By default, this property value is set to the "%ALLUSERSPROFILE%\\Documents\\Shared Virtual Networks\\" directory.

## Examples

The following example displays the **DefaultVNConfigurationPath** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Default VN configuration path: " & _
             objVS.DefaultVNConfigurationPath
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

 

 





