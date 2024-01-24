---
title: CQPM_SETDEFAULTPARAMETERS message (Cmnquery.h)
description: Sent to the CQPageProc callback function of a query form extension page to set alternate default parameters for the page.
ms.assetid: 4d7f1c03-5c67-4f4c-b381-034a142251fe
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
ms.topic: reference
ms.date: 05/31/2018
---

# CQPM\_SETDEFAULTPARAMETERS message

The **CQPM\_SETDEFAULTPARAMETERS** message is sent to the [**CQPageProc**](/windows/desktop/api/Cmnquery/nc-cmnquery-lpcqpageproc) callback function of a query form extension page to set alternate default parameters for the page.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Contains nonzero if the page is the default page or zero otherwise.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**OPENQUERYWINDOW**](/windows/desktop/api/Cmnquery/ns-cmnquery-openquerywindow) structure that contains data about the directory service query dialog box.

</dd> </dl>

## Return value

The return value for this message is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Cmnquery.h</dt> </dl> |



## See also

<dl> <dt>

[**CQPageProc**](/windows/desktop/api/Cmnquery/nc-cmnquery-lpcqpageproc)
</dt> <dt>

[**OPENQUERYWINDOW**](/windows/desktop/api/Cmnquery/ns-cmnquery-openquerywindow)
</dt> </dl>

 

 





