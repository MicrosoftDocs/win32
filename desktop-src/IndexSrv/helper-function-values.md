---
title: Helper-Function Values
description: Values 0xHHHH1800 to 0xHHHH182F are return values produced by the content-indexing helper functions. The following table gives the content-indexing helper-function values in alphabetical order.
ms.assetid: dae558db-00ce-4a5c-b771-0eb77e703c22
topic_type:
- apiref
api_name:
- CI_CORRUPT_CATALOG
- CI_CORRUPT_DATABASE
- CI_CORRUPT_FILTER_BUFFER
- CI_E_ALREADY_INITIALIZED
- CI_E_BUFFERTOOSMALL
- CI_E_CARDINALITY_MISMATCH
- CI_E_CLIENT_FILTER_ABORT
- CI_E_CONFIG_DISK_FULL
- CI_E_DISK_FULL
- CI_E_DUPLICATE_NOTIFICATION
- CI_E_ENUMERATION_STARTED
- CI_E_FILTERING_DISABLED
- CI_E_INVALID_FLAGS_COMBINATION
- CI_E_INVALID_STATE
- CI_E_LOGON_FAILURE
- CI_E_NO_CATALOG
- CI_E_NOT_FOUND
- CI_E_NOT_INITIALIZED
- CI_E_NOT_RUNNING
- CI_E_OUTOFSEQ_INCREMENT_DATA
- CI_E_PROPERTY_NOT_CACHED
- CI_E_PROPERTY_TOOLARGE
- CI_E_SHARING_VIOLATION
- CI_E_SHUTDOWN
- CI_E_STRANGE_PAGEORSECTOR_SIZE
- CI_E_TIMEOUT
- CI_E_UPDATES_DISABLED
- CI_E_USE_DEFAULT_PID
- CI_E_WORKID_NOTVALID
- CI_INCORRECT_VERSION
- CI_INVALID_INDEX
- CI_INVALID_PARTITION
- CI_INVALID_PRIORITY
- CI_NO_CATALOG
- CI_NO_STARTING_KEY
- CI_OUT_OF_INDEX_IDS
- CI_PROPSTORE_INCONSISTENCY
- CI_S_CAT_STOPPED
- CI_S_END_OF_ENUMERATION
- CI_S_NO_DOCSTORE
- CI_S_WORKID_DELETED
api_location:
- Cierror.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Helper-Function Values

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Values 0x*HHHH*1800 to 0x*HHHH*182F are return values produced by the content-indexing helper functions. The following table gives the content-indexing helper-function values in alphabetical order.



