---
Description: The following structures are used with Output Protection Manager (OPM).
ms.assetid: 676a60ca-393e-4b5d-89d3-50cf4b771492
title: OPM Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OPM Structures

The following structures are used with [Output Protection Manager](output-protection-manager.md) (OPM).



| Structure                                                                                              | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GRL\_HEADER**](grl-header.md)                                                                      | Contains the global revocation list (GRL) header.                                                                                                          |
| [**MF\_SIGNATURE**](mf-signature.md)                                                                  | Contains a global revocation list (GRL) signature.                                                                                                         |
| [**OPM\_ACP\_AND\_CGMSA\_SIGNALING**](/windows/win32/opmapi/ns-opmapi-_opm_acp_and_cgmsa_signaling?branch=master)                                 | Contains the result from an [**OPM\_GET\_ACP\_AND\_CGMSA\_SIGNALING**](opm-get-acp-and-cgmsa-signaling.md) query.                                         |
| [**OPM\_ACTUAL\_OUTPUT\_FORMAT**](/windows/win32/opmapi/ns-opmapi-_opm_actual_output_format?branch=master)                                        | Contains the result of an [**OPM\_GET\_ACTUAL\_OUTPUT\_FORMAT**](opm-get-actual-output-format.md) query in Output Protection Manager (OPM).               |
| [**OPM\_CONFIGURE\_PARAMETERS**](/windows/win32/opmapi/ns-opmapi-_opm_configure_parameters?branch=master)                                         | Contains an OPM or Certified Output Protection Manager (COPP) command.                                                                                     |
| [**OPM\_CONNECTED\_HDCP\_DEVICE\_INFORMATION**](/windows/win32/opmapi/ns-opmapi-_opm_connected_hdcp_device_information?branch=master)             | Contains the result from an [**OPM\_GET\_CONNECTED\_HDCP\_DEVICE\_INFORMATION**](opm-get-connected-hdcp-device-information.md) query.                     |
| [**OPM\_COPP\_COMPATIBLE\_GET\_INFO\_PARAMETERS**](/windows/win32/opmapi/ns-opmapi-_opm_copp_compatible_get_info_parameters?branch=master)        | Contains parameters for the [**IOPMVideoOutput::COPPCompatibleGetInformation**](/windows/win32/opmapi/nf-opmapi-iopmvideooutput-coppcompatiblegetinformation?branch=master) method. |
| [**OPM\_ENCRYPTED\_INITIALIZATION\_PARAMETERS**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_encrypted_initialization_parameters?branch=master)          | Contains initialization parameters for an OPM session.                                                                                                     |
| [**OPM\_GET\_CODEC\_INFO\_INFORMATION**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_get_codec_info_information?branch=master)                           | Contains the result from an [**OPM\_GET\_CODEC\_INFO**](opm-get-codec-info.md) query.                                                                     |
| [**OPM\_GET\_CODEC\_INFO\_PARAMETERS**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_get_codec_info_parameters?branch=master)                             | Contains information for the [**OPM\_GET\_CODEC\_INFO**](opm-get-codec-info.md) command.                                                                  |
| [**OPM\_GET\_INFO\_PARAMETERS**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_get_info_parameters?branch=master)                                          | Contains parameters for the [**IOPMVideoOutput::GetInformation**](/windows/win32/opmapi/nf-opmapi-iopmvideooutput-getinformation?branch=master) method.                             |
| [**OPM\_HDCP\_KEY\_SELECTION\_VECTOR**](/windows/win32/opmapi/ns-opmapi-_opm_hdcp_key_selection_vector?branch=master)                             | Contains the key selection vector (KSV) for a High-Bandwidth Digital Content Protection (HDCP) receiver.                                                   |
| [**OPM\_OMAC**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_omac?branch=master)                                                                          | Contains a Message Authentication Code (MAC) for an OPM message.                                                                                           |
| [**OPM\_OUTPUT\_ID\_DATA**](/windows/win32/opmapi/ns-opmapi-_opm_output_id_data?branch=master)                                                    | Contains the result from an [**OPM\_GET\_OUTPUT\_ID**](opm-get-output-id.md) status request.                                                              |
| [**OPM\_RANDOM\_NUMBER**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_random_number?branch=master)                                                       | Contains a 128-bit random number for use with OPM.                                                                                                         |
| [**OPM\_REQUESTED\_INFORMATION**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_requested_information?branch=master)                                       | Contains the result of an OPM status request.                                                                                                              |
| [**OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING\_PARAMETERS**](/windows/win32/opmapi/ns-opmapi-_opm_set_acp_and_cgmsa_signaling_parameters?branch=master) | Contains information for the [**OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING**](opm-set-acp-and-cgmsa-signaling.md) command in OPM.                               |
| [**OPM\_SET\_HDCP\_SRM\_PARAMETERS**](/windows/win32/opmapi/ns-opmapi-_opm_set_hdcp_srm_parameters?branch=master)                                 | Contains parameters for the [**OPM\_SET\_HDCP\_SRM**](opm-set-hdcp-srm.md) command.                                                                       |
| [**OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS**](/windows/win32/opmapi/ns-opmapi-_opm_set_protection_level_parameters?branch=master)                 | Contains data for the [OPM\_SET\_PROTECTION\_LEVEL](opm-set-protection-level.md) command in OPM.                                                          |
| [**OPM\_STANDARD\_INFORMATION**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_standard_information?branch=master)                                         | Contains the result from an OPM status request.                                                                                                            |



 

## Related topics

<dl> <dt>

[OPM Programming Reference](opm-programming-reference.md)
</dt> <dt>

[Output Protection Manager](output-protection-manager.md)
</dt> </dl>

 

 



