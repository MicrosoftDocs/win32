---
Description: Read-Only Variables Available in .Htx Files
ms.assetid: 0167a1a9-0481-4b26-aa4c-dc20f212a731
title: Read-Only Variables Available in .Htx Files
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Read-Only Variables Available in .Htx Files

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following variables are available for use in .htx files. These are set based upon the results of the search. In addition, the other .idq variables mentioned below can be used in the .htx file. In the detail section of the .htx file, any output columns mentioned in the CiColumns parameter can also be used.



| Variable Name                                                                                                             | Meaning                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="_idxs_cibookmark_var"></span><span id="_IDXS_CIBOOKMARK_VAR"></span>CiBookmark                                  | Reference to the first row on the page.                                                                                                                                                         |
| <span id="_idxs_cicontainsfirstrecord_var"></span><span id="_IDXS_CICONTAINSFIRSTRECORD_VAR"></span>CiContainsFirstRecord | Set to 1 if this page contains the first record of the query results; 0 otherwise.                                                                                                              |
| <span id="_idxs_cicontainslastrecord_var"></span><span id="_IDXS_CICONTAINSLASTRECORD_VAR"></span>CiContainsLastRecord    | Set to 1 if this page contain the last record of the query results; 0 otherwise. For a sequential query, this will not be accurate until after the &lt;%enddetail%&gt;section in the .htx file. |
| <span id="_idxs_cicurrentpagenumber_var"></span><span id="_IDXS_CICURRENTPAGENUMBER_VAR"></span>CiCurrentPageNumber       | Current page number of query results (that is, page number x of y pages).                                                                                                                       |
| <span id="_idxs_cicurrentrecordnumber_var"></span><span id="_IDXS_CICURRENTRECORDNUMBER_VAR"></span>CiCurrentRecordNumber | Number displayed for current record.                                                                                                                                                            |
| <span id="_idxs_cierrormessage_var"></span><span id="_IDXS_CIERRORMESSAGE_VAR"></span>CiErrorMessage                      | Error message. Available only for error pages. See [Error Messages and Error Pages](error-messages-and-error-pages.md) for possible error messages.                                            |
| <span id="_idxs_cierrornumber_var"></span><span id="_IDXS_CIERRORNUMBER_VAR"></span>CiErrorNumber                         | Error number. Available only for error pages.                                                                                                                                                   |
| <span id="_idxs_cifirstrecordnumber_var"></span><span id="_IDXS_CIFIRSTRECORDNUMBER_VAR"></span>CiFirstRecordNumber       | Record number of first record on a page.                                                                                                                                                        |
| <span id="_idxs_cilastrecordnumber_var"></span><span id="_IDXS_CILASTRECORDNUMBER_VAR"></span>CiLastRecordNumber          | Last record number on a page. For a sequential query, this will not be accurate until after the &lt;%enddetail%&gt; section in the .htx file.                                                   |
| <span id="_idxs_cimatchedrecordcount_var"></span><span id="_IDXS_CIMATCHEDRECORDCOUNT_VAR"></span>CiMatchedRecordCount    | Total number of records matching a query. Referring to this variable from the .htx file will force the search to use a nonsequential query.                                                     |
| <span id="_idxs_cioutofdate_var"></span><span id="_IDXS_CIOUTOFDATE_VAR"></span>CiOutOfDate                               | Set to 1 if the content index is out of date; 0 otherwise.                                                                                                                                      |
| <span id="_idxs_ciqueryincomplete_var"></span><span id="_IDXS_CIQUERYINCOMPLETE_VAR"></span>CiQueryIncomplete             | Set to 1 if the query could not be resolved using the content index and CiForceUseCI was set; 0 otherwise.                                                                                      |
| <span id="_idxs_ciquerytimedout_var"></span><span id="_IDXS_CIQUERYTIMEDOUT_VAR"></span>CiQueryTimedOut                   | Set to 1 if the query exceeded the time limit for execution; 0 otherwise.                                                                                                                       |
| <span id="_idxs_ciquerydate_var"></span><span id="_IDXS_CIQUERYDATE_VAR"></span>CiQueryDate                               | Date (at the web server) the query was executed.                                                                                                                                                |
| <span id="_idxs_ciquerytime_var"></span><span id="_IDXS_CIQUERYTIME_VAR"></span>CiQueryTime                               | Time (at the web server) the query was executed.                                                                                                                                                |
| <span id="_idxs_ciquerytimezone_var"></span><span id="_IDXS_CIQUERYTIMEZONE_VAR"></span>CiQueryTimeZone                   | Time zone of the web server.                                                                                                                                                                    |
| <span id="_idxs_cirecordsnextpage_var"></span><span id="_IDXS_CIRECORDSNEXTPAGE_VAR"></span>CiRecordsNextPage             | Number of records on the next page. Referring to this variable from the .htx file will force the search to use a nonsequential query.                                                           |
| <span id="_idxs_citotalnumberpages_var"></span><span id="_IDXS_CITOTALNUMBERPAGES_VAR"></span>CiTotalNumberPages          | Total number of pages used to contain query results. Referring to this variable from the .htx file will force the search to use a nonsequential query.                                          |
| <span id="_idxs_civersionmajor_var"></span><span id="_IDXS_CIVERSIONMAJOR_VAR"></span>CiVersionMajor                      | The major version of Indexing Service.                                                                                                                                                          |
| <span id="_idxs_civersionminor_var"></span><span id="_IDXS_CIVERSIONMINOR_VAR"></span>CiVersionMinor                      | The minor version of Indexing Service.                                                                                                                                                          |



 

 

 



