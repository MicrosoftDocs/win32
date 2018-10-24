---
Description: Lists the signal processing modes supported by the stream effect APO.
ms.assetid: 52A04E91-CE12-40BB-B2EC-DBE069306C4B
title: PKEY_SFX_ProcessingModes_Supported_For_Streaming property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PKEY\_SFX\_ProcessingModes\_Supported\_For\_Streaming property

Lists the signal processing modes supported by the stream effect APO.

PROPVARIANT type (vt): **VT\_VECTOR** \| **VT\_LPWSTR**

## Remarks

This list only includes signal processing modes where the APO actually processes the audio signal during streaming.

This list does not include any signal processing modes supported by the APO for discovery purposes only.

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>Audioenginebaseapo.h</dt> </dl> |



## See also

<dl> <dt>

[Core Audio Properties](core-audio-properties.md)
</dt> </dl>

 

 




