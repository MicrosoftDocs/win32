---
Description: A callback function used to notify the host that offline analysis has completed.
MS-HAID: vspixengine.IOfflineAnalysisCallback\_OfflineAnalysisComplete\_DWORD\_HRESULT\_BSTR
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IOfflineAnalysisCallback::OfflineAnalysisComplete method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.iofflineanalysiscallback_offlineanalysiscomplete_dword_hresult_bstr"></span>IOfflineAnalysisCallback::OfflineAnalysisComplete method

A callback function used to notify the host that offline analysis has completed.

## Syntax


```C++
);
```

## Parameters

*cookie*   
A cookie that uniquely identifies the request which initiated offline analysis.

*result*   
Indicates whether offline analysis succeeded or failed. If it succeeded, results were written to a file.

*outputFullFileName*   
A COM string contianing the name of the file where offline analysis results were written.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IOfflineAnalysisCallback**](https://msdn.microsoft.com/library/windows/desktop/mt432706)

 

 



