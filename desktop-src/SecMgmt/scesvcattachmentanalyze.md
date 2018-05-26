---
Description: The SceSvcAttachmentAnalyze function is called by the Security Configuration Engine when the system is analyzed.
ms.assetid: f8420dde-55a2-40a0-b10d-140c28c0e9e4
title: SceSvcAttachmentAnalyze callback function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SceSvcAttachmentAnalyze callback function

The **SceSvcAttachmentAnalyze** function is called by the Security Configuration Engine when the system is analyzed.

## Syntax


```C++
SCESTATUS WINAPI SceSvcAttachmentAnalyze(
  _In_ PSCESVC_CALLBACK_INFO pSceCbInfo
);
```



## Parameters

<dl> <dt>

*pSceCbInfo* \[in\]
</dt> <dd>

Pointer to a [**SCESVC\_CALLBACK\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_callback_info_?branch=master) structure which contains an opaque database handle and callback function pointers to query, set, and free information.

</dd> </dl>

## Return value

If this function succeeds, it returns SCESTATUS\_SUCCESS. Otherwise it returns an error code. For more information about the Security Configuration error codes, see [Attachment Return Values](management-return-values.md#attachment-return-values).

## Remarks

The **SceSvcAttachmentAnalyze** function must do the following:

-   Directly query configuration information from the service.
-   Call the callback function pointed to by the **pfQueryInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_callback_info_?branch=master) structure (pSceCbInfo-&gt;pfQueryInfo) to retrieve information from the security database.
-   Compute the differences between the information based on type and syntax.
-   Call the callback function pointed to by the **pfSetInfo** member of the [**SCESVC\_CALLBACK\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_callback_info_?branch=master) structure (pSceCbInfo-&gt;pfSetInfo) to update the security database with the retrieved service information that is different.

For more information, see [Implementing SceSvcAttachmentAnalyze](implementing-scesvcattachmentanalyze.md).

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Implementing SceSvcAttachmentAnalyze](implementing-scesvcattachmentanalyze.md)
</dt> <dt>

[**SCESVC\_CALLBACK\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_callback_info_?branch=master)
</dt> <dt>

[**SceSvcAttachmentConfig**](scesvcattachmentconfig.md)
</dt> </dl>

 

 




