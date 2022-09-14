---
description: Adds stroke data for a single stroke to a custom recognizer node.
ms.assetid: ab43c9f8-15fe-49db-b9d1-57d34b95d99f
title: IInkAnalyzer::AddStrokeToCustomRecognizer method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.AddStrokeToCustomRecognizer
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::AddStrokeToCustomRecognizer method

Adds stroke data for a single stroke to a custom recognizer node.

## Syntax


```C++
HRESULT AddStrokeToCustomRecognizer(
  [in]  ULONG        ulStrokeId,
  [in]  ULONG        ulStrokePacketDataCount,
  [in]  LONG         *plStrokePacketData,
  [in]  ULONG        ulStrokePacketDescriptionCount,
  [in]  GUID         *pStrokePacketDescriptionGuids,
  [in]  IContextNode *pCustomRecognizer,
  [out] IContextNode **ppContextNodeStrokeAddedTo
);
```



## Parameters

<dl> <dt>

*ulStrokeId* \[in\]
</dt> <dd>

The identifier for the stroke to add.

</dd> <dt>

*ulStrokePacketDataCount* \[in\]
</dt> <dd>

The number of packets in the stroke.

</dd> <dt>

*plStrokePacketData* \[in\]
</dt> <dd>

An array containing the packet data for the stroke.

</dd> <dt>

*ulStrokePacketDescriptionCount* \[in\]
</dt> <dd>

The number of packet properties in each packet.

</dd> <dt>

*pStrokePacketDescriptionGuids* \[in\]
</dt> <dd>

An array containing the packet property identifiers.

</dd> <dt>

*pCustomRecognizer* \[in\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) of type **CustomRecognizer** to which to add the stroke.

</dd> <dt>

*ppContextNodeStrokeAddedTo* \[out\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) to which the ink analyzer added the stroke.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppContextNodeStrokeAddedTo* when you no longer need to use the object.

 

When *ppContextNodeStrokeAddedTo* is **NULL**, it indicates that the caller is not interested in the return value from the method.

The [**IInkAnalyzer**](iinkanalyzer.md) adds the stroke to an [**IContextNode**](icontextnode.md) of type **CustomRecognizer** (see [Context Node Types](context-node-types.md)). This node is in the root node's subnode collection (see [**IInkAnalyzer::GetRootNode Method**](iinkanalyzer-getrootnode.md) and [**IContextNode::GetSubNodes**](icontextnode-getsubnodes.md) methods).

The [**IInkAnalyzer**](iinkanalyzer.md) assigns the culture identifier of the active input thread to the stroke and adds the stroke to the first **UnclassifiedInk** node under the **CustomRecognizer** node. If no **UnclassifiedInk** node exists, it is created. If the [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) associated with the **CustomRecognizer** node does not support the culture identifier, the **IInkAnalyzer** continues analyzing and generates an [**IAnalysisWarning**](ianalysiswarning.md) warning. This warning has an [**AnalysisWarningCode**](/windows/desktop/tablet/analysiswarningcode) value of **AnalysisWarningCode\_LanguageIdNotRespected**.

*plStrokePacketData* contains packet data for all of the points in the stroke. *pStrokePacketDescriptionGuids* contains the globally unique identifiers (GUIDs) that describe the types of packet data included for each point in each stroke. For a complete list of available packet properties, see [PacketPropertyGuids Constants](packetpropertyguids-constants.md).

This method expands the dirty region to the union of the region's current value and the bounding box of the added stroke.

The [**IInkAnalyzer**](iinkanalyzer.md) returns an **HRESULT** of **E\_INVALIDARG** under the following circumstances.

-   The [**IInkAnalyzer**](iinkanalyzer.md) already contains a stroke with the same identifier as the stroke to be added.
-   The *pCustomRecognizer* parameter contains a custom recognizer node that is associated with a different [**IInkAnalyzer**](iinkanalyzer.md) object.
-   The *pCustomRecognizer* parameter contains an [**IContextNode**](icontextnode.md) that is not of type **CustomRecognizer**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> <dt>

[Context Node Types](context-node-types.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokesToCustomRecognizer Method**](iinkanalyzer-addstrokestocustomrecognizer.md)
</dt> <dt>

[**IInkAnalyzer::CreateCustomRecognizer Method**](iinkanalyzer-createcustomrecognizer.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

