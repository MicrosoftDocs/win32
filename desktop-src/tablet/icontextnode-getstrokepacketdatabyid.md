---
description: Retrieves an array containing the packet property data for the specified stroke.
ms.assetid: 02db48b3-edc3-4ecb-8103-79312194937a
title: IContextNode::GetStrokePacketDataById method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.GetStrokePacketDataById
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::GetStrokePacketDataById method

Retrieves an array containing the packet property data for the specified stroke.

## Syntax


```C++
HRESULT GetStrokePacketDataById(
  [in]      LONG  strokeId,
  [in, out] ULONG *pStrokePacketDataCount,
  [out]     LONG  **pplStrokePacketData
);
```



## Parameters

<dl> <dt>

*strokeId* \[in\]
</dt> <dd>

The identifier for the stroke.

</dd> <dt>

*pStrokePacketDataCount* \[in, out\]
</dt> <dd>

The length of the packet data array.

</dd> <dt>

*pplStrokePacketData* \[out\]
</dt> <dd>

A pointer to the packet data for the stroke.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, use [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to release the memory from \**pplStrokePacketData* when you no longer need the information.

 

*plStrokePacketData* contains packet data for all of the points in the stroke. To get the types of packet data included for each point in the stroke, use [**IContextNode::GetStrokePacketDescriptionById**](icontextnode-getstrokepacketdescriptionbyid.md).

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

[**IContextNode::GetStrokePacketDescriptionById**](icontextnode-getstrokepacketdescriptionbyid.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

