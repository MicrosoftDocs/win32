---
title: TBS Return Codes (Tbs.h)
description: TBS uses the following codes to indicate the result of a function call.
ms.assetid: a3888263-aa00-4b31-b51d-c6d448c1edb7
topic_type:
- apiref
api_name:
- TBS_SUCCESS
- TBS_E_INTERNAL_ERROR
- TBS_E_BAD_PARAMETER
- TBS_E_INVALID_OUTPUT_POINTER
- TBS_E_INVALID_CONTEXT
- TBS_E_INSUFFICIENT_BUFFER
- TBS_E_IOERROR
- TBS_E_INVALID_CONTEXT_PARAM
- TBS_E_SERVICE_NOT_RUNNING
- TBS_E_TOO_MANY_TBS_CONTEXTS
- TBS_E_TOO_MANY_RESOURCES
- TBS_E_SERVICE_START_PENDING
- TBS_E_PPI_NOT_SUPPORTED
- TBS_E_COMMAND_CANCELED
- TBS_E_BUFFER_TOO_LARGE
- TBS_E_TPM_NOT_FOUND
- TBS_E_SERVICE_DISABLED
- TBS_E_NO_EVENT_LOG
- TBS_E_ACCESS_DENIED
- TBS_E_PROVISIONING_NOT_ALLOWED
- TBS_E_PPI_FUNCTION_UNSUPPORTED
- TBS_E_OWNERAUTH_NOT_FOUND
- TBS_E_PROVISIONING_INCOMPLETE
api_location:
- Tbs.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBS Return Codes

TBS uses the following codes to indicate the result of a function call.



