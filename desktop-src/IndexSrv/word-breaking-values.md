---
title: Word-Breaking Values
description: Values 0xHHHH1780 to 0xHHHH179F are return values produced during word breaking. The following table gives the word-breaking values in alphabetical order.
ms.assetid: 85af046e-c809-47bc-9646-bd1584cd8e66
topic_type:
- apiref
api_name:
- LANGUAGE_E_DATABASE_NOT_FOUND
- LANGUAGE_S_LARGE_WORD
- PSINK_E_INDEX_ONLY
- PSINK_E_LARGE_ATTACHMENT
- PSINK_E_QUERY_ONLY
- PSINK_S_LARGE_WORD
- WBREAK_E_BUFFER_TOO_SMALL
- WBREAK_E_END_OF_TEXT
- WBREAK_E_INIT_FAILED
- WBREAK_E_QUERY_ONLY
api_location:
- Cierror.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Word-Breaking Values

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Values 0x*HHHH*1780 to 0x*HHHH*179F are return values produced during word breaking. The following table gives the word-breaking values in alphabetical order.



| Constant/value                                                                                                                                                                                                                                                                   | Description                                                                  |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| <span id="LANGUAGE_E_DATABASE_NOT_FOUND"></span><span id="language_e_database_not_found"></span><dl> <dt>**LANGUAGE\_E\_DATABASE\_NOT\_FOUND**</dt> <dt>0x80041784</dt> </dl> | LANGUAGE database/cache file could not be found.<br/>                  |
| <span id="LANGUAGE_S_LARGE_WORD"></span><span id="language_s_large_word"></span><dl> <dt>**LANGUAGE\_S\_LARGE\_WORD**</dt> <dt>0x00041781</dt> </dl>                          | Word larger than maximum length. May be truncated by word sink.<br/>   |
| <span id="PSINK_E_INDEX_ONLY"></span><span id="psink_e_index_only"></span><dl> <dt>**PSINK\_E\_INDEX\_ONLY**</dt> <dt>0x80041791</dt> </dl>                                   | Feature only available in index mode.<br/>                             |
| <span id="PSINK_E_LARGE_ATTACHMENT"></span><span id="psink_e_large_attachment"></span><dl> <dt>**PSINK\_E\_LARGE\_ATTACHMENT**</dt> <dt>0x80041792</dt> </dl>                 | Attachment type beyond valid range.<br/>                               |
| <span id="PSINK_E_QUERY_ONLY"></span><span id="psink_e_query_only"></span><dl> <dt>**PSINK\_E\_QUERY\_ONLY**</dt> <dt>0x80041790</dt> </dl>                                   | Feature only available in query mode.<br/>                             |
| <span id="PSINK_S_LARGE_WORD"></span><span id="psink_s_large_word"></span><dl> <dt>**PSINK\_S\_LARGE\_WORD**</dt> <dt>0x00041793</dt> </dl>                                   | Word larger than maximum length. May be truncated by phrase sink.<br/> |
| <span id="WBREAK_E_BUFFER_TOO_SMALL"></span><span id="wbreak_e_buffer_too_small"></span><dl> <dt>**WBREAK\_E\_BUFFER\_TOO\_SMALL**</dt> <dt>0x80041783</dt> </dl>             | Buffer too small to hold composed phrase.<br/>                         |
| <span id="WBREAK_E_END_OF_TEXT"></span><span id="wbreak_e_end_of_text"></span><dl> <dt>**WBREAK\_E\_END\_OF\_TEXT**</dt> <dt>0x80041780</dt> </dl>                            | End of text reached in text source.<br/>                               |
| <span id="WBREAK_E_INIT_FAILED"></span><span id="wbreak_e_init_failed"></span><dl> <dt>**WBREAK\_E\_INIT\_FAILED**</dt> <dt>0x80041785</dt> </dl>                             | Initialization of word breaker failed.<br/>                            |
| <span id="WBREAK_E_QUERY_ONLY"></span><span id="wbreak_e_query_only"></span><dl> <dt>**WBREAK\_E\_QUERY\_ONLY**</dt> <dt>0x80041782</dt> </dl>                                | Feature only available in query mode.<br/>                             |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>Cierror.h</dt> </dl> |



 

 





