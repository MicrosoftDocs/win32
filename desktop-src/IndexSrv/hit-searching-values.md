---
error-parsing-yaml: 
---

# Hit-Searching Values

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Values 0x*HHHH*16A0 to 0x*HHHH*16AF are return values produced by calling the methods of the **ISearchQueryHits** interface when searching for query hits. The following table gives the hit-searching values in alphabetical order.



| Constant/value                                                                                                                                                                                                                                   | Description                                                                                                              |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| <span id="SEARCH_E_NOMONIKER"></span><span id="search_e_nomoniker"></span><dl> <dt>**SEARCH\_E\_NOMONIKER**</dt> <dt>0x800416A1</dt> </dl>    | Retrieval of hits as monikers is not supported (by filter passed into [**IFilter::Init**](/windows/desktop/api/Filter/nf-filter-ifilter-init)).<br/> |
| <span id="SEARCH_E_NOREGION"></span><span id="search_e_noregion"></span><dl> <dt>**SEARCH\_E\_NOREGION**</dt> <dt>0x800416A2</dt> </dl>       | Retrieval of hits as filter regions is not supported (by filter passed into Init).<br/>                            |
| <span id="SEARCH_S_NOMOREHITS"></span><span id="search_s_nomorehits"></span><dl> <dt>**SEARCH\_S\_NOMOREHITS**</dt> <dt>0x000416A0</dt> </dl> | End of hits has been reached.<br/>                                                                                 |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>Cierror.h</dt> </dl> |



 

 





