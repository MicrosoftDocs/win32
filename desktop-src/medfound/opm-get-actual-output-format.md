---
description: Returns a description of the video signal that is being transmitted over the connector.
ms.assetid: 8464470f-49db-4559-80b2-02cfc473e30e
title: OPM_GET_ACTUAL_OUTPUT_FORMAT (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM\_GET\_ACTUAL\_OUTPUT\_FORMAT

Returns a description of the video signal that is being transmitted over the connector.



| Requirement | Value |
|--------------|------------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_ACTUAL\_OUTPUT\_FORMAT                                             |
| Input data   | None                                                                         |
| Return data  | An [**OPM\_ACTUAL\_OUTPUT\_FORMAT**](/windows/desktop/api/opmapi/ns-opmapi-opm_actual_output_format) structure |



 

## Remarks

The video signal that is transmitted over the connector does not necessarily have the same format as the desktop display mode. For example, the desktop display mode might be 1024 x 768 pixels at 85 Hz, while the connector might be an S-Video connector that transmits a video signal at 720 x 480 pixels, 60/1.01 Hz interlaced. In that case, the driver would return the resolution of the S-Video signal, not the desktop resolution.

This query is equivalent to the DXVA\_COPPQueryDisplayData query used in Certified Output Protection Protocol (COPP).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOPMVideoOutput::COPPCompatibleGetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-coppcompatiblegetinformation)
</dt> <dt>

[**IOPMVideoOutput::GetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-getinformation)
</dt> <dt>

[OPM Status Requests](opm-status-requests.md)
</dt> </dl>

 

 




