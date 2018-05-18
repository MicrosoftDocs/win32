---
title: CMAX
description: Do not use. The (CMAX\_\ ) constants are used to specify index limits on databases.
ms.assetid: '2272dce9-8830-40ce-b51e-b78c8d0fd056'
topic_type:
- apiref
api_name:
- CMAX_INDEXES
- CMAX_KEYS
api_location:
- Directdb.idl
api_type:
- IDLDef
---

# CMAX

Do not use. The (CMAX\_\*) constants are used to specify index limits on databases.



| Constant/value                                                                                                                                                                                                    | Description                                                                                                                                                            |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CMAX_INDEXES"></span><span id="cmax_indexes"></span><dl> <dt>**CMAX\_INDEXES**</dt> <dt>8</dt> </dl> | Defines the maximum number of indices used in the database. Methods taking an argument of the INDEXORDINAL type must specify a value from zero to CMAX - 1.<br/> |
| <span id="CMAX_KEYS"></span><span id="cmax_keys"></span><dl> <dt>**CMAX\_KEYS**</dt> <dt>8</dt> </dl>          | Defines the maximum number of INDEXKEY records (8) that can be used from the TABLEINDEX structure.<br/>                                                          |



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl> |



 

 





