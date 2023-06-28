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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PeakValue

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




