---
Description: Indicates the channel count for the audio file. Possible values are 1 for mono and 2 for stereo.
ms.assetid: 8a028167-dc0f-4ed9-a710-568caf1b9a47
title: System.Audio.ChannelCount
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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

[propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx)
</dt> <dt>

[searchInfo](https://msdn.microsoft.com/library/Bb773885(v=VS.85).aspx)
</dt> <dt>

[labelInfo](https://msdn.microsoft.com/library/Bb773876(v=VS.85).aspx)
</dt> <dt>

[typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx)
</dt> <dt>

[displayInfo](https://msdn.microsoft.com/library/Bb773865(v=VS.85).aspx)
</dt> <dt>

[stringFormat](https://msdn.microsoft.com/library/Bb773886(v=VS.85).aspx)
</dt> <dt>

[booleanFormat](https://msdn.microsoft.com/library/Bb773862(v=VS.85).aspx)
</dt> <dt>

[numberFormat](https://msdn.microsoft.com/library/Bb773877(v=VS.85).aspx)
</dt> <dt>

[dateTimeFormat](https://msdn.microsoft.com/library/Bb773863(v=VS.85).aspx)
</dt> <dt>

[enumeratedList](https://msdn.microsoft.com/library/Bb773871(v=VS.85).aspx)
</dt> <dt>

[drawControl](https://msdn.microsoft.com/library/Bb773866(v=VS.85).aspx)
</dt> <dt>

[editControl](https://msdn.microsoft.com/library/Bb773868(v=VS.85).aspx)
</dt> <dt>

[filterControl](https://msdn.microsoft.com/library/Bb773874(v=VS.85).aspx)
</dt> <dt>

[queryControl](https://msdn.microsoft.com/library/Bb773883(v=VS.85).aspx)
</dt> </dl>

 

 



