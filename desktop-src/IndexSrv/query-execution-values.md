---
title: Query-Execution Values
description: Values 0xHHHH1600 to 0xHHHH164F are query return values produced when resolving a query string against the set of indexes in a catalog. The following table gives the query-execution values in alphabetical order.
ms.assetid: abfb70e3-206e-411b-ab2e-75d0b91cb248
topic_type:
- apiref
api_name:
- QUERY_E_ALLNOISE
- QUERY_E_DIR_ON_REMOVABLE_DRIVE
- QUERY_E_DUPLICATE_OUTPUT_COLUMN
- QUERY_E_FAILED
- QUERY_E_INVALID_DIRECTORY
- QUERY_E_INVALID_OUTPUT_COLUMN
- QUERY_E_INVALIDCATEGORIZE
- QUERY_E_INVALIDQUERY
- QUERY_E_INVALIDRESTRICTION
- QUERY_E_INVALIDSORT
- QUERY_E_TIMEDOUT
- QUERY_E_TOOCOMPLEX
- QUERY_S_NO_QUERY
api_location:
- Cierror.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Query-Execution Values

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Values 0x*HHHH*1600 to 0x*HHHH*164F are query return values produced when resolving a query string against the set of indexes in a catalog. The following table gives the query-execution values in alphabetical order.



| Constant/value                                                                                                                                                                                                                                                                         | Description                                                                                 |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| <span id="QUERY_E_ALLNOISE"></span><span id="query_e_allnoise"></span><dl> <dt>**QUERY\_E\_ALLNOISE**</dt> <dt>0x80041605</dt> </dl>                                                | The query contained only ignored words.<br/>                                          |
| <span id="QUERY_E_DIR_ON_REMOVABLE_DRIVE"></span><span id="query_e_dir_on_removable_drive"></span><dl> <dt>**QUERY\_E\_DIR\_ON\_REMOVABLE\_DRIVE**</dt> <dt>0x8004160B</dt> </dl>   | Specified directory is on a removable medium.<br/>                                    |
| <span id="QUERY_E_DUPLICATE_OUTPUT_COLUMN"></span><span id="query_e_duplicate_output_column"></span><dl> <dt>**QUERY\_E\_DUPLICATE\_OUTPUT\_COLUMN**</dt> <dt>0x80041608</dt> </dl> | One or more columns in the output column list is a duplicate.<br/>                    |
| <span id="QUERY_E_FAILED"></span><span id="query_e_failed"></span><dl> <dt>**QUERY\_E\_FAILED**</dt> <dt>0x80041600</dt> </dl>                                                      | Call failed for unknown reason.<br/>                                                  |
| <span id="QUERY_E_INVALID_DIRECTORY"></span><span id="query_e_invalid_directory"></span><dl> <dt>**QUERY\_E\_INVALID\_DIRECTORY**</dt> <dt>0x8004160A</dt> </dl>                    | Invalid directory name.<br/>                                                          |
| <span id="QUERY_E_INVALID_OUTPUT_COLUMN"></span><span id="query_e_invalid_output_column"></span><dl> <dt>**QUERY\_E\_INVALID\_OUTPUT\_COLUMN**</dt> <dt>0x80041609</dt> </dl>       | One or more columns in the output column list is not valid.<br/>                      |
| <span id="QUERY_E_INVALIDCATEGORIZE"></span><span id="query_e_invalidcategorize"></span><dl> <dt>**QUERY\_E\_INVALIDCATEGORIZE**</dt> <dt>0x80041604</dt> </dl>                     | An invalid categorization order was requested.<br/>                                   |
| <span id="QUERY_E_INVALIDQUERY"></span><span id="query_e_invalidquery"></span><dl> <dt>**QUERY\_E\_INVALIDQUERY**</dt> <dt>0x80041601</dt> </dl>                                    | Invalid parameter.<br/>                                                               |
| <span id="QUERY_E_INVALIDRESTRICTION"></span><span id="query_e_invalidrestriction"></span><dl> <dt>**QUERY\_E\_INVALIDRESTRICTION**</dt> <dt>0x80041602</dt> </dl>                  | The query restriction could not be parsed.<br/>                                       |
| <span id="QUERY_E_INVALIDSORT"></span><span id="query_e_invalidsort"></span><dl> <dt>**QUERY\_E\_INVALIDSORT**</dt> <dt>0x80041603</dt> </dl>                                       | An invalid sort order was requested.<br/>                                             |
| <span id="QUERY_E_TIMEDOUT"></span><span id="query_e_timedout"></span><dl> <dt>**QUERY\_E\_TIMEDOUT**</dt> <dt>0x80041607</dt> </dl>                                                | The query exceeded its execution time limit.<br/>                                     |
| <span id="QUERY_E_TOOCOMPLEX"></span><span id="query_e_toocomplex"></span><dl> <dt>**QUERY\_E\_TOOCOMPLEX**</dt> <dt>0x80041606</dt> </dl>                                          | The query was too complex to be executed.<br/>                                        |
| <span id="QUERY_S_NO_QUERY"></span><span id="query_s_no_query"></span><dl> <dt>**QUERY\_S\_NO\_QUERY**</dt> <dt>0x8004160C</dt> </dl>                                               | The catalog is in a state where indexing continues, but queries are not allowed.<br/> |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>Cierror.h</dt> </dl> |



 

 





