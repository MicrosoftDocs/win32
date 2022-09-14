---
description: Used by the SHGetSetSettings function to specify which members of its SHELLSTATE structure should be set or retrived.
title: SSF Constants (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 2a883110-fdc3-4451-9e47-e58894600e3b
api_name: 
 - SSF_SHOWALLOBJECTS
 - SSF_SHOWEXTENSIONS
 - SSF_HIDDENFILEEXTS
 - SSF_SERVERADMINUI
 - SSF_SHOWCOMPCOLOR
 - SSF_SORTCOLUMNS
 - SSF_SHOWSYSFILES
 - SSF_DOUBLECLICKINWEBVIEW
 - SSF_SHOWATTRIBCOL
 - SSF_DESKTOPHTML
 - SSF_WIN95CLASSIC
 - SSF_DONTPRETTYPATH
 - SSF_MAPNETDRVBUTTON
 - SSF_SHOWINFOTIP
 - SSF_HIDEICONS
 - SSF_NOCONFIRMRECYCLE
 - SSF_FILTER
 - SSF_WEBVIEW
 - SSF_SHOWSUPERHIDDEN
 - SSF_SEPPROCESS
 - SSF_NONETCRAWLING
 - SSF_STARTPANELON
 - SSF_SHOWSTARTPAGE
 - SSF_AUTOCHECKSELECT
 - SSF_ICONSONLY
 - SSF_SHOWTYPEOVERLAY
 - SSF_SHOWSTATUSBAR
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SSF Constants

Used by the [**SHGetSetSettings**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetsetsettings) function to specify which members of its [**SHELLSTATE**](/windows/win32/api/shlobj_core/ns-shlobj_core-shellstatea) structure should be set or retrived.

<dl> <dt>

<span id="SSF_SHOWALLOBJECTS"></span><span id="ssf_showallobjects"></span>**SSF\_SHOWALLOBJECTS**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



The **fShowAllObjects** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_SHOWEXTENSIONS"></span><span id="ssf_showextensions"></span>**SSF\_SHOWEXTENSIONS**
</dt> <dd> <dl> <dt>

0x00000002
</dt> <dt>



The **fShowExtensions** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_HIDDENFILEEXTS"></span><span id="ssf_hiddenfileexts"></span>**SSF\_HIDDENFILEEXTS**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



Not used.


</dt> </dl> </dd> <dt>

<span id="SSF_SERVERADMINUI"></span><span id="ssf_serveradminui"></span>**SSF\_SERVERADMINUI**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



Not used.


</dt> </dl> </dd> <dt>

<span id="SSF_SHOWCOMPCOLOR"></span><span id="ssf_showcompcolor"></span>**SSF\_SHOWCOMPCOLOR**
</dt> <dd> <dl> <dt>

0x00000008
</dt> <dt>



The **fShowCompColor** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_SORTCOLUMNS"></span><span id="ssf_sortcolumns"></span>**SSF\_SORTCOLUMNS**
</dt> <dd> <dl> <dt>

0x00000010
</dt> <dt>



The **lParamSort** and **iSortDirection** members are being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_SHOWSYSFILES"></span><span id="ssf_showsysfiles"></span>**SSF\_SHOWSYSFILES**
</dt> <dd> <dl> <dt>

0x00000020
</dt> <dt>



The **fShowSysFiles** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_DOUBLECLICKINWEBVIEW"></span><span id="ssf_doubleclickinwebview"></span>**SSF\_DOUBLECLICKINWEBVIEW**
</dt> <dd> <dl> <dt>

0x00000080
</dt> <dt>



The **fDoubleClickInWebView** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_SHOWATTRIBCOL"></span><span id="ssf_showattribcol"></span>**SSF\_SHOWATTRIBCOL**
</dt> <dd> <dl> <dt>

0x00000100
</dt> <dt>



The **fShowAttribCol** member is being requested.

**Windows Vista:** Not used.


</dt> </dl> </dd> <dt>

<span id="SSF_DESKTOPHTML"></span><span id="ssf_desktophtml"></span>**SSF\_DESKTOPHTML**
</dt> <dd> <dl> <dt>

0x00000200
</dt> <dt>



The **fDesktopHTML** member is being requested. Set is not available. Instead, for versions of Windows prior to Windows XP, enable desktop HTML by [**IActiveDesktop**](/windows/win32/api/shlobj_core/nn-shlobj_core-iactivedesktop). The use of **IActiveDesktop** for this purpose, however, is not recommended for Windows XP and later versions of Windows, and is deprecated in Windows Vista.


</dt> </dl> </dd> <dt>

<span id="SSF_WIN95CLASSIC"></span><span id="ssf_win95classic"></span>**SSF\_WIN95CLASSIC**
</dt> <dd> <dl> <dt>

0x00000400
</dt> <dt>



The **fWin95Classic** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_DONTPRETTYPATH"></span><span id="ssf_dontprettypath"></span>**SSF\_DONTPRETTYPATH**
</dt> <dd> <dl> <dt>

0x00000800
</dt> <dt>



The **fDontPrettyPath** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_MAPNETDRVBUTTON"></span><span id="ssf_mapnetdrvbutton"></span>**SSF\_MAPNETDRVBUTTON**
</dt> <dd> <dl> <dt>

0x00001000
</dt> <dt>



The **fMapNetDrvBtn** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_SHOWINFOTIP"></span><span id="ssf_showinfotip"></span>**SSF\_SHOWINFOTIP**
</dt> <dd> <dl> <dt>

0x00002000
</dt> <dt>



The **fShowInfoTip** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_HIDEICONS"></span><span id="ssf_hideicons"></span>**SSF\_HIDEICONS**
</dt> <dd> <dl> <dt>

0x00004000
</dt> <dt>



The **fHideIcons** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_NOCONFIRMRECYCLE"></span><span id="ssf_noconfirmrecycle"></span>**SSF\_NOCONFIRMRECYCLE**
</dt> <dd> <dl> <dt>

0x00008000
</dt> <dt>



The **fNoConfirmRecycle** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_FILTER"></span><span id="ssf_filter"></span>**SSF\_FILTER**
</dt> <dd> <dl> <dt>

0x00010000
</dt> <dt>



The **fFilter** member is being requested.

**Windows Vista:** Not used.


</dt> </dl> </dd> <dt>

<span id="SSF_WEBVIEW"></span><span id="ssf_webview"></span>**SSF\_WEBVIEW**
</dt> <dd> <dl> <dt>

0x00020000
</dt> <dt>



The **fWebView** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_SHOWSUPERHIDDEN"></span><span id="ssf_showsuperhidden"></span>**SSF\_SHOWSUPERHIDDEN**
</dt> <dd> <dl> <dt>

0x00040000
</dt> <dt>



The **fShowSuperHidden** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_SEPPROCESS"></span><span id="ssf_sepprocess"></span>**SSF\_SEPPROCESS**
</dt> <dd> <dl> <dt>

0x00080000
</dt> <dt>



The **fSepProcess** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_NONETCRAWLING"></span><span id="ssf_nonetcrawling"></span>**SSF\_NONETCRAWLING**
</dt> <dd> <dl> <dt>

0x00100000
</dt> <dt>



**Windows XP and later**. The **fNoNetCrawling** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_STARTPANELON"></span><span id="ssf_startpanelon"></span>**SSF\_STARTPANELON**
</dt> <dd> <dl> <dt>

0x00200000
</dt> <dt>



**Windows XP and later**. The **fStartPanelOn** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_SHOWSTARTPAGE"></span><span id="ssf_showstartpage"></span>**SSF\_SHOWSTARTPAGE**
</dt> <dd> <dl> <dt>

0x00400000
</dt> <dt>



Not used.


</dt> </dl> </dd> <dt>

<span id="SSF_AUTOCHECKSELECT"></span><span id="ssf_autocheckselect"></span>**SSF\_AUTOCHECKSELECT**
</dt> <dd> <dl> <dt>

0x00800000
</dt> <dt>



**Windows Vista and later**. The **fAutoCheckSelect** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_ICONSONLY"></span><span id="ssf_iconsonly"></span>**SSF\_ICONSONLY**
</dt> <dd> <dl> <dt>

0x01000000
</dt> <dt>



**Windows Vista and later**. The **fIconsOnly** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_SHOWTYPEOVERLAY"></span><span id="ssf_showtypeoverlay"></span>**SSF\_SHOWTYPEOVERLAY**
</dt> <dd> <dl> <dt>

0x02000000
</dt> <dt>



**Windows Vista and later**. The **fShowTypeOverlay** member is being requested.


</dt> </dl> </dd> <dt>

<span id="SSF_SHOWSTATUSBAR"></span><span id="ssf_showstatusbar"></span>**SSF\_SHOWSTATUSBAR**
</dt> <dd> <dl> <dt>

0x04000000
</dt> <dt>



**Windows 8 and later**: The **fShowStatusBar** member is being requested.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
