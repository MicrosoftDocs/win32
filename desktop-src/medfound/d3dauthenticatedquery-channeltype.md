---
description: Returns the type of authenticated channel.
ms.assetid: eec4b117-a9f2-479d-99d7-e5d4053cf6b4
title: D3DAUTHENTICATEDQUERY_CHANNELTYPE (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDQUERY_CHANNELTYPE
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDQUERY\_CHANNELTYPE

Returns the type of authenticated channel.



| Requirement | Value |
|-------------|--------------------------------------------------------------------------------------------------------------|
| Query GUID  | **D3DAUTHENTICATEDQUERY\_CHANNELTYPE**                                                                       |
| Input data  | [**D3DAUTHENTICATEDCHANNEL\_QUERY\_INPUT**](d3dauthenticatedchannel-query-input.md)                         |
| Return data | [**D3DAUTHENTICATEDCHANNEL\_QUERYCHANNELTYPE\_OUTPUT**](d3dauthenticatedchannel-querychanneltype-output.md) |



 

## Remarks

This query is valid for all channel types.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Content Protection Queries](content-protection-queries.md)
</dt> <dt>

[GPU-Based Content Protection](gpu-based-content-protection.md)
</dt> <dt>

[**IDirect3DAuthenticatedChannel9::Query**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query)
</dt> </dl>

 

 




