---
title: MCI Functions Macros and Messages
description: MCI Functions Macros and Messages
ms.assetid: 7cedc46f-f67b-4b1a-b1e0-7ac32c250132
keywords:
- MCI messages
ms.topic: article
ms.date: 05/31/2018
---

# MCI Functions Macros and Messages

Most MCI applications use the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) and [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) functions dozens of times. MCI provides some other useful functions that your application will use less frequently.

The device identifier required by most MCI commands is typically retrieved in a call to the [**open**](open.md) ([**MCI\_OPEN**](mci-open.md)) command. If you need a device identifier but do not want to open the device — for example, if you want to query the capabilities of the device before taking any other action — you can call the [**mciGetDeviceID**](/previous-versions//dd757156(v=vs.85)) function.

The [**mciGetCreatorTask**](/previous-versions//dd757155(v=vs.85)) function allows your application to use a device identifier to retrieve a handle to the task that created that identifier.

You can use the [**mciGetYieldProc**](/previous-versions//dd757159(v=vs.85)) and [**mciSetYieldProc**](/previous-versions//dd757163(v=vs.85)) functions to assign and retrieve the address of the callback function associated with the "wait" (MCI\_WAIT) flag.

The [**mciGetErrorString**](/previous-versions//dd757158(v=vs.85)) function retrieves a string that describes an MCI error value. Each string that MCI returns, whether data or an error description, is a maximum of 128 characters. Dialog box fields that are smaller than 128 characters will truncate the longer strings returned by MCI. For more information about these strings, see [MCIERR Return Values](mcierr-return-values.md).

The MCI macros are tools you can use to create and disassemble values that specify time formats. These time formats are used in many MCI commands. The formats acted on by the macros are hours/minutes/seconds (HMS), minutes/seconds/frames (MSF), and tracks/minutes/seconds/frames (TMSF). The following table lists the macros and their descriptions.



| Macro                                        | Description                                        |
|----------------------------------------------|----------------------------------------------------|
| [**MCI\_HMS\_HOUR**](mci-hms-hour.md)       | Retrieves the hours component from an HMS value.   |
| [**MCI\_HMS\_MINUTE**](mci-hms-minute.md)   | Retrieves the minutes component from an HMS value. |
| [**MCI\_HMS\_SECOND**](mci-hms-second.md)   | Retrieves the seconds component from an HMS value. |
| [**MCI\_MAKE\_HMS**](mci-make-hms.md)       | Creates an HMS value.                              |
| [**MCI\_MAKE\_MSF**](mci-make-msf.md)       | Creates an MSF value.                              |
| [**MCI\_MAKE\_TMSF**](mci-make-tmsf.md)     | Creates a TMSF value.                              |
| [**MCI\_MSF\_FRAME**](/previous-versions//dd743438(v=vs.85))     | Retrieves the frames component from an MSF value.  |
| [**MCI\_MSF\_MINUTE**](mci-msf-minute.md)   | Retrieves the minutes component from an MSF value. |
| [**MCI\_MSF\_SECOND**](mci-msf-second.md)   | Retrieves the seconds component from an MSF value. |
| [**MCI\_TMSF\_FRAME**](mci-tmsf-frame.md)   | Retrieves the frames component from a TMSF value.  |
| [**MCI\_TMSF\_MINUTE**](mci-tmsf-minute.md) | Retrieves the minutes component from a TMSF value. |
| [**MCI\_TMSF\_SECOND**](mci-tmsf-second.md) | Retrieves the seconds component from a TMSF value. |
| [**MCI\_TMSF\_TRACK**](mci-tmsf-track.md)   | Retrieves the tracks component from a TMSF value.  |



 

MCI also provides two messages: [**MM\_MCINOTIFY**](mm-mcinotify.md) and [**MM\_MCISIGNAL**](mm-mcisignal.md). The MM\_MCINOTIFY message notifies an application of the outcome of an MCI command whenever that command specifies the "notify" (MCI\_NOTIFY) flag. The MM\_MCISIGNAL message is specific to digital-video devices; it notifies the application when a specified position is reached.

 

 