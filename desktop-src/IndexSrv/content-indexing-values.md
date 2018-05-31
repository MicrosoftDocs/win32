---
error-parsing-yaml: 
---

# Content-Indexing Values

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Values 0x*HHHH*1680 to 0x*HHHH*169F and 0x*HHHH*1730 to 0x*HHHH*173F are return values produced by the Content-Indexing daemon (CiDaemon) as it filters documents and adds their word lists to the existing indexes in the catalog. The following table gives the content-indexing values in alphabetical order.



| Constant/value                                                                                                                                                                                                                                                                                              | Description                                                                                                  |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|
| <span id="FDAEMON_E_CHANGEUPDATEFAILED"></span><span id="fdaemon_e_changeupdatefailed"></span><dl> <dt>**FDAEMON\_E\_CHANGEUPDATEFAILED**</dt> <dt>0x80041684</dt> </dl>                                 | Documents not stored in content index because update of change list failed.<br/>                       |
| <span id="FDAEMON_E_FATALERROR"></span><span id="fdaemon_e_fatalerror"></span><dl> <dt>**FDAEMON\_E\_FATALERROR**</dt> <dt>0x80041682</dt> </dl>                                                         | A critical error occurred during document filtering. Consult system administrator.<br/>                |
| <span id="FDAEMON_E_LOWRESOURCE"></span><span id="fdaemon_e_lowresource"></span><dl> <dt>**FDAEMON\_E\_LOWRESOURCE**</dt> <dt>0x80041681</dt> </dl>                                                      | The system is running out of one of more resources needed for filtering, usually memory.<br/>          |
| <span id="FDAEMON_E_NOWORDLIST"></span><span id="fdaemon_e_nowordlist"></span><dl> <dt>**FDAEMON\_E\_NOWORDLIST**</dt> <dt>0x80041687</dt> </dl>                                                         | No wordlist is being constructed. May happen after fatal filter error.<br/>                            |
| <span id="FDAEMON_E_PARTITIONDELETED"></span><span id="fdaemon_e_partitiondeleted"></span><dl> <dt>**FDAEMON\_E\_PARTITIONDELETED**</dt> <dt>0x80041683</dt> </dl>                                       | Documents not stored in content index because partition has been deleted.<br/>                         |
| <span id="FDAEMON_E_TOOMANYFILTEREDBLOCKS"></span><span id="fdaemon_e_toomanyfilteredblocks"></span><dl> <dt>**FDAEMON\_E\_TOOMANYFILTEREDBLOCKS**</dt> <dt>0x80041688</dt> </dl>                        | During document filtering the limit on buffers has been exceeded.<br/>                                 |
| <span id="FDAEMON_E_WORDLISTCOMMITFAILED"></span><span id="fdaemon_e_wordlistcommitfailed"></span><dl> <dt>**FDAEMON\_E\_WORDLISTCOMMITFAILED**</dt> <dt>0x80041686</dt> </dl>                           | Commit of wordlist failed. Data not available for query.<br/>                                          |
| <span id="FDAEMON_W_EMPTYWORDLIST"></span><span id="fdaemon_w_emptywordlist"></span><dl> <dt>**FDAEMON\_W\_EMPTYWORDLIST**</dt> <dt>0x00041685</dt> </dl>                                                | Final wordlist was empty.<br/>                                                                         |
| <span id="FDAEMON_W_WORDLISTFULL"></span><span id="fdaemon_w_wordlistfull"></span><dl> <dt>**FDAEMON\_W\_WORDLISTFULL**</dt> <dt>0x00041680</dt> </dl>                                                   | Wordlist has reached maximum size. Additional documents should not be filtered.<br/>                   |
| <span id="FILTER_E_ALREADY_OPEN"></span><span id="filter_e_already_open"></span><dl> <dt>**FILTER\_E\_ALREADY\_OPEN**</dt> <dt>0x80041736</dt> </dl>                                                     | A file is already open. Cannot open another one while file is open.<br/>                               |
| <span id="FILTER_E_CONTENTINDEXCORRUPT"></span><span id="filter_e_contentindexcorrupt"></span><dl> <dt>**FILTER\_E\_CONTENTINDEXCORRUPT**</dt> <dt>0xC0041734</dt> </dl>                                 | The content index is corrupt. A content scan will to be scheduled after chkdsk or autochk is run.<br/> |
| <span id="FILTER_E_IN_USE"></span><span id="filter_e_in_use"></span><dl> <dt>**FILTER\_E\_IN\_USE**</dt> <dt>0x80041738</dt> </dl>                                                                       | The document is in use by another process.<br/>                                                        |
| <span id="FILTER_E_NO_SUCH_PROPERTY"></span><span id="filter_e_no_such_property"></span><dl> <dt>**FILTER\_E\_NO\_SUCH\_PROPERTY**</dt> <dt>0x8004173B</dt> </dl>                                        | There is no property with the given GUID.<br/>                                                         |
| <span id="FILTER_E_NOT_OPEN"></span><span id="filter_e_not_open"></span><dl> <dt>**FILTER\_E\_NOT\_OPEN**</dt> <dt>0x80041739</dt> </dl>                                                                 | The document is not opened.<br/>                                                                       |
| <span id="FILTER_E_OFFLINE"></span><span id="filter_e_offline"></span><dl> <dt>**FILTER\_E\_OFFLINE**</dt> <dt>0x8004173D</dt> </dl>                                                                     | The document is offline.<br/>                                                                          |
| <span id="FILTER_E_PARTIALLY_FILTERED"></span><span id="filter_e_partially_filtered"></span><dl> <dt>**FILTER\_E\_PARTIALLY\_FILTERED**</dt> <dt>0x8004173E</dt> </dl>                                   | The document was too large to filter in its entirety. Portions of the document were not emitted.<br/>  |
| <span id="FILTER_E_TOO_BIG"></span><span id="filter_e_too_big"></span><dl> <dt>**FILTER\_E\_TOO\_BIG**</dt> <dt>0x80041730</dt> </dl>                                                                    | File is too large to filter.<br/>                                                                      |
| <span id="FILTER_E_UNREACHABLE"></span><span id="filter_e_unreachable"></span><dl> <dt>**FILTER\_E\_UNREACHABLE**</dt> <dt>0x80041737</dt> </dl>                                                         | The file is not reachable.<br/>                                                                        |
| <span id="FILTER_S_CONTENTSCAN_DELAYED"></span><span id="filter_s_contentscan_delayed"></span><dl> <dt>**FILTER\_S\_CONTENTSCAN\_DELAYED**</dt> <dt>0x00041733</dt> </dl>                                | A content scan of the disk needs to be scheduled for execution later.<br/>                             |
| <span id="FILTER_S_DISK_FULL"></span><span id="filter_s_disk_full"></span><dl> <dt>**FILTER\_S\_DISK\_FULL**</dt> <dt>0x00041735</dt> </dl>                                                              | The disk is getting full.<br/>                                                                         |
| <span id="FILTER_S_FULL_CONTENTSCAN_IMMEDIATE"></span><span id="filter_s_full_contentscan_immediate"></span><dl> <dt>**FILTER\_S\_FULL\_CONTENTSCAN\_IMMEDIATE**</dt> <dt>0x00041732</dt> </dl>          | A full content scan of the disk needs to be scheduled for immediate execution.<br/>                    |
| <span id="FILTER_S_NO_PROPSETS"></span><span id="filter_s_no_propsets"></span><dl> <dt>**FILTER\_S\_NO\_PROPSETS**</dt> <dt>0x0004173A</dt> </dl>                                                        | The document has no property sets.<br/>                                                                |
| <span id="FILTER_S_NO_SECURITY_DESCRIPTOR"></span><span id="filter_s_no_security_descriptor"></span><dl> <dt>**FILTER\_S\_NO\_SECURITY\_DESCRIPTOR**</dt> <dt>0x0004173C</dt> </dl>                      | The document has no security descriptor.<br/>                                                          |
| <span id="FILTER_S_PARTIAL_CONTENTSCAN_IMMEDIATE"></span><span id="filter_s_partial_contentscan_immediate"></span><dl> <dt>**FILTER\_S\_PARTIAL\_CONTENTSCAN\_IMMEDIATE**</dt> <dt>0x00041731</dt> </dl> | A partial content scan of the disk needs to be scheduled for immediate execution.<br/>                 |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>Cierror.h</dt> </dl> |



 

 





