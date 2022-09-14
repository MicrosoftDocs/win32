---
description: The SceSvcAttachmentUpdate function is called by the Security Configuration snap-ins to pass configuration changes to the security database.
ms.assetid: '2b5b3718-8ccb-480a-97fb-c8115d8f3a5c'
title: SceSvcAttachmentUpdate callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SceSvcAttachmentUpdate
api_type: 
- UserDefined
api_location: 
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

Pointer to a [**SCESVC\_CALLBACK\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_callback_info) structure which contains the callback handle and function pointers to SCE.

</dd> <dt>

*ServiceInfo* \[in\]
</dt> <dd>

Updated configuration information. The data structure used for this information is [**SCESVC\_CONFIGURATION\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_configuration_info).

</dd> </dl>

## Return value

If this function succeeds, it returns SCESTATUS\_SUCCESS. Otherwise it returns an error code. For more information about the Security Configuration error codes, see [Attachment Return Values](management-return-values.md).

## Remarks

The **SceSvcAttachmentUpdate** function must do the following:

-   Call the callback function pointed to by the **pfQueryInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_callback_info) structure (pSceCbInfo->pfQueryInfo) to retrieve the current base configuration information from the security database.
-   Call the callback function pointed to by the **pfQueryInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_callback_info) structure (pSceCbInfo->pfQueryInfo) to retrieve the last set of differences (analysis information) from the security database.
-   Use the supplied service information (see *ServiceInfo*) to compute the new base configuration.
-   Use the supplied service information (see *ServiceInfo*) and the analysis to compute the new difference information.
-   Call the callback function pointed to by the **pfSetInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_callback_info) structure (pSceCbInfo->pfSetInfo)to set the new base configuration in the security database.
-   Call the callback function pointed to by the **pfSetInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_callback_info) structure (pSceCbInfo->pfSetInfo) to set the new analysis information in the security database.

For more information, see [Implementing SceSvcAttachmentUpdate](implementing-scesvcattachmentupdate.md)

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SCESVC\_CALLBACK\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_callback_info)
</dt> <dt>

[**SCESVC\_CONFIGURATION\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_configuration_info)
</dt> </dl>

 

 




