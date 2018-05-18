---
title: CQPM\_PERSIST message
description: Sent to the CQPageProc callback function of a query form extension page to allow the page to read or write query data from persistent memory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'f01586dd-4ed3-45af-9e25-a596a693313d'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["CQPM_PERSIST message Active Directory"]
topic_type:
- apiref
api_name:
- CQPM_PERSIST
api_location:
- Cmnquery.h
api_type:
- HeaderDef
---

# CQPM\_PERSIST message

The **CQPM\_PERSIST** message is sent to the [**CQPageProc**](cqpageproc.md) callback function of a query form extension page to allow the page to read or write query data from persistent memory.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Contains nonzero to read the query data or zero to write the query data.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**IPersistQuery**](ipersistquery.md) interface that the query data should be read from or written to.

</dd> </dl>

## Return value

Returns **S\_OK** if successful or a standard **HRESULT** error code otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Cmnquery.h</dt> </dl> |



## See also

<dl> <dt>

[**CQPageProc**](cqpageproc.md)
</dt> <dt>

[**IPersistQuery**](ipersistquery.md)
</dt> </dl>

 

 





