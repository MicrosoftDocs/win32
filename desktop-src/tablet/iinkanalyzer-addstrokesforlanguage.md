---
description: Adds stroke data for multiple strokes to the IInkAnalyzer and assigns the specified culture identifier to the strokes.
ms.assetid: 1274b24f-204b-4a84-a7c0-0205b6068ae8
title: IInkAnalyzer::AddStrokesForLanguage method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.AddStrokesForLanguage
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::AddStrokesForLanguage method

Adds stroke data for multiple strokes to the [**IInkAnalyzer**](iinkanalyzer.md) and assigns the specified culture identifier to the strokes.

## Syntax


```C++
HRESULT AddStrokesForLanguage(
  [in]  ULONG        ulStrokeIdsCount,
  [in]  LONG         *plIdofStrokesToAdd,
  [in]  LONG         lStrokesLCID,
  [in]  ULONG        ulStrokePacketDescriptionCount,
  [in]  GUID         *pStrokePacketDescriptionGuids,
  [in]  ULONG        *pulPacketDataCountPerStroke,
  [in]  LONG         *plStrokePacketData,
  [out] IContextNode **ppContextNodeStrokeAddedTo
);
```



## Parameters

<dl> <dt>

*ulStrokeIdsCount* \[in\]
</dt> <dd>

The number of strokes to add.

</dd> <dt>

*plIdofStrokesToAdd* \[in\]
</dt> <dd>

An array containing the stroke identifiers.

</dd> <dt>

*lStrokesLCID* \[in\]
</dt> <dd>

A value that represents the culture identifier to assign to the strokes.

</dd> <dt>

*ulStrokePacketDescriptionCount* \[in\]
</dt> <dd>

The number of properties in each packet.

</dd> <dt>

*pStrokePacketDescriptionGuids* \[in\]
</dt> <dd>

An array containing the packet property identifiers.

</dd> <dt>

*pulPacketDataCountPerStroke* \[in\]
</dt> <dd>

An array containing the number of packets in each stroke.

</dd> <dt>

*plStrokePacketData* \[in\]
</dt> <dd>

An array containing the packet data for the strokes.

</dd> <dt>

*ppContextNodeStrokeAddedTo* \[out\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) to which the ink analyzer added the strokes.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppContextNodeStrokeAddedTo* when you no longer need to use the object.

 

When *ppContextNodeStrokeAddedTo* is **NULL**, it indicates that the caller is not interested in the return value from the method.

The [**IInkAnalyzer**](iinkanalyzer.md) adds the strokes to an [**IContextNode**](icontextnode.md) of type UnclassifiedInk (see [Context Node Types](context-node-types.md)). This node is in the root node's subnode collection (see [**IInkAnalyzer::GetRootNode Method**](iinkanalyzer-getrootnode.md) and [**IContextNode::GetSubNodes**](icontextnode-getsubnodes.md) methods).

The [**IInkAnalyzer**](iinkanalyzer.md) assigns the *lStrokeLCID* culture identifier to the strokes and adds the strokes to the first UnclassifiedInk context node under the ink analyzer's root node that contains strokes with the same culture identifier. If the ink analyzer does not have a node with the same culture identifier, it creates a new UnclassifiedInk context node under its root node and adds the strokes to the new UnclassifiedInk context node.

*plStrokePacketData* contains packet data for all of the strokes. *pStrokePacketDescriptionGuids* contains the globally unique identifiers (GUIDs) that describe the types of packet data included for each point in each stroke. For a complete list of available packet properties, see [PacketPropertyGuids Constants](packetpropertyguids-constants.md).

> [!Note]  
> Only strokes with the same packet descriptions can be added in a single call to [**IInkAnalyzer::AddStrokes Method**](iinkanalyzer-addstrokes.md).

 

This method expands the dirty region to the union of the region's current value and the bounding box of the added strokes.

If the [**IInkAnalyzer**](iinkanalyzer.md) already contains a stroke with the same identifier as one of the strokes to be added, the **IInkAnalyzer** returns an **HRESULT** of **E\_INVALIDARG**.

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

[**IInkAnalyzer::AddStroke Method**](iinkanalyzer-addstroke.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokeForLanguage Method**](iinkanalyzer-addstrokeforlanguage.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokes Method**](iinkanalyzer-addstrokes.md)
</dt> <dt>

[**IInkAnalyzer::RemoveStroke Method**](iinkanalyzer-removestroke.md)
</dt> <dt>

[**IInkAnalyzer::RemoveStrokes Method**](iinkanalyzer-removestrokes.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

