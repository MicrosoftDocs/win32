---
Description: Requests to cancel offline analysis in an offline analysis request.
MS-HAID: vspixengine.IOfflineAnalysisRequest\_CancelOfflineAnalysisAsync\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IOfflineAnalysisRequest::CancelOfflineAnalysisAsync method
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.iofflineanalysisrequest_cancelofflineanalysisasync_dword"></span>IOfflineAnalysisRequest::CancelOfflineAnalysisAsync method

Requests to cancel offline analysis in an offline analysis request.

## Syntax


```C++
);
```

## Parameters

*cookie*   
A cookie that uniquely identifies the request, and can be used to signal for it to be cancelled.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IOfflineAnalysisRequest**](https://msdn.microsoft.com/library/windows/desktop/mt432709)

 

 



