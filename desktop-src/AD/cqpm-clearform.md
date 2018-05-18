---
title: CQPM\_CLEARFORM message
description: Sent to the CQPageProc callback function of a query for extension page when the contents of the page should be reset to the default values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '0fd3ec82-0566-43de-a7a1-4b6b76bf2050'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["CQPM_CLEARFORM message Active Directory"]
topic_type:
- apiref
api_name:
- CQPM_CLEARFORM
api_location:
- Cmnquery.h
api_type:
- HeaderDef
---

# CQPM\_CLEARFORM message

The **CQPM\_CLEARFORM** message is sent to the [**CQPageProc**](cqpageproc.md) callback function of a query for extension page when the contents of the page should be reset to the default values.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used.

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
</dt> </dl>

 

 





