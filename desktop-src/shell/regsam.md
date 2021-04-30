---
description: A data type used for specifying the security access attributes in the registry.
title: REGSAM (Winnt.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 003f6be9-e4ba-4d23-b486-a167063c630e
api_name: 
 - KEY_ALL_ACCESS
 - KEY_CREATE_LINK
 - KEY_CREATE_SUB_KEY
 - KEY_ENUMERATE_SUB_KEYS
 - KEY_EXECUTE
 - KEY_NOTIFY
 - KEY_QUERY_VALUE
 - KEY_READ
 - KEY_SET_VALUE
 - KEY_WRITE
api_type: 
 - HeaderDef
api_location: 
 - Winnt.h
topic_type: 
 - APIRef
 - kbSyntax

---

# REGSAM

A data type used for specifying the security access attributes in the registry.



| Constant                                                                                                                                                                                   | Description                                                                                                                                                                                                |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="KEY_ALL_ACCESS"></span><span id="key_all_access"></span><dl> <dt>**KEY\_ALL\_ACCESS**</dt> </dl>                          | Combination of ****KEY\_QUERY\_VALUE****, ****KEY\_ENUMERATE\_SUB\_KEYS****, ****KEY\_NOTIFY****, ****KEY\_CREATE\_SUB\_KEY****, ****KEY\_CREATE\_LINK****, and ****KEY\_SET\_VALUE**** access.<br/> |
| <span id="KEY_CREATE_LINK"></span><span id="key_create_link"></span><dl> <dt>**KEY\_CREATE\_LINK**</dt> </dl>                       | Permission to create a symbolic link.<br/>                                                                                                                                                           |
| <span id="KEY_CREATE_SUB_KEY"></span><span id="key_create_sub_key"></span><dl> <dt>**KEY\_CREATE\_SUB\_KEY**</dt> </dl>             | Permission to create subkeys.<br/>                                                                                                                                                                   |
| <span id="KEY_ENUMERATE_SUB_KEYS"></span><span id="key_enumerate_sub_keys"></span><dl> <dt>**KEY\_ENUMERATE\_SUB\_KEYS**</dt> </dl> | Permission to enumerate subkeys.<br/>                                                                                                                                                                |
| <span id="KEY_EXECUTE"></span><span id="key_execute"></span><dl> <dt>**KEY\_EXECUTE**</dt> </dl>                                    | Permission for read access.<br/>                                                                                                                                                                     |
| <span id="KEY_NOTIFY"></span><span id="key_notify"></span><dl> <dt>**KEY\_NOTIFY**</dt> </dl>                                       | Permission for change notification.<br/>                                                                                                                                                             |
| <span id="KEY_QUERY_VALUE"></span><span id="key_query_value"></span><dl> <dt>**KEY\_QUERY\_VALUE**</dt> </dl>                       | Permission to query subkey data.<br/>                                                                                                                                                                |
| <span id="KEY_READ"></span><span id="key_read"></span><dl> <dt>**KEY\_READ**</dt> </dl>                                             | Combination of ****KEY\_QUERY\_VALUE****, ****KEY\_ENUMERATE\_SUB\_KEYS****, and ****KEY\_NOTIFY**** access.<br/>                                                                                    |
| <span id="KEY_SET_VALUE"></span><span id="key_set_value"></span><dl> <dt>**KEY\_SET\_VALUE**</dt> </dl>                             | Permission to set subkey data.<br/>                                                                                                                                                                  |
| <span id="KEY_WRITE"></span><span id="key_write"></span><dl> <dt>**KEY\_WRITE**</dt> </dl>                                          | Combination of ****KEY\_SET\_VALUE**** and ****KEY\_CREATE\_SUB\_KEY**** access.<br/>                                                                                                                |



## Remarks

A **REGSAM** value can be one or more of the listed values.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winnt.h</dt> </dl> |



 

 




