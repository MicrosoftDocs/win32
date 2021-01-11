---
description: Returns the number of processes that are allowed to open shared resources with restricted access.
ms.assetid: e1b9ef18-fd08-4639-9ba9-4bccd33f5d16
title: D3DAUTHENTICATEDQUERY_RESTRICTEDSHAREDRESOURCEPROCESSCOUNT (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDQUERY_RESTRICTEDSHAREDRESOURCEPROCESSCOUNT
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDQUERY\_RESTRICTEDSHAREDRESOURCEPROCESSCOUNT

Returns the number of processes that are allowed to open shared resources with restricted access.



| Requirement | Value |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Query GUID  | **D3DAUTHENTICATEDQUERY\_RESTRICTEDSHAREDRESOURCEPROCESSCOUNT**                                                                                                |
| Input data  | [**D3DAUTHENTICATEDCHANNEL\_QUERY\_INPUT**](d3dauthenticatedchannel-query-input.md)                                                                           |
| Return data | [**D3DAUTHENTICATEDCHANNEL\_QUERYRESTRICTEDSHAREDRESOURCEPROCESSCOUNT\_OUTPUT**](d3dauthenticatedchannel-queryrestrictedsharedresourceprocesscount-output.md) |



 

## Remarks

The following channel types support this query:

-   **D3DAUTHENTICATEDCHANNEL\_D3D9**
-   **D3DAUTHENTICATEDCHANNEL\_DRIVER\_SOFTWARE**

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

 

 




