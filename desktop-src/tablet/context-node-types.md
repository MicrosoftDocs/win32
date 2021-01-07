---
description: These constants define values that specify the type of IContextNode objects.
ms.assetid: 333db79e-f503-4545-84fd-7c1a39a96728
title: Context Node Types (Iaguid.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GUID_CNT_ANALYSISHINT
- GUID_CNT_CUSTOMRECOGNIZER
- GUID_CNT_IMAGE
- GUID_CNT_INKBULLET
- GUID_CNT_INKDRAWING
- GUID_CNT_INKWORD
- GUID_CNT_LINE
- GUID_CNT_OBJECT
- GUID_CNT_PARAGRAPH
- GUID_CNT_ROOT
- GUID_CNT_TEXTWORD
- GUID_CNT_UNCLASSIFIEDINKNODE
api_type: 
- HeaderDef
api_location: 
- iaguid.h
---

# Context Node Types

These constants define values that specify the type of [**IContextNode**](icontextnode.md) objects.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant/value</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="GUID_CNT_ANALYSISHINT"></span><span id="guid_cnt_analysishint"></span><dl> <dt><strong>GUID_CNT_ANALYSISHINT</strong></dt> <dt>(AnalysisHint)</dt> </dl></td>
<td style="text-align: left;">Represents a node that contains additional context information for a region that the <a href="iinkanalyzer.md"><strong>IInkAnalyzer</strong></a> uses to improve its analysis.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="GUID_CNT_CUSTOMRECOGNIZER"></span><span id="guid_cnt_customrecognizer"></span><dl> <dt><strong>GUID_CNT_CUSTOMRECOGNIZER</strong></dt> <dt>(CustomRecognizer)</dt> </dl></td>
<td style="text-align: left;">Represents a node used for a single recognition operation.<br/> All strokes and nodes that are within a custom recognizer node are recognized by an independent recognition operation and are not analyzed by the <a href="iinkanalyzer.md"><strong>IInkAnalyzer</strong></a>.<br/> A custom recognizer node must be the direct child of ink analyzer's root node.<br/> A custom recognizer node can contain the following types of child elements:<br/>
<ul>
<li>Any number of UnclassifiedInk nodes.</li>
<li>Any number of Object nodes.</li>
<li>Any number of Line nodes.</li>
<li>Any number of InkWord nodes.</li>
<li>Any number of nodes with an unknown Guid value.</li>
</ul></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="GUID_CNT_IMAGE"></span><span id="guid_cnt_image"></span><dl> <dt><strong>GUID_CNT_IMAGE</strong></dt> <dt>(Image)</dt> </dl></td>
<td style="text-align: left;">Represents a node for a two-dimensional region where any non-ink images can exist in the document.<br/> The <a href="iinkanalyzer.md"><strong>IInkAnalyzer</strong></a> does not produce image nodes. Use <a href="icontextnode-createsubnode.md"><strong>IContextNode::CreateSubNode</strong></a> to add an image node to the context node tree. The <strong>IInkAnalyzer</strong> then uses the regions defined by the image node to determine if any ink annotates the non-ink image.<br/> An image node cannot have any child elements.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="GUID_CNT_INKBULLET"></span><span id="guid_cnt_inkbullet"></span><dl> <dt><strong>GUID_CNT_INKBULLET</strong></dt> <dt>(InkBullet)</dt> </dl></td>
<td style="text-align: left;">The InkBullet ContextNodeType represents a collection of strokes that make up a bullet in a bulleted list.<br/> A ContextNode of type InkBullet cannot have any children. It can only be a child of a Paragraph ContextNode. Only one InkBullet can appear in a single Paragraph ContextNode.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="GUID_CNT_INKDRAWING"></span><span id="guid_cnt_inkdrawing"></span><dl> <dt><strong>GUID_CNT_INKDRAWING</strong></dt> <dt>(InkDrawing)</dt> </dl></td>
<td style="text-align: left;">Represents a node for a collection of strokes that constitutes a drawing.<br/> Drawings are strokes that are determined to be shapes or abstract sketches. They are generally any strokes that are not classified as writing strokes.<br/> An ink drawing node cannot have any child elements.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="GUID_CNT_INKWORD"></span><span id="guid_cnt_inkword"></span><dl> <dt><strong>GUID_CNT_INKWORD</strong></dt> <dt>(InkWord)</dt> </dl></td>
<td style="text-align: left;">Represents a node for a collection of strokes that constitutes a logical grouping to form a recognizable word.<br/> An ink word node cannot contain any child elements.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="GUID_CNT_LINE"></span><span id="guid_cnt_line"></span><dl> <dt><strong>GUID_CNT_LINE</strong></dt> <dt>(Line)</dt> </dl></td>
<td style="text-align: left;">Represents a node for a line of words.<br/> A line node can contain the following types of child elements:<br/>
<ul>
<li>Any number of ink word nodes.</li>
<li>Any number of text word nodes.</li>
<li>Any number of nodes with an unknown <strong>GUID</strong> value.</li>
</ul></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="GUID_CNT_OBJECT"></span><span id="guid_cnt_object"></span><dl> <dt><strong>GUID_CNT_OBJECT</strong></dt> <dt>(Object)</dt> </dl></td>
<td style="text-align: left;">Represents a node for an object that is returned from an &quot;object&quot; custom recognizer.<br/> An object node cannot contain any child elements.<br/> Only custom recognizer nodes can contain object nodes.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="GUID_CNT_PARAGRAPH"></span><span id="guid_cnt_paragraph"></span><dl> <dt><strong>GUID_CNT_PARAGRAPH</strong></dt> <dt>(Paragraph)</dt> </dl></td>
<td style="text-align: left;">Represents a node for a collection of nodes that constitutes a logical grouping of lines.<br/> The exact definition of a paragraph is determined by the analyzing engines. In general, a paragraph contains groups of lines that would reflow together if the box that contains the lines were resized.<br/> A paragraph node can contain the following types of child elements:<br/>
<ul>
<li>Any number of ink bullet nodes.</li>
<li>Any number of line nodes.</li>
<li>Any number of nodes with an unknown <strong>GUID</strong> value.</li>
</ul></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="GUID_CNT_ROOT"></span><span id="guid_cnt_root"></span><dl> <dt><strong>GUID_CNT_ROOT</strong></dt> <dt>(Root)</dt> </dl></td>
<td style="text-align: left;">Represents a node for the top node of a tree of nodes that describe the results of ink analysis.<br/> Root nodes are generally obtained from the <a href="iinkanalyzer-getrootnode.md"><strong>IInkAnalyzer::GetRootNode Method</strong></a> method.<br/> A root node can contain the following types of child elements:<br/>
<ul>
<li>Any number of analysis hint nodes.</li>
<li>Any number of custom recognizer nodes.</li>
<li>Any number of image nodes.</li>
<li>Any number of ink drawing nodes.</li>
<li>Any number of writing region nodes.</li>
<li>Any number of unclassified ink nodes.</li>
<li>Any number of nodes with an unknown <strong>GUID</strong> value.</li>
</ul></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="GUID_CNT_TEXTWORD"></span><span id="guid_cnt_textword"></span><dl> <dt><strong>GUID_CNT_TEXTWORD</strong></dt> <dt>(TextWord)</dt> </dl></td>
<td style="text-align: left;">Represents a node for the two-dimensional region where any non-ink text can exist in the document.<br/> The <a href="iinkanalyzer.md"><strong>IInkAnalyzer</strong></a> does not produce text word nodes. Use <a href="icontextnode-createsubnode.md"><strong>IContextNode::CreateSubNode</strong></a> to add a text word node to the context node tree. The <strong>IInkAnalyzer</strong> then uses the regions defined by the text word node to determine if any ink annotates the non-ink text.<br/> Future recognizers may use the region defined by a text word node to determine if any ink annotates the non-ink word.<br/> A text word node cannot have any child elements<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="GUID_CNT_UNCLASSIFIEDINKNODE"></span><span id="guid_cnt_unclassifiedinknode"></span><dl> <dt><strong>GUID_CNT_UNCLASSIFIEDINKNODE</strong></dt> <dt>(UnclassifiedInk)</dt> </dl></td>
<td style="text-align: left;">Represents a node for any strokes that have not yet been classified or recognized.<br/> An unclassified ink node cannot have any child elements.<br/></td>
</tr>
</tbody>
</table>



## Remarks

For more information about the different context node types, see [Ink Analysis Overview](ink-analysis-overview.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | None supported<br/>                                                           |
| Header<br/>                   | <dl> <dt>Iaguid.h</dt> </dl> |



## See also

<dl> <dt>

[**IContextNode::CreatePartiallyPopulatedSubNode**](icontextnode-createpartiallypopulatedsubnode.md)
</dt> <dt>

[**IContextNode::CreateSubNode**](icontextnode-createsubnode.md)
</dt> <dt>

[**IContextNode::GetType**](icontextnode-gettype.md)
</dt> <dt>

[**IInkAnalyzer::CreateAnalysisHint Method**](iinkanalyzer-createanalysishint.md)
</dt> <dt>

[**IInkAnalyzer::CreateCustomRecognizer Method**](iinkanalyzer-createcustomrecognizer.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesOfType Method**](iinkanalyzer-findnodesoftype.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesOfTypeForStrokes Method**](iinkanalyzer-findnodesoftypeforstrokes.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesOfTypeInSubTree Method**](iinkanalyzer-findnodesoftypeinsubtree.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




