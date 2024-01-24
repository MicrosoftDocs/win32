---
description: When implementing your own Microsoft gesture recognizer, you must define the name and Unicode range value for any gesture that your recognizer is to recognize.If you decide to implement the gestures that are already supported or defined as part of the Microsoft gesture recognizer, use the defined names and Unicode range values for these gestures. The entire collection of names and Unicode range values for both implemented and unimplemented gestures in the Microsoft gesture recognizer are provided in the Recdefs.h header file (installed by default in C:\\Program Files\\Microsoft Tablet PC Platform SDK\\Include). The gesture names and Unicode range values are also listed in the following tables.Note  The GESTURE\_NULL gesture is used to indicate that a recognizer does not recognize input as a gesture.
ms.assetid: 931fc69a-1f7a-492c-8158-0691cd2fe57a
title: Unicode Range Values of Gestures
ms.topic: article
ms.date: 05/31/2018
---

# Unicode Range Values of Gestures

When implementing your own Microsoft gesture recognizer, you must define the name and Unicode range value for any gesture that your recognizer is to recognize.

If you decide to implement the gestures that are already supported or defined as part of the Microsoft gesture recognizer, use the defined names and Unicode range values for these gestures. The entire collection of names and Unicode range values for both implemented and unimplemented gestures in the Microsoft gesture recognizer are provided in the Recdefs.h header file (installed by default in C:\\Program Files\\Microsoft Tablet PC Platform SDK\\Include). The gesture names and Unicode range values are also listed in the following tables.

> [!Note]  
> The GESTURE\_NULL gesture is used to indicate that a recognizer does not recognize input as a gesture.

 

## Implemented Gestures



| Gesture name                          | Unicode range value |
|---------------------------------------|---------------------|
| GESTURE\_NULL<br/>              | 0xf000<br/>   |
| GESTURE\_SCRATCHOUT<br/>        | 0xf001<br/>   |
| GESTURE\_TRIANGLE<br/>          | 0xf002<br/>   |
| GESTURE\_SQUARE<br/>            | 0xf003<br/>   |
| GESTURE\_STAR<br/>              | 0xf004<br/>   |
| GESTURE\_CHECK<br/>             | 0xf005<br/>   |
| GESTURE\_CURLICUE<br/>          | 0xf010<br/>   |
| GESTURE\_DOUBLE\_CURLICUE<br/>  | 0xf011<br/>   |
| GESTURE\_CIRCLE<br/>            | 0xf020<br/>   |
| GESTURE\_DOUBLE\_CIRCLE<br/>    | 0xf021<br/>   |
| GESTURE\_SEMICIRCLE\_LEFT<br/>  | 0xf028<br/>   |
| GESTURE\_SEMICIRCLE\_RIGHT<br/> | 0xf029<br/>   |
| GESTURE\_CHEVRON\_UP<br/>       | 0xf030<br/>   |
| GESTURE\_CHEVRON\_DOWN<br/>     | 0xf031<br/>   |
| GESTURE\_CHEVRON\_LEFT<br/>     | 0xf032<br/>   |
| GESTURE\_CHEVRON\_RIGHT<br/>    | 0xf033<br/>   |
| GESTURE\_ARROW\_UP<br/>         | 0xf038<br/>   |
| GESTURE\_ARROW\_DOWN<br/>       | 0xf039<br/>   |
| GESTURE\_ARROW\_LEFT<br/>       | 0xf03a<br/>   |
| GESTURE\_ARROW\_RIGHT<br/>      | 0xf03b<br/>   |
| GESTURE\_UP<br/>                | 0xf058<br/>   |
| GESTURE\_DOWN<br/>              | 0xf059<br/>   |
| GESTURE\_LEFT<br/>              | 0xf05a<br/>   |
| GESTURE\_RIGHT<br/>             | 0xf05b<br/>   |
| GESTURE\_UP\_DOWN<br/>          | 0xf060<br/>   |
| GESTURE\_DOWN\_UP<br/>          | 0xf061<br/>   |
| GESTURE\_LEFT\_RIGHT<br/>       | 0xf062<br/>   |
| GESTURE\_RIGHT\_LEFT<br/>       | 0xf063<br/>   |
| GESTURE\_UP\_LEFT\_LONG<br/>    | 0xf064<br/>   |
| GESTURE\_UP\_RIGHT\_LONG<br/>   | 0xf065<br/>   |
| GESTURE\_DOWN\_LEFT\_LONG<br/>  | 0xf066<br/>   |
| GESTURE\_DOWN\_RIGHT\_LONG<br/> | 0xf067<br/>   |
| GESTURE\_UP\_LEFT<br/>          | 0xf068<br/>   |
| GESTURE\_UP\_RIGHT<br/>         | 0xf069<br/>   |
| GESTURE\_DOWN\_LEFT<br/>        | 0xf06a<br/>   |
| GESTURE\_DOWN\_RIGHT<br/>       | 0xf06b<br/>   |
| GESTURE\_LEFT\_UP<br/>          | 0xf06c<br/>   |
| GESTURE\_LEFT\_DOWN<br/>        | 0xf06d<br/>   |
| GESTURE\_RIGHT\_UP<br/>         | 0xf06e<br/>   |
| GESTURE\_RIGHT\_DOWN<br/>       | 0xf06f<br/>   |
| GESTURE\_EXCLAMATION<br/>       | 0xf0a4<br/>   |
| GESTURE\_TAP<br/>               | 0xf0f0<br/>   |
| GESTURE\_DOUBLE\_TAP<br/>       | 0xf0f1<br/>   |



 

