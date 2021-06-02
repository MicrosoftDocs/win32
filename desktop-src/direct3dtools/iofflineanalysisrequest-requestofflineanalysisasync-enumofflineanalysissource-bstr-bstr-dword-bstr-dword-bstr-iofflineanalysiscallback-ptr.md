---
description: Requests to run offline analysis with the specified source, manifest, parameters and of the specified frame.
MS-HAID: vspixengine.IOfflineAnalysisRequest\_RequestOfflineAnalysisAsync\_enumOFFLINEANALYSISSOURCE\_BSTR\_BSTR\_DWORD\_BSTR\_DWORD\_BSTR\_IOfflineAnalysisCallback\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IOfflineAnalysisRequest::RequestOfflineAnalysisAsync method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: C836D9C1-D3E0-4661-9B89-048B61028F53
api_name: 
 - IOfflineAnalysisRequest.RequestOfflineAnalysisAsync
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.iofflineanalysisrequest_requestofflineanalysisasync_enumofflineanalysissource_bstr_bstr_dword_bstr_dword_bstr_iofflineanalysiscallback_ptr"></span>IOfflineAnalysisRequest::RequestOfflineAnalysisAsync method

Requests to run offline analysis with the specified source, manifest, parameters and of the specified frame.

## Syntax


```C++
HRESULT RequestOfflineAnalysisAsync(
   enum OFFLINEANALYSISSOURCE analysisSource,
   BSTR                       manifestXml,
   BSTR                       parametersXml,
   DWORD                      cookie,
   BSTR                       captureFullFileName,
   DWORD                      frameNumber,
   BSTR                       outputFullFileName,
   IOfflineAnalysisCallback * requestCallback
);
```

## Parameters

*analysisSource*   
Specfies where the analysis source come from cached reports or from playback.

*manifestXml*   
A COM string containing the pathname of the XML manifest file.

*parametersXml*   
A COM string containing the pathname of the XML parameters file.

*cookie*   
A cookie that uniquely identifies the request, and can be used to signal for it to be cancelled.

*captureFullFileName*   
A COM string containing the absolute pathname of the capture file (.vsglog).

*frameNumber*   
The specified frame.

*outputFullFileName*   
A COM string containing the absolute pathname of the file where output is written.

*requestCallback*   
The address of a callback used to notify the host of results.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IOfflineAnalysisRequest**](/windows/desktop/direct3dtools/iofflineanalysisrequest)

 

 
