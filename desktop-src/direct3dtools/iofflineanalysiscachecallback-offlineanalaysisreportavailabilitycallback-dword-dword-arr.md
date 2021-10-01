---
description: A callback function used to notify the host about which frames have offline analysis reports available.
MS-HAID: vspixengine.IOfflineAnalysisCacheCallback\_OfflineAnalaysisReportAvailabilityCallback\_DWORD\_DWORD\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IOfflineAnalysisCacheCallback::OfflineAnalaysisReportAvailabilityCallback method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 2061EB62-4CBD-4668-BFCD-6E43014BB406
api_name: 
 - IOfflineAnalysisCacheCallback.OfflineAnalaysisReportAvailabilityCallback
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.iofflineanalysiscachecallback_offlineanalaysisreportavailabilitycallback_dword_dword_arr"></span>IOfflineAnalysisCacheCallback::OfflineAnalaysisReportAvailabilityCallback method

A callback function used to notify the host about which frames have offline analysis reports available.

## Syntax


```C++
HRESULT OfflineAnalaysisReportAvailabilityCallback(
   DWORD    numFramesWithReports,
   DWORD [] count0_framesWithReports
);
```

## Parameters

*numFramesWithReports*   
The number of frames in count0\_framesWithReports.

*count0\_framesWithReports*   
An array containing the frame numbers of the frames that have offline analysis reports available.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IOfflineAnalysisCacheCallback**](/windows/desktop/direct3dtools/iofflineanalysiscachecallback)

 

 
