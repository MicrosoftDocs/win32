---
Description: Returns the version number of the system renewability message (SRM) currently used by the video output.
ms.assetid: 65d4b98b-369f-4863-a28c-f9e3b4c2b55d
title: OPM\_GET\_CURRENT\_HDCP\_SRM\_VERSION
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OPM\_GET\_CURRENT\_HDCP\_SRM\_VERSION

Returns the version number of the system renewability message (SRM) currently used by the video output.



|              |                                                                             |
|--------------|-----------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_CURRENT\_HDCP\_SRM\_VERSION                                       |
| Input data   | None                                                                        |
| Return data  | An [**OPM\_STANDARD\_INFORMATION**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_standard_information?branch=master) structure |



 

## Remarks

If this query succeeds, the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_standard_information?branch=master) structure contains the SRM version number, in little-endian format.

SRMs are used to update the list of revoked High-Bandwidth Digital Content Protection (HDCP) devices. SRMs are delivered with the video content. To set the SRM, send the [**OPM\_SET\_HDCP\_SRM**](opm-set-hdcp-srm.md) command.

This query can cause the [**IOPMVideoOutput::GetInformation**](/windows/win32/opmapi/nf-opmapi-iopmvideooutput-getinformation?branch=master) method to return any of the following error codes.



| Return code                                            | Description                             |
|--------------------------------------------------------|-----------------------------------------|
| ERROR\_GRAPHICS\_OPM\_HDCP\_SRM\_NEVER\_SET            | The application did not set an SRM.     |
| ERROR\_GRAPHICS\_OPM\_OUTPUT\_DOES\_NOT\_SUPPORT\_HDCP | The video output does not support HDCP. |



 

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOPMVideoOutput::GetInformation**](/windows/win32/opmapi/nf-opmapi-iopmvideooutput-getinformation?branch=master)
</dt> <dt>

[OPM Status Requests](opm-status-requests.md)
</dt> </dl>

 

 




