---
Description: 'Lists the signal processing modes supported by the endpoint effect APO.'
ms.assetid: 'BB54E7D8-5486-44F6-A204-002027255CD8'
title: 'PKEY\_EFX\_ProcessingModes\_Supported\_For\_Streaming property'
---

# PKEY\_EFX\_ProcessingModes\_Supported\_For\_Streaming property

Lists the signal processing modes supported by the endpoint effect APO.

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

 

 




