---
description: A callback function used to notify the host of offline analysis progress.
MS-HAID: vspixengine.IOfflineAnalysisCallback\_OfflineAnalysisProgress\_DWORD\_DOUBLE
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IOfflineAnalysisCallback::OfflineAnalysisProgress method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 17847FD7-A10A-4E52-90AD-ADE446D87E73
api_name: 
 - IOfflineAnalysisCallback.OfflineAnalysisProgress
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.iofflineanalysiscallback_offlineanalysisprogress_dword_double"></span>IOfflineAnalysisCallback::OfflineAnalysisProgress method

A callback function used to notify the host of offline analysis progress.

## Syntax


```C++
HRESULT OfflineAnalysisComplete(
   DWORD   cookie,
   HRESULT result,
   BSTR    outputFullFileName
);
```

## Parameters

*cookie*   
A cookie that uniquely identifies the request, and can be used to signal for it to be cancelled.

*progress*   
The progress percentage.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IOfflineAnalysisCallback**](/windows/desktop/direct3dtools/iofflineanalysiscallback)

 

 
