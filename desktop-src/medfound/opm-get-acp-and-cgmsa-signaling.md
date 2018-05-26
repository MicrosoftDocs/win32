---
ms.assetid: d477fe3e-4498-450b-93b7-ce74ae9ed005
title: OPM\_GET\_ACP\_AND\_CGMSA\_SIGNALING
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OPM\_GET\_ACP\_AND\_CGMSA\_SIGNALING

Returns the following information about a video output:

-   A list of television protection standards supported by the driver.
-   The standard that is currently active.
-   The current aspect ratio or other signaling data.



|              |                                                                                     |
|--------------|-------------------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_ACP\_AND\_CGMSA\_SIGNALING                                                |
| Input data   | None                                                                                |
| Return data  | An [**OPM\_ACP\_AND\_CGMSA\_SIGNALING**](/windows/win32/opmapi/ns-opmapi-_opm_acp_and_cgmsa_signaling?branch=master) structure |



 

## Remarks

This query is equivalent to the DXVA\_COPPQuerySignaling query used in Certified Output Protection Protocol (COPP).

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOPMVideoOutput::COPPCompatibleGetInformation**](/windows/win32/opmapi/nf-opmapi-iopmvideooutput-coppcompatiblegetinformation?branch=master)
</dt> <dt>

[**IOPMVideoOutput::GetInformation**](/windows/win32/opmapi/nf-opmapi-iopmvideooutput-getinformation?branch=master)
</dt> <dt>

[OPM Status Requests](opm-status-requests.md)
</dt> </dl>

 

 




