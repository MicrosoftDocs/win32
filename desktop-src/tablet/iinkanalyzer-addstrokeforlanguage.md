---
description: Adds stroke data for a single stroke to the IInkAnalyzer and assigns a specific culture identifier to the stroke.
ms.assetid: 65eb805e-05ed-4144-b17e-872c47ab33fa
title: IInkAnalyzer::AddStrokeForLanguage method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.AddStrokeForLanguage
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::AddStrokeForLanguage method

Adds stroke data for a single stroke to the [**IInkAnalyzer**](iinkanalyzer.md) and assigns a specific culture identifier to the stroke.

## Syntax


```C++
HRESULT AddStrokeForLanguage(
  [in]  LONG         lStrokeId,
  [in]  LONG         lStrokeLCID,
  [in]  ULONG        ulStrokePacketDataCount,
  [in]  LONG         *plStrokePacketData,
  [in]  ULONG        ulStrokePacketDescriptionCount,
  [in]  GUID         *pStrokePacketDescriptionGuids,
  [out] IContextNode **ppContextNodeStrokeAddedTo
);
```



## Parameters

<dl> <dt>

*lStrokeId* \[in\]
</dt> <dd>

The identifier for the stroke to add.

</dd> <dt>

*lStrokeLCID* \[in\]
</dt> <dd>

The culture identifier to assign to the stroke.

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

The number of properties in each packet.

</dd> <dt>

*pStrokePacketDescriptionGuids* \[in\]
</dt> <dd>

An array containing the packet property identifiers.

</dd> <dt>

*ppContextNodeStrokeAddedTo* \[out\]
</dt> <dd>

A pointer whose value is set to the pointer of the [**IContextNode**](icontextnode.md) that contains the newly added stroke.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppContextNodeStrokeAddedTo* when you no longer need to use the object.

 

When *ppContextNodeStrokeAddedTo* is **NULL**, it indicates that the caller is not interested in the return value from the method.

The [**IInkAnalyzer**](iinkanalyzer.md) adds the stroke to an [**IContextNode**](icontextnode.md) of type UnclassifiedInk (see [Context Node Types](context-node-types.md)). This node is in the root node's subnode collection (see [**IInkAnalyzer::GetRootNode Method**](iinkanalyzer-getrootnode.md) and [**IContextNode::GetSubNodes**](icontextnode-getsubnodes.md) methods).

The [**IInkAnalyzer**](iinkanalyzer.md) assigns *lStrokeLCID* culture identifier to the stroke and adds the stroke to the first UnclassifiedInk context node under the ink analyzer's root node that contains strokes with the same culture identifier. If the ink analyzer does not have a node with the same culture identifier, it creates a new UnclassifiedInk context node under its root node and adds the stroke to the new UnclassifiedInk context node.

*plStrokePacketData* contains packet data for all of the points in the stroke. *pStrokePacketDescriptionGuids* contains the globally unique identifiers (GUIDs) that describe the types of packet data included for each point in the stroke. For a complete list of available packet properties, see [PacketPropertyGuids Constants](packetpropertyguids-constants.md).

This method expands the dirty region to the union of the region's current value and the bounding box of the added stroke.

If the [**IInkAnalyzer**](iinkanalyzer.md) already contains a stroke with the same stroke identifier, the **IInkAnalyzer** returns an **HRESULT** of **E\_INVALIDARG**.

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

[**IInkAnalyzer::AddStrokes Method**](iinkanalyzer-addstrokes.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokesForLanguage Method**](iinkanalyzer-addstrokesforlanguage.md)
</dt> <dt>

[**IInkAnalyzer::RemoveStroke Method**](iinkanalyzer-removestroke.md)
</dt> <dt>

[**IInkAnalyzer::RemoveStrokes Method**](iinkanalyzer-removestrokes.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

