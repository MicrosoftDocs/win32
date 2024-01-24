---
title: Client Error Codes (Winbio\_err.h)
description: Error codes defined in the Winbio\_err.h header file.
ms.assetid: fc1565d2-43f1-45cd-ab84-4e557cf78107
topic_type:
- apiref
api_name:
- WINBIO_E_UNSUPPORTED_FACTOR
- WINBIO_E_INVALID_UNIT
- WINBIO_E_UNKNOWN_ID
- WINBIO_E_CANCELED
- WINBIO_E_NO_MATCH
- WINBIO_E_CAPTURE_ABORTED
- WINBIO_E_ENROLLMENT_IN_PROGRESS
- WINBIO_E_BAD_CAPTURE
- WINBIO_E_INVALID_CONTROL_CODE
- WINBIO_E_DATA_COLLECTION_IN_PROGRESS
- WINBIO_E_UNSUPPORTED_DATA_FORMAT
- WINBIO_E_UNSUPPORTED_DATA_TYPE
- WINBIO_E_UNSUPPORTED_PURPOSE
- WINBIO_E_INVALID_DEVICE_STATE
- WINBIO_E_DEVICE_BUSY
- WINBIO_E_DATABASE_CANT_CREATE
- WINBIO_E_DATABASE_CANT_OPEN
- WINBIO_E_DATABASE_CANT_CLOSE
- WINBIO_E_DATABASE_CANT_ERASE
- WINBIO_E_DATABASE_CANT_FIND
- WINBIO_E_DATABASE_ALREADY_EXISTS
- WINBIO_E_DATABASE_FULL
- WINBIO_E_DATABASE_LOCKED
- WINBIO_E_DATABASE_CORRUPTED
- WINBIO_E_DATABASE_NO_SUCH_RECORD
- WINBIO_E_DUPLICATE_ENROLLMENT
- WINBIO_E_DATABASE_READ_ERROR
- WINBIO_E_DATABASE_WRITE_ERROR
- WINBIO_E_DATABASE_NO_RESULTS
- WINBIO_E_DATABASE_NO_MORE_RECORDS
- WINBIO_E_DATABASE_EOF
- WINBIO_E_DATABASE_BAD_INDEX_VECTOR
- WINBIO_E_INCORRECT_BSP
- WINBIO_E_INCORRECT_SENSOR_POOL
- WINBIO_E_NO_CAPTURE_DATA
- WINBIO_E_INVALID_SENSOR_MODE
- WINBIO_E_LOCK_VIOLATION
- WINBIO_E_DUPLICATE_TEMPLATE
- WINBIO_E_INVALID_OPERATION
- WINBIO_E_SESSION_BUSY
- WINBIO_E_CRED_PROV_DISABLED
- WINBIO_E_CRED_PROV_NO_CREDENTIAL
- WINBIO_E_DISABLED
- WINBIO_E_CONFIGURATION_FAILURE
- WINBIO_E_SENSOR_UNAVAILABLE
- WINBIO_E_SAS_ENABLED
- WINBIO_E_DEVICE_FAILURE
- WINBIO_E_FAST_USER_SWITCH_DISABLED
- WINBIO_E_NOT_ACTIVE_CONSOLE
- WINBIO_E_EVENT_MONITOR_ACTIVE
- WINBIO_E_INVALID_PROPERTY_TYPE
- WINBIO_E_INVALID_PROPERTY_ID
- WINBIO_E_UNSUPPORTED_PROPERTY
- WINBIO_E_ADAPTER_INTEGRITY_FAILURE
- WINBIO_I_MORE_DATA
api_location:
- Winbio_err.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Client Error Codes

The following error codes are defined in the Winbio\_err.h header file.



