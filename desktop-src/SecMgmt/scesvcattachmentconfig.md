---
Description: The SceSvcAttachmentConfig function is called by the Security Configuration Engine when the system is configured.
ms.assetid: c0c1c1e4-de5b-405d-abe8-33a985ce98e5
title: SceSvcAttachmentConfig callback function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SceSvcAttachmentConfig callback function

The **SceSvcAttachmentConfig** function is called by the Security Configuration Engine when the system is configured.

## Syntax


```C++
SCESTATUS WINAPI SceSvcAttachmentConfig(
  _In_ PSCESVC_CALLBACK_INFO pSceCbInfo
);
```



## Parameters

<dl> <dt>

*pSceCbInfo* \[in\]
</dt> <dd>

Pointer to a [**SCESVC\_CALLBACK\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_callback_info_?branch=master) structure that contains the database handle and the callback functions to query, set, and free information.

</dd> </dl>

## Return value

If this function succeeds, it returns SCESTATUS\_SUCCESS. Otherwise it returns an error code. For more information about the Security Configuration error codes, see [Attachment Return Values](management-return-values.md#attachment-return-values).

## Remarks

When implementing this function, use the callback function pointed to by the **pfQueryInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_callback_info_?branch=master) structure (pSceCbInfo-&gt;pfQueryInfo) to retrieve configuration information. Then configure the service using the returned information.

This function must do the following:

-   Query configuration information from the Security Configuration tool set using the callback function pointed to by the **pfQueryInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_callback_info_?branch=master) structure (pSceCbInfo-&gt;pfQueryInfo).
-   Configure the service using the configuration information.

For more information, see [Implementing SceSvcAttachmentConfig](implementing-scesvcattachmentconfig.md)

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SCESVC\_CALLBACK\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_callback_info_?branch=master)
</dt> <dt>

[**SceSvcAttachmentAnalyze**](scesvcattachmentanalyze.md)
</dt> </dl>

 

 




