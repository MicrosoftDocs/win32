---
Description: Sent to the custom callback function in response to the DRMActivate function being called with the DRM\_ACTIVATE\_MACHINE option.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1006464b-5fd2-4bc0-ac43-aacc5cd02322
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: DRM\_MSG\_ACTIVATE\_MACHINE message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DRM\_MSG\_ACTIVATE\_MACHINE message

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **DRM\_MSG\_ACTIVATE\_MACHINE** message is sent to the custom callback function in response to the [**DRMActivate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmactivate) function being called with the **DRM\_ACTIVATE\_MACHINE** option.

## Parameters

<dl> <dt>

*hr* 
</dt> <dd>

The result of the action being monitored. The contents of the *pvParam* parameter is dependent on the value of this parameter. This can be one of the following values.

<dt>

<span id="S_DRM_ALREADY_ACTIVATED"></span><span id="s_drm_already_activated"></span>

<span id="S_DRM_ALREADY_ACTIVATED"></span><span id="s_drm_already_activated"></span>****S\_DRM\_ALREADY\_ACTIVATED**** (**NULL**)


</dt> <dd>

The machine is already activated.

</dd> <dt>

<span id="S_DRM_COMPLETED"></span><span id="s_drm_completed"></span>

<span id="S_DRM_COMPLETED"></span><span id="s_drm_completed"></span>****S\_DRM\_COMPLETED**** (If the **DRM\_ACTIVATE\_DELAYED** flag is used for delayed activation, *pvParam* will be a pointer to a null-terminated Unicode string that contains the path to the activation CAB file (version 1.0 only) holding activation files that must be expanded and run manually. *pvParam* is **NULL** otherwise.)


</dt> <dd>

The activation process is complete.

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

<span id="S_DRM_INPROGRESS"></span><span id="s_drm_inprogress"></span>

<span id="S_DRM_INPROGRESS"></span><span id="s_drm_inprogress"></span>****S\_DRM\_INPROGRESS**** (A pointer to a **DWORD** value that contains an integer that represents the progress of the current request, from zero to 100.)


</dt> <dd>

This can be used for a progress bar or other visual indicator.

</dd> <dt>

<span id="E_DRM_ABORTED"></span><span id="e_drm_aborted"></span>

<span id="E_DRM_ABORTED"></span><span id="e_drm_aborted"></span>****E\_DRM\_ABORTED**** (**NULL**)


</dt> <dd>

The activation operation was aborted.

</dd> <dt>

<span id="E_DRM_ACTIVATIONFAILED"></span><span id="e_drm_activationfailed"></span>

<span id="E_DRM_ACTIVATIONFAILED"></span><span id="e_drm_activationfailed"></span>****E\_DRM\_ACTIVATIONFAILED**** (**NULL**)


</dt> <dd>

The activation operation failed.

</dd> <dt>

<span id="E_DRM_ALREADY_IN_PROGRESS"></span><span id="e_drm_already_in_progress"></span>

<span id="E_DRM_ALREADY_IN_PROGRESS"></span><span id="e_drm_already_in_progress"></span>****E\_DRM\_ALREADY\_IN\_PROGRESS**** (**NULL**)


</dt> <dd>

A machine activation operation is already in progress.

</dd> <dt>

<span id="E_DRM_HID_CORRUPTED"></span><span id="e_drm_hid_corrupted"></span>

<span id="E_DRM_HID_CORRUPTED"></span><span id="e_drm_hid_corrupted"></span>****E\_DRM\_HID\_CORRUPTED**** (**NULL**)


</dt> <dd>

The hardware ID for the machine being activated is corrupt.

</dd> <dt>

<span id="E_DRM_INSTALLATION_FAILED"></span><span id="e_drm_installation_failed"></span>

<span id="E_DRM_INSTALLATION_FAILED"></span><span id="e_drm_installation_failed"></span>****E\_DRM\_INSTALLATION\_FAILED**** (**NULL**)


</dt> <dd>

The machine activation package could not be installed.

</dd> <dt>

<span id="E_DRM_INVALID_SERVER_RESPONSE"></span><span id="e_drm_invalid_server_response"></span>

<span id="E_DRM_INVALID_SERVER_RESPONSE"></span><span id="e_drm_invalid_server_response"></span>****E\_DRM\_INVALID\_SERVER\_RESPONSE**** (**NULL**)


</dt> <dd>

The server sent a response that was not valid.

</dd> <dt>

<span id="E_DRM_NO_CONNECT"></span><span id="e_drm_no_connect"></span>

<span id="E_DRM_NO_CONNECT"></span><span id="e_drm_no_connect"></span>****E\_DRM\_NO\_CONNECT**** (**NULL**)


</dt> <dd>

The AD RMS client could not connect to the Internet.

</dd> <dt>

<span id="E_DRM_SERVER_ERROR"></span><span id="e_drm_server_error"></span>

<span id="E_DRM_SERVER_ERROR"></span><span id="e_drm_server_error"></span>****E\_DRM\_SERVER\_ERROR**** (**NULL**)


</dt> <dd>

A server error occurred.

</dd> <dt>

<span id="E_DRM_SERVER_NOT_FOUND"></span><span id="e_drm_server_not_found"></span>

<span id="E_DRM_SERVER_NOT_FOUND"></span><span id="e_drm_server_not_found"></span>****E\_DRM\_SERVER\_NOT\_FOUND**** (**NULL**)


</dt> <dd>

No machine activation server could be found.

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

If the callback function succeeds, the function returns **S\_OK**.

If the callback function fails, it returns an **HRESULT** error code.

## Remarks

The [**DRMActivate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmactivate) function is an asynchronous function that will return before this message is sent to the callback function. It is the application's responsibility to ensure that this synchronization is properly handled.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 SP2 or later<br/>                          |
| Header<br/>  | <dl> <dt>Msdrmdefs.h</dt> </dl> |



## See also

<dl> <dt>

[Creating a Callback Function](creating-a-callback-function.md)
</dt> <dt>

[**DRM\_STATUS\_MSG**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drm_status_msg)
</dt> <dt>

[**DRMActivate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmactivate)
</dt> </dl>

 

 




