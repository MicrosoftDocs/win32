---
description: Requests to cache offline analysis report of the specified frames.
MS-HAID: vspixengine.IOfflineAnalysisCacheRequest\_RequestOfflineAnalysisReportAvailabilityAsync\_DWORD\_DWORD\_arr\_IOfflineAnalysisCacheCallback\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IOfflineAnalysisCacheRequest::RequestOfflineAnalysisReportAvailabilityAsync method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 10FA71F8-813D-4788-92C8-00B30A9AE5CC
api_name: 
 - IOfflineAnalysisCacheRequest.RequestOfflineAnalysisReportAvailabilityAsync
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.iofflineanalysiscacherequest_requestofflineanalysisreportavailabilityasync_dword_dword_arr_iofflineanalysiscachecallback_ptr"></span>IOfflineAnalysisCacheRequest::RequestOfflineAnalysisReportAvailabilityAsync method

Requests to cache offline analysis report of the specified frames.

## Syntax


```C++
HRESULT RequestOfflineAnalysisReportAvailabilityAsync(
   DWORD                           numFrames,
   DWORD []                        count0_frameNumbers,
   IOfflineAnalysisCacheCallback * requestCallback
);
```

## Parameters

*numFrames*   
The number of frames to generate analysis reports for.

*count0\_frameNumbers*   
The specified frames.

*requestCallback*   
The address of a callback used to notify the host of results.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IOfflineAnalysisCacheRequest**](/windows/desktop/direct3dtools/iofflineanalysiscacherequest)

 

 
