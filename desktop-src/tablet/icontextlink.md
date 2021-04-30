---
description: Represents a relationship between two IContextNode objects.
ms.assetid: ee81d9d7-eba9-4b11-84d0-5a6ca0df7d92
title: IContextLink interface (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextLink
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextLink interface

Represents a relationship between two [**IContextNode**](icontextnode.md) objects.

## Members

The **IContextLink** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IContextLink** also has these types of members:

-   [Methods](#methods)

### Methods

The **IContextLink** interface has these methods.



| Method                                                                  | Description                                                                                                             |
|:------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**GetContextLinkDirection**](icontextlink-getcontextlinkdirection.md) | Retrieves the type of relationship this **IContextLink** represents.<br/>                                         |
| [**GetDestinationNode**](icontextlink-getdestinationnode.md)           | Retrieves the [**IContextNode**](icontextnode.md) object that is the destination for this **IContextLink**.<br/> |
| [**GetSourceNode**](icontextlink-getsourcenode.md)                     | Retrieves the [**IContextNode**](icontextnode.md) object that is the source for this **IContextLink**.<br/>      |



 

## Remarks

The following is an example of a relationship represented by an **IContextLink** object:

-   When an AnalysisHint node is used in ink analysis, the ink analysis operation creates an **IContextLink** object of type AnalysisHint between the analysis hint node and the node that contains writing within the area of the hint. The source node is the analysis hint node and the destination node is the node that contains writing.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IContextNode::GetContextLinks**](icontextnode-getcontextlinks.md)
</dt> <dt>

[**IContextLinks**](icontextlinks.md)
</dt> <dt>

[**ContextLinkDirection**](contextlinkdirection.md)
</dt> <dt>

[Context Node Types](context-node-types.md)
</dt> </dl>

 

