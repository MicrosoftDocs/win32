---
title: MpUpdateStart function (MpClient.h)
description: Starts a signature update operation.
ms.assetid: BB056356-17E5-42F0-9636-9E1C254361E4
keywords:
- MpUpdateStart function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpUpdateStart
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpUpdateStart function

Starts a signature update operation.

## Syntax


```C++
HRESULT WINAPI MpUpdateStart(
  _In_     MPHANDLE         hMpHandle,
  _In_     DWORD            dwUpdateOptions,
  _In_opt_ PMPCALLBACK_INFO pCallbackInfo,
  _Out_    PMPHANDLE        phUpdateHandle
);
```



## Parameters

<dl> <dt>

*hMpHandle* \[in\]
</dt> <dd>

Type: **MPHANDLE**

Handle to the malware protection manager interface. This handle is returned by the [**MpManagerOpen**](mpmanageropen.md) function.

</dd> <dt>

*dwUpdateOptions* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the option for the signature update operation. It can be one of the following values:



| Value                                                                                                                                                                                              | Meaning                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MPUPDATE_OPTION_NONE"></span><span id="mpupdate_option_none"></span><dl> <dt>**MPUPDATE\_OPTION\_NONE**</dt> </dl>                | No specific option is requested.<br/>                                                                                                                                                                                                                                                      |
| <span id="MPUPDATE_OPTION_ASYNC"></span><span id="mpupdate_option_async"></span><dl> <dt>**MPUPDATE\_OPTION\_ASYNC**</dt> </dl>             | The update operation is to be asynchronous, where **MpUpdateStart** returns immediately after the successful initiation of the signature update. (By default the update operation is synchronous, meaning **MpUpdateStart** will return only after the signature update is finished.)<br/> |
| <span id="MPUPDATE_OPTION_PROGRESS"></span><span id="mpupdate_option_progress"></span><dl> <dt>**MPUPDATE\_OPTION\_PROGRESS**</dt> </dl>    | The caller is interested in receiving signature update progress information via a callback.<br/>                                                                                                                                                                                           |
| <span id="MPUPDATE_OPTION_HTTP"></span><span id="mpupdate_option_http"></span><dl> <dt>**MPUPDATE\_OPTION\_HTTP**</dt> </dl>                | The signature update is performed by downloading the full signature package from the Microsoft security portal site. This can be used as a fallback option if the client is experiencing a signature download problem via Microsoft Update.<br/>                                           |
| <span id="MPUPDATE_OPTION_UNC"></span><span id="mpupdate_option_unc"></span><dl> <dt>**MPUPDATE\_OPTION\_UNC**</dt> </dl>                   | Performs signature update using direct download from UNC shares.<br/>                                                                                                                                                                                                                      |
| <span id="MPUPDATE_OPTION_MANAGED"></span><span id="mpupdate_option_managed"></span><dl> <dt>**MPUPDATE\_OPTION\_MANAGED**</dt> </dl>       | Performs signature update using the Managed Service WSUS.<br/>                                                                                                                                                                                                                             |
| <span id="MPUPDATE_OPTION_UNMANAGED"></span><span id="mpupdate_option_unmanaged"></span><dl> <dt>**MPUPDATE\_OPTION\_UNMANAGED**</dt> </dl> | Performs signature update using the Unmanaged Service MU/WU.<br/>                                                                                                                                                                                                                          |



 

</dd> <dt>

*pCallbackInfo* \[in, optional\]
</dt> <dd>

Type: **PMPCALLBACK\_INFO**

A pointer to the callback information used to feed the client with signature update state changes (such as start and complete) and progress information. The [**MPCALLBACK\_DATA**](mpcallback-data.md) passed back in the callback function reports actual update state and progress-related information. The following is a list of possible callbacks:



