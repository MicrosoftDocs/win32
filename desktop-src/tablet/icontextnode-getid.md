---
description: Retrieves the identifier for the IContextNode object.
ms.assetid: 7578bcc1-7c69-45fc-b3c2-7350ce4df99c
title: IContextNode::GetId method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.GetId
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::GetId method

Retrieves the identifier for the [**IContextNode**](icontextnode.md) object.

## Syntax


```C++
HRESULT GetId(
  [out] GUID *pId
);
```



## Parameters

<dl> <dt>

*pId* \[out\]
</dt> <dd>

The identifier for the [**IContextNode**](icontextnode.md) object.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

The ink analyzer assigns a unique identifier to all context nodes it creates. During ink analysis, the ink analyzer may change the identifier for a context node. For example, the ink analyzer may reclassify one word node as two word nodes and then assign the original identifier to one and a new identifier to the other. Or, the ink analyzer may reclassify two word nodes as one word node and assign one of the original identifiers to the new word node.

## Examples

The following example shows a helper method that retrieves information about a specified node, its *pContextNode* parameter. This helper method returns information from the following methods.

-   **IContextNode::GetId**
-   [**IContextNode::GetType**](icontextnode-gettype.md)
-   [**IContextNode::GetLocation**](icontextnode-getlocation.md)
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

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