## Unimplemented Gestures



| Gesture name                             | Unicode range value |
|------------------------------------------|---------------------|
| GESTURE\_INFINITY<br/>             | 0xf006<br/>   |
| GESTURE\_CROSS<br/>                | 0xf007<br/>   |
| GESTURE\_PARAGRAPH<br/>            | 0xf008<br/>   |
| GESTURE\_SECTION<br/>              | 0xf009<br/>   |
| GESTURE\_BULLET<br/>               | 0xf00a<br/>   |
| GESTURE\_BULLET\_CROSS<br/>        | 0xf00b<br/>   |
| GESTURE\_SQUIGGLE<br/>             | 0xf00c<br/>   |
| GESTURE\_SWAP<br/>                 | 0xf00d<br/>   |
| GESTURE\_OPENUP<br/>               | 0xf00e<br/>   |
| GESTURE\_CLOSEUP<br/>              | 0xf00f<br/>   |
| GESTURE\_RECTANGLE<br/>            | 0xf012<br/>   |
| GESTURE\_CIRCLE\_TAP<br/>          | 0xf022<br/>   |
| GESTURE\_CIRCLE\_CIRCLE<br/>       | 0xf023<br/>   |
| GESTURE\_CIRCLE\_CROSS<br/>        | 0xf025<br/>   |
| GESTURE\_CIRCLE\_LINE\_VERT<br/>   | 0xf026<br/>   |
| GESTURE\_CIRCLE\_LINE\_HORZ<br/>   | 0xf027<br/>   |
| GESTURE\_DOUBLE\_ARROW\_UP<br/>    | 0xf03c<br/>   |
| GESTURE\_DOUBLE\_ARROW\_DOWN<br/>  | 0xf03d<br/>   |
| GESTURE\_DOUBLE\_ARROW\_LEFT<br/>  | 0xf03e<br/>   |
| GESTURE\_DOUBLE\_ARROW\_RIGHT<br/> | 0xf03f<br/>   |
| GESTURE\_UP\_ARROW\_LEFT<br/>      | 0xf040<br/>   |
| GESTURE\_UP\_ARROW\_RIGHT<br/>     | 0xf041<br/>   |
| GESTURE\_DOWN\_ARROW\_LEFT<br/>    | 0xf042<br/>   |
| GESTURE\_DOWN\_ARROW\_RIGHT<br/>   | 0xf043<br/>   |
| GESTURE\_LEFT\_ARROW\_UP<br/>      | 0xf044<br/>   |
| GESTURE\_LEFT\_ARROW\_DOWN<br/>    | 0xf045<br/>   |
| GESTURE\_RIGHT\_ARROW\_UP<br/>     | 0xf046<br/>   |
| GESTURE\_RIGHT\_ARROW\_DOWN<br/>   | 0xf047<br/>   |
| GESTURE\_DIAGONAL\_LEFTUP<br/>     | 0xf05c<br/>   |
| GESTURE\_DIAGONAL\_RIGHTUP<br/>    | 0xf05d<br/>   |
| GESTURE\_DIAGONAL\_LEFTDOWN<br/>   | 0xf05e<br/>   |
| GESTURE\_DIAGONAL\_RIGHTDOWN<br/>  | 0xf05f<br/>   |
| GESTURE\_LETTER\_A<br/>            | 0xf080<br/>   |
| GESTURE\_LETTER\_B<br/>            | 0xf081<br/>   |
| GESTURE\_LETTER\_C<br/>            | 0xf082<br/>   |
| GESTURE\_LETTER\_D<br/>            | 0xf083<br/>   |
| GESTURE\_LETTER\_E<br/>            | 0xf084<br/>   |
| GESTURE\_LETTER\_F<br/>            | 0xf085<br/>   |
| GESTURE\_LETTER\_G<br/>            | 0xf086<br/>   |
| GESTURE\_LETTER\_H<br/>            | 0xf087<br/>   |
| GESTURE\_LETTER\_I<br/>            | 0xf088<br/>   |
| GESTURE\_LETTER\_J<br/>            | 0xf089<br/>   |
| GESTURE\_LETTER\_K<br/>            | 0xf08a<br/>   |
| GESTURE\_LETTER\_L<br/>            | 0xf08b<br/>   |
| GESTURE\_LETTER\_M<br/>            | 0xf08c<br/>   |
| GESTURE\_LETTER\_N<br/>            | 0xf08d<br/>   |
| GESTURE\_LETTER\_O<br/>            | 0xf08e<br/>   |
| GESTURE\_LETTER\_P<br/>            | 0xf08f<br/>   |
| GESTURE\_LETTER\_Q<br/>            | 0xf090<br/>   |
| GESTURE\_LETTER\_R<br/>            | 0xf091<br/>   |
| GESTURE\_LETTER\_S<br/>            | 0xf092<br/>   |
| GESTURE\_LETTER\_T<br/>            | 0xf093<br/>   |
| GESTURE\_LETTER\_U<br/>            | 0xf094<br/>   |
| GESTURE\_LETTER\_V<br/>            | 0xf095<br/>   |
| GESTURE\_LETTER\_W<br/>            | 0xf096<br/>   |
| GESTURE\_LETTER\_X<br/>            | 0xf097<br/>   |
| GESTURE\_LETTER\_Y<br/>            | 0xf098<br/>   |
| GESTURE\_LETTER\_Z<br/>            | 0xf099<br/>   |
| GESTURE\_DIGIT\_0<br/>             | 0xf09a<br/>   |
| GESTURE\_DIGIT\_1<br/>             | 0xf09b<br/>   |
| GESTURE\_DIGIT\_2<br/>             | 0xf09c<br/>   |
| GESTURE\_DIGIT\_3<br/>             | 0xf09d<br/>   |
| GESTURE\_DIGIT\_4<br/>             | 0xf09e<br/>   |
| GESTURE\_DIGIT\_5<br/>             | 0xf09f<br/>   |
| GESTURE\_DIGIT\_6<br/>             | 0xf0a0<br/>   |
| GESTURE\_DIGIT\_7<br/>             | 0xf0a1<br/>   |
| GESTURE\_DIGIT\_8<br/>             | 0xf0a2<br/>   |
| GESTURE\_DIGIT\_9<br/>             | 0xf0a3<br/>   |
| GESTURE\_QUESTION<br/>             | 0xf0a5<br/>   |
| GESTURE\_SHARP<br/>                | 0xf0a6<br/>   |
| GESTURE\_DOLLAR<br/>               | 0xf0a7<br/>   |
| GESTURE\_ASTERISK<br/>             | 0xf0a8<br/>   |
| GESTURE\_PLUS<br/>                 | 0xf0a9<br/>   |
| GESTURE\_DOUBLE\_UP<br/>           | 0xf0b8<br/>   |
| GESTURE\_DOUBLE\_DOWN<br/>         | 0xf0b9<br/>   |
| GESTURE\_DOUBLE\_LEFT<br/>         | 0xf0ba<br/>   |
| GESTURE\_DOUBLE\_RIGHT<br/>        | 0xf0bb<br/>   |
| GESTURE\_TRIPLE\_UP<br/>           | 0xf0bc<br/>   |
| GESTURE\_TRIPLE\_DOWN<br/>         | 0xf0bd<br/>   |
| GESTURE\_TRIPLE\_LEFT<br/>         | 0xf0be<br/>   |
| GESTURE\_TRIPLE\_RIGHT<br/>        | 0xf0bf<br/>   |
| GESTURE\_BRACKET\_OVER<br/>        | 0xf0e4<br/>   |
| GESTURE\_BRACKET\_UNDER<br/>       | 0xf0e5<br/>   |
| GESTURE\_BRACKET\_LEFT<br/>        | 0xf0e6<br/>   |
| GESTURE\_BRACKET\_RIGHT<br/>       | 0xf0e7<br/>   |
| GESTURE\_BRACE\_OVER<br/>          | 0xf0e8<br/>   |
| GESTURE\_BRACE\_UNDER<br/>         | 0xf0e9<br/>   |
| GESTURE\_BRACE\_LEFT<br/>          | 0xf0ea<br/>   |
| GESTURE\_BRACE\_RIGHT<br/>         | 0xf0eb<br/>   |
| GESTURE\_TRIPLE\_TAP<br/>          | 0xf0f2<br/>   |
| GESTURE\_QUAD\_TAP<br/>            | 0xf0f3<br/>   |



 

 

 




