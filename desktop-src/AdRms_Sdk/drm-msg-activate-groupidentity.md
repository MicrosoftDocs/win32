---
Description: Sent to the custom callback function in response to the DRMActivate function being called with the DRM\_ACTIVATE\_GROUPIDENTITY option.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 49c8606a-c2d9-4380-9b99-139d75b0689b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: DRM\_MSG\_ACTIVATE\_GROUPIDENTITY message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DRM\_MSG\_ACTIVATE\_GROUPIDENTITY message

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **DRM\_MSG\_ACTIVATE\_GROUPIDENTITY** message is sent to the custom callback function in response to the [**DRMActivate**](/windows/previous-versions/Msdrm/nf-msdrm-drmactivate?branch=master) function being called with the **DRM\_ACTIVATE\_GROUPIDENTITY** option.

## Parameters

<dl> <dt>

*hr* 
</dt> <dd>

The result of the action being monitored. The *pvParam* parameter is dependent on the value of *hr*. This can be one of the following values.

<dt>

<span id="E_DRM_ABORTED"></span><span id="e_drm_aborted"></span>

<span id="E_DRM_ABORTED"></span><span id="e_drm_aborted"></span>****E\_DRM\_ABORTED**** (**NULL**)


</dt> <dd>

The activation attempt was ended.

</dd> <dt>

<span id="E_DRM_ACTIVATIONFAILED"></span><span id="e_drm_activationfailed"></span>

<span id="E_DRM_ACTIVATIONFAILED"></span><span id="e_drm_activationfailed"></span>****E\_DRM\_ACTIVATIONFAILED**** (**NULL**)


</dt> <dd>

The activation attempt failed.

</dd> <dt>

<span id="E_DRM_AD_ENTRY_NOT_FOUND"></span><span id="e_drm_ad_entry_not_found"></span>

<span id="E_DRM_AD_ENTRY_NOT_FOUND"></span><span id="e_drm_ad_entry_not_found"></span>****E\_DRM\_AD\_ENTRY\_NOT\_FOUND**** (**NULL**)


</dt> <dd>

The user could not be found in Active Directory.

</dd> <dt>

<span id="E_DRM_AUTHENTICATION_FAILED"></span><span id="e_drm_authentication_failed"></span>

<span id="E_DRM_AUTHENTICATION_FAILED"></span><span id="e_drm_authentication_failed"></span>****E\_DRM\_AUTHENTICATION\_FAILED**** (**NULL**)


</dt> <dd>

The user could not be authenticated.

</dd> <dt>

<span id="S_DRM_COMPLETED"></span><span id="s_drm_completed"></span>