| Constant/value                                                                                                                                                                                                                                                                      | Description                                                                                               |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| <span id="CI_CORRUPT_CATALOG"></span><span id="ci_corrupt_catalog"></span><dl> <dt>**CI\_CORRUPT\_CATALOG**</dt> <dt>0xC0041801</dt> </dl>                                       | The Content Index meta data is corrupt.<br/>                                                        |
| <span id="CI_CORRUPT_DATABASE"></span><span id="ci_corrupt_database"></span><dl> <dt>**CI\_CORRUPT\_DATABASE**</dt> <dt>0xC0041800</dt> </dl>                                    | The Content Index is corrupt.<br/>                                                                  |
| <span id="CI_CORRUPT_FILTER_BUFFER"></span><span id="ci_corrupt_filter_buffer"></span><dl> <dt>**CI\_CORRUPT\_FILTER\_BUFFER**</dt> <dt>0xC0041807</dt> </dl>                    | The filter buffer is corrupt.<br/>                                                                  |
| <span id="CI_E_ALREADY_INITIALIZED"></span><span id="ci_e_already_initialized"></span><dl> <dt>**CI\_E\_ALREADY\_INITIALIZED**</dt> <dt>0x8004180A</dt> </dl>                    | The object is already initialized.<br/>                                                             |
| <span id="CI_E_BUFFERTOOSMALL"></span><span id="ci_e_buffertoosmall"></span><dl> <dt>**CI\_E\_BUFFERTOOSMALL**</dt> <dt>0x8004180C</dt> </dl>                                    | The buffer is too small.<br/>                                                                       |
| <span id="CI_E_CARDINALITY_MISMATCH"></span><span id="ci_e_cardinality_mismatch"></span><dl> <dt>**CI\_E\_CARDINALITY\_MISMATCH**</dt> <dt>0x80041827</dt> </dl>                 | Mismatch in cardinality of machine(s)/catalog(s)/scope(s).<br/>                                     |
| <span id="CI_E_CLIENT_FILTER_ABORT"></span><span id="ci_e_client_filter_abort"></span><dl> <dt>**CI\_E\_CLIENT\_FILTER\_ABORT**</dt> <dt>0xC0041824</dt> </dl>                   | Filtering of object was aborted by client.<br/>                                                     |
| <span id="CI_E_CONFIG_DISK_FULL"></span><span id="ci_e_config_disk_full"></span><dl> <dt>**CI\_E\_CONFIG\_DISK\_FULL**</dt> <dt>0x80041828</dt> </dl>                            | The disk has reached its configured space limit.<br/>                                               |
| <span id="CI_E_DISK_FULL"></span><span id="ci_e_disk_full"></span><dl> <dt>**CI\_E\_DISK\_FULL**</dt> <dt>0x80041811</dt> </dl>                                                  | The disk is full and the specified operation cannot be done.<br/>                                   |
| <span id="CI_E_DUPLICATE_NOTIFICATION"></span><span id="ci_e_duplicate_notification"></span><dl> <dt>**CI\_E\_DUPLICATE\_NOTIFICATION**</dt> <dt>0x80041817</dt> </dl>           | There were two notifications for the same workid.<br/>                                              |
| <span id="CI_E_ENUMERATION_STARTED"></span><span id="ci_e_enumeration_started"></span><dl> <dt>**CI\_E\_ENUMERATION\_STARTED**</dt> <dt>0xC0041822</dt> </dl>                    | Enumeration has already been started for this query.<br/>                                           |
| <span id="CI_E_FILTERING_DISABLED"></span><span id="ci_e_filtering_disabled"></span><dl> <dt>**CI\_E\_FILTERING\_DISABLED**</dt> <dt>0x80041810</dt> </dl>                       | Filtering is disabled in this content index.<br/>                                                   |
| <span id="CI_E_INVALID_FLAGS_COMBINATION"></span><span id="ci_e_invalid_flags_combination"></span><dl> <dt>**CI\_E\_INVALID\_FLAGS\_COMBINATION**</dt> <dt>0x80041819</dt> </dl> | The combination of flags specified is invalid.<br/>                                                 |
| <span id="CI_E_INVALID_STATE"></span><span id="ci_e_invalid_state"></span><dl> <dt>**CI\_E\_INVALID\_STATE**</dt> <dt>0x8004180F</dt> </dl>                                      | The object is not in a valid state.<br/>                                                            |
| <span id="CI_E_LOGON_FAILURE"></span><span id="ci_e_logon_failure"></span><dl> <dt>**CI\_E\_LOGON\_FAILURE**</dt> <dt>0x8004181C</dt> </dl>                                      | A logon permission violation caused a failure.<br/>                                                 |
| <span id="CI_E_NO_CATALOG"></span><span id="ci_e_no_catalog"></span><dl> <dt>**CI\_E\_NO\_CATALOG**</dt> <dt>0x8004181D</dt> </dl>                                               | There is no catalog.<br/>                                                                           |
| <span id="CI_E_NOT_FOUND"></span><span id="ci_e_not_found"></span><dl> <dt>**CI\_E\_NOT\_FOUND**</dt> <dt>0x80041815</dt> </dl>                                                  | The object was not found.<br/>                                                                      |
| <span id="CI_E_NOT_INITIALIZED"></span><span id="ci_e_not_initialized"></span><dl> <dt>**CI\_E\_NOT\_INITIALIZED**</dt> <dt>0x8004180B</dt> </dl>                                | The object is not initialized.<br/>                                                                 |
| <span id="CI_E_NOT_RUNNING"></span><span id="ci_e_not_running"></span><dl> <dt>**CI\_E\_NOT\_RUNNING**</dt> <dt>0x80041820</dt> </dl>                                            | Service is not running.<br/>                                                                        |
| <span id="CI_E_OUTOFSEQ_INCREMENT_DATA"></span><span id="ci_e_outofseq_increment_data"></span><dl> <dt>**CI\_E\_OUTOFSEQ\_INCREMENT\_DATA**</dt> <dt>0x8004181A</dt> </dl>       | The incremental data given to load is not valid. It may be out of sequence.<br/>                    |
| <span id="CI_E_PROPERTY_NOT_CACHED"></span><span id="ci_e_property_not_cached"></span><dl> <dt>**CI\_E\_PROPERTY\_NOT\_CACHED**</dt> <dt>0x8004180D</dt> </dl>                   | The given property is not cached.<br/>                                                              |
| <span id="CI_E_PROPERTY_TOOLARGE"></span><span id="ci_e_property_toolarge"></span><dl> <dt>**CI\_E\_PROPERTY\_TOOLARGE**</dt> <dt>0xC0041823</dt> </dl>                          | The specified variable length property is too large for the property cache.<br/>                    |
| <span id="CI_E_SHARING_VIOLATION"></span><span id="ci_e_sharing_violation"></span><dl> <dt>**CI\_E\_SHARING\_VIOLATION**</dt> <dt>0x8004181B</dt> </dl>                          | A sharing or locking violation caused a failure.<br/>                                               |
| <span id="CI_E_SHUTDOWN"></span><span id="ci_e_shutdown"></span><dl> <dt>**CI\_E\_SHUTDOWN**</dt> <dt>0x80041812</dt> </dl>                                                      | Content Index has been shut down.<br/>                                                              |
| <span id="CI_E_STRANGE_PAGEORSECTOR_SIZE"></span><span id="ci_e_strange_pageorsector_size"></span><dl> <dt>**CI\_E\_STRANGE\_PAGEORSECTOR\_SIZE**</dt> <dt>0x8004181E</dt> </dl> | Page size is not an integral multiple of the sector size of the volume where index is located.<br/> |
| <span id="CI_E_TIMEOUT"></span><span id="ci_e_timeout"></span><dl> <dt>**CI\_E\_TIMEOUT**</dt> <dt>0x8004181F</dt> </dl>                                                         | Service is busy.<br/>                                                                               |
| <span id="CI_E_UPDATES_DISABLED"></span><span id="ci_e_updates_disabled"></span><dl> <dt>**CI\_E\_UPDATES\_DISABLED**</dt> <dt>0x80041818</dt> </dl>                             | A document update was rejected because updates were disabled.<br/>                                  |
| <span id="CI_E_USE_DEFAULT_PID"></span><span id="ci_e_use_default_pid"></span><dl> <dt>**CI\_E\_USE\_DEFAULT\_PID**</dt> <dt>0x80041816</dt> </dl>                               | The passed-in property ID is not supported.<br/>                                                    |
| <span id="CI_E_WORKID_NOTVALID"></span><span id="ci_e_workid_notvalid"></span><dl> <dt>**CI\_E\_WORKID\_NOTVALID**</dt> <dt>0x80041813</dt> </dl>                                | The work ID is not valid.<br/>                                                                      |
| <span id="CI_INCORRECT_VERSION"></span><span id="ci_incorrect_version"></span><dl> <dt>**CI\_INCORRECT\_VERSION**</dt> <dt>0xC0041821</dt> </dl>                                 | The Content Index data on disk is for the wrong version.<br/>                                       |
| <span id="CI_INVALID_INDEX"></span><span id="ci_invalid_index"></span><dl> <dt>**CI\_INVALID\_INDEX**</dt> <dt>0xC0041808</dt> </dl>                                             | The index is invalid.<br/>                                                                          |
| <span id="CI_INVALID_PARTITION"></span><span id="ci_invalid_partition"></span><dl> <dt>**CI\_INVALID\_PARTITION**</dt> <dt>0xC0041802</dt> </dl>                                 | The Content Index partition is invalid.<br/>                                                        |
| <span id="CI_INVALID_PRIORITY"></span><span id="ci_invalid_priority"></span><dl> <dt>**CI\_INVALID\_PRIORITY**</dt> <dt>0xC0041803</dt> </dl>                                    | The priority is invalid.<br/>                                                                       |
| <span id="CI_NO_CATALOG"></span><span id="ci_no_catalog"></span><dl> <dt>**CI\_NO\_CATALOG**</dt> <dt>0xC0041806</dt> </dl>                                                      | There is no catalog.<br/>                                                                           |
| <span id="CI_NO_STARTING_KEY"></span><span id="ci_no_starting_key"></span><dl> <dt>**CI\_NO\_STARTING\_KEY**</dt> <dt>0xC0041804</dt> </dl>                                      | There is no starting key.<br/>                                                                      |
| <span id="CI_OUT_OF_INDEX_IDS"></span><span id="ci_out_of_index_ids"></span><dl> <dt>**CI\_OUT\_OF\_INDEX\_IDS**</dt> <dt>0xC0041805</dt> </dl>                                  | The Content Index is out of index ids.<br/>                                                         |
| <span id="CI_PROPSTORE_INCONSISTENCY"></span><span id="ci_propstore_inconsistency"></span><dl> <dt>**CI\_PROPSTORE\_INCONSISTENCY**</dt> <dt>0xC0041809</dt> </dl>               | Inconsistency in property store detected.<br/>                                                      |
| <span id="CI_S_CAT_STOPPED"></span><span id="ci_s_cat_stopped"></span><dl> <dt>**CI\_S\_CAT\_STOPPED**</dt> <dt>0x00041826</dt> </dl>                                            | The catalog has been stopped.<br/>                                                                  |
| <span id="CI_S_END_OF_ENUMERATION"></span><span id="ci_s_end_of_enumeration"></span><dl> <dt>**CI\_S\_END\_OF\_ENUMERATION**</dt> <dt>0x00041814</dt> </dl>                      | There are no more documents to enumerate.<br/>                                                      |
| <span id="CI_S_NO_DOCSTORE"></span><span id="ci_s_no_docstore"></span><dl> <dt>**CI\_S\_NO\_DOCSTORE**</dt> <dt>0x00041825</dt> </dl>                                            | For administrative connections from client without association to a docstore.<br/>                  |
| <span id="CI_S_WORKID_DELETED"></span><span id="ci_s_workid_deleted"></span><dl> <dt>**CI\_S\_WORKID\_DELETED**</dt> <dt>0x0004180E</dt> </dl>                                   | The workid is deleted.<br/>                                                                         |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>Cierror.h</dt> </dl> |



 

 





