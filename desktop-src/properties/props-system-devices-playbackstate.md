---
description: The playback state of the device.
ms.assetid: 7F77459B-5900-4967-A2A3-AAEE78DF84E1
title: System.Devices.PlaybackState
ms.topic: article
ms.date: 05/31/2018
---

# System.Devices.PlaybackState

The playback state of the device.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8

```
propertyDescription
   name = System.Devices.PlaybackState
   shellPKey = PKEY_Devices_PlaybackState
   formatID = 3633DE59-6825-4381-A49B-9F6BA13A1471
   propID = 2
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Byte
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = UnknownState
            value = 0
            text = Unknown State
            defineToken = PLAYBACKSTATE_UNKNOWN
         enum
            name = Stopped
            value = 1
            text = Stopped
            defineToken = PLAYBACKSTATE_STOPPED
         enum
            name = Playing
            value = 2
            text = Playing
            defineToken = PLAYBACKSTATE_PLAYING
         enum
            name = Transitioning
            value = 3
            text = Transitioning
            defineToken = PLAYBACKSTATE_TRANSITIONING
         enum
            name = PlaybackPaused
            value = 4
            text = Paused
            defineToken = PLAYBACKSTATE_PAUSED
         enum
            name = RecordingPaused
            value = 5
            text = Recording Paused
            defineToken = PLAYBACKSTATE_RECORDINGPAUSED
         enum
            name = Recording
            value = 6
            text = Recording
            defineToken = PLAYBACKSTATE_RECORDING
         enum
            name = NoMedia
            value = 7
            text = No Media
            defineToken = PLAYBACKSTATE_NOMEDIA
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[propertyDescription](./propdesc-schema-propertydescription.md)
</dt> <dt>

[searchInfo](./propdesc-schema-searchinfo.md)
</dt> <dt>

[labelInfo](./propdesc-schema-labelinfo.md)
</dt> <dt>

[typeInfo](./propdesc-schema-typeinfo.md)
</dt> <dt>

[displayInfo](./propdesc-schema-displayinfo.md)
</dt> <dt>

[stringFormat](./propdesc-schema-stringformat.md)
</dt> <dt>

[booleanFormat](./propdesc-schema-booleanformat.md)
</dt> <dt>

[numberFormat](./propdesc-schema-numberformat.md)
</dt> <dt>

[dateTimeFormat](./propdesc-schema-datetimeformat.md)
</dt> <dt>

[enumeratedList](./propdesc-schema-enumeratedlist.md)
</dt> <dt>

[drawControl](./propdesc-schema-drawcontrol.md)
</dt> <dt>

[editControl](./propdesc-schema-editcontrol.md)
</dt> <dt>

[filterControl](./propdesc-schema-filtercontrol.md)
</dt> <dt>

[queryControl](./propdesc-schema-querycontrol.md)
</dt> </dl>

 

 
