---
title: CFSTR\_DSQUERYPARAMS
description: The CFSTR\_DSQUERYPARAMS clipboard format provides a global memory handle (HGLOBAL) that contains a DSQUERYPARAMS structure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bb8aea98-8309-42bf-993d-fa408bb4deb2
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- CFSTR_DSQUERYPARAMS
api_location:
- DSQuery.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CFSTR\_DSQUERYPARAMS

<dl> <dt>

<span id="CFSTR_DSQUERYPARAMS"></span><span id="cfstr_dsqueryparams"></span>**CFSTR\_DSQUERYPARAMS**
</dt> <dd> <dl> <dt>

"DsQueryParameters"
</dt> <dt>



The **CFSTR\_DSQUERYPARAMS** clipboard format is supported by the [**IDataObject**](_ole_idataobject) provided by the [**ICommonQuery::OpenQueryWindow**](/windows/win32/Cmnquery/?branch=master) method. The **CFSTR\_DSQUERYPARAMS** clipboard format provides a global memory handle (**HGLOBAL**) that contains a [**DSQUERYPARAMS**](/windows/win32/Dsquery/ns-dsquery-dsqueryparams?branch=master) structure.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>DSQuery.h</dt> </dl> |



## See also

<dl> <dt>

[**IDataObject**](_ole_idataobject)
</dt> <dt>

[**ICommonQuery::OpenQueryWindow**](/windows/win32/Cmnquery/?branch=master)
</dt> <dt>

[**DSQUERYPARAMS**](/windows/win32/Dsquery/ns-dsquery-dsqueryparams?branch=master)
</dt> </dl>

 

 





