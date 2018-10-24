---
Description: A callback function used to notify the host of which interfaces are supported.
MS-HAID: vspixengine.IVersionCallback\_VersionTableReady\_GUID\_arr\_UINT
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IVersionCallback::VersionTableReady method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.iversioncallback_versiontableready_guid_arr_uint"></span>IVersionCallback::VersionTableReady method

A callback function used to notify the host of which interfaces are supported.

## Syntax


```C++
);
```

## Parameters

*count1\_interfaceIds*   
An array containing the GUIDs of supported interface IDs.

*count*   
The number of GUIDs passed in count1\_interfaceIds.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IVersionCallback**](https://msdn.microsoft.com/library/windows/desktop/mt432826)

 

 



