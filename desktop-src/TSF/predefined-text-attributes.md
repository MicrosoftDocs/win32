---
title: Predefined Text Attributes (TsAttrid.h)
description: The following values identify text attributes obtained with the ITfContext GetAppProperty method. The data format and contents of each property type are included.
ms.assetid: af73edb8-b706-40e4-a093-4ac22d33ecdc
keywords:
- Predefined Text Attributes Text Services Framework
topic_type:
- apiref
api_name:
- Predefined Text Attributes
api_location:
- TsAttrid.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Predefined Text Attributes

The following values identify text attributes obtained with the [**ITfContext::GetAppProperty**](/windows/desktop/api/msctf/nf-msctf-itfcontext-getappproperty) method. The data format and contents of each property type are included.

## Properties



| Property                                     | Description                                                                                                                                              |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| TSATTRID\_Text                               | Not used.                                                                                                                                                |
| TSATTRID\_Text\_Alignment                    | Not used.                                                                                                                                                |
| TSATTRID\_Text\_Alignment\_Center            | Contains a nonzero value if the text is centered or zero otherwise.                                                                                      |
| TSATTRID\_Text\_Alignment\_Justify           | Contains a nonzero value if the text is justified or zero otherwise.                                                                                     |
| TSATTRID\_Text\_Alignment\_Left              | Contains a nonzero value if the text is left aligned or zero otherwise.                                                                                  |
| TSATTRID\_Text\_Alignment\_Right             | Contains a nonzero value if the text is right aligned or zero otherwise.                                                                                 |
| TSATTRID\_Text\_EmbeddedObject               | Contains a nonzero value if the text is an embedded object or zero otherwise.                                                                            |
| TSATTRID\_Text\_Hyphenation                  | Contains a nonzero value if the text is hyphenated or zero otherwise.                                                                                    |
| TSATTRID\_Text\_Language                     | Contains the **LANGID** language identifier of the text.                                                                                                 |
| TSATTRID\_Text\_Link                         | Contains a pointer to a link object. The caller must use the QueryInterface method to obtain the desired interface, such as **IUniformResourceLocator**. |
| TSATTRID\_Text\_Orientation                  | Specifies the angle, in tenths of degrees, between text base line and the x-axis of the device.                                                          |
| TSATTRID\_Text\_Para                         | Not used.                                                                                                                                                |
| TSATTRID\_Text\_Para\_FirstLineIndent        | Contains the number of points that the first line of a paragraph is indented.                                                                            |
| TSATTRID\_Text\_Para\_LeftIndent             | Contains the number of points that the paragraph is indented from the left.                                                                              |
| TSATTRID\_Text\_Para\_LineSpacing            | Not used.                                                                                                                                                |
| TSATTRID\_Text\_Para\_LineSpacing\_AtLeast   | Contains the minimum number of lines for the line spacing of the paragraph.                                                                              |
| TSATTRID\_Text\_Para\_LineSpacing\_Double    | Contains a nonzero value if the paragraph is double spaced or zero otherwise.                                                                            |
| TSATTRID\_Text\_Para\_LineSpacing\_Exactly   | Contains the exact number of lines for the line spacing of the paragraph.                                                                                |
| TSATTRID\_Text\_Para\_LineSpacing\_Multiple  | Contains the number of lines for the multiple line spacing of the paragraph.                                                                             |
| TSATTRID\_Text\_Para\_LineSpacing\_OnePtFive | Contains a nonzero value if the paragraph is one and one half line spaced or zero otherwise.                                                             |
| TSATTRID\_Text\_Para\_LineSpacing\_Single    | Contains a nonzero value if the paragraph is single spaced or zero otherwise.                                                                            |
| TSATTRID\_Text\_Para\_RightIndent            | Contains the number of points that the paragraph is indented from the right.                                                                             |
| TSATTRID\_Text\_Para\_SpaceAfter             | Contains the number of points of spacing after the paragraph.                                                                                            |
| TSATTRID\_Text\_Para\_SpaceBefore            | Contains the number of points of spacing before the paragraph.                                                                                           |
| TSATTRID\_Text\_ReadOnly                     | Contains zero if the text is read-only or nonzero otherwise.                                                                                             |
| TSATTRID\_Text\_RightToLeft                  | Contains zero if the text is right-to-left reading or nonzero otherwise.                                                                                 |
| TSATTRID\_Text\_VerticalWriting              | Specifies if the text is vertical or horizontal. Contains zero if the text is horizontal or nonzero if the text is vertical.                             |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                       |
| Header<br/>                   | <dl> <dt>TsAttrid.h</dt> </dl> |



 

