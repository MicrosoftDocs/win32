---
title: TF_SFT_ Constants (Ctfutb.h)
description: The TF\_SFT\_\ constants specify display settings of a floating language bar.
ms.assetid: 628e1d85-9614-4327-b89b-723f6eeb0718
topic_type:
- apiref
api_name:
- TF_SFT_SHOWNORMAL
- TF_SFT_DOCK
- TF_SFT_MINIMIZED
- TF_SFT_HIDDEN
- TF_SFT_NOTRANSPARENCY
- TF_SFT_LOWTRANSPARENCY
- TF_SFT_HIGHTRANSPARENCY
- TF_SFT_LABELS
- TF_SFT_NOLABELS
- TF_SFT_EXTRAICONSONMINIMIZED
- TF_SFT_NOEXTRAICONSONMINIMIZED
- TF_SFT_DESKBAND
api_location:
- Ctfutb.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TF\_SFT\_\* Constants

The **TF\_SFT\_\*** constants specify display settings of a floating language bar.



| Constant/value                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                             |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TF_SFT_SHOWNORMAL"></span><span id="tf_sft_shownormal"></span><dl> <dt>**TF\_SFT\_SHOWNORMAL**</dt> <dt>0x00000001</dt> </dl>                                        | Display the language bar as a floating window. This constant cannot be combined with the TF\_SFT\_DOCK, TF\_SFT\_MINIMIZED, TF\_SFT\_HIDDEN, or TF\_SFT\_DESKBAND constants.<br/>                                                                                                 |
| <span id="TF_SFT_DOCK"></span><span id="tf_sft_dock"></span><dl> <dt>**TF\_SFT\_DOCK**</dt> <dt>0x00000002</dt> </dl>                                                          | Dock the language bar in its own task pane. This constant cannot be combined with the TF\_SFT\_SHOWNORMAL, TF\_SFT\_MINIMIZED, TF\_SFT\_HIDDEN, or TF\_SFT\_DESKBAND constants. Available only on Windows XP.<br/>                                                                |
| <span id="TF_SFT_MINIMIZED"></span><span id="tf_sft_minimized"></span><dl> <dt>**TF\_SFT\_MINIMIZED**</dt> <dt>0x00000004</dt> </dl>                                           | Display the language bar as a single icon in the system tray. This constant cannot be combined with the TF\_SFT\_SHOWNORMAL, TF\_SFT\_DOCK, TF\_SFT\_HIDDEN, or TF\_SFT\_DESKBAND constants. In Windows XP, use TF\_SFT\_DESKBAND instead.<br/>                                   |
| <span id="TF_SFT_HIDDEN"></span><span id="tf_sft_hidden"></span><dl> <dt>**TF\_SFT\_HIDDEN**</dt> <dt>0x00000008</dt> </dl>                                                    | Hide the language bar. This constant cannot be combined with the TF\_SFT\_SHOWNORMAL, TF\_SFT\_DOCK, TF\_SFT\_MINIMIZED, or TF\_SFT\_DESKBAND constants.<br/>                                                                                                                     |
| <span id="TF_SFT_NOTRANSPARENCY"></span><span id="tf_sft_notransparency"></span><dl> <dt>**TF\_SFT\_NOTRANSPARENCY**</dt> <dt>0x00000010</dt> </dl>                            | Make the language bar opaque.<br/>                                                                                                                                                                                                                                                |
| <span id="TF_SFT_LOWTRANSPARENCY"></span><span id="tf_sft_lowtransparency"></span><dl> <dt>**TF\_SFT\_LOWTRANSPARENCY**</dt> <dt>0x00000020</dt> </dl>                         | Make the language bar partially transparent. Available only on Windows 2000 or later.<br/>                                                                                                                                                                                        |
| <span id="TF_SFT_HIGHTRANSPARENCY"></span><span id="tf_sft_hightransparency"></span><dl> <dt>**TF\_SFT\_HIGHTRANSPARENCY**</dt> <dt>0x00000040</dt> </dl>                      | Make the language bar highly transparent. Available only on Windows 2000 or later.<br/>                                                                                                                                                                                           |
| <span id="TF_SFT_LABELS"></span><span id="tf_sft_labels"></span><dl> <dt>**TF\_SFT\_LABELS**</dt> <dt>0x00000080</dt> </dl>                                                    | Display text labels next to language bar icons.<br/>                                                                                                                                                                                                                              |
| <span id="TF_SFT_NOLABELS"></span><span id="tf_sft_nolabels"></span><dl> <dt>**TF\_SFT\_NOLABELS**</dt> <dt>0x00000100</dt> </dl>                                              | Hide language bar icon text labels.<br/>                                                                                                                                                                                                                                          |
| <span id="TF_SFT_EXTRAICONSONMINIMIZED"></span><span id="tf_sft_extraiconsonminimized"></span><dl> <dt>**TF\_SFT\_EXTRAICONSONMINIMIZED**</dt> <dt>0x00000200</dt> </dl>       | Display text service icons on the taskbar when the language bar is minimized.<br/>                                                                                                                                                                                                |
| <span id="TF_SFT_NOEXTRAICONSONMINIMIZED"></span><span id="tf_sft_noextraiconsonminimized"></span><dl> <dt>**TF\_SFT\_NOEXTRAICONSONMINIMIZED**</dt> <dt>0x00000400</dt> </dl> | Hide text service icons on the taskbar when the language bar is minimized.<br/>                                                                                                                                                                                                   |
| <span id="TF_SFT_DESKBAND"></span><span id="tf_sft_deskband"></span><dl> <dt>**TF\_SFT\_DESKBAND**</dt> <dt>0x00000800</dt> </dl>                                              | Dock the language bar in the righthand end of the system task bar (immediately left of the system tray/clock). This constant cannot be combined with the TF\_SFT\_SHOWNORMAL, TF\_SFT\_DOCK, TF\_SFT\_MINIMIZED, or TF\_SFT\_HIDDEN constants. Available only on Windows XP.<br/> |



## Remarks

The [ITfLangBarMgr::ShowFloating](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbarmgr-showfloating) method sets the result of a logical **OR** operation on one or more of these constants to specify the attributes of the language bar item.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                       |
| Header<br/>                   | <dl> <dt>Ctfutb.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Ctfutb.idl</dt> </dl> |



## See also

<dl> <dt>

[ITfLangBarMgr::ShowFloating](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbarmgr-showfloating)
</dt> </dl>

 

 