| Constant/value                                                                                                                                                                                                                                                                                         | Description                                                                                                       |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_E_UNSUPPORTED_FACTOR"></span><span id="winbio_e_unsupported_factor"></span><dl> <dt>**WINBIO\_E\_UNSUPPORTED\_FACTOR**</dt> <dt>0x80098001</dt> </dl>                              | The specified biometric factor is not supported.<br/>                                                       |
| <span id="WINBIO_E_INVALID_UNIT"></span><span id="winbio_e_invalid_unit"></span><dl> <dt>**WINBIO\_E\_INVALID\_UNIT**</dt> <dt>0x80098002</dt> </dl>                                                | The unit ID number does not correspond to a valid biometric device.<br/>                                    |
| <span id="WINBIO_E_UNKNOWN_ID"></span><span id="winbio_e_unknown_id"></span><dl> <dt>**WINBIO\_E\_UNKNOWN\_ID**</dt> <dt>0x80098003</dt> </dl>                                                      | The biometric sample does not match any known identity.<br/>                                                |
| <span id="WINBIO_E_CANCELED"></span><span id="winbio_e_canceled"></span><dl> <dt>**WINBIO\_E\_CANCELED**</dt> <dt>0x80098004</dt> </dl>                                                             | The biometric operation was canceled before it could complete.<br/>                                         |
| <span id="WINBIO_E_NO_MATCH"></span><span id="winbio_e_no_match"></span><dl> <dt>**WINBIO\_E\_NO\_MATCH**</dt> <dt>0x80098005</dt> </dl>                                                            | The biometric sample does not match the specified identity or sub-factor.<br/>                              |
| <span id="WINBIO_E_CAPTURE_ABORTED"></span><span id="winbio_e_capture_aborted"></span><dl> <dt>**WINBIO\_E\_CAPTURE\_ABORTED**</dt> <dt>0x80098006</dt> </dl>                                       | A biometric sample could not be captured because the capture operation was aborted.<br/>                    |
| <span id="WINBIO_E_ENROLLMENT_IN_PROGRESS"></span><span id="winbio_e_enrollment_in_progress"></span><dl> <dt>**WINBIO\_E\_ENROLLMENT\_IN\_PROGRESS**</dt> <dt>0x80098007</dt> </dl>                 | An enrollment transaction could not be started because another enrollment is already in progress.<br/>      |
| <span id="WINBIO_E_BAD_CAPTURE"></span><span id="winbio_e_bad_capture"></span><dl> <dt>**WINBIO\_E\_BAD\_CAPTURE**</dt> <dt>0x80098008</dt> </dl>                                                   | The captured sample cannot be used for further biometric operations.<br/>                                   |
| <span id="WINBIO_E_INVALID_CONTROL_CODE"></span><span id="winbio_e_invalid_control_code"></span><dl> <dt>**WINBIO\_E\_INVALID\_CONTROL\_CODE**</dt> <dt>0x80098009</dt> </dl>                       | The biometric unit does not support the specified unit control code.<br/>                                   |
| <span id="WINBIO_E_DATA_COLLECTION_IN_PROGRESS"></span><span id="winbio_e_data_collection_in_progress"></span><dl> <dt>**WINBIO\_E\_DATA\_COLLECTION\_IN\_PROGRESS**</dt> <dt>0x8009800B</dt> </dl> | A pending data collection operation is already in progress.<br/>                                            |
| <span id="WINBIO_E_UNSUPPORTED_DATA_FORMAT"></span><span id="winbio_e_unsupported_data_format"></span><dl> <dt>**WINBIO\_E\_UNSUPPORTED\_DATA\_FORMAT**</dt> <dt>0x8009800C</dt> </dl>              | The biometric sensor driver does not support the requested data format.<br/>                                |
| <span id="WINBIO_E_UNSUPPORTED_DATA_TYPE"></span><span id="winbio_e_unsupported_data_type"></span><dl> <dt>**WINBIO\_E\_UNSUPPORTED\_DATA\_TYPE**</dt> <dt>0x8009800D</dt> </dl>                    | The biometric sensor driver does not support the requested data type.<br/>                                  |
| <span id="WINBIO_E_UNSUPPORTED_PURPOSE"></span><span id="winbio_e_unsupported_purpose"></span><dl> <dt>**WINBIO\_E\_UNSUPPORTED\_PURPOSE**</dt> <dt>0x8009800E</dt> </dl>                           | The biometric sensor driver does not support the requested data purpose.<br/>                               |
| <span id="WINBIO_E_INVALID_DEVICE_STATE"></span><span id="winbio_e_invalid_device_state"></span><dl> <dt>**WINBIO\_E\_INVALID\_DEVICE\_STATE**</dt> <dt>0x8009800F</dt> </dl>                       | The biometric unit is not in the proper state to perform the specified operation.<br/>                      |
| <span id="WINBIO_E_DEVICE_BUSY"></span><span id="winbio_e_device_busy"></span><dl> <dt>**WINBIO\_E\_DEVICE\_BUSY**</dt> <dt>0x80098010</dt> </dl>                                                   | The operation could not be performed because the sensor device was busy.<br/>                               |
| <span id="WINBIO_E_DATABASE_CANT_CREATE"></span><span id="winbio_e_database_cant_create"></span><dl> <dt>**WINBIO\_E\_DATABASE\_CANT\_CREATE**</dt> <dt>0x80098011</dt> </dl>                       | The storage adapter was not able to create a new database.<br/>                                             |
| <span id="WINBIO_E_DATABASE_CANT_OPEN"></span><span id="winbio_e_database_cant_open"></span><dl> <dt>**WINBIO\_E\_DATABASE\_CANT\_OPEN**</dt> <dt>0x80098012</dt> </dl>                             | The storage adapter was not able to open an existing database.<br/>                                         |
| <span id="WINBIO_E_DATABASE_CANT_CLOSE"></span><span id="winbio_e_database_cant_close"></span><dl> <dt>**WINBIO\_E\_DATABASE\_CANT\_CLOSE**</dt> <dt>0x80098013</dt> </dl>                          | The storage adapter was not able to close a database.<br/>                                                  |
| <span id="WINBIO_E_DATABASE_CANT_ERASE"></span><span id="winbio_e_database_cant_erase"></span><dl> <dt>**WINBIO\_E\_DATABASE\_CANT\_ERASE**</dt> <dt>0x80098014</dt> </dl>                          | The storage adapter was not able to erase a database.<br/>                                                  |
| <span id="WINBIO_E_DATABASE_CANT_FIND"></span><span id="winbio_e_database_cant_find"></span><dl> <dt>**WINBIO\_E\_DATABASE\_CANT\_FIND**</dt> <dt>0x80098015</dt> </dl>                             | The storage adapter was not able to find a database.<br/>                                                   |
| <span id="WINBIO_E_DATABASE_ALREADY_EXISTS"></span><span id="winbio_e_database_already_exists"></span><dl> <dt>**WINBIO\_E\_DATABASE\_ALREADY\_EXISTS**</dt> <dt>0x80098016</dt> </dl>              | The storage adapter was not able to create a database because the specified database already exists.<br/>   |
| <span id="WINBIO_E_DATABASE_FULL"></span><span id="winbio_e_database_full"></span><dl> <dt>**WINBIO\_E\_DATABASE\_FULL**</dt> <dt>0x80098018</dt> </dl>                                             | The storage adapter was not able to add a record to the database because the database is full.<br/>         |
| <span id="WINBIO_E_DATABASE_LOCKED"></span><span id="winbio_e_database_locked"></span><dl> <dt>**WINBIO\_E\_DATABASE\_LOCKED**</dt> <dt>0x80098019</dt> </dl>                                       | The database is locked and its contents are inaccessible.<br/>                                              |
| <span id="WINBIO_E_DATABASE_CORRUPTED"></span><span id="winbio_e_database_corrupted"></span><dl> <dt>**WINBIO\_E\_DATABASE\_CORRUPTED**</dt> <dt>0x8009801A</dt> </dl>                              | The contents of the database have become corrupted and are inaccessible.<br/>                               |
| <span id="WINBIO_E_DATABASE_NO_SUCH_RECORD"></span><span id="winbio_e_database_no_such_record"></span><dl> <dt>**WINBIO\_E\_DATABASE\_NO\_SUCH\_RECORD**</dt> <dt>0x8009801B</dt> </dl>             | No records were deleted because the specified identity and sub-factor are not present in the database.<br/> |
| <span id="WINBIO_E_DUPLICATE_ENROLLMENT"></span><span id="winbio_e_duplicate_enrollment"></span><dl> <dt>**WINBIO\_E\_DUPLICATE\_ENROLLMENT**</dt> <dt>0x8009801C</dt> </dl>                        | The specified identity and sub-factor are already enrolled in the database.<br/>                            |
| <span id="WINBIO_E_DATABASE_READ_ERROR"></span><span id="winbio_e_database_read_error"></span><dl> <dt>**WINBIO\_E\_DATABASE\_READ\_ERROR**</dt> <dt>0x8009801D</dt> </dl>                          | An error occurred while trying to read from the database.<br/>                                              |
| <span id="WINBIO_E_DATABASE_WRITE_ERROR"></span><span id="winbio_e_database_write_error"></span><dl> <dt>**WINBIO\_E\_DATABASE\_WRITE\_ERROR**</dt> <dt>0x8009801E</dt> </dl>                       | An error occurred while trying to write to the database.<br/>                                               |
| <span id="WINBIO_E_DATABASE_NO_RESULTS"></span><span id="winbio_e_database_no_results"></span><dl> <dt>**WINBIO\_E\_DATABASE\_NO\_RESULTS**</dt> <dt>0x8009801F</dt> </dl>                          | No records in the database matched the query.<br/>                                                          |
| <span id="WINBIO_E_DATABASE_NO_MORE_RECORDS"></span><span id="winbio_e_database_no_more_records"></span><dl> <dt>**WINBIO\_E\_DATABASE\_NO\_MORE\_RECORDS**</dt> <dt>0x80098020</dt> </dl>          | All records from the most recent database query have been retrieved.<br/>                                   |
| <span id="WINBIO_E_DATABASE_EOF"></span><span id="winbio_e_database_eof"></span><dl> <dt>**WINBIO\_E\_DATABASE\_EOF**</dt> <dt>0x80098021</dt> </dl>                                                | A database operation unexpectedly encountered the end of the file.<br/>                                     |
| <span id="WINBIO_E_DATABASE_BAD_INDEX_VECTOR"></span><span id="winbio_e_database_bad_index_vector"></span><dl> <dt>**WINBIO\_E\_DATABASE\_BAD\_INDEX\_VECTOR**</dt> <dt>0x80098022</dt> </dl>       | A database operation failed due to a malformed index vector.<br/>                                           |
| <span id="WINBIO_E_INCORRECT_BSP"></span><span id="winbio_e_incorrect_bsp"></span><dl> <dt>**WINBIO\_E\_INCORRECT\_BSP**</dt> <dt>0x80098024</dt> </dl>                                             | The biometric unit does not belong to the specified service provider.<br/>                                  |
| <span id="WINBIO_E_INCORRECT_SENSOR_POOL"></span><span id="winbio_e_incorrect_sensor_pool"></span><dl> <dt>**WINBIO\_E\_INCORRECT\_SENSOR\_POOL**</dt> <dt>0x80098025</dt> </dl>                    | The biometric unit does not belong to the specified sensor pool.<br/>                                       |
| <span id="WINBIO_E_NO_CAPTURE_DATA"></span><span id="winbio_e_no_capture_data"></span><dl> <dt>**WINBIO\_E\_NO\_CAPTURE\_DATA**</dt> <dt>0x80098026</dt> </dl>                                      | The sensor adapter capture buffer is empty.<br/>                                                            |
| <span id="WINBIO_E_INVALID_SENSOR_MODE"></span><span id="winbio_e_invalid_sensor_mode"></span><dl> <dt>**WINBIO\_E\_INVALID\_SENSOR\_MODE**</dt> <dt>0x80098027</dt> </dl>                          | The sensor adapter does not support the sensor mode specified in the configuration.<br/>                    |
| <span id="WINBIO_E_LOCK_VIOLATION"></span><span id="winbio_e_lock_violation"></span><dl> <dt>**WINBIO\_E\_LOCK\_VIOLATION**</dt> <dt>0x8009802A</dt> </dl>                                          | The requested operation cannot be performed due to a locking conflict.<br/>                                 |
| <span id="WINBIO_E_DUPLICATE_TEMPLATE"></span><span id="winbio_e_duplicate_template"></span><dl> <dt>**WINBIO\_E\_DUPLICATE\_TEMPLATE**</dt> <dt>0x8009802B</dt> </dl>                              | The data in a biometric template matches that of another template already in the database.<br/>             |
| <span id="WINBIO_E_INVALID_OPERATION"></span><span id="winbio_e_invalid_operation"></span><dl> <dt>**WINBIO\_E\_INVALID\_OPERATION**</dt> <dt>0x8009802C</dt> </dl>                                 | The requested operation is not valid for the current state of the session or the biometric unit.<br/>       |
| <span id="WINBIO_E_SESSION_BUSY"></span><span id="winbio_e_session_busy"></span><dl> <dt>**WINBIO\_E\_SESSION\_BUSY**</dt> <dt>0x8009802D</dt> </dl>                                                | The session cannot begin a new operation because another operation is already in progress.<br/>             |
| <span id="WINBIO_E_CRED_PROV_DISABLED"></span><span id="winbio_e_cred_prov_disabled"></span><dl> <dt>**WINBIO\_E\_CRED\_PROV\_DISABLED**</dt> <dt>0x80098030</dt> </dl>                             | System policy settings have disabled the biometric credential provider.<br/>                                |
| <span id="WINBIO_E_CRED_PROV_NO_CREDENTIAL"></span><span id="winbio_e_cred_prov_no_credential"></span><dl> <dt>**WINBIO\_E\_CRED\_PROV\_NO\_CREDENTIAL**</dt> <dt>0x80098031</dt> </dl>             | The requested credential was not found.<br/>                                                                |
| <span id="WINBIO_E_DISABLED"></span><span id="winbio_e_disabled"></span><dl> <dt>**WINBIO\_E\_DISABLED**</dt> <dt>0x80098032</dt> </dl>                                                             | System policy settings have disabled the biometric service.<br/>                                            |
| <span id="WINBIO_E_CONFIGURATION_FAILURE"></span><span id="winbio_e_configuration_failure"></span><dl> <dt>**WINBIO\_E\_CONFIGURATION\_FAILURE**</dt> <dt>0x80098033</dt> </dl>                     | The biometric unit could not be configured.<br/>                                                            |
| <span id="WINBIO_E_SENSOR_UNAVAILABLE"></span><span id="winbio_e_sensor_unavailable"></span><dl> <dt>**WINBIO\_E\_SENSOR\_UNAVAILABLE**</dt> <dt>0x80098034</dt> </dl>                              | A private pool cannot be created because one or more biometric units are not available.<br/>                |
| <span id="WINBIO_E_SAS_ENABLED"></span><span id="winbio_e_sas_enabled"></span><dl> <dt>**WINBIO\_E\_SAS\_ENABLED**</dt> <dt>0x80098035</dt> </dl>                                                   | A secure attention sequence (CTRL-ALT-DELETE) is required for logon.<br/>                                   |
| <span id="WINBIO_E_DEVICE_FAILURE"></span><span id="winbio_e_device_failure"></span><dl> <dt>**WINBIO\_E\_DEVICE\_FAILURE**</dt> <dt>0x80098036</dt> </dl>                                          | A biometric sensor has failed.<br/>                                                                         |
| <span id="WINBIO_E_FAST_USER_SWITCH_DISABLED"></span><span id="winbio_e_fast_user_switch_disabled"></span><dl> <dt>**WINBIO\_E\_FAST\_USER\_SWITCH\_DISABLED**</dt> <dt>0x80098037</dt> </dl>       | >Fast user switching is disabled.<br/>                                                                   |
| <span id="WINBIO_E_NOT_ACTIVE_CONSOLE"></span><span id="winbio_e_not_active_console"></span><dl> <dt>**WINBIO\_E\_NOT\_ACTIVE\_CONSOLE**</dt> <dt>0x80098038</dt> </dl>                             | The System sensor pool cannot be opened from Terminal Server client sessions.<br/>                          |
| <span id="WINBIO_E_EVENT_MONITOR_ACTIVE"></span><span id="winbio_e_event_monitor_active"></span><dl> <dt>**WINBIO\_E\_EVENT\_MONITOR\_ACTIVE**</dt> <dt>0x80098039 </dt> </dl>                      | There is already an active event monitor associated with the specified session.<br/>                        |
| <span id="WINBIO_E_INVALID_PROPERTY_TYPE"></span><span id="winbio_e_invalid_property_type"></span><dl> <dt>**WINBIO\_E\_INVALID\_PROPERTY\_TYPE**</dt> <dt>0x8009803A</dt> </dl>                    | The value specified is not a valid property type.<br/>                                                      |
| <span id="WINBIO_E_INVALID_PROPERTY_ID"></span><span id="winbio_e_invalid_property_id"></span><dl> <dt>**WINBIO\_E\_INVALID\_PROPERTY\_ID**</dt> <dt>0x8009803B</dt> </dl>                          | The value specified is not a valid property ID.<br/>                                                        |
| <span id="WINBIO_E_UNSUPPORTED_PROPERTY"></span><span id="winbio_e_unsupported_property"></span><dl> <dt>**WINBIO\_E\_UNSUPPORTED\_PROPERTY**</dt> <dt>0x8009803C</dt> </dl>                        | The biometric unit does not support the specified property.<br/>                                            |
| <span id="WINBIO_E_ADAPTER_INTEGRITY_FAILURE"></span><span id="winbio_e_adapter_integrity_failure"></span><dl> <dt>**WINBIO\_E\_ADAPTER\_INTEGRITY\_FAILURE**</dt> <dt>0x8009803D</dt> </dl>        | The adapter did not pass its integrity check.<br/>                                                          |
| <span id="WINBIO_I_MORE_DATA"></span><span id="winbio_i_more_data"></span><dl> <dt>**WINBIO\_I\_MORE\_DATA**</dt> <dt>0x00090001</dt> </dl>                                                         | Another sample is needed for the current enrollment template.<br/>                                          |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Winbio\_err.h</dt> </dl> |



## See also

<dl> <dt>

[Client Application Constants](client-application-constants.md)
</dt> </dl>

 

 





