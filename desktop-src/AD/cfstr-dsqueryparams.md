---
title: CFSTR_DSQUERYPARAMS (DSQuery.h)
description: The CFSTR\_DSQUERYPARAMS clipboard format provides a global memory handle (HGLOBAL) that contains a DSQUERYPARAMS structure.
ms.assetid: bb8aea98-8309-42bf-993d-fa408bb4deb2
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- CFSTR_DSQUERYPARAMS
api_location:
- DSQuery.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CFSTR\_DSQUERYPARAMS

<dl> <dt>

<span id="CFSTR_DSQUERYPARAMS"></span><span id="cfstr_dsqueryparams"></span>**CFSTR\_DSQUERYPARAMS**
</dt> <dd> <dl> <dt>

"DsQueryParameters"
</dt> <dt>



The **CFSTR\_DSQUERYPARAMS** clipboard format is supported by the [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) provided by the [**ICommonQuery::OpenQueryWindow**](/windows/win32/api/cmnquery/nf-cmnquery-icommonquery-openquerywindow) method. The **CFSTR\_DSQUERYPARAMS** clipboard format provides a global memory handle (**HGLOBAL**) that contains a [**DSQUERYPARAMS**](/windows/desktop/api/Dsquery/ns-dsquery-dsqueryparams) structure.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>DSQuery.h</dt> </dl> |



## See also

<dl> <dt>

[**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject)
</dt> <dt>

[**ICommonQuery::OpenQueryWindow**](/windows/win32/api/cmnquery/nf-cmnquery-icommonquery-openquerywindow)
</dt> <dt>

[**DSQUERYPARAMS**](/windows/desktop/api/Dsquery/ns-dsquery-dsqueryparams)
</dt> </dl>

 

