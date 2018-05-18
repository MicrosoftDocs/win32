---
Description: 'Note  This interface has been deprecated.'
ms.assetid: 'a6ca0fe8-84e3-43e6-9421-29dcff056dfd'
title: IDvdControl interface
---

# IDvdControl interface

> [!Note]  
> This interface has been deprecated. It will continue to be supported for backward compatibility with existing applications, but new applications should use [**IDvdControl2**](idvdcontrol2.md).

 

The `IDvdControl` interface controls the playback and search mechanisms of a DVD title that contains one or more video movies. Use this interface to control playback (set root drive, play, stop, and so forth) or use DVD-specific functionality such as menus and buttons when playing DVD-Video files.

## Members

The **IDvdControl** interface inherits from the [**IUnknown**](com.iunknown) interface. **IDvdControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDvdControl** interface has these methods.



| Method                                                                                       | Description                                                                                                                    |
|:---------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**AngleChange**](idvdcontrol-anglechange.md)                                               | Sets the new display angle.<br/>                                                                                         |
| [**AudioStreamChange**](idvdcontrol-audiostreamchange.md)                                   | Sets the current audio stream.<br/>                                                                                      |
| [**BackwardScan**](idvdcontrol-backwardscan.md)                                             | Searches backward through the current disc at the specified speed.<br/>                                                  |
| [**ButtonActivate**](idvdcontrol-buttonactivate.md)                                         | Activates the selected button.<br/>                                                                                      |
| [**ButtonSelectAndActivate**](idvdcontrol-buttonselectandactivate.md)                       | Selects and activates the specified button.<br/>                                                                         |
| [**ChapterPlay**](idvdcontrol-chapterplay.md)                                               | Plays the media file with the specified title index and chapter value.<br/>                                              |
| [**ChapterPlayAutoStop**](idvdcontrol-chapterplayautostop.md)                               | Start playing at the specified chapter within the specified title and play the number of chapters specified.<br/>        |
| [**ChapterSearch**](idvdcontrol-chaptersearch.md)                                           | Halts playback of the current chapter and starts playback from the specified chapter value in the same media file.<br/>  |
| [**ForwardScan**](idvdcontrol-forwardscan.md)                                               | Searches forward through the current disc at the specified speed.<br/>                                                   |
| [**GoUp**](idvdcontrol-goup.md)                                                             | Halts playback of the current media file and starts playback of the designated previous program chain (PGC).<br/>        |
| [**KaraokeAudioPresentationModeChange**](idvdcontrol-karaokeaudiopresentationmodechange.md) | Sets the audio playback mode to karaoke.<br/>                                                                            |
| [**LeftButtonSelect**](idvdcontrol-leftbuttonselect.md)                                     | Selects the left directional button from the displayed menu.<br/>                                                        |
| [**LowerButtonSelect**](idvdcontrol-lowerbuttonselect.md)                                   | Selects the lower directional button from the displayed menu.<br/>                                                       |
| [**MenuCall**](idvdcontrol-menucall.md)                                                     | Displays the specified menu on the screen.<br/>                                                                          |
| [**MenuLanguageSelect**](idvdcontrol-menulanguageselect.md)                                 | Sets the displayed language for navigation menus.<br/>                                                                   |
| [**MouseActivate**](idvdcontrol-mouseactivate.md)                                           | Selects and activates a DVD button in response to a mouse click.<br/>                                                    |
| [**MouseSelect**](idvdcontrol-mouseselect.md)                                               | Selects a DVD button in response to mouse movement.<br/>                                                                 |
| [**NextPGSearch**](idvdcontrol-nextpgsearch.md)                                             | Halts playback of the current program and starts playback from the next program within the program chain (PGC).<br/>     |
| [**ParentalCountrySelect**](idvdcontrol-parentalcountryselect.md)                           | Sets the current country/region for controlling parental access levels.<br/>                                             |
| [**ParentalLevelSelect**](idvdcontrol-parentallevelselect.md)                               | Sets the parental access level for the current media file.<br/>                                                          |
| [**PauseOff**](idvdcontrol-pauseoff.md)                                                     | Unpauses the current media file playback.<br/>                                                                           |
| [**PauseOn**](idvdcontrol-pauseon.md)                                                       | Pauses the current media file playback.<br/>                                                                             |
| [**PrevPGSearch**](idvdcontrol-prevpgsearch.md)                                             | Halts playback of the current program and starts playback from the previous program within the program chain (PGC).<br/> |
| [**Resume**](idvdcontrol-resume.md)                                                         | Returns to playing back a title from a menu.<br/>                                                                        |
| [**RightButtonSelect**](idvdcontrol-rightbuttonselect.md)                                   | Selects the right directional button from the displayed menu.<br/>                                                       |
| [**SetRoot**](idvdcontrol-setroot.md)                                                       | Sets the root directory containing the DVD-Video volume.<br/>                                                            |
| [**StillOff**](idvdcontrol-stilloff.md)                                                     | Resumes playback, canceling still mode.<br/>                                                                             |
| [**StopForResume**](idvdcontrol-stopforresume.md)                                           | Transitions playback to the DVD\_DOMAIN\_Stop state after saving resume information.<br/>                                |
| [**SubpictureStreamChange**](idvdcontrol-subpicturestreamchange.md)                         | Selects the new subpicture stream and enables or disables it for display.<br/>                                           |
| [**TimePlay**](idvdcontrol-timeplay.md)                                                     | Plays the media file with the specified title index, starting at the specified time.<br/>                                |
| [**TimeSearch**](idvdcontrol-timesearch.md)                                                 | Halts playback of the current chapter and starts playback from the specified time in the same media file.<br/>           |
| [**TitlePlay**](idvdcontrol-titleplay.md)                                                   | Finds the media file with the specified title index and plays it back.<br/>                                              |
| [**TopPGSearch**](idvdcontrol-toppgsearch.md)                                               | Halts playback of the current program and restarts playback of the current program within the program chain (PGC).<br/>  |
| [**UpperButtonSelect**](idvdcontrol-upperbuttonselect.md)                                   | Selects the upper directional button from the displayed menu.<br/>                                                       |
| [**VideoModePreferrence**](idvdcontrol-videomodepreferrence.md)                             | Sets the video display mode the user prefers.<br/>                                                                       |



 

## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




