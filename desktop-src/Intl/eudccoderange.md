---
description: The EUDCCodeRange registry key defines end-user-defined character (EUDC) code ranges for various code pages (character sets).
ms.assetid: 11a167a0-f2a3-4b8b-a38c-70cf14c895be
title: EUDCCodeRange
ms.topic: article
ms.date: 05/31/2018
---

# EUDCCodeRange

The EUDCCodeRange registry key defines [end-user-defined character (EUDC)](end-user-defined-characters.md) code ranges for various code pages (character sets). It is used only by tools that create EUDCs, and is not of direct concern to EUDC users. This registry key has the following registry location:

HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\NLS\\CodePage\\EUDCCodeRange

The format is:

EUDCCodeRange CodePage=FromTo\[,FromTo\]

where:



|          |                                                                                                                                                                                                          |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CodePage | One of the strings "932" (Japanese), "936" (Simplified Chinese), "949" (Korean), "950" (Traditional Chinese), or "Unicode" (Unicode). No other values are supported.                                     |
| FromTo   | String value consisting of a pair of 4-digit hexadecimal values separated by a hyphen (-). Up to four FromTo values can be specified, but each must be separated from the previous value by a comma (,). |



 

The following are the correct values for the registry entry.


```C++
932=F040-F9FC
936=A140-A7A0,AAA1-AFFE,F8A1-FEFE
949=C9A1-C9FE,FEA1-FEFE
950=8140-8DFE,8E40-A0FE,C6A1-C8FE,FA40-FEFE
Unicode=E000-F8FF
```



## Related topics

<dl> <dt>

[EUDC Registry Entries](eudc-registry-entries.md)
</dt> <dt>

[EUDC](eudc.md)
</dt> </dl>

 

 



