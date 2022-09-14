---
title: Appendix E Text Attributes for Active Accessibility Text Services Dictionary
description: This appendix provides information about text attributes that are defined in IAccDictionary.
ms.assetid: 9e405140-c151-4f00-91c5-777c84c41806
ms.topic: article
ms.date: 05/31/2018
---

# Appendix E: Text Attributes for Active Accessibility Text Services Dictionary

This appendix provides information about text attributes that are defined in [**IAccDictionary**](/windows/desktop/api/msaatext/nn-msaatext-iaccdictionary). It is organized as a series of tables. Each table includes information about a specific category of attributes. These categories are actually nested, but are separated below so that you can see the attributes.

> [!Note]  
> Active Accessibility Text Services is deprecated. Please see [Microsoft Windows Text Services Framework](../tsf/text-services-framework.md) for more information on advanced text input and natural language technologies.

 

Each entry in a table provides an attribute name and friendly name, type, Cascading Style Sheets (CSS) equivalent, Text Object Model (TOM) equivalent, and any additional comments where appropriate. The TOM equivalent column provides information about the TOM method used with the attribute (part of the [**ITextFont**](/windows/desktop/api/tom/nn-tom-itextfont), [**ITextRange**](/windows/desktop/api/tom/nn-tom-itextrange), or [**ITextPara**](/windows/desktop/api/tom/nn-tom-itextpara) interfaces). The information prior to each table indicates which interface supports the attributes; the information in the TOM equivalent table indicates the name of the method. Each entry in the TOM equivalent column is associated with two methods. For example, the Name entry is associated with the **GetName** and **SetName** methods.

For more information about these interfaces, see the [Text Object Model](../controls/text-object-model.md) documentation in the Windows Software Development Kit (SDK).

## Font

The attributes in the following table are associated with general font attributes. The TOM equivalent is the [**ITextFont**](/windows/desktop/api/tom/nn-tom-itextfont) interface.



| Attribute name, Friendly name       | Type     | CSS equivalent       | TOM equivalent | Comment           |
|-------------------------------------|----------|----------------------|----------------|-------------------|
| Font\_FaceName, facename<br/> | VT\_BSTR | Font-family: Verdana | Name           |                   |
| Font\_SizePts, sizePts<br/>   | VT\_I4   | Font-size: Xpt       | Size           | Size is in points |



 

## Font\_Style

The attributes in the following table address font style attributes (for example, whether the text is set in bold or italic). The TOM equivalent is the [**ITextFont**](/windows/desktop/api/tom/nn-tom-itextfont) interface.



