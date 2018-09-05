---
title: CFSTR_DSOBJECTNAMES
description: The CFSTR\_DSOBJECTNAMES clipboard format provides a global memory handle (HGLOBAL) that contains DSOBJECTNAMES structure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b28428fa-1504-4dcc-9b2b-32ca1ae30ec5
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- CFSTR_DSOBJECTNAMES
api_location:
- DSClient.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CFSTR\_DSOBJECTNAMES

<dl> <dt>

<span id="CFSTR_DSOBJECTNAMES"></span><span id="cfstr_dsobjectnames"></span>**CFSTR\_DSOBJECTNAMES**
</dt> <dd> <dl> <dt>

"DsObjectNames"
</dt> <dt>



The **CFSTR\_DSOBJECTNAMES** clipboard format is supported by the [**IDataObject**](https://msdn.microsoft.com/en-us/library/ms688421(v=VS.85).aspx) provided by the [**ICommonQuery::OpenQueryWindow**](https://msdn.microsoft.com/en-us/library/ms676933(v=VS.85).aspx) method. The **CFSTR\_DSOBJECTNAMES** clipboard format provides a global memory handle (**HGLOBAL**) that contains [**DSOBJECTNAMES**](/windows/desktop/api/Dsclient/ns-dsclient-dsobjectnames) structure.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>DSClient.h</dt> </dl> |



## See also

<dl> <dt>

[**IDataObject**](https://msdn.microsoft.com/en-us/library/ms688421(v=VS.85).aspx)
</dt> <dt>

[**ICommonQuery::OpenQueryWindow**](https://msdn.microsoft.com/en-us/library/ms676933(v=VS.85).aspx)
</dt> <dt>

[**DSOBJECTNAMES**](/windows/desktop/api/Dsclient/ns-dsclient-dsobjectnames)
</dt> </dl>

 

 





