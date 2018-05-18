---
Description: DVD Commands
ms.assetid: '1204c73e-c3de-4488-8ee3-e76edbf72da0'
title: DVD Commands
---

# DVD Commands

The DVD navigation and playback commands are defined in a section of the DVD specification named Annex J, which is why the DirectShow documentation often refers to "Annex J commands." The names given in Annex J are not always very intuitive, however, so DirectShow uses names that may be easier to understand.

The following table lists the Annex J commands and their DirectShow equivalents.



| Annex J command                                                                           | Description                                                                  | IDvdControl2 method                                                                           |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Title\_Play                                                                               | Play a title.                                                                | [**PlayTitle**](idvdcontrol2-playtitle.md)                                                   |
| PTT\_Play                                                                                 | Play a chapter in a title.                                                   | [**PlayChapterInTitle**](idvdcontrol2-playchapterintitle.md)                                 |
| Time\_Play                                                                                | Play a title starting from a specified time.                                 | [**PlayAtTimeInTitle**](idvdcontrol2-playattimeintitle.md)                                   |
| Stop                                                                                      | Stop playback.                                                               | [**Stop**](idvdcontrol2-stop.md)                                                             |
| GoUp                                                                                      | Return from a submenu to the parent menu.                                    | [**ReturnFromSubmenu**](idvdcontrol2-returnfromsubmenu.md)                                   |
| Time\_Search                                                                              | Play at a specified time within the current title.                           | [**PlayAtTime**](idvdcontrol2-playattime.md)                                                 |
| PTT\_Search                                                                               | Play a chapter within the current title.                                     | [**PlayChapter**](idvdcontrol2-playchapter.md)                                               |
| PrevPG\_Search                                                                            | Go to the start of the previous chapter and resume playback.                 | [**PlayPrevChapter**](idvdcontrol2-playprevchapter.md)                                       |
| TopPG\_Search                                                                             | Go to the start of the current chapter and resume playback.                  | [**ReplayChapter**](idvdcontrol2-replaychapter.md)                                           |
| NextPG\_Search                                                                            | Go to the start of the next chapter and resume playback.                     | [**PlayNextChapter**](idvdcontrol2-playnextchapter.md)                                       |
| Forward\_Scan                                                                             | Play forward at a specified playback rate. The default playback rate is 1.0. | [**PlayForwards**](idvdcontrol2-playforwards.md)                                             |
| Backward\_Scan                                                                            | Play backward at a specified playback rate.                                  | [**PlayBackwards**](idvdcontrol2-playbackwards.md)                                           |
| Menu\_Call                                                                                | Show a menu.                                                                 | [**ShowMenu**](idvdcontrol2-showmenu.md)                                                     |
| Resume                                                                                    | Return from a menu and resume playback.                                      | [**Resume**](idvdcontrol2-resume.md)                                                         |
| Upper\_Button\_Select, Lower\_Button\_Select, Left\_Button\_Select, Right\_Button\_Select | Select a button whose position is relative to the currently selected button. | [**SelectButton**](idvdcontrol2-selectbutton.md)                                             |
| Button\_Activate                                                                          | Activate the selected button.                                                | [**ActivateButton**](idvdcontrol2-activatebutton.md)                                         |
| Button\_Select\_and\_Activate                                                             | Select and activate a button.                                                | [**SelectAndActivateButton**](idvdcontrol2-selectandactivatebutton.md)                       |
| Still\_Off                                                                                | Resume playback when displaying a still image.                               | [**StillOff**](idvdcontrol2-stilloff.md)                                                     |
| Pause\_On                                                                                 | Pause playback.                                                              | [**Pause**](idvdcontrol2-pause.md)                                                           |
| Pause\_Off                                                                                | Resume playback from the paused state.                                       | [**Pause**](idvdcontrol2-pause.md)                                                           |
| Menu\_Language\_Select                                                                    | Select the language for menus.                                               | [**SelectDefaultMenuLanguage**](idvdcontrol2-selectdefaultmenulanguage.md)                   |
| Audio\_Stream\_Change                                                                     | Set the audio stream.                                                        | [**SelectAudioStream**](idvdcontrol2-selectaudiostream.md)                                   |
| Sub-picture\_Stream\_Change                                                               | Set the subpicture stream; enable or disable subpicture display.             | [**SelectSubpictureStream**](idvdcontrol2-selectsubpicturestream.md)                         |
| Angle\_Change                                                                             | Set the camera angle.                                                        | [**SelectAngle**](idvdcontrol2-selectangle.md)                                               |
| Parental\_Level\_Select                                                                   | Set the parental level.                                                      | [**SelectParentalLevel**](idvdcontrol2-selectparentallevel.md)                               |
| Parental\_Country\_Select                                                                 | Set the country/region for parental management.                              | [**SelectParentalCountry**](idvdcontrol2-selectparentalcountry.md)                           |
| Karaoke\_Audio\_Presentation\_Mode\_Change                                                | Set the audio mixing mode for karaoke.                                       | [**SelectKaraokeAudioPresentationMode**](idvdcontrol2-selectkaraokeaudiopresentationmode.md) |
| Video\_Presentation\_Mode\_Change                                                         | Set the aspect ratio mode to widescreen, letterbox, or pan scan.             | [**SelectVideoModePreference**](idvdcontrol2-selectvideomodepreference.md)                   |



 

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