| Attribute name, Friendly name                             | Type     | CSS equivalent              | TOM equivalent                                            | Comment                   |
|-----------------------------------------------------------|----------|-----------------------------|-----------------------------------------------------------|---------------------------|
| Font\_Style\_Bold, bold<br/>                        | VT\_BOOL | Font-weight: bold           | Bold                                                      |                           |
| Font\_Style\_Italic, italic<br/>                    | VT\_BOOL | Font-style: italic          | Italic                                                    |                           |
| Font\_Style\_SmallCaps, smallcaps<br/>              | VT\_BOOL | Font-variant: small-caps    | SmallCaps                                                 |                           |
| Font\_Style\_Capitalize,capitalize<br/>             | VT\_BOOL | Text-transform: capitalize  | Not supported                                             |                           |
| Font\_Style\_Uppercase,uppercase<br/>               | VT\_BOOL | Text-transform: uppercase   | AllCaps                                                   |                           |
| Font\_Style\_Lowercase,lowercase<br/>               | VT\_BOOL | Text-transform: lowercase   | Not supported                                             |                           |
| Font\_Style\_Emboss,emboss<br/>                     | VT\_BOOL | Not supported               | Emboss                                                    |                           |
| Font\_Style\_Engrave,engrave<br/>                   | VT\_BOOL | Not supported               | Engrave                                                   |                           |
| Font\_Style\_Hidden                                       | VT\_BOOL | Not supported               | Hidden                                                    |                           |
| Font\_Style\_Kerning,kerning<br/>                   | VT\_R4   | Not supported               | Kerning                                                   | Same values as GetKerning |
| Font\_Style\_Outlined,outlined<br/>                 | VT\_BOOL | Not supported               | Outlined                                                  |                           |
| Font\_Style\_Position,position<br/>                 | VT\_R4   | Not supported               | Position                                                  |                           |
| Font\_Style\_Protected                                    | VT\_BOOL | Not supported               | Protected                                                 |                           |
| Font\_Style\_Shadow,shadow<br/>                     | VT\_BOOL | Line-height (minus numbers) | Shadow                                                    |                           |
| Font\_Style\_Spacing,spacing<br/>                   | VT\_R4   | Letter-spacing              | Spacing                                                   | In points                 |
| Font\_Style\_Weight,weight<br/>                     | VT\_I4   | Font-weight                 | WeightSame values as font-weight and GetWeight<br/> |                           |
| Font\_Style\_Height,height<br/>                     | VT\_R4   | Line-height                 | Not supported                                             | In points                 |
| Font\_Style\_Blink,blink<br/>                       | VT\_BOOL | Text-decoration: blink      | Not supported                                             |                           |
| Font\_Style\_Subscript,subscript<br/>               | VT\_BOOL | Vertical-align: sub         | Subscript (also Position)                                 |                           |
| Font\_Style\_Superscript,superscript<br/>           | VT\_BOOL | Vertical-align: super       | Superscript (also Position)                               |                           |
| Font\_Style\_Color,color<br/>                       | VT\_I4   | Color                       | ForeColor                                                 | RBG COLORREF style        |
| Font\_Style\_BackgroundColor,background\_color<br/> | VT\_I4   | Background-color            | BackColor                                                 | RBG COLORREF style        |



 

## Font\_Style\_Animation

The attributes in the following table address font animation. The TOM equivalent is the [**ITextFont**](/windows/desktop/api/tom/nn-tom-itextfont) interface.



| Attribute name, Friendly name                                              | Type     | CSS equivalent | TOM equivalent |
|----------------------------------------------------------------------------|----------|----------------|----------------|
| Font\_Style\_Animation\_LasVegasLights,LasVegas\_lights<br/>         | VT\_BOOL | Not supported  | Animation      |
| Font\_Style\_Animation\_BlinkingBackground,blinking\_background<br/> | VT\_BOOL | Not supported  | Animation      |
| Font\_Style\_Animation\_SparkleText,sparkle\_text<br/>               | VT\_BOOL | Not supported  | Animation      |
| Font\_Style\_Animation\_MarchingBlackAnts,marching\_black\_ants<br/> | VT\_BOOL | Not supported  | Animation      |
| Font\_Style\_Animation\_MarchingRedAnts,marching\_red\_ants<br/>     | VT\_BOOL | Not supported  | Animation      |
| Font\_Style\_Animation\_Shimmer,Shimmer<br/>                         | VT\_BOOL | Not supported  | Animation      |
| Font\_Style\_Animation\_WipeDown,wipeDown<br/>                       | VT\_BOOL | Not supported  | Animation      |
| Font\_Style\_Animation\_WipeRight,wipeRight<br/>                     | VT\_BOOL | Not supported  | Animation      |



 

## Font\_Style\_Underline

The attributes in the following table address underline styles for fonts. The TOM equivalent is the [**ITextFont**](/windows/desktop/api/tom/nn-tom-itextfont) interface.



| Attribute name, Friendly name                     | Type     | CSS equivalent                | TOM equivalent |
|---------------------------------------------------|----------|-------------------------------|----------------|
| Font\_Style\_Underline\_Single,single<br/>  | VT\_BOOL | Text-decoration: underline    | Underline      |
| Font\_Style\_Underline\_ Double,double<br/> | VT\_BOOL | Text-decoration: line-through | StrikeThrough  |



 

