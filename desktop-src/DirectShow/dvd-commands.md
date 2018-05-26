---
Description: DVD Commands
ms.assetid: 1204c73e-c3de-4488-8ee3-e76edbf72da0
title: DVD Commands
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DVD Commands

The DVD navigation and playback commands are defined in a section of the DVD specification named Annex J, which is why the DirectShow documentation often refers to "Annex J commands." The names given in Annex J are not always very intuitive, however, so DirectShow uses names that may be easier to understand.

The following table lists the Annex J commands and their DirectShow equivalents.



| Annex J command                                                                           | Description                                                                  | IDvdControl2 method                                                                           |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Title\_Play                                                                               | Play a title.                                                                | [**PlayTitle**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-playtitle?branch=master)                                                   |
| PTT\_Play                                                                                 | Play a chapter in a title.                                                   | [**PlayChapterInTitle**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-playchapterintitle?branch=master)                                 |
| Time\_Play                                                                                | Play a title starting from a specified time.                                 | [**PlayAtTimeInTitle**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-playattimeintitle?branch=master)                                   |
| Stop                                                                                      | Stop playback.                                                               | [**Stop**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-stop?branch=master)                                                             |
| GoUp                                                                                      | Return from a submenu to the parent menu.                                    | [**ReturnFromSubmenu**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-returnfromsubmenu?branch=master)                                   |
| Time\_Search                                                                              | Play at a specified time within the current title.                           | [**PlayAtTime**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-playattime?branch=master)                                                 |
| PTT\_Search                                                                               | Play a chapter within the current title.                                     | [**PlayChapter**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-playchapter?branch=master)                                               |
| PrevPG\_Search                                                                            | Go to the start of the previous chapter and resume playback.                 | [**PlayPrevChapter**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-playprevchapter?branch=master)                                       |
| TopPG\_Search                                                                             | Go to the start of the current chapter and resume playback.                  | [**ReplayChapter**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-replaychapter?branch=master)                                           |
| NextPG\_Search                                                                            | Go to the start of the next chapter and resume playback.                     | [**PlayNextChapter**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-playnextchapter?branch=master)                                       |
| Forward\_Scan                                                                             | Play forward at a specified playback rate. The default playback rate is 1.0. | [**PlayForwards**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-playforwards?branch=master)                                             |
| Backward\_Scan                                                                            | Play backward at a specified playback rate.                                  | [**PlayBackwards**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-playbackwards?branch=master)                                           |
| Menu\_Call                                                                                | Show a menu.                                                                 | [**ShowMenu**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-showmenu?branch=master)                                                     |
| Resume                                                                                    | Return from a menu and resume playback.                                      | [**Resume**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-resume?branch=master)                                                         |
| Upper\_Button\_Select, Lower\_Button\_Select, Left\_Button\_Select, Right\_Button\_Select | Select a button whose position is relative to the currently selected button. | [**SelectButton**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-selectbutton?branch=master)                                             |
| Button\_Activate                                                                          | Activate the selected button.                                                | [**ActivateButton**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-activatebutton?branch=master)                                         |
| Button\_Select\_and\_Activate                                                             | Select and activate a button.                                                | [**SelectAndActivateButton**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-selectandactivatebutton?branch=master)                       |
| Still\_Off                                                                                | Resume playback when displaying a still image.                               | [**StillOff**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-stilloff?branch=master)                                                     |
| Pause\_On                                                                                 | Pause playback.                                                              | [**Pause**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-pause?branch=master)                                                           |
| Pause\_Off                                                                                | Resume playback from the paused state.                                       | [**Pause**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-pause?branch=master)                                                           |
| Menu\_Language\_Select                                                                    | Select the language for menus.                                               | [**SelectDefaultMenuLanguage**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-selectdefaultmenulanguage?branch=master)                   |
| Audio\_Stream\_Change                                                                     | Set the audio stream.                                                        | [**SelectAudioStream**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-selectaudiostream?branch=master)                                   |
| Sub-picture\_Stream\_Change                                                               | Set the subpicture stream; enable or disable subpicture display.             | [**SelectSubpictureStream**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-selectsubpicturestream?branch=master)                         |
| Angle\_Change                                                                             | Set the camera angle.                                                        | [**SelectAngle**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-selectangle?branch=master)                                               |
| Parental\_Level\_Select                                                                   | Set the parental level.                                                      | [**SelectParentalLevel**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-selectparentallevel?branch=master)                               |
| Parental\_Country\_Select                                                                 | Set the country/region for parental management.                              | [**SelectParentalCountry**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-selectparentalcountry?branch=master)                           |
| Karaoke\_Audio\_Presentation\_Mode\_Change                                                | Set the audio mixing mode for karaoke.                                       | [**SelectKaraokeAudioPresentationMode**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-selectkaraokeaudiopresentationmode?branch=master) |
| Video\_Presentation\_Mode\_Change                                                         | Set the aspect ratio mode to widescreen, letterbox, or pan scan.             | [**SelectVideoModePreference**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-selectvideomodepreference?branch=master)                   |



 

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



