---
description: DVD Commands
ms.assetid: 1204c73e-c3de-4488-8ee3-e76edbf72da0
title: DVD Commands
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD Commands

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The DVD navigation and playback commands are defined in a section of the DVD specification named Annex J, which is why the DirectShow documentation often refers to "Annex J commands." The names given in Annex J are not always very intuitive, however, so DirectShow uses names that may be easier to understand.

The following table lists the Annex J commands and their DirectShow equivalents.



| Annex J command                                                                           | Description                                                                  | IDvdControl2 method                                                                           |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Title\_Play                                                                               | Play a title.                                                                | [**PlayTitle**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-playtitle)                                                   |
| PTT\_Play                                                                                 | Play a chapter in a title.                                                   | [**PlayChapterInTitle**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-playchapterintitle)                                 |
| Time\_Play                                                                                | Play a title starting from a specified time.                                 | [**PlayAtTimeInTitle**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-playattimeintitle)                                   |
| Stop                                                                                      | Stop playback.                                                               | [**Stop**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-stop)                                                             |
| GoUp                                                                                      | Return from a submenu to the parent menu.                                    | [**ReturnFromSubmenu**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-returnfromsubmenu)                                   |
| Time\_Search                                                                              | Play at a specified time within the current title.                           | [**PlayAtTime**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-playattime)                                                 |
| PTT\_Search                                                                               | Play a chapter within the current title.                                     | [**PlayChapter**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-playchapter)                                               |
| PrevPG\_Search                                                                            | Go to the start of the previous chapter and resume playback.                 | [**PlayPrevChapter**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-playprevchapter)                                       |
| TopPG\_Search                                                                             | Go to the start of the current chapter and resume playback.                  | [**ReplayChapter**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-replaychapter)                                           |
| NextPG\_Search                                                                            | Go to the start of the next chapter and resume playback.                     | [**PlayNextChapter**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-playnextchapter)                                       |
| Forward\_Scan                                                                             | Play forward at a specified playback rate. The default playback rate is 1.0. | [**PlayForwards**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-playforwards)                                             |
| Backward\_Scan                                                                            | Play backward at a specified playback rate.                                  | [**PlayBackwards**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-playbackwards)                                           |
| Menu\_Call                                                                                | Show a menu.                                                                 | [**ShowMenu**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-showmenu)                                                     |
| Resume                                                                                    | Return from a menu and resume playback.                                      | [**Resume**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-resume)                                                         |
| Upper\_Button\_Select, Lower\_Button\_Select, Left\_Button\_Select, Right\_Button\_Select | Select a button whose position is relative to the currently selected button. | [**SelectButton**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectbutton)                                             |
| Button\_Activate                                                                          | Activate the selected button.                                                | [**ActivateButton**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-activatebutton)                                         |
| Button\_Select\_and\_Activate                                                             | Select and activate a button.                                                | [**SelectAndActivateButton**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectandactivatebutton)                       |
| Still\_Off                                                                                | Resume playback when displaying a still image.                               | [**StillOff**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-stilloff)                                                     |
| Pause\_On                                                                                 | Pause playback.                                                              | [**Pause**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-pause)                                                           |
| Pause\_Off                                                                                | Resume playback from the paused state.                                       | [**Pause**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-pause)                                                           |
| Menu\_Language\_Select                                                                    | Select the language for menus.                                               | [**SelectDefaultMenuLanguage**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectdefaultmenulanguage)                   |
| Audio\_Stream\_Change                                                                     | Set the audio stream.                                                        | [**SelectAudioStream**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectaudiostream)                                   |
| Sub-picture\_Stream\_Change                                                               | Set the subpicture stream; enable or disable subpicture display.             | [**SelectSubpictureStream**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectsubpicturestream)                         |
| Angle\_Change                                                                             | Set the camera angle.                                                        | [**SelectAngle**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectangle)                                               |
| Parental\_Level\_Select                                                                   | Set the parental level.                                                      | [**SelectParentalLevel**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectparentallevel)                               |
| Parental\_Country\_Select                                                                 | Set the country/region for parental management.                              | [**SelectParentalCountry**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectparentalcountry)                           |
| Karaoke\_Audio\_Presentation\_Mode\_Change                                                | Set the audio mixing mode for karaoke.                                       | [**SelectKaraokeAudioPresentationMode**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectkaraokeaudiopresentationmode) |
| Video\_Presentation\_Mode\_Change                                                         | Set the aspect ratio mode to widescreen, letterbox, or pan scan.             | [**SelectVideoModePreference**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectvideomodepreference)                   |



 

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



