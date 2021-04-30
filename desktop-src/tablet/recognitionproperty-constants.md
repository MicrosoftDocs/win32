---
description: Defines values that specify the properties of a recognition alternate. The Tablet PC application programming interface (API) uses globally unique identifiers (GUIDs) to identify packet properties, which in Automation are constant strings.
ms.assetid: 2bfb0cbf-73a3-4e83-a4e9-f0803bd3dee8
title: RecognitionProperty Constants (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# RecognitionProperty Constants

Defines values that specify the properties of a recognition alternate. The Tablet PC application programming interface (API) uses globally unique identifiers (GUIDs) to identify packet properties, which in Automation are constant strings.

The following table lists the available recognition alternate property globally unique identifier (GUID) fields. Use these GUIDs to access properties of an [**IInkRecognitionAlternate**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionalternate) object by calling the [**GetPropertyValue**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognitionalternate-getpropertyvalue) method.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant Name</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="___________INKRECOGNITIONPROPERTY_LINENUMBER_________"></span><span id="___________inkrecognitionproperty_linenumber_________"></span><dl> <dt> <strong>INKRECOGNITIONPROPERTY_LINENUMBER</strong> </dt> </dl></td>
<td style="text-align: left;">The GUID that identifies the property for the line number of the <a href="/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionalternate"><strong>IInkRecognitionAlternate</strong></a> object. <br/> LineNumber specifies the alternates with a particular line number.<br/>
<blockquote>
[!Note]<br />
This field is not supported for recognizers of East Asian characters.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________INKRECOGNITIONPROPERTY_SEGMENTATION_________"></span><span id="___________inkrecognitionproperty_segmentation_________"></span><dl> <dt> <strong>INKRECOGNITIONPROPERTY_SEGMENTATION</strong> </dt> </dl></td>
<td style="text-align: left;">The GUID that identifies the property for the segmentation of the <a href="/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionalternate"><strong>IInkRecognitionAlternate</strong></a> object. <br/> Segmentation specifies the basic ink fragment or unit that the recognizer uses to produce a recognition result.<br/>
<blockquote>
[!Note]<br />
Not implemented.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________INKRECOGNITIONPROPERTY_HOTPOINT_________"></span><span id="___________inkrecognitionproperty_hotpoint_________"></span><dl> <dt> <strong>INKRECOGNITIONPROPERTY_HOTPOINT</strong> </dt> </dl></td>
<td style="text-align: left;">The GUID that identifies the property for the recognition hot point of the <a href="/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionalternate"><strong>IInkRecognitionAlternate</strong></a> object. <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________INKRECOGNITIONPROPERTY_MAXIMUMSTROKECOUNT_________"></span><span id="___________inkrecognitionproperty_maximumstrokecount_________"></span><dl> <dt> <strong>INKRECOGNITIONPROPERTY_MAXIMUMSTROKECOUNT</strong> </dt> </dl></td>
<td style="text-align: left;">The GUID that identifies the property for the maximum stroke count of the recognition result for the <a href="/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionalternate"><strong>IInkRecognitionAlternate</strong></a> object. <br/>
<blockquote>
[!Note]<br />
Not implemented.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________INKRECOGNITIONPROPERTY_POINTSPERINCH_________"></span><span id="___________inkrecognitionproperty_pointsperinch_________"></span><dl> <dt> <strong>INKRECOGNITIONPROPERTY_POINTSPERINCH</strong> </dt> </dl></td>
<td style="text-align: left;">The GUID that identifies the property for the points-per-inch metric of the <a href="/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionalternate"><strong>IInkRecognitionAlternate</strong></a> object. <br/>
<blockquote>
[!Note]<br />
Not implemented.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________INKRECOGNITIONPROPERTY_CONFIDENCELEVEL_________"></span><span id="___________inkrecognitionproperty_confidencelevel_________"></span><dl> <dt> <strong>INKRECOGNITIONPROPERTY_CONFIDENCELEVEL</strong> </dt> </dl></td>
<td style="text-align: left;">The GUID that identifies the property for the level of confidence that the recognizer has in the recognition result.<br/>
<blockquote>
[!Note]<br />
Confidence evaluation is available only for United States English and all gesture recognizers in Microsoft Windows XP Tablet PC Edition and Windows Vista. Methods that provide the confidence property for any other recognizer return E_NOTIMPL.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________INKRECOGNITIONPROPERTY_LINEMETRICS_________"></span><span id="___________inkrecognitionproperty_linemetrics_________"></span><dl> <dt> <strong>INKRECOGNITIONPROPERTY_LINEMETRICS</strong> </dt> </dl></td>
<td style="text-align: left;">The GUID that identifies the property for the line metrics of the <a href="/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionalternate"><strong>IInkRecognitionAlternate</strong></a> object, which is the line for which to retrieve metrics. <br/></td>
</tr>
</tbody>
</table>



## Remarks

In C++, you can access these constants in the Msinkaut.h header file, which is located in the <systemdrive>:\\Program Files\\Microsoft SDKs\\Windows\\v6.0\\Include directory if you installed the SDK in the default location.

> [!Note]  
> In C++, these constants are WCHARs, not BSTRs. Convert them into BSTRs before use. For more information about the BSTR data type, see [Using the COM Library](using-the-com-library.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |



## See also

<dl> <dt>

[**AlternatesWithConstantPropertyValues Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognitionalternate-alternateswithconstantpropertyvalues)
</dt> <dt>

[**ConfidenceAlternates Property**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognitionalternate-get_confidencealternates)
</dt> <dt>

[**LineAlternates Property**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognitionalternate-get_linealternates)
</dt> <dt>

[**IInkRecognitionAlternates Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionalternates)
</dt> </dl>

 

 




