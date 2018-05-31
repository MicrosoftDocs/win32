---
title: STAT\_\ Constants
description: Reflects the execution (fill) status and the reliability status of a query.
ms.assetid: 133a6f43-a708-45f3-8b36-3d3bcf070f82
topic_type:
- apiref
api_name:
- STAT_BUSY
- STAT_ERROR
- STAT_DONE
- STAT_REFRESH
- STAT_PARTIAL_SCOPE
- STAT_NOISE_WORDS
- STAT_CONTENT_OUT_OF_DATE
- STAT_REFRESH_INCOMPLETE
- STAT_CONTENT_QUERY_INCOMPLETE
- STAT_TIME_LIMIT_EXCEEDED
- STAT_SHARING_VIOLATION
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

# STAT\_\* Constants

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Reflects the execution (fill) status and the reliability status of a query.

Bits 00-02: Fill Status: How query data is being updated, if at all.



| Constant/value                                                                                                                                                                                                      | Description                                                                                  |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| <span id="STAT_BUSY_"></span><span id="stat_busy_"></span><dl> <dt>**STAT\_BUSY** </dt> <dt>0</dt> </dl>         | The asynchronous query is still running.<br/>                                          |
| <span id="STAT_ERROR"></span><span id="stat_error"></span><dl> <dt>**STAT\_ERROR**</dt> <dt>0x1</dt> </dl>       | The query is in an error state.<br/>                                                   |
| <span id="STAT_DONE"></span><span id="stat_done"></span><dl> <dt>**STAT\_DONE**</dt> <dt>0x2</dt> </dl>          | The query is complete.<br/>                                                            |
| <span id="STAT_REFRESH"></span><span id="stat_refresh"></span><dl> <dt>**STAT\_REFRESH**</dt> <dt>0x3</dt> </dl> | The query is complete, but updates are resulting in additional query computation.<br/> |



Bits 03-15: Reliability: How accurate the query result is.



| Constant/value                                                                                                                                                                                                                                                            | Description                                                                                                                                     |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="STAT_PARTIAL_SCOPE"></span><span id="stat_partial_scope"></span><dl> <dt>**STAT\_PARTIAL\_SCOPE**</dt> <dt>0x8</dt> </dl>                                    | The results of the query are incomplete because one or more servers in a multivolume query were unavailable.<br/>                         |
| <span id="STAT_NOISE_WORDS"></span><span id="stat_noise_words"></span><dl> <dt>**STAT\_NOISE\_WORDS**</dt> <dt>0x10</dt> </dl>                                         | Noise words were replaced by wildcard characters in the content query.<br/>                                                               |
| <span id="STAT_CONTENT_OUT_OF_DATE"></span><span id="stat_content_out_of_date"></span><dl> <dt>**STAT\_CONTENT\_OUT\_OF\_DATE**</dt> <dt>0x20</dt> </dl>               | The results of the query might be incorrect because the query involved modified, but unindexed, files.<br/>                               |
| <span id="STAT_REFRESH_INCOMPLETE"></span><span id="stat_refresh_incomplete"></span><dl> <dt>**STAT\_REFRESH\_INCOMPLETE**</dt> <dt>0x40</dt> </dl>                    | The results of the query might be incorrect because the query involved modified and re-indexed files whose content was not included.<br/> |
| <span id="STAT_CONTENT_QUERY_INCOMPLETE"></span><span id="stat_content_query_incomplete"></span><dl> <dt>**STAT\_CONTENT\_QUERY\_INCOMPLETE**</dt> <dt>0x80</dt> </dl> | The content query was too complex to complete or required enumeration instead of use of the content index.<br/>                           |
| <span id="STAT_TIME_LIMIT_EXCEEDED"></span><span id="stat_time_limit_exceeded"></span><dl> <dt>**STAT\_TIME\_LIMIT\_EXCEEDED**</dt> <dt>0x100</dt> </dl>               | The results of the query might be incorrect because the query execution time reached the maximum allowable time.<br/>                     |
| <span id="STAT_SHARING_VIOLATION"></span><span id="stat_sharing_violation"></span><dl> <dt>**STAT\_SHARING\_VIOLATION**</dt> <dt>0x200</dt> </dl>                      | The results of the query might be incorrect because a sharing violation occurred on the query result.<br/>                                |



## Examples

This example retrieves the fill and reliability status values for the specified rowset.

``` syntax
XInterface<IRowsetInfo> xIRowsetInfo;
HRESULT hr = xIRowset->QueryInterface( IID_IRowsetInfo,
                                       xIRowsetInfo.GetQIPointer() );
 
if ( SUCCEEDED( hr ) )
{
    DBPROPID propId = MSIDXSPROP_ROWSETQUERYSTATUS;
    DBPROPIDSET propSet;
    propSet.rgPropertyIDs = &propId;
    propSet.cPropertyIDs = 1;
    const GUID guidRowsetExt = DBPROPSET_MSIDXS_ROWSETEXT;
    propSet.guidPropertySet = guidRowsetExt;
 
    ULONG cPropertySets = 0;
    DBPROPSET * pPropertySets;
 
    hr = xIRowsetInfo->GetProperties( 1,
                                      &propSet,
                                      &cPropertySets,
                                      &pPropertySets );
 
    if ( SUCCEEDED( hr ) )
    {
        DWORD dwStatus = pPropertySets->rgProperties->vValue.ulVal;
 
        CoTaskMemFree( pPropertySets->rgProperties );
        CoTaskMemFree( pPropertySets );
 
        DWORD dwFill = QUERY_FILL_STATUS( dwStatus );
        DWORD dwReliability = QUERY_RELIABILITY_STATUS( dwStatus );
    }
}
```

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

[**IRowsetInfo**](edc17ecf-242b-4910-8da1-7251fd8fc3c8)
</dt> <dt>

[DBPROPSET\_MSIDXS\_ROWSETEXT](dbpropset-msidxs-rowsetext.md)
</dt> </dl>

 

 