| Value                                                                                                                                                                                                                                | Meaning                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MPNOTIFY_SIGUPDATE_START"></span><span id="mpnotify_sigupdate_start"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_START**</dt> </dl>                                      | Update operation started.<br/>                                                                                                                                  |
| <span id="MPNOTIFY_SIGUPDATE_COMPLETE"></span><span id="mpnotify_sigupdate_complete"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_COMPLETE**</dt> </dl>                             | Update operation completed.<br/>                                                                                                                                |
| <span id="MPNOTIFY_SIGUPDATE_SEARCH_START"></span><span id="mpnotify_sigupdate_search_start"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_SEARCH\_START**</dt> </dl>                | Search for updates started.<br/>                                                                                                                                |
| <span id="MPNOTIFY_SIGUPDATE_SEARCH_COMPLETE"></span><span id="mpnotify_sigupdate_search_complete"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_SEARCH\_COMPLETE**</dt> </dl>       | Search for updates completed. Additional information is available via [**MPSIGUPDATE\_DATA**](mpsigupdate-data.md) structure.<br/>                             |
| <span id="MPNOTIFY_SIGUPDATE_DOWNLOAD_START"></span><span id="mpnotify_sigupdate_download_start"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_DOWNLOAD\_START**</dt> </dl>          | Download for update started.<br/>                                                                                                                               |
| <span id="MPNOTIFY_SIGUPDATE_DOWNLOAD_PROGRESS"></span><span id="mpnotify_sigupdate_download_progress"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_DOWNLOAD\_PROGRESS**</dt> </dl> | Download progress information. Additional information is available via [**MPSIGUPDATE\_DATA**](mpsigupdate-data.md) structure.<br/>                            |
| <span id="MPNOTIFY_SIGUPDATE_DOWNLOAD_COMPLETE"></span><span id="mpnotify_sigupdate_download_complete"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_DOWNLOAD\_COMPLETE**</dt> </dl> | Download for update complete. Additional information is available via [**MPSIGUPDATE\_DATA**](mpsigupdate-data.md) structure.<br/>                             |
| <span id="MPNOTIFY_SIGUPDATE_INSTALL_START"></span><span id="mpnotify_sigupdate_install_start"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_INSTALL\_START**</dt> </dl>             | Installation of update started.<br/>                                                                                                                            |
| <span id="MPNOTIFY_SIGUPDATE_INSTALL_PROGRESS"></span><span id="mpnotify_sigupdate_install_progress"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_INSTALL\_PROGRESS**</dt> </dl>    | Installation progress information. Additional information is available via [**MPSIGUPDATE\_DATA**](mpsigupdate-data.md) structure.<br/>                        |
| <span id="MPNOTIFY_SIGUPDATE_INSTALL_COMPLETE"></span><span id="mpnotify_sigupdate_install_complete"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_INSTALL\_COMPLETE**</dt> </dl>    | Installation of update completed. Additional information is available via [**MPSIGUPDATE\_DATA**](mpsigupdate-data.md) structure.<br/>                         |
| <span id="MPNOTIFY_SIGUPDATE_REQUEST_PROCESSED"></span><span id="mpnotify_sigupdate_request_processed"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_REQUEST\_PROCESSED**</dt> </dl> | The antimalware service processed a signature update request. Failure or success is indicated by *hResult* in [**MPCALLBACK\_DATA**](mpcallback-data.md).<br/> |
| <span id="MPNOTIFY_SIGUPDATE_REBOOT_REQUIRED"></span><span id="mpnotify_sigupdate_reboot_required"></span><dl> <dt>**MPNOTIFY\_SIGUPDATE\_REBOOT\_REQUIRED**</dt> </dl>       | Requires reboot to complete the update operation. Failure or success is indicated by *hResult* in [**MPCALLBACK\_DATA**](mpcallback-data.md).<br/>             |
| <span id="MPNOTIFY_INTERNAL_FAILURE"></span><span id="mpnotify_internal_failure"></span><dl> <dt>**MPNOTIFY\_INTERNAL\_FAILURE**</dt> </dl>                                   | Signature update operation has encountered a generic failure. The *hResult* in [**MPCALLBACK\_DATA**](mpcallback-data.md) has the specific error code.<br/>    |



 

</dd> <dt>

*phUpdateHandle* \[out\]
</dt> <dd>

Type: **PMPHANDLE**

Returned update handle which identifies the currently initiated signature update operation. This handle can be used in subsequent function calls, such as to control the signature update operation. The handle must be closed with the [**MpHandleClose**](mphandleclose.md) function.

</dd> </dl>

## Return value

Type: **HRESULT**

If the function succeeds the return value is **S\_OK**.

If the function fails then the return value is a failed **HRESULT** code. The caller can use the [**MpErrorMessageFormat**](mperrormessageformat.md) function to get a generic description of the error message.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MpClient.dll</dt> </dl> |



## See also

<dl> <dt>

[**MpErrorMessageFormat**](mperrormessageformat.md)
</dt> <dt>

[**MpHandleClose**](mphandleclose.md)
</dt> <dt>

[**MpManagerOpen**](mpmanageropen.md)
</dt> <dt>

[**MPCALLBACK\_DATA**](mpcallback-data.md)
</dt> <dt>

[**MPSIGUPDATE\_DATA**](mpsigupdate-data.md)
</dt> </dl>

 

 





