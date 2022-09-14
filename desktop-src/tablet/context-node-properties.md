---
description: Defines globally unique identifiers (GUIDs) for properties of an IContextNode.
ms.assetid: 14992253-c384-43c1-9465-e015ea2348db
title: Context Node Properties (Iaguid.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GUID_CNP_ALIGNMENTLEVEL
- GUID_CNP_ASCENDERS
- GUID_CNP_BASELINE
- GUID_CNP_CONFIDENCELEVEL
- GUID_CNP_CUSTOMRECOGNIZERID
- GUID_CNP_DESCENDERS
- GUID_CNP_MIDLINE
- GUID_CNP_NODEDATA
- GUID_CNP_RECOGNIZEDSTRING
- GUID_CNP_ROTATEDBOUNDINGBOX
- GUID_CNP_SEMANTICTYPE
- GUID_CNP_SHAPENAME
api_type: 
- HeaderDef
api_location: 
- iaguid.h
---

# Context Node Properties

Defines globally unique identifiers (GUIDs) for properties of an [**IContextNode**](icontextnode.md).

The following table describes information referenced by each constant.



| Constant                                                                                                                                                                                                 | Description                                                                                                                                                  |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GUID_CNP_ALIGNMENTLEVEL"></span><span id="guid_cnp_alignmentlevel"></span><dl> <dt>**GUID\_CNP\_ALIGNMENTLEVEL**</dt> </dl>             | The alignment level of a paragraph.<br/>                                                                                                               |
| <span id="GUID_CNP_ASCENDERS"></span><span id="guid_cnp_ascenders"></span><dl> <dt>**GUID\_CNP\_ASCENDERS**</dt> </dl>                            | The ascenders of an ink word.<br/>                                                                                                                     |
| <span id="GUID_CNP_BASELINE"></span><span id="guid_cnp_baseline"></span><dl> <dt>**GUID\_CNP\_BASELINE**</dt> </dl>                               | The baseline of an ink word.<br/>                                                                                                                      |
| <span id="GUID_CNP_CONFIDENCELEVEL"></span><span id="guid_cnp_confidencelevel"></span><dl> <dt>**GUID\_CNP\_CONFIDENCELEVEL**</dt> </dl>          | The confidence level in the recognition results.<br/>                                                                                                  |
| <span id="GUID_CNP_CUSTOMRECOGNIZERID"></span><span id="guid_cnp_customrecognizerid"></span><dl> <dt>**GUID\_CNP\_CUSTOMRECOGNIZERID**</dt> </dl> | The identifier of the custom ink recognizer for a custom recognizer node.<br/>                                                                         |
| <span id="GUID_CNP_DESCENDERS"></span><span id="guid_cnp_descenders"></span><dl> <dt>**GUID\_CNP\_DESCENDERS**</dt> </dl>                         | The descenders of an ink word.<br/>                                                                                                                    |
| <span id="GUID_CNP_MIDLINE"></span><span id="guid_cnp_midline"></span><dl> <dt>**GUID\_CNP\_MIDLINE**</dt> </dl>                                  | The midline of an ink word.<br/>                                                                                                                       |
| <span id="GUID_CNP_NODEDATA"></span><span id="guid_cnp_nodedata"></span><dl> <dt>**GUID\_CNP\_NODEDATA**</dt> </dl>                               | The image data or text data of an image or a text word.<br/>                                                                                           |
| <span id="GUID_CNP_RECOGNIZEDSTRING"></span><span id="guid_cnp_recognizedstring"></span><dl> <dt>**GUID\_CNP\_RECOGNIZEDSTRING**</dt> </dl>       | The recognized string.<br/>                                                                                                                            |
| <span id="GUID_CNP_ROTATEDBOUNDINGBOX"></span><span id="guid_cnp_rotatedboundingbox"></span><dl> <dt>**GUID\_CNP\_ROTATEDBOUNDINGBOX**</dt> </dl> | The rotated bounding box.<br/>                                                                                                                         |
| <span id="GUID_CNP_SEMANTICTYPE"></span><span id="guid_cnp_semantictype"></span><dl> <dt>**GUID\_CNP\_SEMANTICTYPE**</dt> </dl>                   | The property contains information about the semantic types used in defining an annotation, such as whether it is a callout, a comment, and so on.<br/> |
| <span id="GUID_CNP_SHAPENAME"></span><span id="guid_cnp_shapename"></span><dl> <dt>**GUID\_CNP\_SHAPENAME**</dt> </dl>                            | The shape name of an ink drawing node.<br/>                                                                                                            |



## Remarks

These GUIDs are used to identify properties that the [**IInkAnalyzer**](iinkanalyzer.md) can set on an [**IContextNode**](icontextnode.md). The ink analyzer sets some property data based on the context node's type (see [**IContextNode::GetType**](icontextnode-gettype.md)).

To get or set properties specific to analysis hint nodes, see [**Analysis Hint Properties**](analysis-hint-properties.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | None supported<br/>                                                           |
| Header<br/>                   | <dl> <dt>Iaguid.h</dt> </dl> |



## See also

<dl> <dt>

[Analysis Hint Properties](analysis-hint-properties.md)
</dt> <dt>

[Context Node Types](context-node-types.md)
</dt> <dt>

[**IContextNode::ContainsPropertyData**](icontextnode-containspropertydata.md)
</dt> <dt>

[**IContextNode::GetPropertyData**](icontextnode-getpropertydata.md)
</dt> <dt>

[**IContextNode::GetPropertyDataIds**](icontextnode-getpropertydataids.md)
</dt> <dt>

[**IContextNode::LoadPropertiesData**](icontextnode-loadpropertiesdata.md)
</dt> <dt>

[**IContextNode::RemovePropertyData**](icontextnode-removepropertydata.md)
</dt> <dt>

[**IContextNode::SavePropertiesData**](icontextnode-savepropertiesdata.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




