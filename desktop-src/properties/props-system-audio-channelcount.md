---
description: Indicates the channel count for the audio file. Possible values are 1 for mono and 2 for stereo.
ms.assetid: 8a028167-dc0f-4ed9-a710-568caf1b9a47
title: System.Audio.ChannelCount
ms.topic: article
ms.date: 05/31/2018
---

# System.Audio.ChannelCount

Indicates the channel count for the audio file. Possible values are 1 for mono and 2 for stereo.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Audio.ChannelCount
   shellPKey = PKEY_Audio_ChannelCount
   formatID = 64440490-4C8B-11D1-8B70-080036B11A03
   propID = 7
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Mono
            value = 1
            text = 1 (mono)
            defineToken = AUDIO_CHANNELCOUNT_MONO
         enum
            name = Stereo
            value = 2
            text = 2 (stereo)
            defineToken = AUDIO_CHANNELCOUNT_STEREO
```

## Windows Vista

```
propertyDescription
   name = System.Audio.ChannelCount
   shellPKey = PKEY_Audio_ChannelCount
   formatID = 64440490-4C8B-11D1-8B70-080036B11A03
   propID = 7
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 1
            text = 1 (mono)
            defineName = AUDIO_CHANNELCOUNT_MONO
         enum
            value = 2
            text = 2 (stereo)
            defineName = AUDIO_CHANNELCOUNT_STEREO
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

 

 
