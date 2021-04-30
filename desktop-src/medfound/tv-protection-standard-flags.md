---
description: The constants in the following table specify television standards and formats for Output Protection Manager (OPM).
ms.assetid: 8f26aa92-ed40-483e-ac78-c071619f0e12
title: TV Protection Standard Flags (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# TV Protection Standard Flags

The constants in the following table specify television standards and formats for Output Protection Manager (OPM).



| Constant/value                                                                                                                                                                                                                                                                                                              | Description                                                    |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|
| <span id="OPM_PROTECTION_STANDARD_OTHER"></span><span id="opm_protection_standard_other"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_OTHER**</dt> <dt>0x80000000</dt> </dl>                                             | The protection standard is unknown.<br/>                 |
| <span id="OPM_PROTECTION_STANDARD_NONE"></span><span id="opm_protection_standard_none"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_NONE**</dt> <dt>0x00000000</dt> </dl>                                                | No protection standard is in place.<br/>                 |
| <span id="OPM_PROTECTION_STANDARD_IEC61880_525I"></span><span id="opm_protection_standard_iec61880_525i"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_IEC61880\_525I**</dt> <dt>0x00000001</dt> </dl>                    | The protection standard is IEC 61880, 525i.<br/>         |
| <span id="OPM_PROTECTION_STANDARD_IEC61880_2_525I"></span><span id="opm_protection_standard_iec61880_2_525i"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_IEC61880\_2\_525I**</dt> <dt>0x00000002</dt> </dl>             | The protection standard is IEC 61880-2, 525i.<br/>       |
| <span id="OPM_PROTECTION_STANDARD_IEC62375_625P"></span><span id="opm_protection_standard_iec62375_625p"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_IEC62375\_625P**</dt> <dt>0x00000004</dt> </dl>                    | The protection standard is IEC 62375, 625p.<br/>         |
| <span id="OPM_PROTECTION_STANDARD_EIA608B_525"></span><span id="opm_protection_standard_eia608b_525"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_EIA608B\_525**</dt> <dt>0x00000008</dt> </dl>                          | The protection standard is EIA/CEA-608-B, 525i.<br/>     |
| <span id="OPM_PROTECTION_STANDARD_EN300294_625I"></span><span id="opm_protection_standard_en300294_625i"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_EN300294\_625I**</dt> <dt>0x00000010</dt> </dl>                    | The protection standard is ETSI EN 300 294, 625i.<br/>   |
| <span id="OPM_PROTECTION_STANDARD_CEA805A_TYPEA_525P"></span><span id="opm_protection_standard_cea805a_typea_525p"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_CEA805A\_TYPEA\_525P**</dt> <dt>0x00000020</dt> </dl>    | The protection standard is CEA-805-A Type A, 525p.<br/>  |
| <span id="OPM_PROTECTION_STANDARD_CEA805A_TYPEA_750P"></span><span id="opm_protection_standard_cea805a_typea_750p"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_CEA805A\_TYPEA\_750P**</dt> <dt>0x00000040</dt> </dl>    | The protection standard is CEA-805-A Type A, 750p.<br/>  |
| <span id="OPM_PROTECTION_STANDARD_CEA805A_TYPEA_1125I"></span><span id="opm_protection_standard_cea805a_typea_1125i"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_CEA805A\_TYPEA\_1125I**</dt> <dt>0x00000080</dt> </dl> | The protection standard is CEA-805-A Type A, 1125i.<br/> |
| <span id="OPM_PROTECTION_STANDARD_CEA805A_TYPEB_525P"></span><span id="opm_protection_standard_cea805a_typeb_525p"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_CEA805A\_TYPEB\_525P**</dt> <dt>0x00000100</dt> </dl>    | The protection standard is CEA-805-A Type B, 525p.<br/>  |
| <span id="OPM_PROTECTION_STANDARD_CEA805A_TYPEB_750P"></span><span id="opm_protection_standard_cea805a_typeb_750p"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_CEA805A\_TYPEB\_750P**</dt> <dt>0x00000200</dt> </dl>    | The protection standard is CEA-805-A Type B, 750p.<br/>  |
| <span id="OPM_PROTECTION_STANDARD_CEA805A_TYPEB_1125I"></span><span id="opm_protection_standard_cea805a_typeb_1125i"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_CEA805A\_TYPEB\_1125I**</dt> <dt>0x00000400</dt> </dl> | The protection standard is CEA-805-A Type B, 1125i.<br/> |
| <span id="OPM_PROTECTION_STANDARD_ARIBTRB15_525I"></span><span id="opm_protection_standard_aribtrb15_525i"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_ARIBTRB15\_525I**</dt> <dt>0x00000800</dt> </dl>                 | The protection standard is ARIB TR-B15, 525i.<br/>       |
| <span id="OPM_PROTECTION_STANDARD_ARIBTRB15_525P"></span><span id="opm_protection_standard_aribtrb15_525p"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_ARIBTRB15\_525P**</dt> <dt>0x00001000</dt> </dl>                 | The protection standard is ARIB TR-B15, 525p.<br/>       |
| <span id="OPM_PROTECTION_STANDARD_ARIBTRB15_750P"></span><span id="opm_protection_standard_aribtrb15_750p"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_ARIBTRB15\_750P**</dt> <dt>0x00002000</dt> </dl>                 | The protection standard is ARIB TR-B15, 750p.<br/>       |
| <span id="OPM_PROTECTION_STANDARD_ARIBTRB15_1125I"></span><span id="opm_protection_standard_aribtrb15_1125i"></span><dl> <dt>**OPM\_PROTECTION\_STANDARD\_ARIBTRB15\_1125I**</dt> <dt>0x00004000</dt> </dl>              | The protection standard is ARIB TR-B15, 1125i.<br/>      |



## Remarks

These flags are numerically equivalent to the **COPP\_TVProtectionStandard** enumeration used in Certified Output Protection Protocol (COPP).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Constants](media-foundation-constants.md)
</dt> <dt>

[**OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING**](opm-set-acp-and-cgmsa-signaling.md)
</dt> <dt>

[OPM\_GET\_ACP\_AND\_CGMSA\_SIGNALING](opm-get-acp-and-cgmsa-signaling.md)
</dt> </dl>

 

 