## Font\_Style\_Strikethrough

The attributes in the following table address strikethrough styles for fonts.



| Attribute name, Friendly name                                         | Type     | CSS equivalent | TOM equivalent |
|-----------------------------------------------------------------------|----------|----------------|----------------|
| Font\_Style\_Strikethrough\_Single,strike\_through\_single<br/> | VT\_BOOL | Not supported  | Not supported  |
| Font\_Style\_Strikethrough\_Double,strike\_through\_double<br/> | VT\_BOOL | Not supported  | Not supported  |



 

## Font\_Style\_Overline

The attributes in the following table address overline styles for fonts.



| Attribute name, Friendly name                             | Type     | CSS equivalent            | TOM equivalent |
|-----------------------------------------------------------|----------|---------------------------|----------------|
| Font\_Style\_Overline\_Single,overline\_single<br/> | VT\_BOOL | Text-decoration: overline | Not supported  |
| Font\_Style\_Overline\_Double,overline\_double<br/> | VT\_BOOL | Text-decoration: overline | Not supported  |



 

## Text

The attributes in the following table address general text formatting attributes.



| Attribute name, Friendly name                     | Type        | CSS equivalent | TOM equivalent                                       | Comment                                                                               |
|---------------------------------------------------|-------------|----------------|------------------------------------------------------|---------------------------------------------------------------------------------------|
| Text\_VerticalWriting,vertical writing<br/> | VT\_BOOL    | Not supported  | not supported                                        | As used by Chinese/Japanese                                                           |
| Text\_RightToLeft,righttoleft<br/>          | VT\_BOOL    | Direction      | Not supported                                        |                                                                                       |
| Text\_ReadOnly,read only<br/>               | VT\_BOOL    | Not supported  | ITextFont::CanChange, ITextRange::CanEdit            | The document's editable property takes precedence                                     |
| Text\_Language,language<br/>                | VT\_I4      | Not supported  | ITextFont::GetLanguageID, ITextFont::SetLanguageID   | LANGID                                                                                |
| Text\_Orientation,orientation<br/>          | VT\_I4      | Not supported  | Not supported                                        | 10??? of a degree                                                                     |
| Text\_EmbeddedObject,embedded\_object<br/>  | VT\_BOOL    | Not supported  | Not supported                                        | Allows searching for embedded objects                                                 |
| Text\_Link,link<br/>                        | VT\_UNKNOWN | Link           | Not supported                                        | An interface pointer to the object; call QueryInterface for any interface of interest |
| Text\_Hyphenation,hyphenation<br/>          | VT\_BOOL    | Not supported  | ITextPara::GetHyphenation, ITextPara::SetHyphenation |                                                                                       |



 

## Text\_Alignment

The attributes in the following table address text alignment. The TOM equivalent is the [**ITextPara**](/windows/desktop/api/tom/nn-tom-itextpara) interface.



| Attribute name, Friendly name               | Type     | CSS equivalent | TOM equivalent |
|---------------------------------------------|----------|----------------|----------------|
| Text\_Alignment\_Left,left<br/>       | VT\_BOOL | Text-align     | Alignment      |
| Text\_Alignment\_Right,right<br/>     | VT\_BOOL | Text-align     | Alignment      |
| Text\_Alignment\_Center,center<br/>   | VT\_BOOL | Text-align     | Alignment      |
| Text\_Alignment\_Justify,justify<br/> | VT\_BOOL | Text-align     | Alignment      |



 

## Text\_Para

The attributes in the following table address formatting for paragraphs. The TOM equivalent is the [**ITextPara**](/windows/desktop/api/tom/nn-tom-itextpara) interface.



