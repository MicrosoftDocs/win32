---
description: Specifies the type of confirmation that can occur on an IContextNode object.
ms.assetid: 5c906548-dbf5-4448-b248-070bd43b054e
title: ConfirmationType enumeration (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ConfirmationType
api_type: 
- HeaderDef
api_location: 
- IACom.h
---

# ConfirmationType enumeration

Specifies the type of confirmation that can occur on an [**IContextNode**](icontextnode.md) object.

## Syntax


```C++
typedef enum ConfirmationType { 
  ConfirmationType_None                   = 0,
  ConfirmationType_NodeTypeAndProperties  = 1,
  ConfirmationType_TopBoundary            = 4
} ConfirmationType;
```



## Constants

<dl> <dt>

<span id="ConfirmationType_None"></span><span id="confirmationtype_none"></span><span id="CONFIRMATIONTYPE_NONE"></span>**ConfirmationType\_None**
</dt> <dd>

No confirmation is applied. The [**IInkAnalyzer**](iinkanalyzer.md) is free to change a context node or any of its descendants as needed.

</dd> <dt>

<span id="ConfirmationType_NodeTypeAndProperties"></span><span id="confirmationtype_nodetypeandproperties"></span><span id="CONFIRMATIONTYPE_NODETYPEANDPROPERTIES"></span>**ConfirmationType\_NodeTypeAndProperties**
</dt> <dd>

The [**IInkAnalyzer**](iinkanalyzer.md) cannot change the type or any properties of the specified context node.

</dd> <dt>

<span id="ConfirmationType_TopBoundary"></span><span id="confirmationtype_topboundary"></span><span id="CONFIRMATIONTYPE_TOPBOUNDARY"></span>**ConfirmationType\_TopBoundary**
</dt> <dd>

The [**IInkAnalyzer**](iinkanalyzer.md) will not perform operations, including adding ink or merging with other [**ContextNodes**](icontextnodes.md), that cause the TopBoundary to move beyond the current top boundary. For example:

-   An application analyzes a set of Ink, and a ParagraphNode is identified.
-   The application confirms the TopBoundary of this paragraph.
-   The user of the application writes new ink above the current paragraph. When analyze is called again, the new ink will not be incorporated into the Confirmed paragraph node.
-   Since only the top boundary is confirmed, the ContextNode can continue to grow in other directions. Deleting strokes can cause the top boundary to move down. Translating the ContextNode can cause the location to change, but will not allow additional ink to be merged in the new location.

This ConfirmationType is only applicable to paragraph nodes.

</dd> </dl>

## Remarks

You can use the **NodeTypeAndProperties** value only for ink word and ink drawing nodes (see [**IContextNode::GetType**](icontextnode-gettype.md)). Otherwise, an **E\_INVALIDARG** is returned from [**IContextNode::Confirm**](icontextnode-confirm.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |



## See also

<dl> <dt>

[**IContextNode::Confirm**](icontextnode-confirm.md)
</dt> <dt>

[**IContextNode::IsConfirmed**](icontextnode-isconfirmed.md)
</dt> </dl>

 

 




