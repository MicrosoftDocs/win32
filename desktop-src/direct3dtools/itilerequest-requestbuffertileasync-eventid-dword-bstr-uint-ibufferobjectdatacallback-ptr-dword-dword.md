---
description: Requests to get the raw contents of a tile.
MS-HAID: vspixengine.ITileRequest_RequestBufferTileAsync_EventID_DWORD_BSTR_UINT_IBufferObjectDataCallback_ptr_DWORD_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ITileRequest::RequestBufferTileAsync method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 2D68766F-1BED-439E-AC51-790471DA4F70
api_name: 
 - ITileRequest.RequestBufferTileAsync
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.itilerequest_requestbuffertileasync_eventid_dword_bstr_uint_ibufferobjectdatacallback_ptr_dword_dword"></span>ITileRequest::RequestBufferTileAsync method

Requests to get the raw contents of a tile.

## Syntax


```C++
HRESULT RequestBufferTileAsync(
   EventID                     eventID,
   DWORD                       RequestedDataUID,
   BSTR                        File,
   UINT                        tileIndex,
   IBufferObjectDataCallback * requestCallback,
   DWORD                       requestCookie,
   DWORD                       progressIntervalMsecs
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

If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**ITileRequest**](/windows/desktop/direct3dtools/itilerequest)

 

 
