---
description: Represents a node in a tree of objects that are created as part of ink analysis.
ms.assetid: 44ef4401-cb14-4348-9ed8-b11a40d04940
title: IContextNode interface (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode interface

Represents a node in a tree of objects that are created as part of ink analysis.

## Members

The **IContextNode** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IContextNode** also has these types of members:

-   [Methods](#methods)

### Methods

The **IContextNode** interface has these methods.



| Method                                                                                  | Description                                                                                                                                                                                                                   |
|:----------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddContextLink**](icontextnode-addcontextlink.md)                                   | Adds a new [**IContextLink**](icontextlink.md) to the **IContextNode** object's context link collection.<br/>                                                                                                          |
| [**AddPropertyData**](icontextnode-addpropertydata.md)                                 | Adds a piece of application-specific data.<br/>                                                                                                                                                                         |
| [**Confirm**](icontextnode-confirm.md)                                                 | Modifies the confirmation type, which controls what the [**IInkAnalyzer**](iinkanalyzer.md) object can change about the **IContextNode**.<br/>                                                                         |
| [**ContainsPropertyData**](icontextnode-containspropertydata.md)                       | Determines whether the **IContextNode** object contains data stored under the specified identifier.<br/>                                                                                                                |
| [**CreatePartiallyPopulatedSubNode**](icontextnode-createpartiallypopulatedsubnode.md) | Creates a child **IContextNode** object that contains only information on type, identifier, and location.<br/>                                                                                                          |
| [**CreateSubNode**](icontextnode-createsubnode.md)                                     | Creates a new child **IContextNode** object.<br/>                                                                                                                                                                       |
| [**DeleteContextLink**](icontextnode-deletecontextlink.md)                             | Deletes an [**IContextLink**](icontextlink.md) object from the **IContextNode** object's link collection.<br/>                                                                                                         |
| [**DeleteSubNode**](icontextnode-deletesubnode.md)                                     | Removes a child **IContextNode**.<br/>                                                                                                                                                                                  |
| [**GetContextLinks**](icontextnode-getcontextlinks.md)                                 | Retrieves a collection of [**IContextLink**](icontextlink.md) objects that represents relationships with other **IContextNode** objects.<br/>                                                                          |
| [**GetId**](icontextnode-getid.md)                                                     | Retrieves the identifier for the **IContextNode** object.<br/>                                                                                                                                                          |
| [**GetLocation**](icontextnode-getlocation.md)                                         | Retrieves the position and size of the **IContextNode** object.<br/>                                                                                                                                                    |
| [**GetParentNode**](icontextnode-getparentnode.md)                                     | Retrieves the parent node of this **IContextNode** in the context node tree.<br/>                                                                                                                                       |
| [**GetPartiallyPopulated**](icontextnode-getpartiallypopulated.md)                     | Retrieves the value that indicates whether an **IContextNode** object is partially populated or fully populated.<br/>                                                                                                   |
| [**GetPropertyData**](icontextnode-getpropertydata.md)                                 | Retrieves application-specific data or other property data given the specified identifier.<br/>                                                                                                                         |
| [**GetPropertyDataIds**](icontextnode-getpropertydataids.md)                           | Retrieves the identifiers for which there is property data.<br/>                                                                                                                                                        |
| [**GetStrokeCount**](icontextnode-getstrokecount.md)                                   | Retrieves the number of strokes associated with the **IContextNode** object.<br/>                                                                                                                                       |
| [**GetStrokeId**](icontextnode-getstrokeid.md)                                         | Retrieves the stroke identifier for the stroke referenced by an index value within the **IContextNode** object.<br/>                                                                                                    |
| [**GetStrokeIds**](icontextnode-getstrokeids.md)                                       | Retrieves an array of identifiers for the strokes within the **IContextNode** object.<br/>                                                                                                                              |
| [**GetStrokePacketDataById**](icontextnode-getstrokepacketdatabyid.md)                 | Retrieves an array containing the packet property data for the specified stroke.<br/>                                                                                                                                   |
| [**GetStrokePacketDescriptionById**](icontextnode-getstrokepacketdescriptionbyid.md)   | Retrieves an array containing the packet property identifiers for the specified stroke.<br/>                                                                                                                            |
| [**GetSubNodes**](icontextnode-getsubnodes.md)                                         | Retrieves the direct child nodes of the **IContextNode** object.<br/>                                                                                                                                                   |
| [**GetType**](icontextnode-gettype.md)                                                 | Retrieves the type of the **IContextNode** object.<br/>                                                                                                                                                                 |
| [**GetTypeName**](icontextnode-gettypename.md)                                         | Retrieves a human-readable type name of this **IContextNode**.<br/>                                                                                                                                                     |
| [**IsConfirmed**](icontextnode-isconfirmed.md)                                         | Retrieves a value that indicates whether the **IContextNode** object is confirmed. [**IInkAnalyzer**](iinkanalyzer.md) cannot change the node type and associated strokes for confirmed **IContextNode** objects.<br/> |
| [**LoadPropertiesData**](icontextnode-loadpropertiesdata.md)                           | Recreates the application-specific and internal property data for an array of bytes that was previously created with [**IContextNode::SavePropertiesData**](icontextnode-savepropertiesdata.md).<br/>                  |
| [**MoveSubNodeToPosition**](icontextnode-movesubnodetoposition.md)                     | Reorders a specified child **IContextNode** object to the specified index.<br/>                                                                                                                                         |
| [**RemovePropertyData**](icontextnode-removepropertydata.md)                           | Removes a piece of application-specific data.<br/>                                                                                                                                                                      |
| [**Reparent**](icontextnode-reparent.md)                                               | Moves this **IContextNode** object from its parent context node's subnodes collection to the specified context node's subnodes collection.<br/>                                                                         |
| [**ReparentStrokeByIdToNode**](icontextnode-reparentstrokebyidtonode.md)               | Moves stroke data from this **IContextNode** to the specified **IContextNode**.<br/>                                                                                                                                    |
| [**SavePropertiesData**](icontextnode-savepropertiesdata.md)                           | Retrieves an array of bytes that contains the application-specific and internal property data for this **IContextNode**.<br/>                                                                                           |
| [**SetLocation**](icontextnode-setlocation.md)                                         | Updates the position and size of this **IContextNode**.<br/>                                                                                                                                                            |
| [**SetPartiallyPopulated**](icontextnode-setpartiallypopulated.md)                     | Modifies the value that indicates whether this **IContextNode** is partially or fully populated.<br/>                                                                                                                   |
| [**SetStrokes**](icontextnode-setstrokes.md)                                           | Associates the specified strokes with this **IContextNode**.<br/>                                                                                                                                                       |



 

## Remarks

The types of nodes are described in the [Context Node Types](context-node-types.md) constants.

## Examples

The following example shows a method that examines an **IContextNode**; the method does the following:

-   Gets the context node's type. If the context node is an unclassified ink, analysis hint, or custom recognizer node, it calls a helper method to examine specific properties of the node type.
-   If the node has subnodes, it examines each subnode by calling itself.
-   If the node is an ink leaf node, it examines the stroke data for the node by calling a helper method.

Ihe InkAnalysis API allows you to create a line node that contains ink words and text words. However, the parser will ignore these mixed nodes and will treat them like foreign nodes. This will have impact the parsing accuracy of detecting ink annotations when the end user writes on or around this mixed node.


```C++
HRESULT CMyClass::ExploreContextNode(
    IContextNode *pContextNode)
{
    // Check for certain types of context nodes.
    GUID ContextNodeType;
    HRESULT hr = pContextNode->GetType(&ContextNodeType);

    if (SUCCEEDED(hr))
    {
        if (IsEqualGUID(GUID_CNT_UNCLASSIFIEDINK, ContextNodeType))
        {
            // Call a helper method that explores unclassified ink nodes.
            hr = this->ExploreUnclassifiedInkNode(pContextNode);
        }
        else if (IsEqualGUID(GUID_CNT_ANALYSISHINT, ContextNodeType))
        {
            // Call a helper method that explores analysis hint nodes.
            hr = this->ExploreAnalysisHintNode(pContextNode);
        }
        else if (IsEqualGUID(GUID_CNT_CUSTOMRECOGNIZER, ContextNodeType))
        {
            // Call a helper method that explores custom recognizer nodes.
            hr = this->ExploreCustomRecognizerNode(pContextNode);
        }

        if (SUCCEEDED(hr))
        {
            // Check if this node is a branch or a leaf node.
            IContextNodes *pSubNodes = NULL;
            hr = pContextNode->GetSubNodes(&pSubNodes);

            if (SUCCEEDED(hr))
            {
                ULONG ulSubNodeCount;
                hr = pSubNodes->GetCount(&ulSubNodeCount);

                if (SUCCEEDED(hr))
                {
                    if (ulSubNodeCount > 0)
                    {
                        // This node has child nodes; explore each child node.
                        IContextNode *pSubNode = NULL;
                        for (ULONG index=0; index<ulSubNodeCount; index++)
                        {
                            hr = pSubNodes->GetContextNode(index, &pSubNode);

                            if (SUCCEEDED(hr))
                            {
                                // Recursive call to explore the child node of this
                                // context node.
                                hr = this->ExploreContextNode(pSubNode);
                            }

                            // Release this reference to the child context node.
                            if (pSubNode != NULL)
                            {
                                pSubNode->Release();
                                pSubNode = NULL;
                            }

                            if (FAILED(hr))
                            {
                                break;
                            }
                        }
                    }
                    else
                    {
                        // This is a leaf node. Check if it contains stroke data.
                        ULONG ulStrokeCount;
                        hr = pContextNode->GetStrokeCount(&ulStrokeCount);

                        if (SUCCEEDED(hr))
                        {
                            if (ulStrokeCount > 0)
                            {
                                // This node is an ink leaf node; call helper
                                // method that explores available stroke data.
                                hr = this->ExploreNodeStrokeData(pContextNode);
                            }
                        }
                    }
                }
            }

            // Release this reference to the subnodes collection.
            if (pSubNodes != NULL)
            {
                pSubNodes->Release();
                pSubNodes = NULL;
            }
        }
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

[**IContextNodes**](icontextnodes.md)
</dt> <dt>

[Context Node Types](context-node-types.md)
</dt> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

