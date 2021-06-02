---
title: COM Error Codes (STG, RPC) (Winerror.h)
description: The following table provides a list of error codes used by COM-based APIs. | COM Error Codes (STG, RPC) (Winerror.h)
ms.assetid: d1b39eea-c910-4da0-b15a-2f9cabf9a2c9
topic_type:
- apiref
api_name:
- STG_E_INVALIDFUNCTION
- STG_E_FILENOTFOUND
- STG_E_PATHNOTFOUND
- STG_E_TOOMANYOPENFILES
- STG_E_ACCESSDENIED
- STG_E_INVALIDHANDLE
- STG_E_INSUFFICIENTMEMORY
- STG_E_INVALIDPOINTER
- STG_E_NOMOREFILES
- STG_E_DISKISWRITEPROTECTED
- STG_E_SEEKERROR
- STG_E_WRITEFAULT
- STG_E_READFAULT
- STG_E_SHAREVIOLATION
- STG_E_LOCKVIOLATION
- STG_E_FILEALREADYEXISTS
- STG_E_INVALIDPARAMETER
- STG_E_MEDIUMFULL
- STG_E_PROPSETMISMATCHED
- STG_E_ABNORMALAPIEXIT
- STG_E_INVALIDHEADER
- STG_E_INVALIDNAME
- STG_E_UNKNOWN
- STG_E_UNIMPLEMENTEDFUNCTION
- STG_E_INVALIDFLAG
- STG_E_INUSE
- STG_E_NOTCURRENT
- STG_E_REVERTED
- STG_E_CANTSAVE
- STG_E_OLDFORMAT
- STG_E_OLDDLL
- STG_E_SHAREREQUIRED
- STG_E_NOTFILEBASEDSTORAGE
- STG_E_EXTANTMARSHALLINGS
- STG_E_DOCFILECORRUPT
- STG_E_BADBASEADDRESS
- STG_E_DOCFILETOOLARGE
- STG_E_NOTSIMPLEFORMAT
- STG_E_INCOMPLETE
- STG_E_TERMINATED
- STG_S_CONVERTED
- STG_S_BLOCK
- STG_S_RETRYNOW
- STG_S_MONITORING
- STG_S_MULTIPLEOPENS
- STG_S_CONSOLIDATIONFAILED
- STG_S_CANNOTCONSOLIDATE
- STG_E_STATUS_COPY_PROTECTION_FAILURE
- STG_E_CSS_AUTHENTICATION_FAILURE
- STG_E_CSS_KEY_NOT_PRESENT
- STG_E_CSS_KEY_NOT_ESTABLISHED
- STG_E_CSS_SCRAMBLED_SECTOR
- STG_E_CSS_REGION_MISMATCH
- STG_E_RESETS_EXHAUSTED
- RPC_E_CALL_REJECTED
- RPC_E_CALL_CANCELED
- RPC_E_CANTPOST_INSENDCALL
- RPC_E_CANTCALLOUT_INASYNCCALL
- RPC_E_CANTCALLOUT_INEXTERNALCALL
- RPC_E_CONNECTION_TERMINATED
- RPC_E_SERVER_DIED
- RPC_E_CLIENT_DIED
- RPC_E_INVALID_DATAPACKET
- RPC_E_CANTTRANSMIT_CALL
- RPC_E_CLIENT_CANTMARSHAL_DATA
- RPC_E_CLIENT_CANTUNMARSHAL_DATA
- RPC_E_SERVER_CANTMARSHAL_DATA
- RPC_E_SERVER_CANTUNMARSHAL_DATA
- RPC_E_INVALID_DATA
- RPC_E_INVALID_PARAMETER
- RPC_E_CANTCALLOUT_AGAIN
- RPC_E_SERVER_DIED_DNE
- RPC_E_SYS_CALL_FAILED
- RPC_E_OUT_OF_RESOURCES
- RPC_E_ATTEMPTED_MULTITHREAD
- RPC_E_NOT_REGISTERED
- RPC_E_FAULT
- RPC_E_SERVERFAULT
- RPC_E_CHANGED_MODE
- RPC_E_INVALIDMETHOD
- RPC_E_DISCONNECTED
- RPC_E_RETRY
- RPC_E_SERVERCALL_RETRYLATER
- RPC_E_SERVERCALL_REJECTED
- RPC_E_INVALID_CALLDATA
- RPC_E_CANTCALLOUT_ININPUTSYNCCALL
- RPC_E_WRONG_THREAD
- RPC_E_THREAD_NOT_INIT
- RPC_E_VERSION_MISMATCH
- RPC_E_INVALID_HEADER
- RPC_E_INVALID_EXTENSION
- RPC_E_INVALID_IPID
- RPC_E_INVALID_OBJECT
- RPC_S_CALLPENDING
- RPC_S_WAITONTIMER
- RPC_E_CALL_COMPLETE
- RPC_E_UNSECURE_CALL
- RPC_E_TOO_LATE
- RPC_E_NO_GOOD_SECURITY_PACKAGES
- RPC_E_ACCESS_DENIED
- RPC_E_REMOTE_DISABLED
- RPC_E_INVALID_OBJREF
- RPC_E_NO_CONTEXT
- RPC_E_TIMEOUT
- RPC_E_NO_SYNC
- RPC_E_FULLSIC_REQUIRED
- RPC_E_INVALID_STD_NAME
- CO_E_FAILEDTOIMPERSONATE
- CO_E_FAILEDTOGETSECCTX
- CO_E_FAILEDTOOPENTHREADTOKEN
- CO_E_FAILEDTOGETTOKENINFO
- CO_E_TRUSTEEDOESNTMATCHCLIENT
- CO_E_FAILEDTOQUERYCLIENTBLANKET
- CO_E_FAILEDTOSETDACL
- CO_E_ACCESSCHECKFAILED
- CO_E_NETACCESSAPIFAILED
- CO_E_WRONGTRUSTEENAMESYNTAX
- CO_E_INVALIDSID
- CO_E_CONVERSIONFAILED
- CO_E_NOMATCHINGSIDFOUND
- CO_E_LOOKUPACCSIDFAILED
- CO_E_NOMATCHINGNAMEFOUND
- CO_E_LOOKUPACCNAMEFAILED
- CO_E_SETSERLHNDLFAILED
- CO_E_FAILEDTOGETWINDIR
- CO_E_PATHTOOLONG
- CO_E_FAILEDTOGENUUID
- CO_E_FAILEDTOCREATEFILE
- CO_E_FAILEDTOCLOSEHANDLE
- CO_E_EXCEEDSYSACLLIMIT
- CO_E_ACESINWRONGORDER
- CO_E_INCOMPATIBLESTREAMVERSION
- CO_E_FAILEDTOOPENPROCESSTOKEN
- CO_E_DECODEFAILED
- CO_E_ACNOTINITIALIZED
- CO_E_CANCEL_DISABLED
- RPC_E_UNEXPECTED
api_location:
- Winerror.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# COM Error Codes (STG, RPC)

