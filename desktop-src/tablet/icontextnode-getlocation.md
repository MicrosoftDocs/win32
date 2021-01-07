---
description: Retrieves the position and size of the IContextNode object.
ms.assetid: 40787a9b-1017-4209-aec8-09b7332bfa8a
title: IContextNode::GetLocation method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.GetLocation
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::GetLocation method

Retrieves the position and size of the [**IContextNode**](icontextnode.md) object.

## Syntax


```C++
HRESULT GetLocation(
  [out] IAnalysisRegion **ppIAnalysisRegion
);
```



## Parameters

<dl> <dt>

*ppIAnalysisRegion* \[out\]
</dt> <dd>

A pointer to the position and size of the [**IContextNode**](icontextnode.md) object.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**ppIAnalysisRegion* when you no longer need to use the analysis region.

 

The location for a container node is determined by finding the union of all the leaf's locations. The location for an ink leaf node is determined by finding the union of the bounding box of the associated strokes. The location for a non-ink leaf node is set when the node is created and can be updated using [**IContextNode::SetLocation**](icontextnode-setlocation.md).

## Examples

The following example shows a helper method that retrieves information about a specified node, its *pContextNode* parameter. This helper method returns information from the following methods.

-   [**IContextNode::GetId**](icontextnode-getid.md)
-   [**IContextNode::GetType**](icontextnode-gettype.md)
-   **IContextNode::GetLocation**
-   [**IContextNode::GetParentNode**](icontextnode-getparentnode.md)


```C++
// Helper method for collecting information about a context node.
HRESULT CMyClass::GetNodeInformation(
    IContextNode *pContextNode,
    GUID *pNodeIdentifier,
    GUID *pContextNodeType,
    IAnalysisRegion **ppAnalysisRegion,
    IContextNode **ppParentNode,
    IContextNodes **ppSubNodes)
{
    // Get the identifier of the context node.
    HRESULT hr = pContextNode->GetId(pNodeIdentifier);

    if (FAILED(hr))
    {
        return hr;
    }

    // Get the type identifier for the context node.
    hr = pContextNode->GetType(pContextNodeType);

    if (FAILED(hr))
    {
        return hr;
    }

    // Get the location of the context node.
    hr = pContextNode->GetLocation(ppAnalysisRegion);

    if (FAILED(hr))
    {
        return hr;
    }

    // Get the parent node of the context node.
    hr = pContextNode->GetParentNode(ppParentNode);

    if (FAILED(hr))
    {
        if ((*ppAnalysisRegion) != NULL)
        {
            (*ppAnalysisRegion)->Release();
            (*ppAnalysisRegion) = NULL;
        }
        return hr;
    }

    // Get the subnodes of the context node.
    hr = pContextNode->GetSubNodes(ppSubNodes);

    if (FAILED(hr))
    {
        if (*ppAnalysisRegion)
        {
            (*ppAnalysisRegion)->Release();
            (*ppAnalysisRegion) = NULL;
        }
        if (*ppParentNode)
        {
            (*ppParentNode)->Release();
            (*ppParentNode) = NULL;
        }
        return hr;
    }

    return hr;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[**IAnalysisRegion**](ianalysisregion.md)
</dt> <dt>

[**IContextNode::SetLocation**](icontextnode-setlocation.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

