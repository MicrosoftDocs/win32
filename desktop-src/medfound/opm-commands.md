---
description: OPM Commands
ms.assetid: 52165e1b-a178-4483-bf76-4197281f856d
title: OPM Commands
ms.topic: article
ms.date: 05/31/2018
---

# OPM Commands

This section lists the available commands for [Output Protection Manager](output-protection-manager.md) (OPM).

To send an OPM command, call [**IOPMVideoOutput::Configure**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-configure). For each command, the following information is listed.



|              |                                                                                                                                                             |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Command GUID | Identifies the command. Set the **guidSetting** member of the [**OPM\_CONFIGURE\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_configure_parameters) structure equal to this value. |
| Input data   | Specifies how to interpret the **abParameters** array in the [**OPM\_CONFIGURE\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_configure_parameters) structure.                      |



 

The following commands are defined:



| Command                                                                                                       | Description                                                                                         |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING**](opm-set-acp-and-cgmsa-signaling.md)                               | Specifies information about the video signal, other than the protection level.                      |
| [**OPM\_SET\_HDCP\_SRM**](opm-set-hdcp-srm.md)                                                               | Updates the system renewability message (SRM) for High-Bandwidth Digital Content Protection (HDCP). |
| [**OPM\_SET\_PROTECTION\_LEVEL**](opm-set-protection-level.md)                                               | Sets the protection level for an output protection mechanism.                                       |
| [**OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD**](opm-set-protection-level-according-to-css-dvd.md) | Sets the HDCP protection level for DVD playback, following DVD Content Scramble System (CSS) rules. |



 

## Related topics

<dl> <dt>

[OPM Programming Reference](opm-programming-reference.md)
</dt> <dt>

[Output Protection Manager](output-protection-manager.md)
</dt> </dl>

 

 



