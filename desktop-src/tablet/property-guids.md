---
Description: 'The Microsoft recognizers use the following GUIDs.'
ms.assetid: 'a7488c26-b61f-47d8-a19b-d630a8c00875'
title: Property GUIDs
---

# Property GUIDs

The Microsoft recognizers use the following GUIDs. Whenever possible, applications should use these GUIDs. However, it is expected and encouraged that other recognizers will use additional GUIDs for properties that are not supported by the Microsoft recognizers.

All property functions have been developed with the understanding that the list of GUIDs may be extended by other recognizers. These property functions include:

-   [**GetContextPropertyList Function**](getcontextpropertylist.md)
-   [**GetContextPropertyValue Function**](getcontextpropertyvalue.md)
-   [**GetResultPropertyList Function**](getresultpropertylist.md)
-   [**SetContextPropertyValue Function**](setcontextpropertyvalue.md)

The following table lists Tablet PC property GUIDs defined in msinkaut.h (installed in c:\\Program Files\\Microsoft Tablet PC Platform SDK\\Include by default).



| GUID                                                  | Definition                                                                                   |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------|
| INKRECOGNITIONPROPERTY\_BOXNUMBER<br/>          | The recognizer alternate box index in box mode<br/>                                    |
| INKRECOGNITIONPROPERTY\_LINENUMBER<br/>         | The line number<br/>                                                                   |
| INKRECOGNITIONPROPERTY\_SEGMENTATION<br/>       | How the recognizer segments words and characters<br/>                                  |
| INKRECOGNITIONPROPERTY\_HOTPOINT<br/>           | The gesture hot point<br/>                                                             |
| INKRECOGNITIONPROPERTY\_MAXIMUMSTROKECOUNT<br/> | Maximum number of strokes for a segment<br/>                                           |
| INKRECOGNITIONPROPERTY\_POINTSPERINCH<br/>      | The points-per-inch metric<br/>                                                        |
| INKRECOGNITIONPROPERTY\_CONFIDENCELEVEL<br/>    | [**CONFIDENCE\_LEVEL**](confidence-level.md) enumeration<br/>                         |
| INKRECOGNITIONPROPERTY\_LINEMETRICS<br/>        | Information for computing baseline, midline, or both, that is used in the lattice<br/> |



 

 

 




