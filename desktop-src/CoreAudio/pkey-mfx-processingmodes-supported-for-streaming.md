---
description: Lists the signal processing modes supported by the mode effect APO.
ms.assetid: 166B55B4-08F9-4B41-B659-FF8D750397F0
title: PKEY_MFX_ProcessingModes_Supported_For_Streaming property (Audioenginebaseapo.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_MFX\_ProcessingModes\_Supported\_For\_Streaming property

Lists the signal processing modes supported by the mode effect APO.

PROPVARIANT type (vt): **VT\_VECTOR** \| **VT\_LPWSTR**

## Remarks

This list only includes signal processing modes where the APO actually processes the audio signal during streaming.

This list does not include any signal processing modes supported by the APO for discovery purposes only.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>Audioenginebaseapo.h</dt> </dl> |



## See also

<dl> <dt>

[Core Audio Properties](core-audio-properties.md)
</dt> </dl>

 

 




