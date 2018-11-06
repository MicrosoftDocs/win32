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
ms.date: 05/31/2018
---

# Registry Entries for Tracking Installation Progress

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

 

 




