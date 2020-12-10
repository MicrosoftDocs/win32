---
title: WINBIO_BIR_PURPOSE Constants (Winbio\_types.h)
description: Specify the purpose for which the biometric information record (BIR) is intended or for which it is suitable.
ms.assetid: AAFD3203-4D3D-43B5-A833-1258E1E281D3
topic_type:
- apiref
api_name:
- WINBIO_NO_PURPOSE_AVAILABLE
- WINBIO_PURPOSE_VERIFY
- WINBIO_PURPOSE_IDENTIFY
- WINBIO_PURPOSE_ENROLL
- WINBIO_PURPOSE_ENROLL_FOR_VERIFICATION
- WINBIO_PURPOSE_ENROLL_FOR_IDENTIFICATION
- WINBIO_PURPOSE_AUDIT
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_BIR\_PURPOSE Constants

The following flags are used by the **Purpose** member of the [**WINBIO\_BIR\_HEADER**](winbio-bir-header.md) structure to specify the purpose for which the biometric information record (BIR) is intended or for which it is suitable.



| Constant                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_NO_PURPOSE_AVAILABLE"></span><span id="winbio_no_purpose_available"></span><dl> <dt>**WINBIO\_NO\_PURPOSE\_AVAILABLE**</dt> </dl>                                         | No purpose is specified.<br/>                                                                                                                                                                                                                                                                                                         |
| <span id="WINBIO_PURPOSE_VERIFY"></span><span id="winbio_purpose_verify"></span><dl> <dt>**WINBIO\_PURPOSE\_VERIFY**</dt> </dl>                                                            | Verify the identity of a user.<br/>                                                                                                                                                                                                                                                                                                   |
| <span id="WINBIO_PURPOSE_IDENTIFY"></span><span id="winbio_purpose_identify"></span><dl> <dt>**WINBIO\_PURPOSE\_IDENTIFY**</dt> </dl>                                                      | Identify a user.<br/>                                                                                                                                                                                                                                                                                                                 |
| <span id="WINBIO_PURPOSE_ENROLL"></span><span id="winbio_purpose_enroll"></span><dl> <dt>**WINBIO\_PURPOSE\_ENROLL**</dt> </dl>                                                            | Enroll a user.<br/>                                                                                                                                                                                                                                                                                                                   |
| <span id="WINBIO_PURPOSE_ENROLL_FOR_VERIFICATION"></span><span id="winbio_purpose_enroll_for_verification"></span><dl> <dt>**WINBIO\_PURPOSE\_ENROLL\_FOR\_VERIFICATION**</dt> </dl>       | Capture a biometric sample and determine whether the sample corresponds to the specified user identity.<br/>                                                                                                                                                                                                                          |
| <span id="WINBIO_PURPOSE_ENROLL_FOR_IDENTIFICATION"></span><span id="winbio_purpose_enroll_for_identification"></span><dl> <dt>**WINBIO\_PURPOSE\_ENROLL\_FOR\_IDENTIFICATION**</dt> </dl> | Capture a biometric sample and determine whether it matches an existing biometric template.<br/>                                                                                                                                                                                                                                      |
| <span id="WINBIO_PURPOSE_AUDIT"></span><span id="winbio_purpose_audit"></span><dl> <dt>**WINBIO\_PURPOSE\_AUDIT**</dt> </dl>                                                               | Extra information that can be used for logging or for display. This value is ignored on input by all functions. On output, it will only be available if supported by the biometric unit and you specify **WINBIO\_DATA\_FLAG\_RAW** in the *Flags* parameter of the [**WinBioCaptureSample**](/windows/desktop/api/Winbio/nf-winbio-winbiocapturesample) function.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Constants](client-application-constants.md)
</dt> <dt>

[**WINBIO\_BIR\_HEADER**](winbio-bir-header.md)
</dt> </dl>

 

 





