---
title: Predefined Font Attributes (TsAttrid.h)
description: The following values identify font attributes obtained with the ITfContext GetAppProperty method. The data format and contents of each property type are included.
ms.assetid: 8d73c258-77d5-46db-9d31-ac41d9e7acb3
keywords:
- Predefined Font Attributes Text Services Framework
topic_type:
- apiref
api_name:
- Predefined Font Attributes
api_location:
- TsAttrid.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Predefined Font Attributes

The following values identify font attributes obtained with the [ITfContext::GetAppProperty](/windows/desktop/api/msctf/nf-msctf-itfcontext-getappproperty) method. The data format and contents of each property type are included.

## Properties



| Property                                                 | Description                                                                                                                 |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **TSATTRID\_Font**                                       | Not used.                                                                                                                   |
| **TSATTRID\_Font\_FaceName**                             | Contains the face name of the text font.                                                                                    |
| **TSATTRID\_Font\_SizePts**                              | Contains the point size of the text font.                                                                                   |
| **TSATTRID\_Font\_Style**                                | Not used.                                                                                                                   |
| **TSATTRID\_Font\_Style\_Animation**                     | Not used.                                                                                                                   |
| **TSATTRID\_Font\_Style\_Animation\_BlinkingBackground** | Contains a nonzero value if the text has the specified animation or zero otherwise.                                         |
| **TSATTRID\_Font\_Style\_Animation\_LasVegasLights**     | Contains a nonzero value if the text has the specified animation or zero otherwise.                                         |
| **TSATTRID\_Font\_Style\_Animation\_MarchingBlackAnts**  | Contains a nonzero value if the text has the specified animation or zero otherwise.                                         |
| **TSATTRID\_Font\_Style\_Animation\_MarchingRedAnts**    | Contains a nonzero value if the text has the specified animation or zero otherwise.                                         |
| **TSATTRID\_Font\_Style\_Animation\_Shimmer**            | Contains a nonzero value if the text has the specified animation or zero otherwise.                                         |
| **TSATTRID\_Font\_Style\_Animation\_SparkleText**        | Contains a nonzero value if the text has the specified animation or zero otherwise.                                         |
| **TSATTRID\_Font\_Style\_Animation\_WipeDown**           | Contains a nonzero value if the text has the specified animation or zero otherwise.                                         |
| **TSATTRID\_Font\_Style\_Animation\_WipeRight**          | Contains a nonzero value if the text has the specified animation or zero otherwise.                                         |
| **TSATTRID\_Font\_Style\_BackgroundColor**               | Contains the RGB value of the text background. Contains 0xFF000000 if the text color is automatic.                          |
| **TSATTRID\_Font\_Style\_Blink**                         | Contains a nonzero value if the text is blinking or zero otherwise.                                                         |
| **TSATTRID\_Font\_Style\_Bold**                          | Contains a nonzero value if the text is bold or zero otherwise.                                                             |
| **TSATTRID\_Font\_Style\_Capitalize**                    | Contains a nonzero value if the text is capitalized or zero otherwise.                                                      |
| **TSATTRID\_Font\_Style\_Color**                         | Contains the RGB value of the text color. Contains 0xFF000000 if the text color is automatic.                               |
| **TSATTRID\_Font\_Style\_Emboss**                        | Contains a nonzero value if the text is embossed or zero otherwise.                                                         |
| **TSATTRID\_Font\_Style\_Engrave**                       | Contains a nonzero value if the text is engraved or zero otherwise.                                                         |
| **TSATTRID\_Font\_Style\_Height**                        | Contains the font height. For more information, see the **lfHeight** member of the LOGFONT structure.                       |
| **TSATTRID\_Font\_Style\_Hidden**                        | Contains a nonzero value if the text is hidden or zero otherwise.                                                           |
| **TSATTRID\_Font\_Style\_Italic**                        | Contains a nonzero value if the text is italic or zero otherwise.                                                           |
| **TSATTRID\_Font\_Style\_Kerning**                       | Contains the minimum kerning size. For more information, see ITextFont::GetKerning.                                         |
| **TSATTRID\_Font\_Style\_Lowercase**                     | Contains a nonzero value if the text is lowercase or zero otherwise.                                                        |
| **TSATTRID\_Font\_Style\_Outlined**                      | Contains a nonzero value if the text is outlined or zero otherwise.                                                         |
| **TSATTRID\_Font\_Style\_Overline**                      | Contains a nonzero value if the text is overlined or zero otherwise.                                                        |
| **TSATTRID\_Font\_Style\_Overline\_Double**              | Contains a nonzero value if the text is double overlined or zero otherwise.                                                 |
| **TSATTRID\_Font\_Style\_Overline\_Single**              | Contains a nonzero value if the text is single overlined or zero otherwise.                                                 |
| **TSATTRID\_Font\_Style\_Position**                      | Contains the font position.                                                                                                 |
| **TSATTRID\_Font\_Style\_Protected**                     | Contains a nonzero value if the text is protected or zero otherwise.                                                        |
| **TSATTRID\_Font\_Style\_Shadow**                        | Contains a nonzero value if the text is shadowed or zero otherwise.                                                         |
| **TSATTRID\_Font\_Style\_SmallCaps**                     | Contains a nonzero value if the text is lowercase or zero otherwise.                                                        |
| **TSATTRID\_Font\_Style\_Spacing**                       | Contains the font spacing.                                                                                                  |
| **TSATTRID\_Font\_Style\_Strikethrough**                 | Not used.                                                                                                                   |
| **TSATTRID\_Font\_Style\_Strikethrough\_Double**         | Contains a nonzero value if the text is double strikethrough or zero otherwise.                                             |
| **TSATTRID\_Font\_Style\_Strikethrough\_Single**         | Contains a nonzero value if the text is single strikethrough or zero otherwise.                                             |
| **TSATTRID\_Font\_Style\_Subscript**                     | Contains a nonzero value if the text is subscript or zero otherwise.                                                        |
| **TSATTRID\_Font\_Style\_Superscript**                   | Contains a nonzero value if the text is superscript or zero otherwise.                                                      |
| **TSATTRID\_Font\_Style\_Underline**                     | Contains a nonzero value if the text is underlined or zero otherwise.                                                       |
| **TSATTRID\_Font\_Style\_Underline\_Double**             | Contains a nonzero value if the text is double underlined or zero otherwise.                                                |
| **TSATTRID\_Font\_Style\_Underline\_Single**             | Contains a nonzero value if the text is single underlined or zero otherwise.                                                |
| **TSATTRID\_Font\_Style\_Uppercase**                     | Contains a nonzero value if the text is uppercase or zero otherwise.                                                        |
| **TSATTRID\_Font\_Style\_Weight**                        | Contains the font weight. For more information about possible values, see the **lfWeight** member of the LOGFONT structure. |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                       |
| Header<br/>                   | <dl> <dt>TsAttrid.h</dt> </dl> |



## See also

<dl> <dt>

[ITfContext::GetAppProperty](/windows/desktop/api/msctf/nf-msctf-itfcontext-getappproperty)
</dt> </dl>

 

