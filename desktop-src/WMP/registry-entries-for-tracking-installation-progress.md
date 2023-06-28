---
title: Registry Entries for Tracking Installation Progress
description: Registry Entries for Tracking Installation Progress
ms.assetid: 898f9117-94fd-4230-9378-b8c6a4401a96
keywords:
- Windows Media Player,tracking installation progress
- Windows Media Player,installation progress tracking
- Windows Media Player,progress tracking of installations
- Windows Media Player,registry
- registry,tracking installation progress
- registry,installation progress tracking
- registry,progress tracking of installations
- registry,settings for Windows Media Player
- tracking installation progress
- installing progress tracking
- progress tracking of installations
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Registry Entries for Tracking Installation Progress

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Player 11 setup program, setup\_wm.exe, writes the following entries in the registry so that installation programs can track the progress of the Windows Media Player setup program as it runs.


```C++
[HKEY_LOCAL_MACHINE\Software\Microsoft\MediaPlayer\Setup]
"Progress_CurrentDialog" = dword:value
"Progress_MaxDialog" = dword:value
"Progress_CurrentInstall" = dword:value
"Progress_MaxInstall" = dword:value
```



In the preceding registry syntax, *value* is a placeholder for an integer value.

Progress\_CurrentDialog indicates which dialog box Windows Media Player setup is currently displaying. Progress\_MaxDialog indicates the total number of dialog boxes that Windows Media will display. For example, if Progress\_CurrentDialog = 2 and Progress\_MaxDialog = 5, Windows Media Player is currently displaying the second dialog box in a sequence of five.

Progress\_CurrentInstall and Progress\_MaxInstall, taken together, indicate the percent of completion of the current dialog. For example, if Progress\_CurrentInstall = 6 and Progress\_MaxInstall = 25, the current dialog is 6/25 (that is, 24%) complete.

## Related topics

<dl> <dt>

[**Registry Settings**](registry-settings.md)
</dt> </dl>

 

 




