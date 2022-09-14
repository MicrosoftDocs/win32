---
description: This topic contains the resource file for the tutorial How to Play Media Files with Media Foundation.
ms.assetid: 5454c92b-5f71-4be3-ac98-b2195c482ea4
title: player.rc
ms.topic: article
ms.date: 05/31/2018
---

# player.rc

This topic contains the resource file for the tutorial [How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md).


```C++
// Microsoft Visual C++ generated resource script.
//
#include "resource.h"

#include "windows.h"

/////////////////////////////////////////////////////////////////////////////
#undef APSTUDIO_READONLY_SYMBOLS

/////////////////////////////////////////////////////////////////////////////
// English (U.S.) resources

#if !defined(AFX_RESOURCE_DLL) || defined(AFX_TARG_ENU)
#ifdef _WIN32
LANGUAGE LANG_ENGLISH, SUBLANG_ENGLISH_US
#pragma code_page(1252)
#endif //_WIN32

/////////////////////////////////////////////////////////////////////////////
//
// Menu
//

IDC_MFPLAYBACK MENU 
BEGIN
    POPUP "&File"
    BEGIN
        MENUITEM "&Open File",                  ID_FILE_OPENFILE
        MENUITEM "Open &Url",                   ID_FILE_OPENURL
        MENUITEM SEPARATOR
        MENUITEM "E&xit",                       IDM_EXIT
    END
END


/////////////////////////////////////////////////////////////////////////////
//
// Dialog
//

IDD_OPENURL DIALOGEX 0, 0, 186, 90
STYLE DS_SETFONT | DS_MODALFRAME | DS_FIXEDSYS | WS_POPUP | WS_CAPTION | WS_SYSMENU
CAPTION "Open URL"
FONT 8, "MS Shell Dlg", 400, 0, 0x1
BEGIN
    DEFPUSHBUTTON   "OK",IDOK,75,69,50,14
    PUSHBUTTON      "Cancel",IDCANCEL,129,69,50,14
    EDITTEXT        IDC_EDIT_URL,7,21,172,14,ES_AUTOHSCROLL
    LTEXT           "Enter the URL to open:",IDC_STATIC,7,7,104,8
END

#endif    // English (U.S.) resources
/////////////////////////////////////////////////////////////////////////////

```



## Related topics

<dl> <dt>

[Media Session Playback Example](media-session-playback-example.md)
</dt> <dt>

[Audio/Video Playback](audio-video-playback.md)
</dt> </dl>

 

 



