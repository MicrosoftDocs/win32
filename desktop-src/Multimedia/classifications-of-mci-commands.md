---
title: Classifications of MCI Commands
description: Classifications of MCI Commands
ms.assetid: e03edfab-06c9-4337-935b-9effd2996c2e
keywords:
- MCI commands,classifications
ms.topic: article
ms.date: 05/31/2018
---

# Classifications of MCI Commands

MCI defines four command classifications: system, required, basic, and extended. The following list describes these command classifications:

-   *System commands* are handled by MCI directly, rather than by the driver.
-   *Required commands* are handled by the driver. All MCI drivers must support the required commands and flags.
-   *Basic commands* (or optional commands) are used by some devices. If a device supports a basic command, it must support a defined set of flags for that command.
-   *Extended commands* are specific to a device type or driver. Extended commands include commands, like the [**put**](put.md) ([**MCI\_PUT**](mci-put.md)) and [**where**](where.md) ([**MCI\_WHERE**](mci-where.md)) commands for the **digitalvideo** and **overlay** device types, and extensions to existing commands (like the "stretch" flag of the [**status**](status.md) ([**MCI\_STATUS**](mci-status.md)) command for the overlay device type).

While system and required commands are the minimum command set for any MCI driver, basic and extended commands are not supported by all drivers. Your application can always use system and required commands and their flags, but if it needs to use a basic or extended command or flag, it should first query the driver by using the [**capability**](capability.md) ([**MCI\_GETDEVCAPS**](mci-getdevcaps.md)) command. The following sections summarize the specific commands in each category.

## System Commands

MCI processes the following system commands directly, rather than passing them to MCI devices.



| String                 | Message                             | Description                            |
|------------------------|-------------------------------------|----------------------------------------|
| [**break**](break.md) | [**MCI\_BREAK**](mci-break.md)     | Sets a break key for an MCI device.    |
| [sysinfo](sysinfo.md) | [**MCI\_SYSINFO**](mci-sysinfo.md) | Returns information about MCI devices. |



 

## Required Commands

All MCI devices support the following required commands.



| String                           | Message                                   | Description                                                                                                               |
|----------------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**capability**](capability.md) | [**MCI\_GETDEVCAPS**](mci-getdevcaps.md) | Obtains the capabilities of a device.                                                                                     |
| [**close**](close.md)           | [**MCI\_CLOSE**](mci-close.md)           | Closes the device.                                                                                                        |
| [**info**](info.md)             | [**MCI\_INFO**](mci-info.md)             | Obtains textual information from a device.                                                                                |
| [**open**](open.md)             | [**MCI\_OPEN**](mci-open.md)             | Initializes the device.                                                                                                   |
| [**status**](status.md)         | [**MCI\_STATUS**](mci-status.md)         | Obtains status information from the device. Some of this command's flags are not required, so it is also a basic command. |



 

Devices must also support a standard set of command flags for the required commands.

## Basic Commands

The following list summarizes the basic commands. The use of these commands by an MCI device is optional.



| String                   | Message                           | Description                                                                                                                                                                                                                             |
|--------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**load**](load.md)     | [**MCI\_LOAD**](mci-load.md)     | Loads data from a file.                                                                                                                                                                                                                 |
| [**pause**](pause.md)   | [**MCI\_PAUSE**](mci-pause.md)   | Stops playing. Playback or recording can be resumed at the current position.                                                                                                                                                            |
| [**play**](play.md)     | [**MCI\_PLAY**](mci-play.md)     | Starts transmitting output data.                                                                                                                                                                                                        |
| [**record**](record.md) | [**MCI\_RECORD**](mci-record.md) | Starts recording input data.                                                                                                                                                                                                            |
| [**resume**](resume.md) | [**MCI\_RESUME**](mci-resume.md) | Resumes playing or recording on a paused device.                                                                                                                                                                                        |
| [**save**](save.md)     | [**MCI\_SAVE**](mci-save.md)     | Saves data to a disk file.                                                                                                                                                                                                              |
| [**seek**](seek.md)     | [**MCI\_SEEK**](mci-seek.md)     | Seeks forward or backward.                                                                                                                                                                                                              |
| [**set**](set.md)       | [**MCI\_SET**](mci-set.md)       | Sets the operating state of the device.                                                                                                                                                                                                 |
| [**status**](status.md) | [**MCI STATUS**](mci-status.md)  | Obtains status information about the device. This is also a required command; since some of its flags are not required, it is also listed here. (The optional items support devices that use linear media with identifiable positions.) |
| [**stop**](stop.md)     | [**MCI\_STOP**](mci-stop.md)     | Stops playing.                                                                                                                                                                                                                          |



 

