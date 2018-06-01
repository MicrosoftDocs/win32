---
Description: Specifies scope depths and scope restriction paths. You can combine these flags by choosing one value from the first pair (QUERY\_SHALLOW or QUERY\_DEEP) and one value from the second pair (QUERY\_PHYSICAL\_PATH or QUERY\_VIRTUAL\_PATH).
ms.assetid: 77bf0e7e-d575-4ae7-b390-ab75eac2f58d
title: QUERY\_\* Scope Constants
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# QUERY\_\* Scope Constants

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Specifies scope depths and scope restriction paths. You can combine these flags by choosing one value from the first pair (QUERY\_SHALLOW or QUERY\_DEEP) and one value from the second pair (QUERY\_PHYSICAL\_PATH or QUERY\_VIRTUAL\_PATH).



| Constant/value                                                                                                                                                                                                       | Description                                                                                                                         |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| <span id="QUERY_SHALLOW"></span><span id="query_shallow"></span><dl> <dt>**QUERY\_SHALLOW**</dt> <dt>0</dt> </dl> | Only files in the scope directory are included in the results. Cannot be combined with QUERY\_DEEP.<br/>                      |
| <span id="QUERY_DEEP"></span><span id="query_deep"></span><dl> <dt>**QUERY\_DEEP**</dt> <dt>1</dt> </dl>          | Files in the scope directory and all subdirectories are included in the results. Cannot be combined with QUERY\_SHALLOW.<br/> |





| Constant/value                                                                                                                                                                                                                          | Description                                                                                                                  |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| <span id="QUERY_PHYSICAL_PATH"></span><span id="query_physical_path"></span><dl> <dt>**QUERY\_PHYSICAL\_PATH**</dt> <dt>0</dt> </dl> | The scope is a physical directory. Cannot be combined with QUERY\_VIRTUAL\_PATH.<br/>                                  |
| <span id="QUERY_VIRTUAL_PATH"></span><span id="query_virtual_path"></span><dl> <dt>**QUERY\_VIRTUAL\_PATH**</dt> <dt>2</dt> </dl>    | The scope is a virtual (Internet Information Services) directory. Cannot be combined with QUERY\_PHYSICAL\_PATH. <br/> |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>Ntquery.h</dt> </dl> |



## See also

<dl> <dt>

[**CIMakeICommand**](/windows/desktop/api/Ntquery/nf-ntquery-cimakeicommand)
</dt> <dt>

[DBPROPSET\_FSCIFRMWRK\_EXT](dbpropset-fscifrmwrk-ext.md)
</dt> </dl>

 

 




