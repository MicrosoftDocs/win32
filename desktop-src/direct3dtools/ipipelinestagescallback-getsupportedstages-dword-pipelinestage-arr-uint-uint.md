---
description: A callback that notifies the host of which pipeline stages are used by the draw call of the assocaited request.
MS-HAID: vspixengine.IPipeLineStagesCallback\_GetSupportedStages\_DWORD\_PipeLineStage\_arr\_UINT\_UINT
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPipeLineStagesCallback::GetSupportedStages method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: F7046A41-5C9C-42FE-B1E2-879A47CE08E3
api_name: 
 - IPipeLineStagesCallback.GetSupportedStages
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipipelinestagescallback_getsupportedstages_dword_pipelinestage_arr_uint_uint"></span>IPipeLineStagesCallback::GetSupportedStages method

A callback that notifies the host of which pipeline stages are used by the draw call of the assocaited request.

## Syntax


```C++
HRESULT GetSupportedStages(
   DWORD            numColumns,
   PipeLineStage [] count0_pStages,
   UINT             swapChainWidth,
   UINT             swapChainHeight
);
```

## Parameters

*numColumns*   
The number of stages returned.

*count0\_pStages*   
The pipeline stages.

*swapChainWidth*   
The width of the swap chain assocaited with the draw call. This is used when requesting pipeline preview images.

*swapChainHeight*   
The height of the swap chain assocaited with the draw call. This is used when requesting pipeline preview images.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPipeLineStagesCallback**](/windows/desktop/direct3dtools/ipipelinestagescallback)

 

 
