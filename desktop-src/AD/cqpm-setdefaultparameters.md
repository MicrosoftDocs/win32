---
title: CQPM\_SETDEFAULTPARAMETERS message
description: Sent to the CQPageProc callback function of a query form extension page to set alternate default parameters for the page.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4d7f1c03-5c67-4f4c-b381-034a142251fe
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- CQPM_SETDEFAULTPARAMETERS message Active Directory
topic_type:
- apiref
api_name:
- CQPM_SETDEFAULTPARAMETERS
api_location:
- Cmnquery.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CQPM\_SETDEFAULTPARAMETERS message

The **CQPM\_SETDEFAULTPARAMETERS** message is sent to the [**CQPageProc**](/windows/win32/Cmnquery/nc-cmnquery-lpcqpageproc?branch=master) callback function of a query form extension page to set alternate default parameters for the page.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Contains nonzero if the page is the default page or zero otherwise.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**OPENQUERYWINDOW**](/windows/win32/Cmnquery/ns-cmnquery-openquerywindow?branch=master) structure that contains data about the directory service query dialog box.

</dd> </dl>

## Return value

The return value for this message is ignored.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Cmnquery.h</dt> </dl> |



## See also

<dl> <dt>

[**CQPageProc**](/windows/win32/Cmnquery/nc-cmnquery-lpcqpageproc?branch=master)
</dt> <dt>

[**OPENQUERYWINDOW**](/windows/win32/Cmnquery/ns-cmnquery-openquerywindow?branch=master)
</dt> </dl>

 

 





