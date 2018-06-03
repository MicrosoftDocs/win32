---
Description: The Active Directory Rights Management Services (AD RMS) functions that return licenses and certificates to a client are asynchronous.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7d880b74-1934-4282-a7ca-1dac3602d6b4
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Creating a Callback Function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Callback Function

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services (AD RMS) functions that return licenses and certificates to a client are asynchronous. They return immediately to the caller and continue processing on another thread. To retrieve status information from these functions, you must create a custom callback.

All AD RMS asynchronous functions return status information to the callback. Also, if you request an [*issuance license*](https://www.bing.com/search?q=*issuance license*), the license is returned to the callback. All other licenses and certificates are copied to the certificate store and you must enumerate the store to retrieve the desired item.

The callback function pointer must be passed directly into the following functions:

-   [**DRMCreateClientSession**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateclientsession)
-   [**DRMGetSignedIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsignedissuancelicense)

The callback function pointer is indirectly passed into the following functions through the session handle parameter. Also, these functions allow arbitrary data to be passed through their *pvContext* parameter to the *pvContext* parameter of the callback. The parameter can contain any 32-bit value. It often contains, for example, an event handle that can be used to signal that an asynchronous function has completed. The responsibility for handling this parameter belongs to the callback function.

-   [**DRMAcquireAdvisories**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquireadvisories)
-   [**DRMAcquireLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquirelicense)
-   [**DRMActivate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmactivate)

For more information, see the following topics.

| Topic                                                                      | Description                                                                                                                                           |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Callback Prototype**](/previous-versions/windows/desktop/api/Msdrmdefs/nc-msdrmdefs-drmcallback)                           | Specifies the syntax of the custom callback function.                                                                                                 |
| [Issuance License Callback Example](issuance-license-callback-example.md) | Includes a callback function that retrieves an issuance license after [**DRMGetSignedIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsignedissuancelicense) is called.   |
| [End-User License Callback Example](end-user-license-callback-example.md) | Includes a callback function that copies an end user license to the certificate store after [**DRMAcquireLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquirelicense) is called. |



 

## Related topics

<dl> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> </dl>

 

 



