---
description: Updates the system renewability message (SRM) for High-Bandwidth Digital Content Protection (HDCP).
ms.assetid: ea18baba-0e03-4471-af0e-a588773c98d2
title: OPM_SET_HDCP_SRM (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM\_SET\_HDCP\_SRM

Updates the system renewability message (SRM) for High-Bandwidth Digital Content Protection (HDCP).



| Requirement | Value |
|--------------|-------------------------------------------------------------------------------------|
| Command GUID | OPM\_SET\_HDCP\_SRM                                                                 |
| Input data   | An [**OPM\_SET\_HDCP\_SRM\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_set_hdcp_srm_parameters) structure |



 

The *pbAdditionalParameters* parameter of [**IOPMVideoOutput::Configure**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-configure) must point to a buffer that contains the SRM. The format of an HDCP SRM is documented in the HDCP specification. Set the *ulAdditionalParametersSize* parameter equal to the size of the buffer, in bytes.

## Remarks

SRMs are used to update the list of revoked HDCP devices. SRMs are delivered with the video content.

This command updates the video output's current SRM. If HDCP is enabled at the time of the command, the video output uses the new SRM to check whether any of the connected HDCP devices are revoked. If the video output detects a revoked device, it stops displaying video. If you send this command while HDCP is disabled, the video output validates the SRM and stores it. Later, if the application enables HDCP, the video output uses the new SRM to check the device's revocation status.

This command can cause the **Configure** method to return any of the following error codes.



| Return code                                            | Description                             |
|--------------------------------------------------------|-----------------------------------------|
| ERROR\_GRAPHICS\_OPM\_INVALID\_SRM                     | The SRM is not valid.                   |
| ERROR\_GRAPHICS\_OPM\_OUTPUT\_DOES\_NOT\_SUPPORT\_HDCP | The video output does not support HDCP. |



 

This command is not supported when the **IOPMVideoOutput** interface emulates Certified Output Protection Protocol (COPP). When COPP semantics are used, the application is responsible for parsing SRMs and checking the revocation status of the HDCP device. Use the [OPM\_GET\_CONNECTED\_HDCP\_DEVICE\_INFORMATION](opm-get-connected-hdcp-device-information.md) status request to get the device's key selection vector (KSV), which is needed to check the revocation status. For more information about SRMs, refer to the HDCP specification.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOPMVideoOutput::Configure**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-configure)
</dt> <dt>

[OPM Commands](opm-commands.md)
</dt> </dl>

 

 




