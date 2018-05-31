---
title: CICAT\_\ Constants
description: Set and retrieve the state of an Indexing Service catalog. When setting the state, these values represent mutually exclusive states of the catalog and are not meant to be combined.
ms.assetid: 0316d876-4d0d-4b1e-a944-e5621b625922
topic_type:
- apiref
api_name:
- CICAT_GET_STATE
- CICAT_NO_QUERY
- CICAT_READONLY
- CICAT_STOPPED
- CICAT_WRITABLE
api_location:
- Ntquery.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CICAT\_\* Constants

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Set and retrieve the state of an Indexing Service catalog. When setting the state, these values represent mutually exclusive states of the catalog and are not meant to be combined.



| Constant/value                                                                                                                                                                                                                 | Description                                                                                    |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| <span id="CICAT_GET_STATE"></span><span id="cicat_get_state"></span><dl> <dt>**CICAT\_GET\_STATE**</dt> <dt>0x10</dt> </dl> | Retrieve the current state of the catalog.<br/>                                          |
| <span id="CICAT_NO_QUERY"></span><span id="cicat_no_query"></span><dl> <dt>**CICAT\_NO\_QUERY**</dt> <dt>0x8</dt> </dl>     | Set the catalog to a no-query state. Indexing can take place, but querying cannot. <br/> |
| <span id="CICAT_READONLY"></span><span id="cicat_readonly"></span><dl> <dt>**CICAT\_READONLY**</dt> <dt>0x2</dt> </dl>      | Set the catalog to read-only. Querying can take place, but indexing cannot.<br/>         |
| <span id="CICAT_STOPPED"></span><span id="cicat_stopped"></span><dl> <dt>**CICAT\_STOPPED**</dt> <dt>0x1</dt> </dl>         | Stop the catalog. No querying or indexing can take place.<br/>                           |
| <span id="CICAT_WRITABLE"></span><span id="cicat_writable"></span><dl> <dt>**CICAT\_WRITABLE**</dt> <dt>0x4</dt> </dl>      | Set the catalog to be writable. Both indexing and querying can take place. <br/>         |



## Remarks

The following table describes the various states possible for an Indexing Service catalog. You do not have to stop the catalog first to set its state. To retrieve only the current state, use a setting of CICAT\_GET\_STATE.



| Desired state              | Constant         |
|----------------------------|------------------|
| Catalog stopped or offline | CICAT\_STOPPED   |
| Processing queries only    | CICAT\_READONLY  |
| Querying and indexing      | CICAT\_WRITABLE  |
| Indexing only              | CICAT\_NO\_QUERY |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>Ntquery.h</dt> </dl> |



## See also

<dl> <dt>

[**SetCatalogState**](/windows/desktop/api/Ntquery/nf-ntquery-setcatalogstate)
</dt> </dl>

 

 





