---
description: Defines globally unique identifiers (GUIDs) for properties of an analysis hint node (see IContextNode::GetType).
ms.assetid: 8300c792-a741-49de-a03b-f4840ea5d647
title: Analysis Hint Properties (Iaguid.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GUID_AHP_ALLOWPARTIALDICTIONARYTERMS
- GUID_AHP_ANALYSISHINTNAME
- GUID_AHP_COERCETOFACTOID
- GUID_AHP_ENABLEDUNICODECHARACTERRANGES
- GUID_AHP_FACTOID
- GUID_AHP_GUIDE
- GUID_AHP_PREFIXTEXT
- GUID_AHP_SUFFIXTEXT
- GUID_AHP_TOPINKBREAKSONLY
- GUID_AHP_WORDLIST
- GUID_AHP_WORDMODE
api_type: 
- HeaderDef
api_location: 
- iaguid.h
---

# Analysis Hint Properties

Defines globally unique identifiers (GUIDs) for properties of an analysis hint node (see [**IContextNode::GetType**](icontextnode-gettype.md)).

The following table describes information referenced by each constant.



| Constant                                                                                                                                                                                                                                  | Description                                                                                                                                               |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GUID_AHP_ALLOWPARTIALDICTIONARYTERMS"></span><span id="guid_ahp_allowpartialdictionaryterms"></span><dl> <dt>**GUID\_AHP\_ALLOWPARTIALDICTIONARYTERMS**</dt> </dl>       | Whether partial dictionary terms are allowed on an analysis hint.<br/>                                                                              |
| <span id="GUID_AHP_ANALYSISHINTNAME"></span><span id="guid_ahp_analysishintname"></span><dl> <dt>**GUID\_AHP\_ANALYSISHINTNAME**</dt> </dl>                                        | The name of an analysis hint.<br/>                                                                                                                  |
| <span id="GUID_AHP_COERCETOFACTOID"></span><span id="guid_ahp_coercetofactoid"></span><dl> <dt>**GUID\_AHP\_COERCETOFACTOID**</dt> </dl>                                           | Whether the ink analyzer limits its analysis of ink within the hint's area to conform to the factoid.<br/>                                          |
| <span id="GUID_AHP_ENABLEDUNICODECHARACTERRANGES"></span><span id="guid_ahp_enabledunicodecharacterranges"></span><dl> <dt>**GUID\_AHP\_ENABLEDUNICODECHARACTERRANGES**</dt> </dl> | The hint contains an array of characters that represent the restricted set of supported unicode character set supported by this InkRecognizer.<br/> |
| <span id="GUID_AHP_FACTOID"></span><span id="guid_ahp_factoid"></span><dl> <dt>**GUID\_AHP\_FACTOID**</dt> </dl>                                                                   | The factoid on an analysis hint.<br/>                                                                                                               |
| <span id="GUID_AHP_GUIDE"></span><span id="guid_ahp_guide"></span><dl> <dt>**GUID\_AHP\_GUIDE**</dt> </dl>                                                                         | The [**InkAnalysisRecognizerGuide**](inkanalysisrecognizerguide.md) structure that represents the guide for an analysis hint.<br/>                 |
| <span id="GUID_AHP_PREFIXTEXT"></span><span id="guid_ahp_prefixtext"></span><dl> <dt>**GUID\_AHP\_PREFIXTEXT**</dt> </dl>                                                          | The prefix text on an analysis hint.<br/>                                                                                                           |
| <span id="GUID_AHP_SUFFIXTEXT"></span><span id="guid_ahp_suffixtext"></span><dl> <dt>**GUID\_AHP\_SUFFIXTEXT**</dt> </dl>                                                          | The suffix text on an analysis hint.<br/>                                                                                                           |
| <span id="GUID_AHP_TOPINKBREAKSONLY"></span><span id="guid_ahp_topinkbreaksonly"></span><dl> <dt>**GUID\_AHP\_TOPINKBREAKSONLY**</dt> </dl>                                        | Whether the multiple segmentations in the ink recognition results are disabled.<br/>                                                                |
| <span id="GUID_AHP_WORDLIST"></span><span id="guid_ahp_wordlist"></span><dl> <dt>**GUID\_AHP\_WORDLIST**</dt> </dl>                                                                | The array of strings that represents the word list for an analysis hint.<br/>                                                                       |
| <span id="GUID_AHP_WORDMODE"></span><span id="guid_ahp_wordmode"></span><dl> <dt>**GUID\_AHP\_WORDMODE**</dt> </dl>                                                                | Whether the ink analyzer prioritizes single-word results over multiple-word results for an analysis hint.<br/>                                      |



## Remarks

These GUIDs are used to identify properties that the [**IInkAnalyzer**](iinkanalyzer.md) can set on an analysis hint context node (see [**IContextNode::GetType**](icontextnode-gettype.md)).

To get or set properties of an [**IContextNode**](icontextnode.md) in general, see [Context Node Properties](context-node-properties.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | None supported<br/>                                                           |
| Header<br/>                   | <dl> <dt>Iaguid.h</dt> </dl> |



## See also

<dl> <dt>

[Context Node Properties](context-node-properties.md)
</dt> <dt>

[Context Node Types](context-node-types.md)
</dt> <dt>

[**IInkAnalyzer::CreateAnalysisHint Method**](iinkanalyzer-createanalysishint.md)
</dt> <dt>

[**IInkAnalyzer::GetAnalysisHintsByName Method**](iinkanalyzer-getanalysishintsbyname.md)
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

 

 




