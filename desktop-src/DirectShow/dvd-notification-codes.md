---
description: DVD Event Notification Codes
ms.assetid: c028918e-aba2-49b2-a6ce-c620ab38b558
title: DVD Event Notification Codes
ms.topic: article
ms.date: 05/31/2018
---

# DVD Event Notification Codes

This section lists the event notification codes for DVD playback and navigation in DirectShow.

For information about receiving events in DirectShow, see [Event Notification in DirectShow](event-notification-in-directshow.md).

For other non-DVD event codes, see [Event Notification Codes](event-notification-codes.md).



| Event notification code                                                        | Description                                                                                                                                                               |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EC\_DVD\_ANGLE\_CHANGE**](ec-dvd-angle-change.md)                          | Signals that either the number of available angles changed or that the current angle number changed.                                                                      |
| [**EC\_DVD\_ANGLES\_AVAILABLE**](ec-dvd-angles-available.md)                  | Indicates whether an angle block is being played and angle changes can be performed.                                                                                      |
| [**EC\_DVD\_AUDIO\_STREAM\_CHANGE**](ec-dvd-audio-stream-change.md)           | Signals that the current audio stream number changed for the main title.                                                                                                  |
| [**EC\_DVD\_BeginNavigationCommands**](ec-dvd-beginnavigationcommands.md)     | Sent when a set of DVD navigation commands are starting.                                                                                                                  |
| [**EC\_DVD\_BUTTON\_AUTO\_ACTIVATED**](ec-dvd-button-auto-activated.md)       | Signals that a menu button has been automatically activated per instructions on the disc.                                                                                 |
| [**EC\_DVD\_BUTTON\_CHANGE**](ec-dvd-button-change.md)                        | Signals that either the number of available buttons changed or that the currently selected button number changed.                                                         |
| [**EC\_DVD\_CHAPTER\_AUTOSTOP**](ec-dvd-chapter-autostop.md)                  | Indicates that playback stopped as the result of a call to the [**IDvdControl2::PlayChaptersAutoStop**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-playchaptersautostop) method.                    |
| [**EC\_DVD\_CHAPTER\_START**](ec-dvd-chapter-start.md)                        | Signals that the DVD Navigator started playback of a new chapter in the current title.                                                                                    |
| [**EC\_DVD\_CMD\_START**](ec-dvd-cmd-start.md)                                | Signals that a particular command has begun.                                                                                                                              |
| [**EC\_DVD\_CMD\_END**](ec-dvd-cmd-end.md)                                    | Signals that a particular command has completed.                                                                                                                          |
| [**EC\_DVD\_CURRENT\_HMSF\_TIME**](ec-dvd-current-hmsf-time.md)               | Signals the current time in [**DVD\_HMSF\_TIMECODE**](/windows/win32/api/strmif/ns-strmif-dvd_hmsf_timecode) format at the beginning of every video object unit (VOBU).                                   |
| [**EC\_DVD\_CURRENT\_TIME**](ec-dvd-current-time.md)                          | Signals the beginning of every VOBU.                                                                                                                                      |
| [**EC\_DVD\_DISC\_EJECTED**](ec-dvd-disc-ejected.md)                          | Signals that a disc has been ejected from the drive.                                                                                                                      |
| [**EC\_DVD\_DISC\_INSERTED**](ec-dvd-disc-inserted.md)                        | Signals that a disc has been inserted into the drive.                                                                                                                     |
| [**EC\_DVD\_DOMAIN\_CHANGE**](ec-dvd-domain-change.md)                        | Indicates the DVD Navigator's new domain.                                                                                                                                 |
| [**EC\_DVD\_ERROR**](ec-dvd-error.md)                                         | Signals a DVD error condition.                                                                                                                                            |
| [**EC\_DVD\_GPRM\_Change**](ec-dvd-gprm-change.md)                            | Sent when the value of a general parameter register (GPRM) changes.                                                                                                       |
| [**EC\_DVD\_KARAOKE\_MODE**](ec-dvd-karaoke-mode.md)                          | Indicates that the Navigator has either begun playing or finished playing karaoke data.                                                                                   |
| [**EC\_DVD\_NavigationCommand**](ec-dvd-navigationcommand.md)                 | Sent when the [DVD Navigator](dvd-navigator-filter.md) processes a DVD navigation command.                                                                               |
| [**EC\_DVD\_NO\_FP\_PGC**](ec-dvd-no-fp-pgc.md)                               | Indicates that the DVD disc does not have a FP\_PGC (First Play Program Chain).                                                                                           |
| [**EC\_DVD\_PARENTAL\_LEVEL\_CHANGE**](ec-dvd-parental-level-change.md)       | Signals that the parental level of the authored content is about to change.                                                                                               |
| [**EC\_DVD\_PLAYBACK\_RATE\_CHANGE**](ec-dvd-playback-rate-change.md)         | Indicates that a playback rate change has been initiated and the new rate is in the parameter.                                                                            |
| [**EC\_DVD\_PLAYBACK\_STOPPED**](ec-dvd-playback-stopped.md)                  | Indicates that playback has been stopped. The DVD Navigator has completed playback of the title and did not find any other branching instruction for subsequent playback. |
| [**EC\_DVD\_PLAYPERIOD\_AUTOSTOP**](ec-dvd-playperiod-autostop.md)            | Indicates that the Navigator has finished playing the segment specified in a call to PlayPeriodInTitleAutoStop.                                                           |
| [**EC\_DVD\_PROGRAM\_CELL\_CHANGE**](ec-dvd-program-cell-change.md)           | Sent when the DVD program number or cell number changes.                                                                                                                  |
| [**EC\_DVD\_PROGRAM\_CHAIN\_CHANGE**](ec-dvd-program-chain-change.md)         | Sent when current program chain (PGC) changes.                                                                                                                            |
| [**EC\_DVD\_SPRM\_Change**](ec-dvd-sprm-change.md)                            | Sent when the value of a system parameter register (SPRM) changes.                                                                                                        |
| [**EC\_DVD\_STILL\_OFF**](ec-dvd-still-off.md)                                | Signals the end of any still.                                                                                                                                             |
| [**EC\_DVD\_STILL\_ON**](ec-dvd-still-on.md)                                  | Signals the beginning of any still.                                                                                                                                       |
| [**EC\_DVD\_SUBPICTURE\_STREAM\_CHANGE**](ec-dvd-subpicture-stream-change.md) | Signals that the current subpicture stream number changed for the main title.                                                                                             |
| [**EC\_DVD\_TITLE\_SET\_CHANGE**](ec-dvd-title-set-change.md)                 | Sent when current Video Title Set (VTS) changes.                                                                                                                          |
| [**EC\_DVD\_TITLE\_CHANGE**](ec-dvd-title-change.md)                          | Indicates when the current title number changes.                                                                                                                          |
| [**EC\_DVD\_VALID\_UOPS\_CHANGE**](ec-dvd-valid-uops-change.md)               | Signals that the available set of [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2) interface methods has changed.                                                                     |
| [**EC\_DVD\_VOBU\_Offset**](ec-dvd-vobu-offset.md)                            | Sent when the [DVD Navigator](dvd-navigator-filter.md) parses a PCI packet.                                                                                              |
| [**EC\_DVD\_VOBU\_Timestamp**](ec-dvd-vobu-timestamp.md)                      | Sent when the [DVD Navigator](dvd-navigator-filter.md) parses a PCI packet.                                                                                              |
| [**EC\_DVD\_WARNING**](ec-dvd-warning.md)                                     | Signals a DVD warning condition.                                                                                                                                          |



 

## Related topics

<dl> <dt>

[Constants and GUIDs](constants-and-guids.md)
</dt> </dl>

 

 



