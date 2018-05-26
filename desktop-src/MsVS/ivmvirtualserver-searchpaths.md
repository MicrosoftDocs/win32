---
title: IVMVirtualServer SearchPaths property
description: The SearchPaths property contains an array of file system paths which are used to find files associated with Virtual Server.
ms.assetid: bda34c02-5ce2-43b8-aca7-642d359723b3
keywords:
- SearchPaths property Virtual Server
- SearchPaths property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , SearchPaths property
- SearchPaths property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , SearchPaths property
topic_type:
- apiref
api_name:
- IVMVirtualServer.SearchPaths
- IVMVirtualServer.get_SearchPaths
- IVMVirtualServer.put_SearchPaths
- VMVirtualServer.SearchPaths
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

# IVMVirtualServer::SearchPaths property

The **SearchPaths** property contains an array of file system paths which are used to find files associated with Virtual Server.

This property is read/write.

## Syntax


```C++
HRESULT put_SearchPaths(
  [in]  VARIANT searchPaths
);

HRESULT get_SearchPaths(
  [out] VARIANT *searchPaths
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
<td><pre><code>VMVirtualServer.SearchPaths( _
  ByRef searchPaths, _
  ByVal searchPaths _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains a safearray containing a file system path for each entry.

This property value is read/write.

## Error codes



| Name                                                                                               | Meaning                                                                                                                               |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                   | The operation was successful.<br/>                                                                                              |
| <dl> <dt>E\_POINTER</dt> </dl>              | The *searchPaths* parameter is **NULL**.<br/>                                                                                   |
| <dl> <dt>E\_INVALIDARG</dt> </dl>           | The *searchPaths* parameter is not valid and could not be parsed into an array of paths.<br/>                                   |
| <dl> <dt>E\_FILE\_NOT\_FOUND</dt> </dl>     | The system cannot find a directory specified in the *searchPaths* parameter.<br/>                                               |
| <dl> <dt>E\_PATH\_NOT\_FOUND</dt> </dl>     | The system cannot find a path specified by the *searchPaths* parameter.<br/>                                                    |
| <dl> <dt>E\_INVALID\_NAME</dt> </dl>        | A path specified in the *searchPaths* parameter contains illegal characters. The illegal characters are "\*?&lt;&gt;/\|":"<br/> |
| <dl> <dt>E\_BAD\_PATHNAME</dt> </dl>        | A path contained in the *searchPaths* parameter specifies an empty or relative path. An absolute path is required.<br/>         |
| <dl> <dt>E\_BUFFER\_OVERFLOW</dt> </dl>     | The path specified in the *searchPaths* parameter is too long. The length of the path must be less than 260 characters.<br/>    |
| <dl> <dt>VM\_E\_PREF\_NOT\_FOUND</dt> </dl> | The preference was not found.<br/>                                                                                              |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>      | An unexpected error occurred.<br/>                                                                                              |



## Examples

The following example displays the **SearchPaths** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Dim allPaths

Wscript.Echo "Name: " & objVS.Name

allPaths = objVS.SearchPaths

If UBound (allPaths) = -1 Then
  Wscript.Echo "File search paths: [empty]"
Else
  Wscript.Echo "File search paths: "
  For i = LBound(allPaths) to UBound(allPaths)
    wscript.echo allPaths(i)
  Next
End If
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

 

 