<span id="S_DRM_COMPLETED"></span><span id="s_drm_completed"></span>****S\_DRM\_COMPLETED**** (A pointer to a null-terminated Unicode string that contains the retrieved [*rights account certificate*](r-gly.md#-rm-rights-account-certificate-gly). The certificate is also entered in the license store, where it can be retrieved by using the [**DRMEnumerateLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmenumeratelicense?branch=master) function. The memory will be deallocated immediately after returning from the callback function, so you must copy the string within the callback if you want to keep it.)


</dt> <dd>

This is the last value a successful activation attempt should send.

</dd> <dt>

<span id="S_DRM_CONNECTED"></span><span id="s_drm_connected"></span>

<span id="S_DRM_CONNECTED"></span><span id="s_drm_connected"></span>****S\_DRM\_CONNECTED**** (**NULL**)


</dt> <dd>

The system has connected to a server.

</dd> <dt>

<span id="S_DRM_CONNECTING"></span><span id="s_drm_connecting"></span>

<span id="S_DRM_CONNECTING"></span><span id="s_drm_connecting"></span>****S\_DRM\_CONNECTING**** (**NULL**)


</dt> <dd>

A connection has not yet occurred.

</dd> <dt>

<span id="E_DRM_EMAIL_NOT_VERIFIED"></span><span id="e_drm_email_not_verified"></span>

<span id="E_DRM_EMAIL_NOT_VERIFIED"></span><span id="e_drm_email_not_verified"></span>****E\_DRM\_EMAIL\_NOT\_VERIFIED**** (**NULL**)


</dt> <dd>

The supplied email address cannot be verified.

</dd> <dt>

<span id="S_DRM_INPROGRESS"></span><span id="s_drm_inprogress"></span>

<span id="S_DRM_INPROGRESS"></span><span id="s_drm_inprogress"></span>****S\_DRM\_INPROGRESS**** (A pointer to a **DWORD** that contains an integer that represents the progress of the current request, from zero to 100.)


</dt> <dd>

This can be used for a progress bar or other visual indicator.

</dd> <dt>

<span id="E_DRM_INVALID_EMAIL"></span><span id="e_drm_invalid_email"></span>

<span id="E_DRM_INVALID_EMAIL"></span><span id="e_drm_invalid_email"></span>****E\_DRM\_INVALID\_EMAIL**** (**NULL**)


</dt> <dd>

The supplied email address is not valid.

</dd> <dt>

<span id="E_DRM_INVALID_SERVER_RESPONSE"></span><span id="e_drm_invalid_server_response"></span>

<span id="E_DRM_INVALID_SERVER_RESPONSE"></span><span id="e_drm_invalid_server_response"></span>****E\_DRM\_INVALID\_SERVER\_RESPONSE**** (**NULL**)


</dt> <dd>

The response from the server is not valid.

</dd> <dt>

<span id="E_DRM_NEEDS_MACHINE_ACTIVATION"></span><span id="e_drm_needs_machine_activation"></span>

<span id="E_DRM_NEEDS_MACHINE_ACTIVATION"></span><span id="e_drm_needs_machine_activation"></span>****E\_DRM\_NEEDS\_MACHINE\_ACTIVATION**** (**NULL**)


</dt> <dd>

The computer must be activated before the user can be activated.

</dd> <dt>

<span id="E_DRM_NO_CONNECT"></span><span id="e_drm_no_connect"></span>

<span id="E_DRM_NO_CONNECT"></span><span id="e_drm_no_connect"></span>****E\_DRM\_NO\_CONNECT**** (**NULL**)


</dt> <dd>

Cannot connect to the Active Directory Rights Management Services (AD RMS) server.

</dd> <dt>

<span id="E_DRM_REQUEST_DENIED"></span><span id="e_drm_request_denied"></span>

<span id="E_DRM_REQUEST_DENIED"></span><span id="e_drm_request_denied"></span>****E\_DRM\_REQUEST\_DENIED**** (**NULL**)


</dt> <dd>

The request to activate the user was denied.

</dd> <dt>

<span id="E_DRM_SERVER_ERROR"></span><span id="e_drm_server_error"></span>

<span id="E_DRM_SERVER_ERROR"></span><span id="e_drm_server_error"></span>****E\_DRM\_SERVER\_ERROR**** (**NULL**)


</dt> <dd>

A general server error occurred.

</dd> <dt>

<span id="E_DRM_SERVER_NOT_FOUND"></span><span id="e_drm_server_not_found"></span>

<span id="E_DRM_SERVER_NOT_FOUND"></span><span id="e_drm_server_not_found"></span>****E\_DRM\_SERVER\_NOT\_FOUND**** (**NULL**)


</dt> <dd>

The AD RMS server was not found.

</dd> <dt>

<span id="E_DRM_SERVICE_GONE"></span><span id="e_drm_service_gone"></span>

<span id="E_DRM_SERVICE_GONE"></span><span id="e_drm_service_gone"></span>****E\_DRM\_SERVICE\_GONE**** (**NULL**)


</dt> <dd>

The activation service was not found.

</dd> <dt>

<span id="E_DRM_SERVICE_MOVED"></span><span id="e_drm_service_moved"></span>

<span id="E_DRM_SERVICE_MOVED"></span><span id="e_drm_service_moved"></span>****E\_DRM\_SERVICE\_MOVED**** (**NULL**)


</dt> <dd>

The activation service has moved to another server.

</dd> <dt>

<span id="E_DRM_VALIDITYTIME_VIOLATION"></span><span id="e_drm_validitytime_violation"></span>

<span id="E_DRM_VALIDITYTIME_VIOLATION"></span><span id="e_drm_validitytime_violation"></span>****E\_DRM\_VALIDITYTIME\_VIOLATION**** (**NULL**)


</dt> <dd>

The certificate validity has expired.

</dd> </dl> </dd> <dt>

*pvParam* 
</dt> <dd>

The contents of this parameter is dependent on the value in the *hr* parameter. For more information, see the *hr* parameter description.

</dd> <dt>

*pvContext* 
</dt> <dd>

An application-defined value, such as a pointer to a callback function, a pointer to an event handle, or other value.

</dd> </dl>

## Return value

If the function succeeds, the function returns S\_OK.

If the function fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](https://msdn.microsoft.com/library/windows/desktop/aa378137).

## Remarks

The [**DRMActivate**](/windows/previous-versions/Msdrm/nf-msdrm-drmactivate?branch=master) function is an asynchronous function that will return before this message is sent to the callback function. It is the application's responsibility to ensure that this synchronization is properly handled.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 SP2 or later<br/>                          |
| Header<br/>  | <dl> <dt>Msdrmdefs.h</dt> </dl> |



## See also

<dl> <dt>

[Creating a Callback Function](creating-a-callback-function.md)
</dt> <dt>

[**DRM\_STATUS\_MSG**](/windows/previous-versions/Msdrmdefs/ne-msdrmdefs-_drm_status_msg?branch=master)
</dt> <dt>

[**DRMActivate**](/windows/previous-versions/Msdrm/nf-msdrm-drmactivate?branch=master)
</dt> </dl>

 

 




