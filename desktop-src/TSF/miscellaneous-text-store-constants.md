---
title: Miscellaneous Text Store Constants
description: The miscellaneous text store constants set certain properties for text stores.
ms.assetid: 6e05ed74-fff3-4bc4-a21e-9af9492af23b
topic_type:
- apiref
api_name:
- TS_DEFAULT_SELECTION
- TS_GEA_HIDDEN
- TS_GTA_HIDDEN
- TS_ST_CORRECTION
- TS_TC_CORRECTION
- TS_VCOOKIE_NUL
api_location:
- Textstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Miscellaneous Text Store Constants

The miscellaneous text store constants set certain properties for text stores.



| Constant/value                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TS_DEFAULT_SELECTION"></span><span id="ts_default_selection"></span><dl> <dt>**TS\_DEFAULT\_SELECTION**</dt> <dt>( ( ULONG )-1 )</dt> </dl> | If the *ulIndex* parameter of [ITfContext::GetSelection](/windows/win32/Msctf/nf-msctf-itfcontext-getselection?branch=master) is set to this value, the default selection is obtained.<br/>                                                                                                                                                                                                                                                                      |
| <span id="TS_GEA_HIDDEN"></span><span id="ts_gea_hidden"></span><dl> <dt>**TS\_GEA\_HIDDEN**</dt> <dt>( 0x1 )</dt> </dl>                              | If *dwFlags* parameter of [ITextStoreAnchor::GetEmbedded](/windows/win32/Textstor/nf-textstor-itextstoreanchor-getembedded?branch=master) is set to this value, an embedded object can be located within hidden text.<br/>                                                                                                                                                                                                                                             |
| <span id="TS_GTA_HIDDEN"></span><span id="ts_gta_hidden"></span><dl> <dt>**TS\_GTA\_HIDDEN**</dt> <dt>( 0x1 )</dt> </dl>                              | Not used.<br/>                                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="TS_ST_CORRECTION"></span><span id="ts_st_correction"></span><dl> <dt>**TS\_ST\_CORRECTION**</dt> <dt>( 0x1 )</dt> </dl>                     | If *dwFlags* parameter of [ITextStoreACP::SetText](/windows/win32/Textstor/nf-textstor-itextstoreacp-settext?branch=master), [ITextStoreAnchor::SetText](/windows/win32/Textstor/nf-textstor-itextstoreanchor-settext?branch=master), or [ITextStoreACPSink::OnTextChange](/windows/win32/Textstor/nf-textstor-itextstoreacpsink-ontextchange?branch=master) is set to this value, the text is a transform (correction) of existing content, and any special text markup information (metadata) is retained, such as .wav file data or a language identifier.<br/> |
| <span id="TS_TC_CORRECTION"></span><span id="ts_tc_correction"></span><dl> <dt>**TS\_TC\_CORRECTION**</dt> <dt>( 0x1 )</dt> </dl>                     | If *dwFlags* parameter of [ITextStoreAnchorSink::OnTextChange](/windows/win32/Textstor/nf-textstor-itextstoreanchorsink-ontextchange?branch=master) is set to this value, the text is a transform (correction) of existing content, and any special text markup information (metadata) is retained, such as .wav file data or a language identifier.<br/>                                                                                                              |
| <span id="TS_VCOOKIE_NUL"></span><span id="ts_vcookie_nul"></span><dl> <dt>**TS\_VCOOKIE\_NUL**</dt> <dt>( 0xffffffff )</dt> </dl>                    | Used internally by TSF.<br/>                                                                                                                                                                                                                                                                                                                                                                                             |



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                         |
| Header<br/>                   | <dl> <dt>Textstor.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Textstor.idl</dt> </dl> |



## See also

<dl> <dt>

[ITfContext::GetSelection](/windows/win32/Msctf/nf-msctf-itfcontext-getselection?branch=master)
</dt> <dt>

[ITextStoreACP::SetText](/windows/win32/Textstor/nf-textstor-itextstoreacp-settext?branch=master)
</dt> <dt>

[ITextStoreAnchor::SetText](/windows/win32/Textstor/nf-textstor-itextstoreanchor-settext?branch=master)
</dt> <dt>

[ITextStoreAnchor::GetEmbedded](/windows/win32/Textstor/nf-textstor-itextstoreanchor-getembedded?branch=master)
</dt> <dt>

[ITextStoreACPSink::OnTextChange](/windows/win32/Textstor/nf-textstor-itextstoreacpsink-ontextchange?branch=master)
</dt> <dt>

[ITextStoreAnchorSink::OnTextChange](/windows/win32/Textstor/nf-textstor-itextstoreanchorsink-ontextchange?branch=master)
</dt> <dt>

[Miscellaneous Framework Constants](miscellaneous-framework-constants.md)
</dt> </dl>

 

 





