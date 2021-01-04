---
title: WINBIO_FLAG Constants (Winbio\_types.h)
description: Specify biometric unit configuration and access characteristics for the new session.
ms.assetid: 82b57023-6c27-433d-bf13-f136f501fc60
topic_type:
- apiref
api_name:
- WINBIO_FLAG_DEFAULT
- WINBIO_FLAG_BASIC
- WINBIO_FLAG_ADVANCED
- WINBIO_FLAG_RAW
- WINBIO_FLAG_MAINTENANCE
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_FLAG Constants

The following constants can be used in the [**WinBioOpenSession**](/windows/desktop/api/Winbio/nf-winbio-winbioopensession) function to specify biometric unit configuration and access characteristics for the new session.



| Constant                                                                                                                                                                                     | Description                                                                                                                                                                              |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_FLAG_DEFAULT"></span><span id="winbio_flag_default"></span><dl> <dt>**WINBIO\_FLAG\_DEFAULT**</dt> </dl>             | Sensor configuration flag. The biometric units operate in the manner specified during installation.<br/>                                                                           |
| <span id="WINBIO_FLAG_BASIC"></span><span id="winbio_flag_basic"></span><dl> <dt>**WINBIO\_FLAG\_BASIC**</dt> </dl>                   | Sensor configuration flag. The biometric units operate only as basic capture devices.<br/>                                                                                         |
| <span id="WINBIO_FLAG_ADVANCED"></span><span id="winbio_flag_advanced"></span><dl> <dt>**WINBIO\_FLAG\_ADVANCED**</dt> </dl>          | Sensor configuration flag. The biometric units use internal processing and storage capabilities.<br/>                                                                              |
| <span id="WINBIO_FLAG_RAW"></span><span id="winbio_flag_raw"></span><dl> <dt>**WINBIO\_FLAG\_RAW**</dt> </dl>                         | Desired access flag. The client application captures raw biometric data using [**WinBioCaptureSample**](/windows/desktop/api/Winbio/nf-winbio-winbiocapturesample).<br/>                                             |
| <span id="WINBIO_FLAG_MAINTENANCE"></span><span id="winbio_flag_maintenance"></span><dl> <dt>**WINBIO\_FLAG\_MAINTENANCE**</dt> </dl> | Desired access flag. The client performs vendor-defined control operations on a biometric unit by calling [**WinBioControlUnitPrivileged**](/windows/desktop/api/Winbio/nf-winbio-winbiocontrolunitprivileged).<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Constants](client-application-constants.md)
</dt> </dl>

 

 





