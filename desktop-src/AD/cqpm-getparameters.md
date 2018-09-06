---
title: CQPM_GETPARAMETERS message
description: Sent to the CQPageProc callback function of a query form extension page to retrieve data about the query performed by the page.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6b94b318-8356-4554-99fe-f82364325e6e
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- CQPM_GETPARAMETERS message Active Directory
topic_type:
- apiref
api_name:
- CQPM_GETPARAMETERS
api_location:
- Cmnquery.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CQPM\_GETPARAMETERS message

The **CQPM\_GETPARAMETERS** message is sent to the [**CQPageProc**](/windows/desktop/api/Cmnquery/nc-cmnquery-lpcqpageproc) callback function of a query form extension page to retrieve data about the query performed by the page.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**LPDSQUERYPARAMS**](/windows/desktop/api/Dsquery/ns-dsquery-dsqueryparams) value that receives data about the query performed by the page. If this parameter is **NULL**, the **DSQUERYPARAMS** structure must be allocated by the extension using the [**CoTaskMemAlloc**](https://msdn.microsoft.com/en-us/library/ms692727(v=VS.85).aspx) function.

</dd> </dl>

## Return value

Returns **S\_OK** if successful or a standard **HRESULT** error code otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Cmnquery.h</dt> </dl> |



## See also

<dl> <dt>

[**CQPageProc**](/windows/desktop/api/Cmnquery/nc-cmnquery-lpcqpageproc)
</dt> <dt>

[**DSQUERYPARAMS**](/windows/desktop/api/Dsquery/ns-dsquery-dsqueryparams)
</dt> <dt>

[**CoTaskMemAlloc**](https://msdn.microsoft.com/en-us/library/ms692727(v=VS.85).aspx)
</dt> </dl>

 

 





