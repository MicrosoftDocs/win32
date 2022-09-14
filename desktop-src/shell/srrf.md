---
description: Flags that restrict the data to be set or returned.
title: SRRF (Shlwapi.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: c9dbffd1-3b3e-4a25-89ee-1666e2812a62
api_name: 
 - SRRF_RT_REG_NONE
 - SRRF_RT_REG_SZ
 - SRRF_RT_REG_EXPAND_SZ
 - SRRF_RT_REG_BINARY
 - SRRF_RT_REG_DWORD
 - SRRF_RT_REG_MULTI_SZ
 - SRRF_RT_REG_QWORD
 - SRRF_RT_DWORD
 - SRRF_RT_QWORD
 - SRRF_RT_ANY
 - SRRF_RM_ANY
 - SRRF_RM_NORMAL
 - SRRF_RM_SAFE
 - SRRF_RM_SAFENETWORK
 - SRRF_NOEXPAND
 - SRRF_ZEROONFAILURE
 - SRRF_NOVIRT
api_type: 
 - HeaderDef
api_location: 
 - Shlwapi.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SRRF

Flags that restrict the data to be set or returned.



| Constant/value                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                            |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SRRF_RT_REG_NONE"></span><span id="srrf_rt_reg_none"></span><dl> <dt>**SRRF\_RT\_REG\_NONE**</dt> <dt>0x00000001</dt> </dl>                 | Type REG\_NONE.<br/>                                                                                                                                                                                             |
| <span id="SRRF_RT_REG_SZ"></span><span id="srrf_rt_reg_sz"></span><dl> <dt>**SRRF\_RT\_REG\_SZ**</dt> <dt>0x00000002</dt> </dl>                       | Type REG\_SZ. REG\_EXPAND\_SZ types are automatically converted to REG\_SZ unless the SRRF\_NOEXPAND flag is specified.<br/>                                                                                     |
| <span id="SRRF_RT_REG_EXPAND_SZ"></span><span id="srrf_rt_reg_expand_sz"></span><dl> <dt>**SRRF\_RT\_REG\_EXPAND\_SZ**</dt> <dt>0x00000004</dt> </dl> | Type REG\_EXPAND\_SZ. If retrieving a value, you must also get the SRRF\_NOEXPAND flag, or [**SHRegGetValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shreggetvaluea) fails with ERROR\_INVALID\_PARAMETER.<br/>                                     |
| <span id="SRRF_RT_REG_BINARY"></span><span id="srrf_rt_reg_binary"></span><dl> <dt>**SRRF\_RT\_REG\_BINARY**</dt> <dt>0x00000008</dt> </dl>           | Type REG\_BINARY.<br/>                                                                                                                                                                                           |
| <span id="SRRF_RT_REG_DWORD"></span><span id="srrf_rt_reg_dword"></span><dl> <dt>**SRRF\_RT\_REG\_DWORD**</dt> <dt>0x00000010</dt> </dl>              | Type REG\_DWORD.<br/>                                                                                                                                                                                            |
| <span id="SRRF_RT_REG_MULTI_SZ"></span><span id="srrf_rt_reg_multi_sz"></span><dl> <dt>**SRRF\_RT\_REG\_MULTI\_SZ**</dt> <dt>0x00000020</dt> </dl>    | Type REG\_MULTI\_SZ.<br/>                                                                                                                                                                                        |
| <span id="SRRF_RT_REG_QWORD"></span><span id="srrf_rt_reg_qword"></span><dl> <dt>**SRRF\_RT\_REG\_QWORD**</dt> <dt>0x00000040</dt> </dl>              | Type REG\_QWORD.<br/>                                                                                                                                                                                            |
| <span id="SRRF_RT_DWORD"></span><span id="srrf_rt_dword"></span><dl> <dt>**SRRF\_RT\_DWORD**</dt> <dt>0x00000018</dt> </dl>                           | REG\_DWORD and 32-bit REG\_BINARY types. This is equivalent to SRRF\_RT\_REG\_BINARY \| SRRF\_RT\_REG\_DWORD. If retrieving a value, if the value's binary data is larger than 32 bits, it is not returned.<br/> |
| <span id="SRRF_RT_QWORD"></span><span id="srrf_rt_qword"></span><dl> <dt>**SRRF\_RT\_QWORD**</dt> <dt>0x00000048</dt> </dl>                           | REG\_QWORD and 64-bit REG\_BINARY types. This is equivalent to SRRF\_RT\_REG\_BINARY \| SRRF\_RT\_REG\_QWORD. If retrieving a value, if the value's binary data is larger than 64 bits, it is not returned.<br/> |
| <span id="SRRF_RT_ANY"></span><span id="srrf_rt_any"></span><dl> <dt>**SRRF\_RT\_ANY**</dt> <dt>0x0000FFFF</dt> </dl>                                 | All types. Set this flag if no other SRRF\_RT value is set.<br/>                                                                                                                                                 |
| <span id="SRRF_RM_ANY"></span><span id="srrf_rm_any"></span><dl> <dt>**SRRF\_RM\_ANY**</dt> <dt>0x00000000</dt> </dl>                                 | No mode restriction. This is the default value.<br/>                                                                                                                                                             |
| <span id="SRRF_RM_NORMAL"></span><span id="srrf_rm_normal"></span><dl> <dt>**SRRF\_RM\_NORMAL**</dt> <dt>0x00010000</dt> </dl>                        | Restrict system startup mode to "normal boot".<br/>                                                                                                                                                              |
| <span id="SRRF_RM_SAFE"></span><span id="srrf_rm_safe"></span><dl> <dt>**SRRF\_RM\_SAFE**</dt> <dt>0x00020000</dt> </dl>                              | Restrict system startup mode to "safe mode".<br/>                                                                                                                                                                |
| <span id="SRRF_RM_SAFENETWORK"></span><span id="srrf_rm_safenetwork"></span><dl> <dt>**SRRF\_RM\_SAFENETWORK**</dt> <dt>0x00040000</dt> </dl>         | Restrict system startup mode to "safe mode with networking".<br/>                                                                                                                                                |
| <span id="SRRF_NOEXPAND"></span><span id="srrf_noexpand"></span><dl> <dt>**SRRF\_NOEXPAND**</dt> <dt>0x10000000</dt> </dl>                            | Do not automatically expand REG\_EXPAND\_SZ environment strings.<br/>                                                                                                                                            |
| <span id="SRRF_ZEROONFAILURE"></span><span id="srrf_zeroonfailure"></span><dl> <dt>**SRRF\_ZEROONFAILURE**</dt> <dt>0x20000000</dt> </dl>             | If retrieving a value, if *pvData* is not **NULL**, set the contents of the *pvData* buffer to all zeros on failure.<br/>                                                                                        |
| <span id="SRRF_NOVIRT"></span><span id="srrf_novirt"></span><dl> <dt>**SRRF\_NOVIRT**</dt> <dt>0x40000000</dt> </dl>                                  | When retrieving a value, if the requested key is virtualized, fail with ERROR\_FILE\_NOT\_FOUND.<br/>                                                                                                            |



## Remarks

These values are defined in Shlwapi.h.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Shlwapi.h</dt> </dl> |



## See also

<dl> <dt>

[**SHRegSetValue**](/windows/desktop/api/shlwapi/nf-shlwapi-shregsetvalue)
</dt> <dt>

[**SHRegGetValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shreggetvaluea)
</dt> </dl>

 

 




