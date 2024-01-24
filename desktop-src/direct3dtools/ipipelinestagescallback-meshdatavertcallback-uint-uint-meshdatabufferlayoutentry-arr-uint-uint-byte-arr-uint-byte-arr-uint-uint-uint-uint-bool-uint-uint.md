---
description: A callback that notifies the host of pipeline stages mesh information returned by the assocaited request.
MS-HAID: vspixengine.IPipeLineStagesCallback\_MeshDataVertCallback\_UINT\_UINT\_MeshDataBufferLayoutEntry\_arr\_UINT\_UINT\_BYTE\_arr\_UINT\_BYTE\_arr\_UINT\_UINT\_UINT\_UINT\_BOOL\_UINT\_UINT
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPipeLineStagesCallback::MeshDataVertCallback method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: E75EDE35-AC8E-4452-B79B-860C39B156F0
api_name: 
 - IPipeLineStagesCallback.MeshDataVertCallback
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipipelinestagescallback_meshdatavertcallback_uint_uint_meshdatabufferlayoutentry_arr_uint_uint_byte_arr_uint_byte_arr_uint_uint_uint_uint_bool_uint_uint"></span>IPipeLineStagesCallback::MeshDataVertCallback method

A callback that notifies the host of pipeline stages mesh information returned by the assocaited request.

## Syntax


```C++
HRESULT MeshDataVertCallback(
   UINT                         numVertices,
   UINT                         numBufferLayoutEntries,
   MeshDataBufferLayoutEntry [] count1_entries,
   UINT                         stride,
   UINT                         numVBBytes,
   BYTE []                      count4_pVBData,
   UINT                         numIBBytes,
   BYTE []                      count6_pIBData,
   UINT                         indexSize,
   UINT                         IBOffset,
   UINT                         baseVertex,
   UINT                         minVertex,
   BOOL                         IBIndexesVB,
   UINT                         numIndices,
   UINT                         topology
);
```

## Parameters

*numVertices*   
The number of vertices in the results.

*numBufferLayoutEntries*   
The number of buffer layout entries in the results.

*count1\_entries*   
The buffer layout entires. These describe the shader output signature.

*stride*   
The size (stride) of an entire output chunk.

*numVBBytes*   
The size of the vertex buffer in bytes.

*count4\_pVBData*   
The vertex buffer.

*numIBBytes*   
The size of the index buffer in bytes.

*count6\_pIBData*   
The index buffer.

*indexSize*   
The size of each index in bytes.

*IBOffset*   
An offset into the index buffer that specifies where indices should start being used.

*baseVertex*   
An offset into the vertex buffer that specifies where vertices should start being used.

*minVertex*   

*IBIndexesVB*   
true when the index buffer is used; otherwise false.

*numIndices*   
The number of indices used.

*topology*   
The topolology of the shader. This is not necessarily the same as the topology of the associated draw call.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPipeLineStagesCallback**](/windows/desktop/direct3dtools/ipipelinestagescallback)

 

 
