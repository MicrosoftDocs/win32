---
Description: The SceSvcAttachmentUpdate function is called by the Security Configuration snap-ins to pass configuration changes to the security database.
ms.assetid: 3c0a71f6-f643-4a5e-8b5c-15c976a3736e
title: SceSvcAttachmentUpdate callback function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SceSvcAttachmentUpdate callback function

The **SceSvcAttachmentUpdate** function is called by the Security Configuration snap-ins to pass configuration changes to the security database.

## Syntax


```C++
SCESTATUS WINAPI SceSvcAttachmentUpdate(
  _In_ PSCESVC_CALLBACK_INFO     pSceCbInfo,
  _In_ SCESVC_CONFIGURATION_INFO *ServiceInfo
);
```



## Parameters

<dl> <dt>

*pSceCbInfo* \[in\]
</dt> <dd>

Pointer to a [**SCESVC\_CALLBACK\_INFO**](/windows/desktop/api/Scesvc/ns-scesvc-_scesvc_callback_info_) structure which contains the callback handle and function pointers to SCE.

</dd> <dt>

*ServiceInfo* \[in\]
</dt> <dd>

Updated configuration information. The data structure used for this information is [**SCESVC\_CONFIGURATION\_INFO**](/windows/desktop/api/Scesvc/ns-scesvc-_scesvc_configuration_info_).

</dd> </dl>

## Return value

If this function succeeds, it returns SCESTATUS\_SUCCESS. Otherwise it returns an error code. For more information about the Security Configuration error codes, see [Attachment Return Values](https://www.bing.com/search?q=Attachment Return Values).

## Remarks

The **SceSvcAttachmentUpdate** function must do the following:

-   Call the callback function pointed to by the **pfQueryInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/desktop/api/Scesvc/ns-scesvc-_scesvc_callback_info_) structure (pSceCbInfo-&gt;pfQueryInfo) to retrieve the current base configuration information from the security database.
-   Call the callback function pointed to by the **pfQueryInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/desktop/api/Scesvc/ns-scesvc-_scesvc_callback_info_) structure (pSceCbInfo-&gt;pfQueryInfo) to retrieve the last set of differences (analysis information) from the security database.
-   Use the supplied service information (see *ServiceInfo*) to compute the new base configuration.
-   Use the supplied service information (see *ServiceInfo*) and the analysis to compute the new difference information.
-   Call the callback function pointed to by the **pfSetInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/desktop/api/Scesvc/ns-scesvc-_scesvc_callback_info_) structure (pSceCbInfo-&gt;pfSetInfo)to set the new base configuration in the security database.
-   Call the callback function pointed to by the **pfSetInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/desktop/api/Scesvc/ns-scesvc-_scesvc_callback_info_) structure (pSceCbInfo-&gt;pfSetInfo) to set the new analysis information in the security database.

For more information, see [Implementing SceSvcAttachmentUpdate](implementing-scesvcattachmentupdate.md)

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SCESVC\_CALLBACK\_INFO**](/windows/desktop/api/Scesvc/ns-scesvc-_scesvc_callback_info_)
</dt> <dt>

[**SCESVC\_CONFIGURATION\_INFO**](/windows/desktop/api/Scesvc/ns-scesvc-_scesvc_configuration_info_)
</dt> </dl>

 

 