The following table provides a list of error codes used by COM-based APIs.

If you are experiencing difficulty with an application you are installing or running, contact customer support for the software that is displaying the error message. To obtain support for a Microsoft product, go to [https://support.microsoft.com](https://support.microsoft.com).



| Constant/value                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                            |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="STG_E_INVALIDFUNCTION"></span><span id="stg_e_invalidfunction"></span><dl> <dt>**STG\_E\_INVALIDFUNCTION**</dt> <dt>0x80030001</dt> </dl>                                                 | Unable to perform requested operation.<br/>                                                                                                                      |
| <span id="STG_E_FILENOTFOUND"></span><span id="stg_e_filenotfound"></span><dl> <dt>**STG\_E\_FILENOTFOUND**</dt> <dt>0x80030002</dt> </dl>                                                          | could not be found.<br/>                                                                                                                                         |
| <span id="STG_E_PATHNOTFOUND"></span><span id="stg_e_pathnotfound"></span><dl> <dt>**STG\_E\_PATHNOTFOUND**</dt> <dt>0x80030003</dt> </dl>                                                          | The path %1 could not be found.<br/>                                                                                                                             |
| <span id="STG_E_TOOMANYOPENFILES"></span><span id="stg_e_toomanyopenfiles"></span><dl> <dt>**STG\_E\_TOOMANYOPENFILES**</dt> <dt>0x80030004</dt> </dl>                                              | There are insufficient resources to open another file.<br/>                                                                                                      |
| <span id="STG_E_ACCESSDENIED"></span><span id="stg_e_accessdenied"></span><dl> <dt>**STG\_E\_ACCESSDENIED**</dt> <dt>0x80030005</dt> </dl>                                                          | Access Denied.<br/>                                                                                                                                              |
| <span id="STG_E_INVALIDHANDLE"></span><span id="stg_e_invalidhandle"></span><dl> <dt>**STG\_E\_INVALIDHANDLE**</dt> <dt>0x80030006</dt> </dl>                                                       | Attempted an operation on an invalid object.<br/>                                                                                                                |
| <span id="STG_E_INSUFFICIENTMEMORY"></span><span id="stg_e_insufficientmemory"></span><dl> <dt>**STG\_E\_INSUFFICIENTMEMORY**</dt> <dt>0x80030008</dt> </dl>                                        | There is insufficient memory available to complete operation.<br/>                                                                                               |
| <span id="STG_E_INVALIDPOINTER"></span><span id="stg_e_invalidpointer"></span><dl> <dt>**STG\_E\_INVALIDPOINTER**</dt> <dt>0x80030009</dt> </dl>                                                    | Invalid pointer error.<br/>                                                                                                                                      |
| <span id="STG_E_NOMOREFILES"></span><span id="stg_e_nomorefiles"></span><dl> <dt>**STG\_E\_NOMOREFILES**</dt> <dt>0x80030012</dt> </dl>                                                             | There are no more entries to return.<br/>                                                                                                                        |
| <span id="STG_E_DISKISWRITEPROTECTED"></span><span id="stg_e_diskiswriteprotected"></span><dl> <dt>**STG\_E\_DISKISWRITEPROTECTED**</dt> <dt>0x80030013</dt> </dl>                                  | Disk is write-protected.<br/>                                                                                                                                    |
| <span id="STG_E_SEEKERROR"></span><span id="stg_e_seekerror"></span><dl> <dt>**STG\_E\_SEEKERROR**</dt> <dt>0x80030019</dt> </dl>                                                                   | An error occurred during a seek operation.<br/>                                                                                                                  |
| <span id="STG_E_WRITEFAULT"></span><span id="stg_e_writefault"></span><dl> <dt>**STG\_E\_WRITEFAULT**</dt> <dt>0x8003001D</dt> </dl>                                                                | A disk error occurred during a write operation.<br/>                                                                                                             |
| <span id="STG_E_READFAULT"></span><span id="stg_e_readfault"></span><dl> <dt>**STG\_E\_READFAULT**</dt> <dt>0x8003001E</dt> </dl>                                                                   | A disk error occurred during a read operation.<br/>                                                                                                              |
| <span id="STG_E_SHAREVIOLATION"></span><span id="stg_e_shareviolation"></span><dl> <dt>**STG\_E\_SHAREVIOLATION**</dt> <dt>0x80030020</dt> </dl>                                                    | A share violation has occurred.<br/>                                                                                                                             |
| <span id="STG_E_LOCKVIOLATION"></span><span id="stg_e_lockviolation"></span><dl> <dt>**STG\_E\_LOCKVIOLATION**</dt> <dt>0x80030021</dt> </dl>                                                       | A lock violation has occurred.<br/>                                                                                                                              |
| <span id="STG_E_FILEALREADYEXISTS"></span><span id="stg_e_filealreadyexists"></span><dl> <dt>**STG\_E\_FILEALREADYEXISTS**</dt> <dt>0x80030050</dt> </dl>                                           | already exists.<br/>                                                                                                                                             |
| <span id="STG_E_INVALIDPARAMETER"></span><span id="stg_e_invalidparameter"></span><dl> <dt>**STG\_E\_INVALIDPARAMETER**</dt> <dt>0x80030057</dt> </dl>                                              | Invalid parameter error.<br/>                                                                                                                                    |
| <span id="STG_E_MEDIUMFULL"></span><span id="stg_e_mediumfull"></span><dl> <dt>**STG\_E\_MEDIUMFULL**</dt> <dt>0x80030070</dt> </dl>                                                                | There is insufficient disk space to complete operation.<br/>                                                                                                     |
| <span id="STG_E_PROPSETMISMATCHED"></span><span id="stg_e_propsetmismatched"></span><dl> <dt>**STG\_E\_PROPSETMISMATCHED**</dt> <dt>0x800300F0</dt> </dl>                                           | Illegal write of non-simple property to simple property set.<br/>                                                                                                |
| <span id="STG_E_ABNORMALAPIEXIT"></span><span id="stg_e_abnormalapiexit"></span><dl> <dt>**STG\_E\_ABNORMALAPIEXIT**</dt> <dt>0x800300FA</dt> </dl>                                                 | An API call exited abnormally.<br/>                                                                                                                              |
| <span id="STG_E_INVALIDHEADER"></span><span id="stg_e_invalidheader"></span><dl> <dt>**STG\_E\_INVALIDHEADER**</dt> <dt>0x800300FB</dt> </dl>                                                       | The file %1 is not a valid compound file.<br/>                                                                                                                   |
| <span id="STG_E_INVALIDNAME"></span><span id="stg_e_invalidname"></span><dl> <dt>**STG\_E\_INVALIDNAME**</dt> <dt>0x800300FC</dt> </dl>                                                             | The name %1 is not valid.<br/>                                                                                                                                   |
| <span id="STG_E_UNKNOWN"></span><span id="stg_e_unknown"></span><dl> <dt>**STG\_E\_UNKNOWN**</dt> <dt>0x800300FD</dt> </dl>                                                                         | An unexpected error occurred.<br/>                                                                                                                               |
| <span id="STG_E_UNIMPLEMENTEDFUNCTION"></span><span id="stg_e_unimplementedfunction"></span><dl> <dt>**STG\_E\_UNIMPLEMENTEDFUNCTION**</dt> <dt>0x800300FE</dt> </dl>                               | That function is not implemented.<br/>                                                                                                                           |
| <span id="STG_E_INVALIDFLAG"></span><span id="stg_e_invalidflag"></span><dl> <dt>**STG\_E\_INVALIDFLAG**</dt> <dt>0x800300FF</dt> </dl>                                                             | Invalid flag error.<br/>                                                                                                                                         |
| <span id="STG_E_INUSE"></span><span id="stg_e_inuse"></span><dl> <dt>**STG\_E\_INUSE**</dt> <dt>0x80030100</dt> </dl>                                                                               | Attempted to use an object that is busy.<br/>                                                                                                                    |
| <span id="STG_E_NOTCURRENT"></span><span id="stg_e_notcurrent"></span><dl> <dt>**STG\_E\_NOTCURRENT**</dt> <dt>0x80030101</dt> </dl>                                                                | The storage has been changed since the last commit.<br/>                                                                                                         |
| <span id="STG_E_REVERTED"></span><span id="stg_e_reverted"></span><dl> <dt>**STG\_E\_REVERTED**</dt> <dt>0x80030102</dt> </dl>                                                                      | Attempted to use an object that has ceased to exist.<br/>                                                                                                        |
| <span id="STG_E_CANTSAVE"></span><span id="stg_e_cantsave"></span><dl> <dt>**STG\_E\_CANTSAVE**</dt> <dt>0x80030103</dt> </dl>                                                                      | Can't save.<br/>                                                                                                                                                 |
| <span id="STG_E_OLDFORMAT"></span><span id="stg_e_oldformat"></span><dl> <dt>**STG\_E\_OLDFORMAT**</dt> <dt>0x80030104</dt> </dl>                                                                   | The compound file %1 was produced with an incompatible version of storage.<br/>                                                                                  |
| <span id="STG_E_OLDDLL"></span><span id="stg_e_olddll"></span><dl> <dt>**STG\_E\_OLDDLL**</dt> <dt>0x80030105</dt> </dl>                                                                            | The compound file %1 was produced with a newer version of storage.<br/>                                                                                          |
| <span id="STG_E_SHAREREQUIRED"></span><span id="stg_e_sharerequired"></span><dl> <dt>**STG\_E\_SHAREREQUIRED**</dt> <dt>0x80030106</dt> </dl>                                                       | Share.exe or equivalent is required for operation.<br/>                                                                                                          |
| <span id="STG_E_NOTFILEBASEDSTORAGE"></span><span id="stg_e_notfilebasedstorage"></span><dl> <dt>**STG\_E\_NOTFILEBASEDSTORAGE**</dt> <dt>0x80030107</dt> </dl>                                     | Illegal operation called on non-file based storage.<br/>                                                                                                         |
| <span id="STG_E_EXTANTMARSHALLINGS"></span><span id="stg_e_extantmarshallings"></span><dl> <dt>**STG\_E\_EXTANTMARSHALLINGS**</dt> <dt>0x80030108</dt> </dl>                                        | Illegal operation called on object with extant marshallings.<br/>                                                                                                |
| <span id="STG_E_DOCFILECORRUPT"></span><span id="stg_e_docfilecorrupt"></span><dl> <dt>**STG\_E\_DOCFILECORRUPT**</dt> <dt>0x80030109</dt> </dl>                                                    | The docfile has been corrupted.<br/>                                                                                                                             |
| <span id="STG_E_BADBASEADDRESS"></span><span id="stg_e_badbaseaddress"></span><dl> <dt>**STG\_E\_BADBASEADDRESS**</dt> <dt>0x80030110</dt> </dl>                                                    | OLE32.DLL has been loaded at the wrong address.<br/>                                                                                                             |
| <span id="STG_E_DOCFILETOOLARGE"></span><span id="stg_e_docfiletoolarge"></span><dl> <dt>**STG\_E\_DOCFILETOOLARGE**</dt> <dt>0x80030111</dt> </dl>                                                 | The compound file is too large for the current implementation<br/>                                                                                               |
| <span id="STG_E_NOTSIMPLEFORMAT"></span><span id="stg_e_notsimpleformat"></span><dl> <dt>**STG\_E\_NOTSIMPLEFORMAT**</dt> <dt>0x80030112</dt> </dl>                                                 | The compound file was not created with the STGM\_SIMPLE flag<br/>                                                                                                |
| <span id="STG_E_INCOMPLETE"></span><span id="stg_e_incomplete"></span><dl> <dt>**STG\_E\_INCOMPLETE**</dt> <dt>0x80030201</dt> </dl>                                                                | The file download was aborted abnormally. The file is incomplete.<br/>                                                                                           |
| <span id="STG_E_TERMINATED"></span><span id="stg_e_terminated"></span><dl> <dt>**STG\_E\_TERMINATED**</dt> <dt>0x80030202</dt> </dl>                                                                | The file download has been terminated.<br/>                                                                                                                      |
| <span id="STG_S_CONVERTED"></span><span id="stg_s_converted"></span><dl> <dt>**STG\_S\_CONVERTED**</dt> <dt>0x00030200</dt> </dl>                                                                   | The underlying file was converted to compound file format.<br/>                                                                                                  |
| <span id="STG_S_BLOCK"></span><span id="stg_s_block"></span><dl> <dt>**STG\_S\_BLOCK**</dt> <dt>0x00030201</dt> </dl>                                                                               | The storage operation should block until more data is available.<br/>                                                                                            |
| <span id="STG_S_RETRYNOW"></span><span id="stg_s_retrynow"></span><dl> <dt>**STG\_S\_RETRYNOW**</dt> <dt>0x00030202</dt> </dl>                                                                      | The storage operation should retry immediately.<br/>                                                                                                             |
| <span id="STG_S_MONITORING"></span><span id="stg_s_monitoring"></span><dl> <dt>**STG\_S\_MONITORING**</dt> <dt>0x00030203</dt> </dl>                                                                | The notified event sink will not influence the storage operation.<br/>                                                                                           |
| <span id="STG_S_MULTIPLEOPENS"></span><span id="stg_s_multipleopens"></span><dl> <dt>**STG\_S\_MULTIPLEOPENS**</dt> <dt>0x00030204</dt> </dl>                                                       | Multiple opens prevent consolidated. (commit succeeded).<br/>                                                                                                    |
| <span id="STG_S_CONSOLIDATIONFAILED"></span><span id="stg_s_consolidationfailed"></span><dl> <dt>**STG\_S\_CONSOLIDATIONFAILED**</dt> <dt>0x00030205</dt> </dl>                                     | Consolidation of the storage file failed. (commit succeeded).<br/>                                                                                               |
| <span id="STG_S_CANNOTCONSOLIDATE"></span><span id="stg_s_cannotconsolidate"></span><dl> <dt>**STG\_S\_CANNOTCONSOLIDATE**</dt> <dt>0x00030206</dt> </dl>                                           | Consolidation of the storage file is inappropriate. (commit succeeded).<br/>                                                                                     |
| <span id="STG_E_STATUS_COPY_PROTECTION_FAILURE"></span><span id="stg_e_status_copy_protection_failure"></span><dl> <dt>**STG\_E\_STATUS\_COPY\_PROTECTION\_FAILURE**</dt> <dt>0x80030305</dt> </dl> | Generic Copy Protection Error.<br/>                                                                                                                              |
| <span id="STG_E_CSS_AUTHENTICATION_FAILURE"></span><span id="stg_e_css_authentication_failure"></span><dl> <dt>**STG\_E\_CSS\_AUTHENTICATION\_FAILURE**</dt> <dt>0x80030306</dt> </dl>              | Copy Protection Error - DVD CSS Authentication failed.<br/>                                                                                                      |
| <span id="STG_E_CSS_KEY_NOT_PRESENT"></span><span id="stg_e_css_key_not_present"></span><dl> <dt>**STG\_E\_CSS\_KEY\_NOT\_PRESENT**</dt> <dt>0x80030307</dt> </dl>                                  | Copy Protection Error - The given sector does not have a valid CSS key.<br/>                                                                                     |
| <span id="STG_E_CSS_KEY_NOT_ESTABLISHED"></span><span id="stg_e_css_key_not_established"></span><dl> <dt>**STG\_E\_CSS\_KEY\_NOT\_ESTABLISHED**</dt> <dt>0x80030308</dt> </dl>                      | Copy Protection Error - DVD session key not established.<br/>                                                                                                    |
| <span id="STG_E_CSS_SCRAMBLED_SECTOR"></span><span id="stg_e_css_scrambled_sector"></span><dl> <dt>**STG\_E\_CSS\_SCRAMBLED\_SECTOR**</dt> <dt>0x80030309</dt> </dl>                                | Copy Protection Error - The read failed because the sector is encrypted.<br/>                                                                                    |
| <span id="STG_E_CSS_REGION_MISMATCH"></span><span id="stg_e_css_region_mismatch"></span><dl> <dt>**STG\_E\_CSS\_REGION\_MISMATCH**</dt> <dt>0x8003030A</dt> </dl>                                   | Copy Protection Error - The current DVD's region does not correspond to the region setting of the drive.<br/>                                                    |
| <span id="STG_E_RESETS_EXHAUSTED"></span><span id="stg_e_resets_exhausted"></span><dl> <dt>**STG\_E\_RESETS\_EXHAUSTED**</dt> <dt>0x8003030B</dt> </dl>                                             | Copy Protection Error - The drive's region setting may be permanent or the number of user resets has been exhausted.<br/>                                        |
| <span id="RPC_E_CALL_REJECTED"></span><span id="rpc_e_call_rejected"></span><dl> <dt>**RPC\_E\_CALL\_REJECTED**</dt> <dt>0x80010001</dt> </dl>                                                      | Call was rejected by callee.<br/>                                                                                                                                |
| <span id="RPC_E_CALL_CANCELED"></span><span id="rpc_e_call_canceled"></span><dl> <dt>**RPC\_E\_CALL\_CANCELED**</dt> <dt>0x80010002</dt> </dl>                                                      | Call was canceled by the message filter.<br/>                                                                                                                    |
| <span id="RPC_E_CANTPOST_INSENDCALL"></span><span id="rpc_e_cantpost_insendcall"></span><dl> <dt>**RPC\_E\_CANTPOST\_INSENDCALL**</dt> <dt>0x80010003</dt> </dl>                                    | The caller is dispatching an intertask SendMessage call and cannot call out via PostMessage.<br/>                                                                |
| <span id="RPC_E_CANTCALLOUT_INASYNCCALL"></span><span id="rpc_e_cantcallout_inasynccall"></span><dl> <dt>**RPC\_E\_CANTCALLOUT\_INASYNCCALL**</dt> <dt>0x80010004</dt> </dl>                        | The caller is dispatching an asynchronous call and cannot make an outgoing call on behalf of this call.<br/>                                                     |
| <span id="RPC_E_CANTCALLOUT_INEXTERNALCALL"></span><span id="rpc_e_cantcallout_inexternalcall"></span><dl> <dt>**RPC\_E\_CANTCALLOUT\_INEXTERNALCALL**</dt> <dt>0x80010005</dt> </dl>               | It is illegal to call out while inside message filter.<br/>                                                                                                      |
| <span id="RPC_E_CONNECTION_TERMINATED"></span><span id="rpc_e_connection_terminated"></span><dl> <dt>**RPC\_E\_CONNECTION\_TERMINATED**</dt> <dt>0x80010006</dt> </dl>                              | The connection terminated or is in a bogus state and cannot be used any more. Other connections are still valid.<br/>                                            |
| <span id="RPC_E_SERVER_DIED"></span><span id="rpc_e_server_died"></span><dl> <dt>**RPC\_E\_SERVER\_DIED**</dt> <dt>0x80010007</dt> </dl>                                                            | The callee (server \[not server application\]) is not available and disappeared; all connections are invalid. The call may have executed.<br/>                   |
| <span id="RPC_E_CLIENT_DIED"></span><span id="rpc_e_client_died"></span><dl> <dt>**RPC\_E\_CLIENT\_DIED**</dt> <dt>0x80010008</dt> </dl>                                                            | The caller (client) disappeared while the callee (server) was processing a call.<br/>                                                                            |
| <span id="RPC_E_INVALID_DATAPACKET"></span><span id="rpc_e_invalid_datapacket"></span><dl> <dt>**RPC\_E\_INVALID\_DATAPACKET**</dt> <dt>0x80010009</dt> </dl>                                       | The data packet with the marshalled parameter data is incorrect.<br/>                                                                                            |
| <span id="RPC_E_CANTTRANSMIT_CALL"></span><span id="rpc_e_canttransmit_call"></span><dl> <dt>**RPC\_E\_CANTTRANSMIT\_CALL**</dt> <dt>0x8001000A</dt> </dl>                                          | The call was not transmitted properly; the message queue was full and was not emptied after yielding.<br/>                                                       |
| <span id="RPC_E_CLIENT_CANTMARSHAL_DATA"></span><span id="rpc_e_client_cantmarshal_data"></span><dl> <dt>**RPC\_E\_CLIENT\_CANTMARSHAL\_DATA**</dt> <dt>0x8001000B</dt> </dl>                       | The client (caller) cannot marshal the parameter data - low memory, etc.<br/>                                                                                    |
| <span id="RPC_E_CLIENT_CANTUNMARSHAL_DATA"></span><span id="rpc_e_client_cantunmarshal_data"></span><dl> <dt>**RPC\_E\_CLIENT\_CANTUNMARSHAL\_DATA**</dt> <dt>0x8001000C</dt> </dl>                 | The client (caller) cannot unmarshal the return data - low memory, etc.<br/>                                                                                     |
| <span id="RPC_E_SERVER_CANTMARSHAL_DATA"></span><span id="rpc_e_server_cantmarshal_data"></span><dl> <dt>**RPC\_E\_SERVER\_CANTMARSHAL\_DATA**</dt> <dt>0x8001000D</dt> </dl>                       | The server (callee) cannot marshal the return data - low memory, etc.<br/>                                                                                       |
| <span id="RPC_E_SERVER_CANTUNMARSHAL_DATA"></span><span id="rpc_e_server_cantunmarshal_data"></span><dl> <dt>**RPC\_E\_SERVER\_CANTUNMARSHAL\_DATA**</dt> <dt>0x8001000E</dt> </dl>                 | The server (callee) cannot unmarshal the parameter data - low memory, etc.<br/>                                                                                  |
| <span id="RPC_E_INVALID_DATA"></span><span id="rpc_e_invalid_data"></span><dl> <dt>**RPC\_E\_INVALID\_DATA**</dt> <dt>0x8001000F</dt> </dl>                                                         | Received data is invalid; could be server or client data.<br/>                                                                                                   |
| <span id="RPC_E_INVALID_PARAMETER"></span><span id="rpc_e_invalid_parameter"></span><dl> <dt>**RPC\_E\_INVALID\_PARAMETER**</dt> <dt>0x80010010</dt> </dl>                                          | A particular parameter is invalid and cannot be (un)marshalled.<br/>                                                                                             |
| <span id="RPC_E_CANTCALLOUT_AGAIN"></span><span id="rpc_e_cantcallout_again"></span><dl> <dt>**RPC\_E\_CANTCALLOUT\_AGAIN**</dt> <dt>0x80010011</dt> </dl>                                          | There is no second outgoing call on same channel in DDE conversation.<br/>                                                                                       |
| <span id="RPC_E_SERVER_DIED_DNE"></span><span id="rpc_e_server_died_dne"></span><dl> <dt>**RPC\_E\_SERVER\_DIED\_DNE**</dt> <dt>0x80010012</dt> </dl>                                               | The callee (server \[not server application\]) is not available and disappeared; all connections are invalid. The call did not execute.<br/>                     |
| <span id="RPC_E_SYS_CALL_FAILED"></span><span id="rpc_e_sys_call_failed"></span><dl> <dt>**RPC\_E\_SYS\_CALL\_FAILED**</dt> <dt>0x80010100</dt> </dl>                                               | System call failed.<br/>                                                                                                                                         |
| <span id="RPC_E_OUT_OF_RESOURCES"></span><span id="rpc_e_out_of_resources"></span><dl> <dt>**RPC\_E\_OUT\_OF\_RESOURCES**</dt> <dt>0x80010101</dt> </dl>                                            | Could not allocate some required resource (memory, events, ...)<br/>                                                                                             |
| <span id="RPC_E_ATTEMPTED_MULTITHREAD"></span><span id="rpc_e_attempted_multithread"></span><dl> <dt>**RPC\_E\_ATTEMPTED\_MULTITHREAD**</dt> <dt>0x80010102</dt> </dl>                              | Attempted to make calls on more than one thread in single threaded mode.<br/>                                                                                    |
| <span id="RPC_E_NOT_REGISTERED"></span><span id="rpc_e_not_registered"></span><dl> <dt>**RPC\_E\_NOT\_REGISTERED**</dt> <dt>0x80010103</dt> </dl>                                                   | The requested interface is not registered on the server object.<br/>                                                                                             |
| <span id="RPC_E_FAULT"></span><span id="rpc_e_fault"></span><dl> <dt>**RPC\_E\_FAULT**</dt> <dt>0x80010104</dt> </dl>                                                                               | RPC could not call the server or could not return the results of calling the server.<br/>                                                                        |
| <span id="RPC_E_SERVERFAULT"></span><span id="rpc_e_serverfault"></span><dl> <dt>**RPC\_E\_SERVERFAULT**</dt> <dt>0x80010105</dt> </dl>                                                             | The server threw an exception.<br/>                                                                                                                              |
| <span id="RPC_E_CHANGED_MODE"></span><span id="rpc_e_changed_mode"></span><dl> <dt>**RPC\_E\_CHANGED\_MODE**</dt> <dt>0x80010106</dt> </dl>                                                         | Cannot change thread mode after it is set.<br/>                                                                                                                  |
| <span id="RPC_E_INVALIDMETHOD"></span><span id="rpc_e_invalidmethod"></span><dl> <dt>**RPC\_E\_INVALIDMETHOD**</dt> <dt>0x80010107</dt> </dl>                                                       | The method called does not exist on the server.<br/>                                                                                                             |
| <span id="RPC_E_DISCONNECTED"></span><span id="rpc_e_disconnected"></span><dl> <dt>**RPC\_E\_DISCONNECTED**</dt> <dt>0x80010108</dt> </dl>                                                          | The object invoked has disconnected from its clients.<br/>                                                                                                       |
| <span id="RPC_E_RETRY"></span><span id="rpc_e_retry"></span><dl> <dt>**RPC\_E\_RETRY**</dt> <dt>0x80010109</dt> </dl>                                                                               | The object invoked chose not to process the call now. Try again later.<br/>                                                                                      |
| <span id="RPC_E_SERVERCALL_RETRYLATER"></span><span id="rpc_e_servercall_retrylater"></span><dl> <dt>**RPC\_E\_SERVERCALL\_RETRYLATER**</dt> <dt>0x8001010A</dt> </dl>                              | The message filter indicated that the application is busy.<br/>                                                                                                  |
| <span id="RPC_E_SERVERCALL_REJECTED"></span><span id="rpc_e_servercall_rejected"></span><dl> <dt>**RPC\_E\_SERVERCALL\_REJECTED**</dt> <dt>0x8001010B</dt> </dl>                                    | The message filter rejected the call.<br/>                                                                                                                       |
| <span id="RPC_E_INVALID_CALLDATA"></span><span id="rpc_e_invalid_calldata"></span><dl> <dt>**RPC\_E\_INVALID\_CALLDATA**</dt> <dt>0x8001010C</dt> </dl>                                             | A call control interfaces was called with invalid data.<br/>                                                                                                     |
| <span id="RPC_E_CANTCALLOUT_ININPUTSYNCCALL"></span><span id="rpc_e_cantcallout_ininputsynccall"></span><dl> <dt>**RPC\_E\_CANTCALLOUT\_ININPUTSYNCCALL**</dt> <dt>0x8001010D</dt> </dl>            | An outgoing call cannot be made since the application is dispatching an input-synchronous call.<br/>                                                             |
| <span id="RPC_E_WRONG_THREAD"></span><span id="rpc_e_wrong_thread"></span><dl> <dt>**RPC\_E\_WRONG\_THREAD**</dt> <dt>0x8001010E</dt> </dl>                                                         | The application called an interface that was marshalled for a different thread.<br/>                                                                             |
| <span id="RPC_E_THREAD_NOT_INIT"></span><span id="rpc_e_thread_not_init"></span><dl> <dt>**RPC\_E\_THREAD\_NOT\_INIT**</dt> <dt>0x8001010F</dt> </dl>                                               | CoInitialize has not been called on the current thread.<br/>                                                                                                     |
| <span id="RPC_E_VERSION_MISMATCH"></span><span id="rpc_e_version_mismatch"></span><dl> <dt>**RPC\_E\_VERSION\_MISMATCH**</dt> <dt>0x80010110</dt> </dl>                                             | The version of OLE on the client and server machines does not match.<br/>                                                                                        |
| <span id="RPC_E_INVALID_HEADER"></span><span id="rpc_e_invalid_header"></span><dl> <dt>**RPC\_E\_INVALID\_HEADER**</dt> <dt>0x80010111</dt> </dl>                                                   | OLE received a packet with an invalid header.<br/>                                                                                                               |
| <span id="RPC_E_INVALID_EXTENSION"></span><span id="rpc_e_invalid_extension"></span><dl> <dt>**RPC\_E\_INVALID\_EXTENSION**</dt> <dt>0x80010112</dt> </dl>                                          | OLE received a packet with an invalid extension.<br/>                                                                                                            |
| <span id="RPC_E_INVALID_IPID"></span><span id="rpc_e_invalid_ipid"></span><dl> <dt>**RPC\_E\_INVALID\_IPID**</dt> <dt>0x80010113</dt> </dl>                                                         | The requested object or interface does not exist.<br/>                                                                                                           |
| <span id="RPC_E_INVALID_OBJECT"></span><span id="rpc_e_invalid_object"></span><dl> <dt>**RPC\_E\_INVALID\_OBJECT**</dt> <dt>0x80010114</dt> </dl>                                                   | The requested object does not exist.<br/>                                                                                                                        |
| <span id="RPC_S_CALLPENDING"></span><span id="rpc_s_callpending"></span><dl> <dt>**RPC\_S\_CALLPENDING**</dt> <dt>0x80010115</dt> </dl>                                                             | OLE has sent a request and is waiting for a reply.<br/>                                                                                                          |
| <span id="RPC_S_WAITONTIMER"></span><span id="rpc_s_waitontimer"></span><dl> <dt>**RPC\_S\_WAITONTIMER**</dt> <dt>0x80010116</dt> </dl>                                                             | OLE is waiting before retrying a request.<br/>                                                                                                                   |
| <span id="RPC_E_CALL_COMPLETE"></span><span id="rpc_e_call_complete"></span><dl> <dt>**RPC\_E\_CALL\_COMPLETE**</dt> <dt>0x80010117</dt> </dl>                                                      | Call context cannot be accessed after call completed.<br/>                                                                                                       |
| <span id="RPC_E_UNSECURE_CALL"></span><span id="rpc_e_unsecure_call"></span><dl> <dt>**RPC\_E\_UNSECURE\_CALL**</dt> <dt>0x80010118</dt> </dl>                                                      | Impersonate on unsecure calls is not supported.<br/>                                                                                                             |
| <span id="RPC_E_TOO_LATE"></span><span id="rpc_e_too_late"></span><dl> <dt>**RPC\_E\_TOO\_LATE**</dt> <dt>0x80010119</dt> </dl>                                                                     | Security must be initialized before any interfaces are marshalled or unmarshalled. It cannot be changed once initialized.<br/>                                   |
| <span id="RPC_E_NO_GOOD_SECURITY_PACKAGES"></span><span id="rpc_e_no_good_security_packages"></span><dl> <dt>**RPC\_E\_NO\_GOOD\_SECURITY\_PACKAGES**</dt> <dt>0x8001011A</dt> </dl>                | No security packages are installed on this machine or the user is not logged on or there are no compatible security packages between the client and server.<br/> |
| <span id="RPC_E_ACCESS_DENIED"></span><span id="rpc_e_access_denied"></span><dl> <dt>**RPC\_E\_ACCESS\_DENIED**</dt> <dt>0x8001011B</dt> </dl>                                                      | Access is denied.<br/>                                                                                                                                           |
| <span id="RPC_E_REMOTE_DISABLED"></span><span id="rpc_e_remote_disabled"></span><dl> <dt>**RPC\_E\_REMOTE\_DISABLED**</dt> <dt>0x8001011C</dt> </dl>                                                | Remote calls are not allowed for this process.<br/>                                                                                                              |
| <span id="RPC_E_INVALID_OBJREF"></span><span id="rpc_e_invalid_objref"></span><dl> <dt>**RPC\_E\_INVALID\_OBJREF**</dt> <dt>0x8001011D</dt> </dl>                                                   | The marshaled interface data packet (OBJREF) has an invalid or unknown format.<br/>                                                                              |
| <span id="RPC_E_NO_CONTEXT"></span><span id="rpc_e_no_context"></span><dl> <dt>**RPC\_E\_NO\_CONTEXT**</dt> <dt>0x8001011E</dt> </dl>                                                               | No context is associated with this call. This happens for some custom marshalled calls and on the client side of the call.<br/>                                  |
| <span id="RPC_E_TIMEOUT"></span><span id="rpc_e_timeout"></span><dl> <dt>**RPC\_E\_TIMEOUT**</dt> <dt>0x8001011F</dt> </dl>                                                                         | This operation returned because the timeout period expired.<br/>                                                                                                 |
| <span id="RPC_E_NO_SYNC"></span><span id="rpc_e_no_sync"></span><dl> <dt>**RPC\_E\_NO\_SYNC**</dt> <dt>0x80010120</dt> </dl>                                                                        | There are no synchronize objects to wait on.<br/>                                                                                                                |
| <span id="RPC_E_FULLSIC_REQUIRED"></span><span id="rpc_e_fullsic_required"></span><dl> <dt>**RPC\_E\_FULLSIC\_REQUIRED**</dt> <dt>0x80010121</dt> </dl>                                             | Full subject issuer chain SSL principal name expected from the server.<br/>                                                                                      |
| <span id="RPC_E_INVALID_STD_NAME"></span><span id="rpc_e_invalid_std_name"></span><dl> <dt>**RPC\_E\_INVALID\_STD\_NAME**</dt> <dt>0x80010122</dt> </dl>                                            | Principal name is not a valid MSSTD name.<br/>                                                                                                                   |
| <span id="CO_E_FAILEDTOIMPERSONATE"></span><span id="co_e_failedtoimpersonate"></span><dl> <dt>**CO\_E\_FAILEDTOIMPERSONATE**</dt> <dt>0x80010123</dt> </dl>                                        | Unable to impersonate DCOM client<br/>                                                                                                                           |
| <span id="CO_E_FAILEDTOGETSECCTX"></span><span id="co_e_failedtogetsecctx"></span><dl> <dt>**CO\_E\_FAILEDTOGETSECCTX**</dt> <dt>0x80010124</dt> </dl>                                              | Unable to obtain server's security context<br/>                                                                                                                  |
| <span id="CO_E_FAILEDTOOPENTHREADTOKEN"></span><span id="co_e_failedtoopenthreadtoken"></span><dl> <dt>**CO\_E\_FAILEDTOOPENTHREADTOKEN**</dt> <dt>0x80010125</dt> </dl>                            | Unable to open the access token of the current thread<br/>                                                                                                       |
| <span id="CO_E_FAILEDTOGETTOKENINFO"></span><span id="co_e_failedtogettokeninfo"></span><dl> <dt>**CO\_E\_FAILEDTOGETTOKENINFO**</dt> <dt>0x80010126</dt> </dl>                                     | Unable to obtain user info from an access token<br/>                                                                                                             |
| <span id="CO_E_TRUSTEEDOESNTMATCHCLIENT"></span><span id="co_e_trusteedoesntmatchclient"></span><dl> <dt>**CO\_E\_TRUSTEEDOESNTMATCHCLIENT**</dt> <dt>0x80010127</dt> </dl>                         | The client who called IAccessControl::IsAccessPermitted was not the trustee provided to the method<br/>                                                          |
| <span id="CO_E_FAILEDTOQUERYCLIENTBLANKET"></span><span id="co_e_failedtoqueryclientblanket"></span><dl> <dt>**CO\_E\_FAILEDTOQUERYCLIENTBLANKET**</dt> <dt>0x80010128</dt> </dl>                   | Unable to obtain the client's security blanket<br/>                                                                                                              |
| <span id="CO_E_FAILEDTOSETDACL"></span><span id="co_e_failedtosetdacl"></span><dl> <dt>**CO\_E\_FAILEDTOSETDACL**</dt> <dt>0x80010129</dt> </dl>                                                    | Unable to set a discretionary ACL into a security descriptor<br/>                                                                                                |
| <span id="CO_E_ACCESSCHECKFAILED"></span><span id="co_e_accesscheckfailed"></span><dl> <dt>**CO\_E\_ACCESSCHECKFAILED**</dt> <dt>0x8001012A</dt> </dl>                                              | The system function, AccessCheck, returned false<br/>                                                                                                            |
| <span id="CO_E_NETACCESSAPIFAILED"></span><span id="co_e_netaccessapifailed"></span><dl> <dt>**CO\_E\_NETACCESSAPIFAILED**</dt> <dt>0x8001012B</dt> </dl>                                           | Either NetAccessDel or NetAccessAdd returned an error code.<br/>                                                                                                 |
| <span id="CO_E_WRONGTRUSTEENAMESYNTAX"></span><span id="co_e_wrongtrusteenamesyntax"></span><dl> <dt>**CO\_E\_WRONGTRUSTEENAMESYNTAX**</dt> <dt>0x8001012C</dt> </dl>                               | One of the trustee strings provided by the user did not conform to the <Domain>\\<Name> syntax and it was not the "\*" string<br/>                   |
| <span id="CO_E_INVALIDSID"></span><span id="co_e_invalidsid"></span><dl> <dt>**CO\_E\_INVALIDSID**</dt> <dt>0x8001012D</dt> </dl>                                                                   | One of the security identifiers provided by the user was invalid<br/>                                                                                            |
| <span id="CO_E_CONVERSIONFAILED"></span><span id="co_e_conversionfailed"></span><dl> <dt>**CO\_E\_CONVERSIONFAILED**</dt> <dt>0x8001012E</dt> </dl>                                                 | Unable to convert a wide character trustee string to a multibyte trustee string<br/>                                                                             |
| <span id="CO_E_NOMATCHINGSIDFOUND"></span><span id="co_e_nomatchingsidfound"></span><dl> <dt>**CO\_E\_NOMATCHINGSIDFOUND**</dt> <dt>0x8001012F</dt> </dl>                                           | Unable to find a security identifier that corresponds to a trustee string provided by the user<br/>                                                              |
| <span id="CO_E_LOOKUPACCSIDFAILED"></span><span id="co_e_lookupaccsidfailed"></span><dl> <dt>**CO\_E\_LOOKUPACCSIDFAILED**</dt> <dt>0x80010130</dt> </dl>                                           | The system function, LookupAccountSID, failed<br/>                                                                                                               |
| <span id="CO_E_NOMATCHINGNAMEFOUND"></span><span id="co_e_nomatchingnamefound"></span><dl> <dt>**CO\_E\_NOMATCHINGNAMEFOUND**</dt> <dt>0x80010131</dt> </dl>                                        | Unable to find a trustee name that corresponds to a security identifier provided by the user<br/>                                                                |
| <span id="CO_E_LOOKUPACCNAMEFAILED"></span><span id="co_e_lookupaccnamefailed"></span><dl> <dt>**CO\_E\_LOOKUPACCNAMEFAILED**</dt> <dt>0x80010132</dt> </dl>                                        | The system function, LookupAccountName, failed<br/>                                                                                                              |
| <span id="CO_E_SETSERLHNDLFAILED"></span><span id="co_e_setserlhndlfailed"></span><dl> <dt>**CO\_E\_SETSERLHNDLFAILED**</dt> <dt>0x80010133</dt> </dl>                                              | Unable to set or reset a serialization handle<br/>                                                                                                               |
| <span id="CO_E_FAILEDTOGETWINDIR"></span><span id="co_e_failedtogetwindir"></span><dl> <dt>**CO\_E\_FAILEDTOGETWINDIR**</dt> <dt>0x80010134</dt> </dl>                                              | Unable to obtain the Windows directory<br/>                                                                                                                      |
| <span id="CO_E_PATHTOOLONG"></span><span id="co_e_pathtoolong"></span><dl> <dt>**CO\_E\_PATHTOOLONG**</dt> <dt>0x80010135</dt> </dl>                                                                | Path too long<br/>                                                                                                                                               |
| <span id="CO_E_FAILEDTOGENUUID"></span><span id="co_e_failedtogenuuid"></span><dl> <dt>**CO\_E\_FAILEDTOGENUUID**</dt> <dt>0x80010136</dt> </dl>                                                    | Unable to generate a uuid.<br/>                                                                                                                                  |
| <span id="CO_E_FAILEDTOCREATEFILE"></span><span id="co_e_failedtocreatefile"></span><dl> <dt>**CO\_E\_FAILEDTOCREATEFILE**</dt> <dt>0x80010137</dt> </dl>                                           | Unable to create file<br/>                                                                                                                                       |
| <span id="CO_E_FAILEDTOCLOSEHANDLE"></span><span id="co_e_failedtoclosehandle"></span><dl> <dt>**CO\_E\_FAILEDTOCLOSEHANDLE**</dt> <dt>0x80010138</dt> </dl>                                        | Unable to close a serialization handle or a file handle.<br/>                                                                                                    |
| <span id="CO_E_EXCEEDSYSACLLIMIT"></span><span id="co_e_exceedsysacllimit"></span><dl> <dt>**CO\_E\_EXCEEDSYSACLLIMIT**</dt> <dt>0x80010139</dt> </dl>                                              | The number of ACEs in an ACL exceeds the system limit.<br/>                                                                                                      |
| <span id="CO_E_ACESINWRONGORDER"></span><span id="co_e_acesinwrongorder"></span><dl> <dt>**CO\_E\_ACESINWRONGORDER**</dt> <dt>0x8001013A</dt> </dl>                                                 | Not all the DENY\_ACCESS ACEs are arranged in front of the GRANT\_ACCESS ACEs in the stream.<br/>                                                                |
| <span id="CO_E_INCOMPATIBLESTREAMVERSION"></span><span id="co_e_incompatiblestreamversion"></span><dl> <dt>**CO\_E\_INCOMPATIBLESTREAMVERSION**</dt> <dt>0x8001013B</dt> </dl>                      | The version of ACL format in the stream is not supported by this implementation of IAccessControl<br/>                                                           |
| <span id="CO_E_FAILEDTOOPENPROCESSTOKEN"></span><span id="co_e_failedtoopenprocesstoken"></span><dl> <dt>**CO\_E\_FAILEDTOOPENPROCESSTOKEN**</dt> <dt>0x8001013C</dt> </dl>                         | Unable to open the access token of the server process<br/>                                                                                                       |
| <span id="CO_E_DECODEFAILED"></span><span id="co_e_decodefailed"></span><dl> <dt>**CO\_E\_DECODEFAILED**</dt> <dt>0x8001013D</dt> </dl>                                                             | Unable to decode the ACL in the stream provided by the user<br/>                                                                                                 |
| <span id="CO_E_ACNOTINITIALIZED"></span><span id="co_e_acnotinitialized"></span><dl> <dt>**CO\_E\_ACNOTINITIALIZED**</dt> <dt>0x8001013F</dt> </dl>                                                 | The COM IAccessControl object is not initialized<br/>                                                                                                            |
| <span id="CO_E_CANCEL_DISABLED"></span><span id="co_e_cancel_disabled"></span><dl> <dt>**CO\_E\_CANCEL\_DISABLED**</dt> <dt>0x80010140</dt> </dl>                                                   | Call Cancellation is disabled<br/>                                                                                                                               |
| <span id="RPC_E_UNEXPECTED"></span><span id="rpc_e_unexpected"></span><dl> <dt>**RPC\_E\_UNEXPECTED**</dt> <dt>0x8001FFFF</dt> </dl>                                                                | An internal error occurred.<br/>                                                                                                                                 |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winerror.h</dt> </dl> |



## See also

<dl> <dt>

[COM Error Codes](com-error-codes.md)
</dt> </dl>

 

 





