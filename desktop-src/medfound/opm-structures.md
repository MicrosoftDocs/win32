---
description: The following structures are used with Output Protection Manager (OPM).
ms.assetid: 676a60ca-393e-4b5d-89d3-50cf4b771492
title: OPM Structures
ms.topic: article
ms.date: 05/31/2018
---

# OPM Structures

The following structures are used with [Output Protection Manager](output-protection-manager.md) (OPM).



| Structure                                                                                              | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GRL\_HEADER**](grl-header.md)                                                                      | Contains the global revocation list (GRL) header.                                                                                                          |
| [**MF\_SIGNATURE**](mf-signature.md)                                                                  | Contains a global revocation list (GRL) signature.                                                                                                         |
| [**OPM\_ACP\_AND\_CGMSA\_SIGNALING**](/windows/desktop/api/opmapi/ns-opmapi-opm_acp_and_cgmsa_signaling)                                 | Contains the result from an [**OPM\_GET\_ACP\_AND\_CGMSA\_SIGNALING**](opm-get-acp-and-cgmsa-signaling.md) query.                                         |
| [**OPM\_ACTUAL\_OUTPUT\_FORMAT**](/windows/desktop/api/opmapi/ns-opmapi-opm_actual_output_format)                                        | Contains the result of an [**OPM\_GET\_ACTUAL\_OUTPUT\_FORMAT**](opm-get-actual-output-format.md) query in Output Protection Manager (OPM).               |
| [**OPM\_CONFIGURE\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_configure_parameters)                                         | Contains an OPM or Certified Output Protection Manager (COPP) command.                                                                                     |
| [**OPM\_CONNECTED\_HDCP\_DEVICE\_INFORMATION**](/windows/desktop/api/opmapi/ns-opmapi-opm_connected_hdcp_device_information)             | Contains the result from an [**OPM\_GET\_CONNECTED\_HDCP\_DEVICE\_INFORMATION**](opm-get-connected-hdcp-device-information.md) query.                     |
| [**OPM\_COPP\_COMPATIBLE\_GET\_INFO\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_copp_compatible_get_info_parameters)        | Contains parameters for the [**IOPMVideoOutput::COPPCompatibleGetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-coppcompatiblegetinformation) method. |
| [**OPM\_ENCRYPTED\_INITIALIZATION\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_encrypted_initialization_parameters)          | Contains initialization parameters for an OPM session.                                                                                                     |
| [**OPM\_GET\_CODEC\_INFO\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_get_codec_info_information)                           | Contains the result from an [**OPM\_GET\_CODEC\_INFO**](opm-get-codec-info.md) query.                                                                     |
| [**OPM\_GET\_CODEC\_INFO\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_get_codec_info_parameters)                             | Contains information for the [**OPM\_GET\_CODEC\_INFO**](opm-get-codec-info.md) command.                                                                  |
| [**OPM\_GET\_INFO\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_get_info_parameters)                                          | Contains parameters for the [**IOPMVideoOutput::GetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-getinformation) method.                             |
| [**OPM\_HDCP\_KEY\_SELECTION\_VECTOR**](/windows/desktop/api/opmapi/ns-opmapi-opm_hdcp_key_selection_vector)                             | Contains the key selection vector (KSV) for a High-Bandwidth Digital Content Protection (HDCP) receiver.                                                   |
| [**OPM\_OMAC**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_omac)                                                                          | Contains a Message Authentication Code (MAC) for an OPM message.                                                                                           |
| [**OPM\_OUTPUT\_ID\_DATA**](/windows/desktop/api/opmapi/ns-opmapi-opm_output_id_data)                                                    | Contains the result from an [**OPM\_GET\_OUTPUT\_ID**](opm-get-output-id.md) status request.                                                              |
| [**OPM\_RANDOM\_NUMBER**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_random_number)                                                       | Contains a 128-bit random number for use with OPM.                                                                                                         |
| [**OPM\_REQUESTED\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_requested_information)                                       | Contains the result of an OPM status request.                                                                                                              |
| [**OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_set_acp_and_cgmsa_signaling_parameters) | Contains information for the [**OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING**](opm-set-acp-and-cgmsa-signaling.md) command in OPM.                               |
| [**OPM\_SET\_HDCP\_SRM\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_set_hdcp_srm_parameters)                                 | Contains parameters for the [**OPM\_SET\_HDCP\_SRM**](opm-set-hdcp-srm.md) command.                                                                       |
| [**OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_set_protection_level_parameters)                 | Contains data for the [OPM\_SET\_PROTECTION\_LEVEL](opm-set-protection-level.md) command in OPM.                                                          |
| [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information)                                         | Contains the result from an OPM status request.                                                                                                            |



 

## Related topics

<dl> <dt>

[OPM Programming Reference](opm-programming-reference.md)
</dt> <dt>

[Output Protection Manager](output-protection-manager.md)
</dt> </dl>

 

 



