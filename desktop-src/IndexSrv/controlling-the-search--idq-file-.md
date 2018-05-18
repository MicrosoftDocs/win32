---
title: Controlling the Search (.Idq File)
description: Controlling the Search (.Idq File)
ms.assetid: '0de08c8d-14e2-4c89-b1b9-4278671f9cda'
---

# Controlling the Search (.Idq File)

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The Internet Data Query (.idq) file defines query parameters such as the scope of your search, any restrictions, and query results sets. The following example shows a basic .idq file:


```
[Query]
# CiCatalog=d:\ <= COMMENTED OUT - default registry value used
CiColumns=filename,size,rank,characterization,vpath,DocTitle,write
CiRestriction=%CiRestriction%
CiMaxRecordsInResultSet=300
CiMaxRecordsPerPage=10
CiScope=/
CiFlags=DEEP
CiTemplate=/iissamples/issamples/ixtourqy.htx
CiSort=rank[d]
CiForceUseCi=true
```



The following list explains each line of the sample .idq file:

<dl> <dt>

<span id="_Query_"></span><span id="_query_"></span><span id="_QUERY_"></span>\[Query\]
</dt> <dd>

Identifies the following information as a query restriction.

</dd> <dt>

<span id="CiCatalog_d___"></span><span id="cicatalog_d___"></span><span id="CICATALOG_D___"></span>CiCatalog=d: \\
</dt> <dd>

Points to the index to use. In this case, the statement is commented out, so a default is used.

</dd> <dt>

<span id="CiColumns_filename_size_rank_characterization__vpath_DocTitle_write"></span><span id="cicolumns_filename_size_rank_characterization__vpath_doctitle_write"></span><span id="CICOLUMNS_FILENAME_SIZE_RANK_CHARACTERIZATION__VPATH_DOCTITLE_WRITE"></span>CiColumns=filename,size,rank,characterization, vpath,DocTitle,write
</dt> <dd>

Indicates the kind of information to return in the result set.

</dd> <dt>

<span id="CiRestriction__CiRestriction_"></span><span id="cirestriction__cirestriction_"></span><span id="CIRESTRICTION__CIRESTRICTION_"></span>CiRestriction=%CiRestriction%
</dt> <dd>

Indicates the query terms to search for. In this case, the *CiRestriction* form parameter is used.

</dd> <dt>

<span id="CiMaxRecordsInResultSet_300"></span><span id="cimaxrecordsinresultset_300"></span><span id="CIMAXRECORDSINRESULTSET_300"></span>CiMaxRecordsInResultSet=300
</dt> <dd>

Sets the maximum number of results to be returned; in this example, 300.

</dd> <dt>

<span id="CiMaxRecordsPerPage_10"></span><span id="cimaxrecordsperpage_10"></span><span id="CIMAXRECORDSPERPAGE_10"></span>CiMaxRecordsPerPage=10
</dt> <dd>

Determines how many results are shown on each webpage returned. In this case, 10 results will be shown per webpage.

</dd> <dt>

<span id="CiScope__"></span><span id="ciscope__"></span><span id="CISCOPE__"></span>CiScope=/
</dt> <dd>

Tells where to start the query. In this example, the query starts at the root of the virtual directory space. You can list more than one virtual directory in your scope by separating the directories with a comma (,). For example: CiScope=/docs,/work,/school

</dd> <dt>

<span id="CiFlags_DEEP"></span><span id="ciflags_deep"></span><span id="CIFLAGS_DEEP"></span>CiFlags=DEEP
</dt> <dd>

Instructs the query to search all subdirectories within the scope.

</dd> <dt>

<span id="CiTemplate__iissamples_issamples_ixtourqy.htx_"></span><span id="citemplate__iissamples_issamples_ixtourqy.htx_"></span><span id="CITEMPLATE__IISSAMPLES_ISSAMPLES_IXTOURQY.HTX_"></span>CiTemplate=/iissamples/issamples/ixtourqy.htx 
</dt> <dd>

Indicates which file to use to format the results; in this case, Ixtourqy.htx.

</dd> <dt>

<span id="CiSort_rank_d_"></span><span id="cisort_rank_d_"></span><span id="CISORT_RANK_D_"></span>CiSort=rank\[d\]
</dt> <dd>

Tells how to sort the results. This example calls for results to be listed in descending \[d\] rank order; that is, the results are listed in order from the file with the most hits to the file with the least hits.

</dd> <dt>

<span id="CiForceUseCi_true"></span><span id="ciforceuseci_true"></span><span id="CIFORCEUSECI_TRUE"></span>CiForceUseCi=true
</dt> <dd>

This is an optional variable that, when set to TRUE, forces Indexing Service to search the content index even if it is out of date.

</dd> </dl>

When the results are returned in raw format, Indexing Service formats the results according to the .htx file specified in the [CiTemplate](variables-in-forms-and-in-idq-files.md#-idxs-citemplate-var) parameter.

For details about the .idq file and how to format it, see [Internet Data Query Files](internet-data-query-files.md).

 

 




