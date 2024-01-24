---
description: Font Package Function Error Messages
ms.assetid: 3cf7a8a1-66b2-45ca-b53d-29c80f95ff70
title: Font Package Function Error Messages
ms.topic: article
ms.date: 05/31/2018
---

# Font Package Function Error Messages

The following LONG values are returned by the font package functions ( [**CreateFontPackage**](/windows/desktop/api/FontSub/nf-fontsub-createfontpackage) and [**MergeFontPackage**](/windows/desktop/api/FontSub/nf-fontsub-mergefontpackage) ) when errors are encountered. When functions are successful, the value NO\_ERROR is returned.



| Return value                   | Value | Description                                                                                                      |
|--------------------------------|-------|------------------------------------------------------------------------------------------------------------------|
| NO\_ERROR                      | 0     | No error occurred.                                                                                               |
| ERR\_FORMAT                    | 1006  | An input data format error occurred.                                                                             |
| ERR\_GENERIC                   | 1000  | An error occurred in generic code.                                                                               |
| ERR\_MEM                       | 1005  | An error occurred during memory allocation.                                                                      |
| ERR\_NO\_GLYPHS                | 1009  | No glyphs were found.                                                                                            |
| ERR\_INVALID\_BASE             | 1085  | The font contained an invalid baseline data (BASE) table. Currently this value is not used.                      |
| ERR\_INVALID\_CMAP             | 1030  | The font contained an invalid character-to-glyph mapping (cmap) table.                                           |
| ERR\_INVALID\_DELTA\_FORMAT    | 1013  | An invalid delta format was detected while trying to subset a format 1 or 2 font.                                |
| ERR\_INVALID\_EBLC             | 1086  | The font contained an invalid embedded bitmap location data (EBLC) table.                                        |
| ERR\_INVALID\_GLYF             | 1061  | The font contained an invalid glyph data (glyf) table.                                                           |
| ERR\_INVALID\_GDEF             | 1083  | The font contained an invalid glyph definition data (GDEF) table. Currently this value is not used.              |
| ERR\_INVALID\_GPOS             | 1082  | The font contained an invalid glyph positioning data (GPOS) table. Currently this value is not used.             |
| ERR\_INVALID\_GSUB             | 1081  | The font contained an invalid glyph substitution data (GSUB) table.                                              |
| ERR\_INVALID\_HDMX             | 1089  | The font contained an invalid horizontal device metrics (hdmx) table.                                            |
| ERR\_INVALID\_HEAD             | 1062  | The font contained an invalid font header (head) table.                                                          |
| ERR\_INVALID\_HHEA             | 1063  | The font contained an invalid horizontal header (hhea) table.                                                    |
| ERR\_INVALID\_HHEA\_OR\_VHEA   | 1072  | The font contained an invalid horizontal header (hhea) table or an invalid vertical metrics header (vhea) table. |
| ERR\_INVALID\_HMTX             | 1064  | The font contained an invalid horizontal metrics (hmtx) table.                                                   |
| ERR\_INVALID\_HMTX\_OR\_VMTX   | 1073  | The font contained an invalid horizontal metrics (hmtx) table or an invalid vertical metrics (vmtx) table.       |
| ERR\_INVALID\_JSTF             | 1084  | The font contained an invalid justification data (JSTF) table.                                                   |
| ERR\_INVALID\_LTSH             | 1087  | The font contained an invalid linear threshold data (LTSH) table.                                                |
| ERR\_INVALID\_TTO              | 1080  | The font was an invalid TrueType Open font.                                                                      |
| ERR\_INVALID\_VDMX             | 1088  | The font contained an invalid vertical device metrics (VDMX) table.                                              |
| ERR\_INVALID\_LOCA             | 1065  | The font contained an invalid index to location (loca) table.                                                    |
| ERR\_INVALID\_MAXP             | 1066  | The font contained an invalid maximum profile (maxp) table.                                                      |
| ERR\_INVALID\_MERGE\_CHECKSUMS | 1011  | An attempt to merge checksums for two fonts from a different mother font was unsuccessful.                       |
| ERR\_INVALID\_MERGE\_FORMATS   | 1010  | An attempt to merge fonts with the wrong dttf formats was unsuccessful.                                          |
| ERR\_INVALID\_MERGE\_NUMGLYPHS | 1012  | An attempt to merge the number of glyphs for two fonts from a different mother font was unsuccessful.            |
| ERR\_INVALID\_NAME             | 1067  | The font package name or a font name was invalid.                                                                |
| ERR\_INVALID\_POST             | 1068  | The font contained an invalid PostScript information (post) table.                                               |
| ERR\_INVALID\_OS2              | 1069  | The font contained an invalid OS/2 and Windows-specific metrics (OS/2) table.                                    |
| ERR\_INVALID\_VHEA             | 1070  | The font contained an invalid vertical metrics header (vhea) table.                                              |
| ERR\_INVALID\_VMTX             | 1071  | The font contained an invalid vertical metrics (vmtx) table.                                                     |
| ERR\_INVALID\_TTC\_INDEX       | 1015  | An invalid zero-based (TTC) index into the font file was passed.                                                 |
| ERR\_MISSING\_CMAP             | 1030  | The font did not contain a cmap table.                                                                           |
| ERR\_MISSING\_EBDT             | 1044  | The font did not contain an EBDT table.                                                                          |
| ERR\_MISSING\_GLYF             | 1031  | The font did not contain a glyf table.                                                                           |
| ERR\_MISSING\_HEAD             | 1032  | The font did not contain a head table.                                                                           |
| ERR\_MISSING\_HHEA             | 1033  | The font did not contain an hhea table.                                                                          |
| ERR\_MISSING\_HMTX             | 1034  | The font did not contain an hmtx table.                                                                          |
| ERR\_MISSING\_LOCA             | 1035  | The font did not contain a loca table.                                                                           |
| ERR\_MISSING\_MAXP             | 1036  | The font did not contain a maxp table.                                                                           |
| ERR\_MISSING\_NAME             | 1037  | The font did not contain a naming (name) table.                                                                  |
| ERR\_MISSING\_POST             | 1038  | The font did not contain a post table.                                                                           |
| ERR\_MISSING\_OS2              | 1039  | The font did not contain an OS/2 table.                                                                          |
| ERR\_MISSING\_VHEA             | 1040  | The font did not contain a vhea table.                                                                           |
| ERR\_MISSING\_VMTX             | 1041  | The font did not contain a vmtx table.                                                                           |
| ERR\_MISSING\_HHEA\_OR\_VHEA   | 1042  | The font did not contain an hhea table or a vhea table.                                                          |
| ERR\_MISSING\_HMTX\_OR\_VMTX   | 1043  | The font did not contain an hmtx table or a vmtx table.                                                          |
| ERR\_NOT\_TTC                  | 1014  | The provided value was not an index for a TTC file.                                                              |
| ERR\_PARAMETER0                | 1100  | Calling function parameter 0 was invalid.                                                                        |
| ERR\_PARAMETER1                | 1101  | Calling function parameter 1 was invalid.                                                                        |
| ERR\_PARAMETER2                | 1102  | Calling function parameter 2 was invalid.                                                                        |
| ERR\_PARAMETER3                | 1103  | Calling function parameter 3 was invalid.                                                                        |
| ERR\_PARAMETER4                | 1104  | Calling function parameter 4 was invalid.                                                                        |
| ERR\_PARAMETER5                | 1105  | Calling function parameter 5 was invalid.                                                                        |
| ERR\_PARAMETER6                | 1106  | Calling function parameter 6 was invalid.                                                                        |
| ERR\_PARAMETER7                | 1107  | Calling function parameter 7 was invalid.                                                                        |
| ERR\_PARAMETER8                | 1108  | Calling function parameter 8 was invalid.                                                                        |
| ERR\_PARAMETER9                | 1109  | Calling function parameter 9 was invalid.                                                                        |
| ERR\_PARAMETER10               | 1110  | Calling function parameter 10 was invalid.                                                                       |
| ERR\_PARAMETER11               | 1111  | Calling function parameter 11 was invalid.                                                                       |
| ERR\_PARAMETER12               | 1112  | Calling function parameter 12 was invalid.                                                                       |
| ERR\_PARAMETER13               | 1113  | Calling function parameter 13 was invalid.                                                                       |
| ERR\_PARAMETER14               | 1114  | Calling function parameter 14 was invalid.                                                                       |
| ERR\_PARAMETER15               | 1115  | Calling function parameter 15 was invalid.                                                                       |
| ERR\_PARAMETER16               | 1116  | Calling function parameter 16 was invalid.                                                                       |
| ERR\_READCONTROL               | 1003  | The read control structure did not match data.                                                                   |
| ERR\_READOUTOFBOUNDS           | 1001  | A read from memory was not allowed, possibly because data was out of bounds or corrupt.                          |
| ERR\_VERSION                   | 1008  | Major dttf.version value of the input data was greater than the version the function can read.                   |
| ERR\_WOULD\_GROW               | 1007  | The requested action caused data to grow and the application must use original data.                             |
| ERR\_WRITECONTROL              | 1004  | The write control structure did not match data.                                                                  |
| ERR\_WRITEOUTOFBOUNDS          | 1002  | A write to memory was not allowed, possibly because data was out of bounds.                                      |



 

 

 



