---
description: A callback function used to notify the host of which interfaces are supported.
MS-HAID: vspixengine.IVersionCallback\_VersionTableReady\_GUID\_arr\_UINT
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IVersionCallback::VersionTableReady method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 58D5E6B4-2CF8-4C13-9A62-93418D46CBCF
api_name: 
 - IVersionCallback.VersionTableReady
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.iversioncallback_versiontableready_guid_arr_uint"></span>IVersionCallback::VersionTableReady method

A callback function used to notify the host of which interfaces are supported.

## Syntax


```C++
HRESULT VersionTableReady(
   GUID [] count1_interfaceIds,
   UINT    count
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

[**IVersionCallback**](/windows/desktop/direct3dtools/iversioncallback)

 

 
