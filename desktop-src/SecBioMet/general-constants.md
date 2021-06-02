---
title: General Constants (Winbio\_types.h)
description: Specify maximum SID length, handles, IDs, maximum string length, and maximum sample buffer size.
ms.assetid: 62e87bd8-a708-4d00-aaa8-9cac8e3736a7
topic_type:
- apiref
api_name:
- SECURITY_MAX_SID_SIZE
- WINBIO_UNIT_ID
- WINBIO_SESSION_HANDLE
- WINBIO_FRAMEWORK_HANDLE
- WINBIO_UUID
- WINBIO_STRING
- WINBIO_MAX_STRING_LEN
- WINBIO_MAX_SAMPLE_BUFFER_SIZE
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# General Constants (Winbio\_types.h)

The following constants are used throughout the Windows Biometric Framework.



| Constant/value                                                                                                                                                                                                                                                                   | Description                                                                                 |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| <span id="SECURITY_MAX_SID_SIZE"></span><span id="security_max_sid_size"></span><dl> <dt>**SECURITY\_MAX\_SID\_SIZE**</dt> </dl>                                                                                          | The maximum length of a security identifier (SID) value. Currently this is 68.<br/>   |
| <span id="WINBIO_UNIT_ID"></span><span id="winbio_unit_id"></span><dl> <dt>**WINBIO\_UNIT\_ID**</dt> </dl>                                                                                                                | ID number of a biometric unit.<br/>                                                   |
| <span id="WINBIO_SESSION_HANDLE"></span><span id="winbio_session_handle"></span><dl> <dt>**WINBIO\_SESSION\_HANDLE**</dt> </dl>                                                                                           | An unsigned long integer that contains the handle for an open biometric session.<br/> |
| <span id="WINBIO_FRAMEWORK_HANDLE"></span><span id="winbio_framework_handle"></span><dl> <dt>**WINBIO\_FRAMEWORK\_HANDLE**</dt> </dl>                                                                                     | An unsigned long integer that contains the handle for an open framework session.<br/> |
| <span id="WINBIO_UUID"></span><span id="winbio_uuid"></span><dl> <dt>**WINBIO\_UUID**</dt> </dl>                                                                                                                          | A GUID.<br/>                                                                          |
| <span id="WINBIO_STRING"></span><span id="winbio_string"></span><dl> <dt>**WINBIO\_STRING**</dt> </dl>                                                                                                                    | A byte array that contains a null-terminated Unicode string.<br/>                     |
| <span id="WINBIO_MAX_STRING_LEN_"></span><span id="winbio_max_string_len_"></span><dl> <dt>**WINBIO\_MAX\_STRING\_LEN** </dt> </dl>                                                                                       | The maximum length of a **WINBIO\_STRING** value. Currently this is 256.<br/>         |
| <span id="WINBIO_MAX_SAMPLE_BUFFER_SIZE"></span><span id="winbio_max_sample_buffer_size"></span><dl> <dt>**WINBIO\_MAX\_SAMPLE\_BUFFER\_SIZE**</dt> <dt>0x7FFFFFFF</dt> </dl> | The maximum number of bytes in a single biometric data capture.<br/>                  |



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

 

 





