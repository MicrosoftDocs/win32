---
Description: 'Returns the type of I/O bus used to send data to the GPU.'
ms.assetid: '5a180a5c-6798-40ba-9e2c-ce1f755fcc08'
title: 'D3DAUTHENTICATEDQUERY\_ACCESSIBILITYATTRIBUTES'
---

# D3DAUTHENTICATEDQUERY\_ACCESSIBILITYATTRIBUTES

Returns the type of I/O bus used to send data to the GPU.



|             |                                                                                                              |
|-------------|--------------------------------------------------------------------------------------------------------------|
| Query GUID  | **D3DAUTHENTICATEDQUERY\_ACCESSIBILITYATTRIBUTES**                                                           |
| Input data  | [**D3DAUTHENTICATEDCHANNEL\_QUERY\_INPUT**](d3dauthenticatedchannel-query-input.md)                         |
| Return data | [**D3DAUTHENTICATEDCHANNEL\_QUERYINFOBUSTYPE\_OUTPUT**](d3dauthenticatedchannel-queryinfobustype-output.md) |



 

## Remarks

This query also returns information about how accessible the content is when put into video memory.

The following channel types support this query:

-   **D3DAUTHENTICATEDCHANNEL\_DRIVER\_HARDWARE**
-   **D3DAUTHENTICATEDCHANNEL\_DRIVER\_SOFTWARE**

## Requirements



|                                     |                                                                                        |
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

[**IDirect3DAuthenticatedChannel9::Query**](idirect3dauthenticatedchannel9-query.md)
</dt> </dl>

 

 




