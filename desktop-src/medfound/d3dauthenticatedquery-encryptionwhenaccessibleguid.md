---
Description: 'Returns one of the encryption types that can be used to encrypt content before it becomes accessible to the CPU or bus.'
ms.assetid: '263c6f00-8bc9-4e9c-8b98-fb8f87c6c008'
title: 'D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUID'
---

# D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUID

Returns one of the encryption types that can be used to encrypt content before it becomes accessible to the CPU or bus.



|             |                                                                                                                                    |
|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| Query GUID  | **D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUID**                                                                            |
| Input data  | [**D3DAUTHENTICATEDCHANNEL\_QUERYEVICTIONENCRYPTIONGUID\_INPUT**](d3dauthenticatedchannel-queryevictionencryptionguid-input.md)   |
| Return data | [**D3DAUTHENTICATEDCHANNEL\_QUERYEVICTIONENCRYPTIONGUID\_OUTPUT**](d3dauthenticatedchannel-queryevictionencryptionguid-output.md) |



 

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

 

 




