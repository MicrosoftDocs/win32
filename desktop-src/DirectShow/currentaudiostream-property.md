---
description: The CurrentAudioStream property sets or retrieves the number of the enabled audio stream.
ms.assetid: 9efaae3f-1fb8-41ab-b7a9-889cc3cc39c3
title: CurrentAudioStream Property
ms.topic: reference
ms.date: 05/31/2018
---

# CurrentAudioStream Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentAudioStream` property sets or retrieves the number of the enabled audio stream.

``` syntax
[ iStream = ] MSWebDVD.CurrentAudioStream
```

## Return Value

Returns an integer value from 0 through 7 indicating the current audio stream.

## Remarks

This property is read/write with no default value. Before attempting to set a new audio stream, call [**IsAudioStreamEnabled**](isaudiostreamenabled-method.md) to verify that the stream is available.

## See also

<dl> <dt>

[**AudioStreamsAvailable**](audiostreamsavailable-property.md)
</dt> </dl>

 

 



