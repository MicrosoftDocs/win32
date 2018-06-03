---
Description: This section describes the usage of the DRM\_STATUS\_MSG enumeration values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5B63AE51-1B03-401F-9201-E4A2221FFBF7
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: DRM\_STATUS\_MSG Values
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DRM\_STATUS\_MSG Values

This section describes the usage of the [**DRM\_STATUS\_MSG**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drm_status_msg) enumeration values.

## In this section



| Topic                                                                                                          | Description                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRM\_MSG\_ACQUIRE\_ADVISORY**](drm-msg-acquire-advisory.md)<br/>                                     | sent to the custom callback function in response to the [**DRMAcquireAdvisories**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquireadvisories) function being called.<br/>                                 |
| [**DRM\_MSG\_ACQUIRE\_CLIENTLICENSOR**](drm-msg-acquire-clientlicensor.md)<br/>                         | sent to the custom callback function in response to the [**DRMAcquireLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquirelicense) function being called with a client session handle.<br/>          |
| [**DRM\_MSG\_ACQUIRE\_ISSUANCE\_LICENSE\_TEMPLATE**](drm-msg-acquire-issuance-license-template.md)<br/> | is sent to the custom callback function when you call the [**DRMAcquireIssuanceLicenseTemplate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquireissuancelicensetemplate) function.<br/>                  |
| [**DRM\_MSG\_ACQUIRE\_LICENSE**](drm-msg-acquire-license.md)<br/>                                       | sent to the custom callback function in response to the [**DRMAcquireLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquirelicense) function being called with a license storage session handle.<br/> |
| [**DRM\_MSG\_ACTIVATE\_GROUPIDENTITY**](drm-msg-activate-groupidentity.md)<br/>                         | sent to the custom callback function in response to the [**DRMActivate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmactivate) function being called with the **DRM\_ACTIVATE\_GROUPIDENTITY** option.<br/>  |
| [**DRM\_MSG\_ACTIVATE\_MACHINE**](drm-msg-activate-machine.md)<br/>                                     | sent to the custom callback function in response to the [**DRMActivate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmactivate) function being called with the **DRM\_ACTIVATE\_MACHINE** option.<br/>        |
| [**DRM\_MSG\_SIGN\_ISSUANCE\_LICENSE**](drm-msg-sign-issuance-license.md)<br/>                          | sent to the custom callback function in response to the [**DRMGetSignedIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsignedissuancelicense) function being called.<br/>                   |



 

 

 




