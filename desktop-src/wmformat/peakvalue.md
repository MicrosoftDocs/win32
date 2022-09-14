---
title: PeakValue
description: The PeakValue attribute contains contains a 16-bit amplitude value designating the peak volume level of audio content.
ms.assetid: 885f6d4c-661a-4681-96b6-c1a282c8bf18
keywords:
- PeakValue windows Media Format
topic_type:
- apiref
api_name:
- PeakValue
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# PeakValue

The **PeakValue** attribute contains contains a 16-bit amplitude value designating the peak volume level of audio content. With [**AverageLevel**](averagelevel.md), this attribute is used for normalization. Normalization is the process of adjusting the playback volume level of audio files so that the loudest parts of files playback at the same level and the average volume for each is the same..

## Global Constant

g\_wszPeakValue

## Data Type

**WMT\_TYPE\_DWORD**

## Remarks

This attribute is set by the writer object based on information from the codec. Only streams compressed with one of the Windows Media Audio codecs have an automatically set value.

**PeakValue** is not read-only. However, if the file will be played by the Windows Media Player, you should not alter this value. The Windows Media Player uses this for normalizing the levels of files in a playlist.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




