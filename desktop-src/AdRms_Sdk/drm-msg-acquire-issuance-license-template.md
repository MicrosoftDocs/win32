---
Description: Is sent to the custom callback function when you call the DRMAcquireIssuanceLicenseTemplate function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e690fd96-c11f-43fe-85ad-466f62209e6d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: DRM\_MSG\_ACQUIRE\_ISSUANCE\_LICENSE\_TEMPLATE message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DRM\_MSG\_ACQUIRE\_ISSUANCE\_LICENSE\_TEMPLATE message

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **DRM\_MSG\_ACQUIRE\_ISSUANCE\_LICENSE\_TEMPLATE** message is sent to the custom callback function when you call the [**DRMAcquireIssuanceLicenseTemplate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquireissuancelicensetemplate) function.

## Parameters

<dl> <dt>

*hr* 
</dt> <dd>

The result of the action being monitored. This can be one of the following values, which are defined in msdrmerror.h.

<dt>

<span id="S_DRM_COMPLETED"></span><span id="s_drm_completed"></span>

<span id="S_DRM_COMPLETED"></span><span id="s_drm_completed"></span>****S\_DRM\_COMPLETED**** ()


</dt> <dd>

The operation is complete. The template collection is saved in the local template store.

</dd> <dt>

<span id="E_DRM_ABORTED"></span><span id="e_drm_aborted"></span>

<span id="E_DRM_ABORTED"></span><span id="e_drm_aborted"></span>****E\_DRM\_ABORTED**** ()


</dt> <dd>

Template acquisition was canceled.

</dd> <dt>

<span id="E_DRM_NO_CONNECT"></span><span id="e_drm_no_connect"></span>

<span id="E_DRM_NO_CONNECT"></span><span id="e_drm_no_connect"></span>****E\_DRM\_NO\_CONNECT**** ()


</dt> <dd>

The server was not available.

</dd> <dt>

<span id="E_DRM_SERVER_NOT_FOUND"></span><span id="e_drm_server_not_found"></span>

<span id="E_DRM_SERVER_NOT_FOUND"></span><span id="e_drm_server_not_found"></span>****E\_DRM\_SERVER\_NOT\_FOUND**** ()


</dt> <dd>

The attempt to contact the server returned HTTP 404, indicating that the template distribution service was not found.

</dd> <dt>

<span id="E_DRM_TEMPLATE_ACQUISITION_FAILED"></span><span id="e_drm_template_acquisition_failed"></span>

<span id="E_DRM_TEMPLATE_ACQUISITION_FAILED"></span><span id="e_drm_template_acquisition_failed"></span>****E\_DRM\_TEMPLATE\_ACQUISITION\_FAILED**** ()


</dt> <dd>

The template collection could not be retrieved from the server. This can occur for a variety of reasons such as an HTTP 401 (authentication) error.

</dd> </dl> </dd> <dt>

*pvParam* 
</dt> <dd>

This parameter is always **NULL**.

</dd> <dt>

*pvContext* 
</dt> <dd>

An application-defined value, such as a pointer to a callback function, a pointer to an event handle, or other value.

</dd> </dl>

## Return value

If the callback function succeeds, the function returns **S\_OK**.

If the callback function fails, it returns an **HRESULT** error code.

## Remarks

The [**DRMAcquireIssuanceLicenseTemplate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquireissuancelicensetemplate) function is an asynchronous function that will return before this message is sent to the callback function. It is the application's responsibility to ensure that this synchronization is properly handled.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msdrmdefs.h</dt> </dl> |



## See also

<dl> <dt>

[Creating a Callback Function](creating-a-callback-function.md)
</dt> <dt>

[**DRM\_STATUS\_MSG**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drm_status_msg)
</dt> <dt>

[**DRMAcquireIssuanceLicenseTemplate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquireissuancelicensetemplate)
</dt> </dl>

 

 




