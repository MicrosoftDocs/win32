---
title: Filter-Interface Values
description: Values 0xHHHH1700 to 0xHHHH172F are return values produced when calling the methods of the IFilter interface to extract the text from a document, including any embedded or linked objects within it.
ms.assetid: a9f94b0d-f3d0-4cf1-9dfe-74c938601abc
topic_type:
- apiref
api_name:
- FILTER_E_ACCESS
- FILTER_E_EMBEDDING_UNAVAILABLE
- FILTER_E_END_OF_CHUNKS
- FILTER_E_LINK_UNAVAILABLE
- FILTER_E_NO_MORE_TEXT
- FILTER_E_NO_MORE_VALUES
- FILTER_E_NO_TEXT
- FILTER_E_NO_VALUES
- FILTER_E_PASSWORD
- FILTER_E_UNKNOWNFORMAT
- FILTER_S_LAST_TEXT
- FILTER_S_LAST_VALUES
- FILTER_W_MONIKER_CLIPPED
api_location:
- Cierror.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Filter-Interface Values

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Values 0x*HHHH*1700 to 0x*HHHH*172F are return values produced when calling the methods of the [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface to extract the text from a document, including any embedded or linked objects within it. The following table gives the filter-interface values in alphabetical order.



| Constant/value                                                                                                                                                                                                                                                                     | Description                                                               |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| <span id="FILTER_E_ACCESS"></span><span id="filter_e_access"></span><dl> <dt>**FILTER\_E\_ACCESS**</dt> <dt>0x80041703</dt> </dl>                                               | Unable to access object.<br/>                                       |
| <span id="FILTER_E_EMBEDDING_UNAVAILABLE"></span><span id="filter_e_embedding_unavailable"></span><dl> <dt>**FILTER\_E\_EMBEDDING\_UNAVAILABLE**</dt> <dt>0x80041707</dt> </dl> | Unable to bind [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) for embedded object.<br/> |
| <span id="FILTER_E_END_OF_CHUNKS"></span><span id="filter_e_end_of_chunks"></span><dl> <dt>**FILTER\_E\_END\_OF\_CHUNKS**</dt> <dt>0x80041700</dt> </dl>                        | No more chunks of text available in object.<br/>                    |
| <span id="FILTER_E_LINK_UNAVAILABLE"></span><span id="filter_e_link_unavailable"></span><dl> <dt>**FILTER\_E\_LINK\_UNAVAILABLE**</dt> <dt>0x80041708</dt> </dl>                | Unable to bind [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) for linked object.<br/>   |
| <span id="FILTER_E_NO_MORE_TEXT"></span><span id="filter_e_no_more_text"></span><dl> <dt>**FILTER\_E\_NO\_MORE\_TEXT**</dt> <dt>0x80041701</dt> </dl>                           | No more text available in chunk.<br/>                               |
| <span id="FILTER_E_NO_MORE_VALUES"></span><span id="filter_e_no_more_values"></span><dl> <dt>**FILTER\_E\_NO\_MORE\_VALUES**</dt> <dt>0x80041702</dt> </dl>                     | No more property values available in chunk.<br/>                    |
| <span id="FILTER_E_NO_TEXT"></span><span id="filter_e_no_text"></span><dl> <dt>**FILTER\_E\_NO\_TEXT**</dt> <dt>0x80041705</dt> </dl>                                           | No text in current chunk.<br/>                                      |
| <span id="FILTER_E_NO_VALUES"></span><span id="filter_e_no_values"></span><dl> <dt>**FILTER\_E\_NO\_VALUES**</dt> <dt>0x80041706</dt> </dl>                                     | No values in current chunk.<br/>                                    |
| <span id="FILTER_E_PASSWORD"></span><span id="filter_e_password"></span><dl> <dt>**FILTER\_E\_PASSWORD**</dt> <dt>0x8004170B</dt> </dl>                                         | File was not filtered due to password protection.<br/>              |
| <span id="FILTER_E_UNKNOWNFORMAT"></span><span id="filter_e_unknownformat"></span><dl> <dt>**FILTER\_E\_UNKNOWNFORMAT**</dt> <dt>0x8004170C</dt> </dl>                          | The document format is not recognized by the filter.<br/>           |
| <span id="FILTER_S_LAST_TEXT"></span><span id="filter_s_last_text"></span><dl> <dt>**FILTER\_S\_LAST\_TEXT**</dt> <dt>0x00041709</dt> </dl>                                     | This is the last text in the current chunk.<br/>                    |
| <span id="FILTER_S_LAST_VALUES"></span><span id="filter_s_last_values"></span><dl> <dt>**FILTER\_S\_LAST\_VALUES**</dt> <dt>0x0004170A</dt> </dl>                               | This is the last value in the current chunk.<br/>                   |
| <span id="FILTER_W_MONIKER_CLIPPED"></span><span id="filter_w_moniker_clipped"></span><dl> <dt>**FILTER\_W\_MONIKER\_CLIPPED**</dt> <dt>0x00041704</dt> </dl>                   | Moniker does not cover entire region.<br/>                          |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>Cierror.h</dt> </dl> |



 

 





