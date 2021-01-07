---
description: The style of a dialog box is specified in the Attributes column of the Dialog table by a 32-bit word composed of style bit flags.
ms.assetid: aad719e8-86b3-4b2b-b417-db55013f8d3a
title: Dialog Style Bits
ms.topic: article
ms.date: 05/31/2018
---

# Dialog Style Bits

The style of a dialog box is specified in the Attributes column of the [Dialog table](dialog-table.md) by a 32-bit word composed of style bit flags.

The following list provides links to descriptions of reserved dialog box style bits.



| Name                                                      | Decimal | Hexadecimal | Constant                                                                                                                                       |
|-----------------------------------------------------------|---------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [Visible](visible-dialog-style-bit.md)                   | 1       | 0x00000001  | **msidbDialogAttributesVisible**                                                                                                               |
| [Modal](modal-dialog-style-bit.md)                       | 2       | 0x00000002  | **msidbDialogAttributesModal**                                                                                                                 |
| [Minimize](minimize-dialog-style-bit.md)                 | 4       | 0x00000004  | **msidbDialogAttributesMinimize**                                                                                                              |
| [SysModal](sysmodal-dialog-style-bit.md)                 | 8       | 0x00000008  | **msidbDialogAttributesSysModal**                                                                                                              |
| [KeepModeless](keepmodeless-dialog-style-bit.md)         | 16      | 0x00000010  | **msidbDialogAttributesKeepModeless**                                                                                                          |
| [TrackDiskSpace](trackdiskspace-dialog-style-bit.md)     | 32      | 0x00000020  | **msidbDialogAttributesTrackDiskSpace**                                                                                                        |
| [UseCustomPalette](usecustompalette-dialog-style-bit.md) | 64      | 0x00000040  | **msidbDialogAttributesUseCustomPalette**                                                                                                      |
| [RTLRO](rtlro-dialog-style-bit.md)                       | 128     | 0x00000080  | **msidbDialogAttributesRTLRO**                                                                                                                 |
| [RightAligned](rightaligned-dialog-style-bit.md)         | 256     | 0x00000100  | **msidbDialogAttributesRightAligned**                                                                                                          |
| [LeftScroll](leftscroll-dialog-style-bit.md)             | 512     | 0x00000200  | **msidbDialogAttributesLeftScroll**                                                                                                            |
| [BiDi](bidi-dialog-style-bit.md)                         | 896     | 0x00000380  | **msidbDialogAttributesBiDi** = **msidbDialogAttributesRTLRO** \| **msidbDialogAttributesRightAligned** \| **msidbDialogAttributesLeftScroll** |
| [Error](error-dialog-style-bit.md)                       | 65536   | 0x00010000  | **msidbDialogAttributesError**                                                                                                                 |



 

 

 



