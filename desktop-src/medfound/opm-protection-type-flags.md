---
description: The flags in the following table specify output protection mechanisms for Output Protection Manager (OPM).
ms.assetid: 484dfea9-301d-4b2b-b5d1-d785ebaa8c8f
title: OPM Protection Type Flags (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM Protection Type Flags

The flags in the following table specify output protection mechanisms for Output Protection Manager (OPM).



| Constant/value                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                 |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="OPM_PROTECTION_TYPE_OTHER"></span><span id="opm_protection_type_other"></span><dl> <dt>**OPM\_PROTECTION\_TYPE\_OTHER**</dt> <dt>0x80000000</dt> </dl>                                                | Unknown protection mechanism.<br/>                                                                                                                                                                                    |
| <span id="OPM_PROTECTION_TYPE_NONE"></span><span id="opm_protection_type_none"></span><dl> <dt>**OPM\_PROTECTION\_TYPE\_NONE**</dt> <dt>0x00000000</dt> </dl>                                                   | No protection mechanisms.<br/>                                                                                                                                                                                        |
| <span id="OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP"></span><span id="opm_protection_type_copp_compatible_hdcp"></span><dl> <dt>**OPM\_PROTECTION\_TYPE\_COPP\_COMPATIBLE\_HDCP**</dt> <dt>0x00000001</dt> </dl> | High-Bandwidth Digital Content Protection (HDCP). This flag is used when emulating Certified Output Protection Protocol (COPP). For more information, see Remarks. This flag is not supported for OPM semantics.<br/> |
| <span id="OPM_PROTECTION_TYPE_ACP"></span><span id="opm_protection_type_acp"></span><dl> <dt>**OPM\_PROTECTION\_TYPE\_ACP**</dt> <dt>0x00000002</dt> </dl>                                                      | Analog Copy Protection (ACP).<br/>                                                                                                                                                                                    |
| <span id="OPM_PROTECTION_TYPE_CGMSA"></span><span id="opm_protection_type_cgmsa"></span><dl> <dt>**OPM\_PROTECTION\_TYPE\_CGMSA**</dt> <dt>0x00000004</dt> </dl>                                                | Copy Generation Management System—Analog (CGMS-A).<br/>                                                                                                                                                               |
| <span id="OPM_PROTECTION_TYPE_HDCP"></span><span id="opm_protection_type_hdcp"></span><dl> <dt>**OPM\_PROTECTION\_TYPE\_HDCP**</dt> <dt>0x00000008</dt> </dl>                                                   | HDCP. This flag is used when the OPM object has OPM semantics. It is not supported for COPP semantics.<br/>                                                                                                           |
| <span id="OPM_PROTECTION_TYPE_DPCP"></span><span id="opm_protection_type_dpcp"></span><dl> <dt>**OPM\_PROTECTION\_TYPE\_DPCP**</dt> <dt>0x00000010</dt> </dl>                                                   | DisplayPort Content Protection (DPCP).<br/>                                                                                                                                                                           |



## Remarks

These flags are used in the following OPM commands and status requests.

-   [OPM\_SET\_PROTECTION\_LEVEL](opm-set-protection-level.md)
-   [OPM\_GET\_VIRTUAL\_PROTECTION\_LEVEL](opm-get-virtual-protection-level.md)
-   [OPM\_GET\_ACTUAL\_PROTECTION\_LEVEL](opm-get-actual-protection-level.md)

### HDCP

The following two flags are defined for HDCP.



| Value                                         | Description                                                                                                                                                                    |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OPM\_PROTECTION\_TYPE\_HDCP                   | Use this flag if the [**IOPMVideoOutput**](/windows/desktop/api/opmapi/nn-opmapi-iopmvideooutput) pointer was created with OPM semantics.                                                                        |
| OPM\_PROTECTION\_TYPE\_COPP\_COMPATIBLE\_HDCP | Use this flag if the [**IOPMVideoOutput**](/windows/desktop/api/opmapi/nn-opmapi-iopmvideooutput) pointer was created with COPP semantics. This flag corresponds to the COPP\_ProtectionType\_HDCP flag in COPP. |



 

Both modes (OPM semantics and COPP semantics) support the following operations for HDCP:

-   Enable or disable HDCP by using the [OPM\_SET\_PROTECTION\_LEVEL](opm-set-protection-level.md) command.
-   Query whether HDCP is enabled by using the [OPM\_GET\_VIRTUAL\_PROTECTION\_LEVEL](opm-get-virtual-protection-level.md) or [OPM\_GET\_ACTUAL\_PROTECTION\_LEVEL](opm-get-actual-protection-level.md) status request.

OPM semantics also support the following:

-   HDCP repeaters. An *HDCP repeater* is an HDCP device that can receive HDCP content and also re-encrypt and transmit the same content.
-   HDCP revocation. If a revoked HDCP device is attached to the OPM video output, the video output will not transmit the video. The application does not need to parse HDCP system renewability messages (SRMs) or determine whether the output device has been revoked. For more information, see the [**OPM\_SET\_HDCP\_SRM**](opm-set-hdcp-srm.md) command.

When COPP semantics are used, the [**IOPMVideoOutput**](/windows/desktop/api/opmapi/nn-opmapi-iopmvideooutput) interface does not support HDCP repeaters. Also, it does not handle HDCP revocation. Instead, the application must parse the SRM to determine whether an HDCP device has been revoked.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[OPM Enumerations](opm-enumerations.md)
</dt> </dl>

 

 




