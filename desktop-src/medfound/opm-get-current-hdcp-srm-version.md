---
description: Returns the version number of the system renewability message (SRM) currently used by the video output.
ms.assetid: 65d4b98b-369f-4863-a28c-f9e3b4c2b55d
title: OPM_GET_CURRENT_HDCP_SRM_VERSION (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM\_GET\_CURRENT\_HDCP\_SRM\_VERSION

Returns the version number of the system renewability message (SRM) currently used by the video output.



| Requirement | Value |
|--------------|-----------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_CURRENT\_HDCP\_SRM\_VERSION                                       |
| Input data   | None                                                                        |
| Return data  | An [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure |



 

## Remarks

If this query succeeds, the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure contains the SRM version number, in little-endian format.

SRMs are used to update the list of revoked High-Bandwidth Digital Content Protection (HDCP) devices. SRMs are delivered with the video content. To set the SRM, send the [**OPM\_SET\_HDCP\_SRM**](opm-set-hdcp-srm.md) command.

This query can cause the [**IOPMVideoOutput::GetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-getinformation) method to return any of the following error codes.



| Return code                                            | Description                             |
|--------------------------------------------------------|-----------------------------------------|
| ERROR\_GRAPHICS\_OPM\_HDCP\_SRM\_NEVER\_SET            | The application did not set an SRM.     |
| ERROR\_GRAPHICS\_OPM\_OUTPUT\_DOES\_NOT\_SUPPORT\_HDCP | The video output does not support HDCP. |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOPMVideoOutput::GetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-getinformation)
</dt> <dt>

[OPM Status Requests](opm-status-requests.md)
</dt> </dl>

 

 