| Constant/value                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TBS_SUCCESS"></span><span id="tbs_success"></span><dl> <dt>**TBS\_SUCCESS**</dt> <dt>0 (0x0)</dt> </dl>                                                                             | The function succeeded.<br/>                                                                                                                                                                                                         |
| <span id="TBS_E_INTERNAL_ERROR"></span><span id="tbs_e_internal_error"></span><dl> <dt>**TBS\_E\_INTERNAL\_ERROR**</dt> <dt>2150121473 (0x80284001)</dt> </dl>                                | An internal software error occurred.<br/>                                                                                                                                                                                            |
| <span id="TBS_E_BAD_PARAMETER"></span><span id="tbs_e_bad_parameter"></span><dl> <dt>**TBS\_E\_BAD\_PARAMETER**</dt> <dt>2150121474 (0x80284002)</dt> </dl>                                   | One or more parameter values are not valid.<br/>                                                                                                                                                                                     |
| <span id="TBS_E_INVALID_OUTPUT_POINTER"></span><span id="tbs_e_invalid_output_pointer"></span><dl> <dt>**TBS\_E\_INVALID\_OUTPUT\_POINTER**</dt> <dt>2150121475 (0x80284003)</dt> </dl>       | A specified output pointer is bad.<br/>                                                                                                                                                                                              |
| <span id="TBS_E_INVALID_CONTEXT"></span><span id="tbs_e_invalid_context"></span><dl> <dt>**TBS\_E\_INVALID\_CONTEXT**</dt> <dt>2150121476 (0x80284004)</dt> </dl>                             | The specified context handle does not refer to a valid context.<br/>                                                                                                                                                                 |
| <span id="TBS_E_INSUFFICIENT_BUFFER"></span><span id="tbs_e_insufficient_buffer"></span><dl> <dt>**TBS\_E\_INSUFFICIENT\_BUFFER**</dt> <dt>2150121477 (0x80284005)</dt> </dl>                 | The specified output buffer is too small.<br/>                                                                                                                                                                                       |
| <span id="TBS_E_IOERROR"></span><span id="tbs_e_ioerror"></span><dl> <dt>**TBS\_E\_IOERROR**</dt> <dt>2150121478 (0x80284006)</dt> </dl>                                                      | An error occurred while communicating with the TPM.<br/>                                                                                                                                                                             |
| <span id="TBS_E_INVALID_CONTEXT_PARAM"></span><span id="tbs_e_invalid_context_param"></span><dl> <dt>**TBS\_E\_INVALID\_CONTEXT\_PARAM**</dt> <dt>2150121479 (0x80284007)</dt> </dl>          | A context parameter that is not valid was passed when attempting to create a TBS context.<br/>                                                                                                                                       |
| <span id="TBS_E_SERVICE_NOT_RUNNING"></span><span id="tbs_e_service_not_running"></span><dl> <dt>**TBS\_E\_SERVICE\_NOT\_RUNNING**</dt> <dt>2150121480 (0x80284008)</dt> </dl>                | The TBS service is not running and could not be started.<br/>                                                                                                                                                                        |
| <span id="TBS_E_TOO_MANY_TBS_CONTEXTS"></span><span id="tbs_e_too_many_tbs_contexts"></span><dl> <dt>**TBS\_E\_TOO\_MANY\_TBS\_CONTEXTS**</dt> <dt>2150121481 (0x80284009)</dt> </dl>         | A new context could not be created because there are too many open contexts.<br/>                                                                                                                                                    |
| <span id="TBS_E_TOO_MANY_RESOURCES"></span><span id="tbs_e_too_many_resources"></span><dl> <dt>**TBS\_E\_TOO\_MANY\_RESOURCES**</dt> <dt>2150121482 (0x8028400A)</dt> </dl>                   | A new virtual resource could not be created because there are too many open virtual resources.<br/>                                                                                                                                  |
| <span id="TBS_E_SERVICE_START_PENDING"></span><span id="tbs_e_service_start_pending"></span><dl> <dt>**TBS\_E\_SERVICE\_START\_PENDING**</dt> <dt>2150121483 (0x8028400B)</dt> </dl>          | The TBS service has been started but is not yet running.<br/>                                                                                                                                                                        |
| <span id="TBS_E_PPI_NOT_SUPPORTED"></span><span id="tbs_e_ppi_not_supported"></span><dl> <dt>**TBS\_E\_PPI\_NOT\_SUPPORTED**</dt> <dt>2150121484 (0x8028400C)</dt> </dl>                      | The physical presence interface is not supported.<br/>                                                                                                                                                                               |
| <span id="TBS_E_COMMAND_CANCELED"></span><span id="tbs_e_command_canceled"></span><dl> <dt>**TBS\_E\_COMMAND\_CANCELED**</dt> <dt>2150121485 (0x8028400D)</dt> </dl>                          | The command was canceled.<br/>                                                                                                                                                                                                       |
| <span id="TBS_E_BUFFER_TOO_LARGE"></span><span id="tbs_e_buffer_too_large"></span><dl> <dt>**TBS\_E\_BUFFER\_TOO\_LARGE**</dt> <dt>2150121486 (0x8028400E)</dt> </dl>                         | The input or output buffer is too large.<br/>                                                                                                                                                                                        |
| <span id="TBS_E_TPM_NOT_FOUND"></span><span id="tbs_e_tpm_not_found"></span><dl> <dt>**TBS\_E\_TPM\_NOT\_FOUND**</dt> <dt>2150121487 (0x8028400F)</dt> </dl>                                  | A compatible Trusted Platform Module (TPM) Security Device cannot be found on this computer.<br/>                                                                                                                                    |
| <span id="TBS_E_SERVICE_DISABLED"></span><span id="tbs_e_service_disabled"></span><dl> <dt>**TBS\_E\_SERVICE\_DISABLED**</dt> <dt>2150121488 (0x80284010)</dt> </dl>                          | The TBS service has been disabled.<br/>                                                                                                                                                                                              |
| <span id="TBS_E_NO_EVENT_LOG"></span><span id="tbs_e_no_event_log"></span><dl> <dt>**TBS\_E\_NO\_EVENT\_LOG**</dt> <dt>2150121489 (0x80284011)</dt> </dl>                                     | The TBS event log is not available.<br/>                                                                                                                                                                                             |
| <span id="TBS_E_ACCESS_DENIED"></span><span id="tbs_e_access_denied"></span><dl> <dt>**TBS\_E\_ACCESS\_DENIED**</dt> <dt>2150121490 (0x80284012)</dt> </dl>                                   | The caller does not have the appropriate rights to perform the requested operation.<br/>                                                                                                                                             |
| <span id="TBS_E_PROVISIONING_NOT_ALLOWED"></span><span id="tbs_e_provisioning_not_allowed"></span><dl> <dt>**TBS\_E\_PROVISIONING\_NOT\_ALLOWED**</dt> <dt>2150121491 (0x80284013)</dt> </dl> | The TPM provisioning action is not allowed by the specified flags.<br/>                                                                                                                                                              |
| <span id="TBS_E_PPI_FUNCTION_UNSUPPORTED"></span><span id="tbs_e_ppi_function_unsupported"></span><dl> <dt>**TBS\_E\_PPI\_FUNCTION\_UNSUPPORTED**</dt> <dt>2150121492 (0x80284014)</dt> </dl> | The Physical Presence Interface of this firmware does not support the requested method.<br/>                                                                                                                                         |
| <span id="TBS_E_OWNERAUTH_NOT_FOUND"></span><span id="tbs_e_ownerauth_not_found"></span><dl> <dt>**TBS\_E\_OWNERAUTH\_NOT\_FOUND**</dt> <dt>2150121493 (0x80284015)</dt> </dl>                | The requested TPM OwnerAuth value was not found.<br/>                                                                                                                                                                                |
| <span id="TBS_E_PROVISIONING_INCOMPLETE"></span><span id="tbs_e_provisioning_incomplete"></span><dl> <dt>**TBS\_E\_PROVISIONING\_INCOMPLETE**</dt> <dt>2150121493 (0x80284015)</dt> </dl>     | The TPM provisioning did not complete. For more information on completing the provisioning, call the [**Win32\_Tpm**](/windows/desktop/SecProv/win32-tpm) WMI method for provisioning the TPM ('Provision') and check the returned information.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Tbs.h</dt> </dl> |



 

