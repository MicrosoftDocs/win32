---
Description: Requests to get the raw contents of a tile.
MS-HAID: vspixengine.ITileRequest\_RequestBufferTileAsync\_EventID\_DWORD\_BSTR\_UINT\_IBufferObjectDataCallback\_ptr\_DWORD\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ITileRequest::RequestBufferTileAsync method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.itilerequest_requestbuffertileasync_eventid_dword_bstr_uint_ibufferobjectdatacallback_ptr_dword_dword"></span>ITileRequest::RequestBufferTileAsync method

Requests to get the raw contents of a tile.

## Syntax


```C++
);
```

## Parameters

*eventID*   
The specified event to match the tile's content to (for example, a render target could change over time).

*RequestedDataUID*   
The address of the specified tile.

*File*   
A COM string that contains the pathname of the file where results are written.

*tileIndex*   
The index of the specified tile.

*requestCallback*   
The address of callback used to notify the host of results.

*requestCookie*   
A cookie that uniquely identifies the request, and can be used to signal for it to be cancelled.

*progressIntervalMsecs*   
Not used.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**ITileRequest**](https://msdn.microsoft.com/library/windows/desktop/mt432819)

 

 