If a driver supports a basic command, it must also support a standard set of flags for the command.

## Extended Commands

Some MCI devices have additional commands, or they add flags to existing commands. While some extended commands apply only to a specific device driver, most of them apply to all drivers of a particular device type. For example, the command set for the **sequencer** device type extends the [**set**](set.md) ([**MCI\_SET**](mci-set.md)) command to add time formats that are needed by MIDI sequencers.

You should not assume that the device supports the extended commands or flags. You can use the [**capability**](capability.md) ([**MCI\_GETDEVCAPS**](mci-getdevcaps.md)) command to determine whether a specific feature is supported, and your application should be ready to deal with "unsupported command" or "unsupported function" return values.

The following extended commands are available with the listed device types.



| String                         | Message                                 | Device types            | Description                                                                                       |
|--------------------------------|-----------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------|
| [**configure**](configure.md) | [**MCI\_CONFIGURE**](mci-configure.md) | digitalvideo            | Displays a configuration dialog box.                                                              |
| [**cue**](cue.md)             | [**MCI\_CUE**](mci-cue.md)             | digitalvideo, waveaudio | Prepares for playing or recording.                                                                |
| [**delete**](delete.md)       | [**MCI\_DELETE**](mci-delete.md)       | waveaudio               | Deletes a data segment from the media file.                                                       |
| [escape](escape.md)           | [**MCI\_ESCAPE**](mci-escape.md)       | videodisc               | Sends custom information to a device.                                                             |
| [**freeze**](freeze.md)       | [**MCI\_FREEZE**](mci-freeze.md)       | overlay                 | Disables video acquisition to the frame buffer.                                                   |
| [**put**](put.md)             | [**MCI PUT**](mci-put.md)              | digitalvideo, overlay   | Defines the source, destination, and frame windows.                                               |
| [**realize**](realize.md)     | [**MCI\_REALIZE**](mci-realize.md)     | digitalvideo            | Tells the device to select and realize its palette into a device context of the displayed window. |
| [**setaudio**](setaudio.md)   | [**MCI\_ SETAUDIO**](mci-setaudio.md)  | digitalvideo            | Sets audio parameters for video.                                                                  |
| [**setvideo**](setvideo.md)   | [**MCI\_ SETVIDEO**](mci-setvideo.md)  | digitalvideo            | Sets video parameters.                                                                            |
| [**signal**](signal.md)       | [**MCI\_SIGNAL**](mci-signal.md)       | digitalvideo            | Identifies a specified position with a signal.                                                    |
| [**spin**](spin.md)           | [**MCI\_SPIN**](mci-spin.md)           | videodisc               | Starts the disc spinning or stops the disc from spinning.                                         |
| [**step**](step.md)           | [**MCI\_STEP**](mci-step.md)           | digitalvideo, videodisc | Steps the play one or more frames forward or reverse.                                             |
| [**unfreeze**](unfreeze.md)   | [**MCI\_UNFREEZE**](mci-unfreeze.md)   | overlay                 | Enables the frame buffer to acquire video data.                                                   |
| [**update**](update.md)       | [**MCI\_UPDATE**](mci-update.md)       | digitalvideo            | Repaints the current frame into the device context.                                               |
| [**where**](where.md)         | [**MCI WHERE**](mci-where.md)          | digitalvideo, overlay   | Obtains the rectangle specifying the source, destination, or frame area.                          |
| [**window**](window.md)       | [**MCI\_WINDOW**](mci-window.md)       | digitalvideo, overlay   | Controls the display window.                                                                      |



 

 

 




