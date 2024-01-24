---
description: Contains a collection of objects that implement the IContextNode interface and that are the result of an ink analysis operation.
ms.assetid: 2c4e9d84-243a-40e4-b3f9-5c4cafc5aac4
title: IContextNodes interface (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNodes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNodes interface

Contains a collection of objects that implement the [**IContextNode**](icontextnode.md) interface and that are the result of an ink analysis operation.

## Members

The **IContextNodes** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IContextNodes** also has these types of members:

-   [Methods](#methods)

### Methods

The **IContextNodes** interface has these methods.



| Method                                                       | Description                                                                                                          |
|:-------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**AddContextNode**](icontextnodes-addcontextnode.md)       | Adds an [**IContextNode**](icontextnode.md) object to this collection. <br/>                                  |
| [**GetContextNode**](icontextnodes-getcontextnode.md)       | Retrieves the [**IContextNode**](icontextnode.md) object at the specified index within this collection. <br/> |
| [**GetCount**](icontextnodes-getcount.md)                   | Retrieves the number of [**IContextNode**](icontextnode.md) objects contained in this collection. <br/>       |
| [**RemoveContextNode**](icontextnodes-removecontextnode.md) | Removes an [**IContextNode**](icontextnode.md) object from this collection. <br/>                             |



 

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

 

