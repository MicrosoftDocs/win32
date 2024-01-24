---
description: Retrieves an array containing the packet property identifiers for the specified stroke.
ms.assetid: 169e3ce3-fb81-4ed6-b380-ef0d12444ba7
title: IContextNode::GetStrokePacketDescriptionById method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.GetStrokePacketDescriptionById
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::GetStrokePacketDescriptionById method

Retrieves an array containing the packet property identifiers for the specified stroke.

## Syntax


```C++
HRESULT GetStrokePacketDescriptionById(
  [in]      LONG  lStrokeId,
  [in, out] ULONG *pulStrokePacketDescriptionCount,
  [out]     GUID  **ppStrokePacketDescriptionGuids
);
```



## Parameters

<dl> <dt>

*lStrokeId* \[in\]
</dt> <dd>

The identifier for the stroke.

</dd> <dt>

*pulStrokePacketDescriptionCount* \[in, out\]
</dt> <dd>

The number of packet properties in each packet.

</dd> <dt>

*ppStrokePacketDescriptionGuids* \[out\]
</dt> <dd>

An array containing the packet property identifiers.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, use [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to release the memory from \**ppStrokePacketDescriptionGuids* when you no longer need the information.

 

\**ppStrokePacketDescriptionGuids* contains the globally unique identifiers (GUIDs) that describe the types of packet data included for each point in the stroke. For a complete list of available packet properties, see [PacketPropertyGuids Constants](packetpropertyguids-constants.md).

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

[**IContextNode::GetStrokePacketDataById**](icontextnode-getstrokepacketdatabyid.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

