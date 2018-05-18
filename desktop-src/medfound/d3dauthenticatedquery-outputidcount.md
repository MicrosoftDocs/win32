---
Description: 'Returns the number of output identifiers associated with a specified cryptographic session and Direct3D device.'
ms.assetid: 'a5b17250-6a40-40a9-93b6-3b98b56b09d6'
title: 'D3DAUTHENTICATEDQUERY\_OUTPUTIDCOUNT'
---

# D3DAUTHENTICATEDQUERY\_OUTPUTIDCOUNT

Returns the number of output identifiers associated with a specified cryptographic session and Direct3D device.



|             |                                                                                                                  |
|-------------|------------------------------------------------------------------------------------------------------------------|
| Query GUID  | **D3DAUTHENTICATEDQUERY\_OUTPUTIDCOUNT**                                                                         |
| Input data  | [**D3DAUTHENTICATEDCHANNEL\_QUERYOUTPUTIDCOUNT\_INPUT**](d3dauthenticatedchannel-queryoutputidcount-input.md)   |
| Return data | [**D3DAUTHENTICATEDCHANNEL\_QUERYOUTPUTIDCOUNT\_OUTPUT**](d3dauthenticatedchannel-queryoutputidcount-output.md) |



 

## Remarks

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

 

 




