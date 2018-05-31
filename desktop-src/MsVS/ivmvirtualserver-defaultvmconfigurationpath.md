---
title: IVMVirtualServer DefaultVMConfigurationPath property
description: The DefaultVMConfigurationPath property contains the default directory searched by the web application to create lists of available virtual machine configuration files.
ms.assetid: 5cca7155-21b2-4ac5-acda-cfe7a22eb332
keywords:
- DefaultVMConfigurationPath property Virtual Server
- DefaultVMConfigurationPath property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , DefaultVMConfigurationPath property
- DefaultVMConfigurationPath property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , DefaultVMConfigurationPath property
topic_type:
- apiref
api_name:
- IVMVirtualServer.DefaultVMConfigurationPath
- IVMVirtualServer.get_DefaultVMConfigurationPath
- IVMVirtualServer.put_DefaultVMConfigurationPath
- VMVirtualServer.DefaultVMConfigurationPath
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

# IVMVirtualServer::DefaultVMConfigurationPath property

The **DefaultVMConfigurationPath** property contains the default directory searched by the web application to create lists of available virtual machine configuration files.

This property is read/write.

## Syntax


```C++
HRESULT put_DefaultVMConfigurationPath(
  [in]  BSTR configurationPath
);

HRESULT get_DefaultVMConfigurationPath(
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
<td><pre><code>VMVirtualServer.DefaultVMConfigurationPath( _
  ByRef configurationPath, _
  ByVal configurationPath _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The default virtual machine configurations directory path. In the path string, a backslash (\) may appear immediately before the terminating null character.

This property value is read/write.

## Error codes



| Name                                                                                           | Meaning                                                                                                                                  |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>                                                                                                 |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *configurationPath* parameter is **NULL**.<br/>                                                                                |
| <dl> <dt>E\_FILE\_NOT\_FOUND</dt> </dl> | The system cannot find the directory specified by the *configurationPath* parameter.<br/>                                          |
| <dl> <dt>E\_PATH\_NOT\_FOUND</dt> </dl> | The system cannot find the path specified by the *configurationPath* parameter.<br/>                                               |
| <dl> <dt>E\_INVALID\_NAME</dt> </dl>    | The *configurationPath* parameter contains an invalid character (one of the following: "\*?&lt;&gt;/\|":").<br/>                   |
| <dl> <dt>E\_BAD\_PATHNAME</dt> </dl>    | The *configurationPath* parameter specifies an empty or relative path. An absolute path is required.<br/>                          |
| <dl> <dt>E\_BUFFER\_OVERFLOW</dt> </dl> | The path specified by the *configurationPath* parameter is too long. The length of the path must be less than 260 characters.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>  | An unexpected error occurred.<br/>                                                                                                 |



## Remarks

By default, this property value is set to the following directory: "%ALLUSERSPROFILE%\\Documents\\Shared Virtual Machines\\".

## Examples

The following example displays the **DefaultVMConfigurationPath** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Default VM configuration path: " & _
             objVS.DefaultVMConfigurationPath
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

 

 





