---
Description: A callback that notifies the host of Mesh information written by the associated request.
MS-HAID: vspixengine.IPipeLineStagesCallback3\_MeshFileReadyCallback\_BSTR
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPipeLineStagesCallback3::MeshFileReadyCallback method
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.ipipelinestagescallback3_meshfilereadycallback_bstr"></span>IPipeLineStagesCallback3::MeshFileReadyCallback method

A callback that notifies the host of Mesh information written by the associated request.

## Syntax


```C++
);
```

## Parameters

*meshFilename*   
A COM string containing the pathname of the file where the mesh data is written.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPipeLineStagesCallback3**](https://msdn.microsoft.com/library/windows/desktop/mt432720)

 

 



