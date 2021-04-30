---
description: Contains a collection of objects that implement the IContextLink interface.
ms.assetid: 34d1bbbb-85c0-4209-97ca-c22f22a1b625
title: IContextLinks interface (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextLinks
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextLinks interface

Contains a collection of objects that implement the [**IContextLink**](icontextlink.md) interface.

## Members

The **IContextLinks** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IContextLinks** also has these types of members:

-   [Methods](#methods)

### Methods

The **IContextLinks** interface has these methods.



| Method                                                 | Description                                                                                         |
|:-------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**GetContextLink**](icontextlinks-getcontextlink.md) | Retrieves the [**IContextLink**](icontextlink.md) at the specified index.<br/>               |
| [**GetCount**](icontextlinks-getcount.md)             | Retrieves the number of [**IContextLink**](icontextlink.md) objects in this collection.<br/> |



 

## Remarks

This is usually accessed through the [**IContextNode::GetContextLinks**](icontextnode-getcontextlinks.md) method.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IContextLink**](icontextlink.md)
</dt> <dt>

[**IContextNode::AddContextLink**](icontextnode-addcontextlink.md)
</dt> <dt>

[**IContextNode::DeleteContextLink**](icontextnode-deletecontextlink.md)
</dt> <dt>

[**IContextNode::GetContextLinks**](icontextnode-getcontextlinks.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

