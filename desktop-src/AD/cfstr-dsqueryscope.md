---
title: CFSTR\_DSQUERYSCOPE
description: The CFSTR\_DSQUERYSCOPE clipboard format provides a global memory handle (HGLOBAL) that contains a string that specifies the query scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3cf51543-eca4-466c-bf0c-1351fd90798b
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- CFSTR_DSQUERYSCOPE
api_location:
- DSQuery.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CFSTR\_DSQUERYSCOPE

<dl> <dt>

<span id="CFSTR_DSQUERYSCOPE"></span><span id="cfstr_dsqueryscope"></span>**CFSTR\_DSQUERYSCOPE**
</dt> <dd> <dl> <dt>

"DsQueryScope"
</dt> <dt>



The **CFSTR\_DSQUERYSCOPE** clipboard format is supported by the [**IDataObject**](https://msdn.microsoft.com/windows/desktop/8a002deb-2727-456c-8078-a9b0d5893ed4) provided by the [**ICommonQuery::OpenQueryWindow**](/windows/desktop/api/Cmnquery/) method. The **CFSTR\_DSQUERYSCOPE** clipboard format provides a global memory handle (**HGLOBAL**) that contains a string that specifies the query scope.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>DSQuery.h</dt> </dl> |



## See also

<dl> <dt>

[**IDataObject**](https://msdn.microsoft.com/windows/desktop/8a002deb-2727-456c-8078-a9b0d5893ed4)
</dt> <dt>

[**ICommonQuery::OpenQueryWindow**](/windows/desktop/api/Cmnquery/)
</dt> </dl>

 

 





