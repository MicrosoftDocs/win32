---
title: RESERVED
description: Do not use. The RESERVED\_ constants are used to define boundries for reserved database identifiers.
ms.assetid: 01ce5d03-6e32-42a0-a6d1-966cda069dd2
topic_type:
- apiref
api_name:
- RESERVED_ID_MIN
- RESERVED_ID_MAX
- RESERVED_KEYS
api_location:
- Directdb.idl
api_type:
- IDLDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RESERVED

Do not use. The RESERVED\_ constants are used to define boundries for reserved database identifiers.



| Constant/value                                                                                                                                                                                                                       | Description                                                                                                                                                         |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RESERVED_ID_MIN"></span><span id="reserved_id_min"></span><dl> <dt>**RESERVED\_ID\_MIN**</dt> <dt>0xFFFFFBFF</dt> </dl> | Defines the lower boundary for reserved IDs. IDatabase::GenerateId() will never return an ID between RESERVED\_ID\_MIN and RESERVED\_ID\_MAX, inclusive.<br/> |
| <span id="RESERVED_ID_MAX"></span><span id="reserved_id_max"></span><dl> <dt>**RESERVED\_ID\_MAX**</dt> <dt>0xFFFFFFFF</dt> </dl> | Defines the upper boundary for reserved IDs. IDatabase::GenerateId() will never return an ID between RESERVED\_ID\_MIN and RESERVED\_ID\_MAX, inclusive.<br/> |
| <span id="RESERVED_KEYS"></span><span id="reserved_keys"></span><dl> <dt>**RESERVED\_KEYS**</dt> <dt>8</dt> </dl>                 | Defines the maximum number of INDEXKEY records (8) that can be used from the TABLEINDEX structure.<br/>                                                       |



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl> |



 

 





