---
description: OPM Status Requests
ms.assetid: 428d08c6-e9f0-49fb-9ef9-d0f95416669d
title: OPM Status Requests
ms.topic: article
ms.date: 05/31/2018
---

# OPM Status Requests

This section lists the available status requests for [Output Protection Manager](output-protection-manager.md) (OPM). To send an OPM status request, call [**IOPMVideoOutput::GetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-getinformation). For each request, the following information is listed.



|              |                                                                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Request GUID | Identifies the request. Set the **guidSetting** member of the [**OPM\_GET\_INFO\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_get_info_parameters) structure equal to this value. |
| Input data   | Specifies how to interpret the **abParameters** array in the [**OPM\_GET\_INFO\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_get_info_parameters) structure.                      |
| Output data  | Specifies how to interpret the **abRequestedInformation** array in the [**OPM\_REQUESTED\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_requested_information) structure.         |



 

The following status requests are defined:



| Status request                                                                                      | Description                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OPM\_GET\_ACP\_AND\_CGMSA\_SIGNALING**](opm-get-acp-and-cgmsa-signaling.md)                     | Returns the following information about a video output:                                                                                               |
| [**OPM\_GET\_ACTUAL\_OUTPUT\_FORMAT**](opm-get-actual-output-format.md)                            | Returns a description of the video signal that is being transmitted over the connector.                                                               |
| [**OPM\_GET\_ACTUAL\_PROTECTION\_LEVEL**](opm-get-actual-protection-level.md)                      | Returns the global protection level for a specified protection mechanism.                                                                             |
| [**OPM\_GET\_ADAPTER\_BUS\_TYPE**](opm-get-adapter-bus-type.md)                                    | Returns the type of I/O bus used by the video output.                                                                                                 |
| [**OPM\_GET\_CODEC\_INFO**](opm-get-codec-info.md)                                                 | Gets the merit value of a hardware codec.                                                                                                             |
| [**OPM\_GET\_CONNECTED\_HDCP\_DEVICE\_INFORMATION**](opm-get-connected-hdcp-device-information.md) | Gets information about a High-Bandwidth Digital Content Protection (HDCP) device attached to the video output. The following information is returned: |
| [**OPM\_GET\_CONNECTOR\_TYPE**](opm-get-connector-type.md)                                         | Returns the physical connector type of the video output.                                                                                              |
| [**OPM\_GET\_CURRENT\_HDCP\_SRM\_VERSION**](opm-get-current-hdcp-srm-version.md)                   | Returns the version number of the system renewability message (SRM) currently used by the video output.                                               |
| [**OPM\_GET\_DVI\_CHARACTERISTICS**](opm-get-dvi-characteristics.md)                               | Queries whether a digital video interface (DVI) connector supports DVI version 1.1 or later.                                                          |
| [**OPM\_GET\_OUTPUT\_ID**](opm-get-output-id.md)                                                   | Returns the unique identifier of the monitor associated with this video output.                                                                       |
| [**OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES**](opm-get-supported-protection-types.md)                | Returns the list of protection mechanisms that are supported by the connector.                                                                        |
| [**OPM\_GET\_VIRTUAL\_PROTECTION\_LEVEL**](opm-get-virtual-protection-level.md)                    | Returns the virtual protection level for a specified protection mechanism.                                                                            |



 

## Related topics

<dl> <dt>

[OPM Programming Reference](opm-programming-reference.md)
</dt> <dt>

[Output Protection Manager](output-protection-manager.md)
</dt> </dl>

 

 