| Attribute name, Friendly name                              | Type   | CSS equivalent | TOM equivalent  | Comment |
|------------------------------------------------------------|--------|----------------|-----------------|---------|
| Text\_Para\_FirstLineIndent,first\_line\_indent<br/> | VT\_R4 | Not supported  | FirstLineIndent | In pts  |
| Text\_Para\_LeftIndent,left\_indent<br/>             | VT\_R4 | Not supported  | LeftIndent      | In pts  |
| Text\_Para\_RightIndent,right\_indent<br/>           | VT\_R4 | Not supported  | RightIndent     | In pts  |
| Text\_Para\_SpaceAfter,space\_after<br/>             | VT\_R4 | Not supported  | SpaceAfter      | In pts  |
| Text\_Para\_SpaceBefore,space\_after<br/>            | VT\_R4 | Not supported  | SpaceAfter      | In pts  |



 

## Text\_Para\_lineSpacing

The attributes in the following table address line spacing in paragraphs. The TOM equivalent is the [**ITextPara**](/windows/desktop/api/tom/nn-tom-itextpara) interface.



| Attribute name, Friendly name                               | Type     | CSS equivalent | TOM equivalent | Comment  |
|-------------------------------------------------------------|----------|----------------|----------------|----------|
| Text\_Para\_lineSpacing\_Single,single<br/>           | VT\_BOOL | Not supported  | LineSpacing    |          |
| Text\_Para\_lineSpacing\_OnePtFive,one\_pt\_five<br/> | VT\_BOOL | Not supported  | LineSpacing    |          |
| Text\_Para\_lineSpacing\_Double,double<br/>           | VT\_BOOL | Not supported  | LineSpacing    |          |
| Text\_Para\_lineSpacing\_AtLeast,at\_least<br/>       | VT\_R4   | Not supported  | LineSpacing    | In lines |
| Text\_Para\_lineSpacing\_Exactly,exactly<br/>         | VT\_R4   | Not supported  | LineSpacing    | In lines |
| Text\_Para\_lineSpacing\_Mutiple,multiple<br/>        | VT\_R4   | Not supported  | LineSpacing    | In lines |



 

## Text\_List

The attributes in the following table address lists and levels of text lists. The TOM equivalent is the [**ITextPara**](/windows/desktop/api/tom/nn-tom-itextpara) interface.



| Attribute name, Friendly name | Type   | CSS equivalent | TOM equivalent | Comment                                                       |
|-------------------------------|--------|----------------|----------------|---------------------------------------------------------------|
| Text\_List\_LevelIndex,       | VT\_I4 | Not supported  | ListLevelIndex | Where 1 is the outermost list, 2 is the next level, and so on |



 

## Text\_List\_Type

The attributes in the following table address list styles for text. The TOM equivalent is the [**ITextPara**](/windows/desktop/api/tom/nn-tom-itextpara) interface.



| Attribute name, Friendly name                          | Type     | CSS equivalent  | TOM equivalent |
|--------------------------------------------------------|----------|-----------------|----------------|
| Text\_List\_Type\_Bullet,bullet<br/>             | VT\_BOOL | List-type       | ListType       |
| Text\_List\_Type\_Arabic,Arabic<br/>             | VT\_BOOL | List-style-type | ListType       |
| Text\_List\_Type\_LowerLetter,lower\_letter<br/> | VT\_BOOL | List-style-type | ListType       |
| Text\_List\_Type\_UpperLetter,upper\_letter<br/> | VT\_BOOL | List-style-type | ListType       |
| Text\_List\_Type\_LowerRoman,lower\_roman<br/>   | VT\_BOOL | List-style-type | ListType       |
| Text\_List\_Type\_UpperRoman,upper\_roman<br/>   | VT\_BOOL | List-style-type | ListType       |



 

## App



| Attribute name, Friendly name                         | Type     | CSS equivalent | TOM equivalent |
|-------------------------------------------------------|----------|----------------|----------------|
| App\_IncorrectSpelling,incorrect\_spelling<br/> | VT\_BOOL |                | Not supported  |
| App\_IncorrectGrammar,incorrect\_grammar<br/>   | VT\_BOOL |                | Not supported  |



 

 

