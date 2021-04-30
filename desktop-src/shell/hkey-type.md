---
description: These data types can be used to specify the type of a registry value.
title: Registry Data Types (Winnt.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 4185e7af-e1f0-40af-91c7-0ff7e27896ae
api_name: 
 - REG_BINARY
 - REG_DWORD
 - REG_QWORD
 - REG_DWORD_LITTLE_ENDIAN
 - REG_QWORD_LITTLE_ENDIAN
 - REG_DWORD_BIG_ENDIAN
 - REG_EXPAND_SZ
 - REG_LINK
 - REG_MULTI_SZ
 - REG_NONE
 - REG_RESOURCE_LIST
 - REG_SZ
api_type: 
 - HeaderDef
api_location: 
 - Winnt.h
topic_type: 
 - APIRef
 - kbSyntax

---

# Registry Data Types

These data types can be used to specify the type of a registry value.



| Constant                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                  |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="REG_BINARY"></span><span id="reg_binary"></span><dl> <dt>**REG\_BINARY**</dt> </dl>                                          | Binary data in any form.<br/>                                                                                                                                                                                                                                                                                          |
| <span id="REG_DWORD"></span><span id="reg_dword"></span><dl> <dt>**REG\_DWORD**</dt> </dl>                                             | 32-bit number.<br/>                                                                                                                                                                                                                                                                                                    |
| <span id="REG_QWORD"></span><span id="reg_qword"></span><dl> <dt>**REG\_QWORD**</dt> </dl>                                             | 64-bit number.<br/>                                                                                                                                                                                                                                                                                                    |
| <span id="REG_DWORD_LITTLE_ENDIAN"></span><span id="reg_dword_little_endian"></span><dl> <dt>**REG\_DWORD\_LITTLE\_ENDIAN**</dt> </dl> | 32-bit number in little-endian format. This is equivalent to **REG\_DWORD**.<br/> In little-endian format, a multibyte value is stored in memory from the lowest byte (the "little end") to the highest byte. For example, the value 0x12345678 is stored as (0x78 0x56 0x34 0x12) in little-endian format.<br/> |
| <span id="REG_QWORD_LITTLE_ENDIAN"></span><span id="reg_qword_little_endian"></span><dl> <dt>**REG\_QWORD\_LITTLE\_ENDIAN**</dt> </dl> | A 64-bit number in little-endian format. This is equivalent to **REG\_QWORD**. <br/>                                                                                                                                                                                                                                   |
| <span id="REG_DWORD_BIG_ENDIAN"></span><span id="reg_dword_big_endian"></span><dl> <dt>**REG\_DWORD\_BIG\_ENDIAN**</dt> </dl>          | 32-bit number in big-endian format.<br/> In big-endian format, a multibyte value is stored in memory from the highest byte (the "big end") to the lowest byte. For example, the value 0x12345678 is stored as (0x12 0x34 0x56 0x78) in big-endian format.<br/>                                                   |
| <span id="REG_EXPAND_SZ"></span><span id="reg_expand_sz"></span><dl> <dt>**REG\_EXPAND\_SZ**</dt> </dl>                                | Null-terminated string that contains unexpanded references to environment variables (for example, "%PATH%"). It will be a Unicode or ANSI string, depending on whether you use the Unicode or ANSI functions.<br/>                                                                                                     |
| <span id="REG_LINK"></span><span id="reg_link"></span><dl> <dt>**REG\_LINK**</dt> </dl>                                                | Unicode symbolic link.<br/>                                                                                                                                                                                                                                                                                            |
| <span id="REG_MULTI_SZ"></span><span id="reg_multi_sz"></span><dl> <dt>**REG\_MULTI\_SZ**</dt> </dl>                                   | Array of null-terminated strings that are terminated by two null characters.<br/>                                                                                                                                                                                                                                      |
| <span id="REG_NONE"></span><span id="reg_none"></span><dl> <dt>**REG\_NONE**</dt> </dl>                                                | No defined value type.<br/>                                                                                                                                                                                                                                                                                            |
| <span id="REG_RESOURCE_LIST"></span><span id="reg_resource_list"></span><dl> <dt>**REG\_RESOURCE\_LIST**</dt> </dl>                    | Device-driver resource list.<br/>                                                                                                                                                                                                                                                                                      |
| <span id="REG_SZ"></span><span id="reg_sz"></span><dl> <dt>**REG\_SZ**</dt> </dl>                                                      | Null-terminated string. It will be a Unicode or ANSI string, depending on whether you use the Unicode or ANSI functions.<br/>                                                                                                                                                                                          |



## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winnt.h</dt> </dl> |



 

 




