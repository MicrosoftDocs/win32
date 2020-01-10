---
title: AverageLevel
description: The AverageLevel attribute contains a 16-bit amplitude value designating the average volume level of audio content.
ms.assetid: e6270ac8-5de3-4dee-824c-ba25fdd272c8
keywords:
- AverageLevel windows Media Format
topic_type:
- apiref
api_name:
- AverageLevel
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AverageLevel

The **AverageLevel** attribute contains a 16-bit amplitude value designating the average volume level of audio content. With [**PeakValue**](peakvalue.md), this attribute is used for normalization. Normalization is the process of adjusting the playback volume level of audio files so that the loudest parts of files playback at the same level and the average volume for each is the same.

## Global Constant

g\_wszAverageLevel

## Data Type

**WMT\_TYPE\_DWORD**

## Remarks

This attribute is set by the writer object based on information from the codec. Only streams compressed with one of the Windows Media Audio codecs have an automatically set value.

**AverageLevel** is not read-only. However, if the file will be played by the Windows Media Player, you should not alter this value. The Windows Media Player uses this for normalizing the levels of files in a playlist.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




