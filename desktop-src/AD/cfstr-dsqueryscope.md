---
title: CFSTR_DSQUERYSCOPE (DSQuery.h)
description: The CFSTR\_DSQUERYSCOPE clipboard format provides a global memory handle (HGLOBAL) that contains a string that specifies the query scope.
ms.assetid: 3cf51543-eca4-466c-bf0c-1351fd90798b
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- CFSTR_DSQUERYSCOPE
api_location:
- DSQuery.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CFSTR\_DSQUERYSCOPE

<dl> <dt>

<span id="CFSTR_DSQUERYSCOPE"></span><span id="cfstr_dsqueryscope"></span>**CFSTR\_DSQUERYSCOPE**
</dt> <dd> <dl> <dt>

"DsQueryScope"
</dt> <dt>



The **CFSTR\_DSQUERYSCOPE** clipboard format is supported by the [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) provided by the [**ICommonQuery::OpenQueryWindow**](/windows/win32/api/cmnquery/nf-cmnquery-icommonquery-openquerywindow) method. The **CFSTR\_DSQUERYSCOPE** clipboard format provides a global memory handle (**HGLOBAL**) that contains a string that specifies the query scope.


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
</dt> </dl>

 

