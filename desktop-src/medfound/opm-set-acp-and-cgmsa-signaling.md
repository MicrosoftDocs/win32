---
description: Specifies information about the video signal, other than the protection level.
ms.assetid: ed78b7eb-bf15-4068-ab86-ae42a5e62096
title: OPM_SET_ACP_AND_CGMSA_SIGNALING (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING

Specifies information about the video signal, other than the protection level.



| Requirement | Value |
|--------------|---------------------------------------------------------------------------------------------------------------------|
| Command GUID | OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING                                                                                |
| Input data   | An [**OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_set_acp_and_cgmsa_signaling_parameters) structure |



 

## Remarks

This command is equivalent to the DXVA\_COPPSetSignaling command used in Certified Output Protection Protocol (COPP).

For CGMS-A, certain protection standards require that the television signal contain information within the same VBI waveform packets as the CGMS-A bits. Among other things, this information includes the picture aspect ratio. Televisions may display poorly if the aspect ratio information is not consistent with the video stream. The application can use this command to specify the aspect ratio so that the graphics driver can generate the correct VBI packets.

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

 

 




