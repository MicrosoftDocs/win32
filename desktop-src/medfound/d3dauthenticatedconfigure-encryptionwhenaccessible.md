---
Description: 'Sets the level of encryption that is performed before protected content becomes accessible to the CPU or bus.'
ms.assetid: '6de6c4a3-705a-4420-b9f4-8d4d442b23bf'
title: 'D3DAUTHENTICATEDCONFIGURE\_ENCRYPTIONWHENACCESSIBLE'
---

# D3DAUTHENTICATEDCONFIGURE\_ENCRYPTIONWHENACCESSIBLE

Sets the level of encryption that is performed before protected content becomes accessible to the CPU or bus.



|              |                                                                                                                             |
|--------------|-----------------------------------------------------------------------------------------------------------------------------|
| Command GUID | **D3DAUTHENTICATEDCONFIGURE\_ENCRYPTIONWHENACCESSIBLE**                                                                     |
| Input data   | [**D3DAUTHENTICATEDCHANNEL\_CONFIGUREUNCOMPRESSEDENCRYPTION**](d3dauthenticatedchannel-configureuncompressedencryption.md) |



 

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

[Content Protection Commands](content-protection-commands.md)
</dt> <dt>

[GPU-Based Content Protection](gpu-based-content-protection.md)
</dt> <dt>

[**IDirect3DAuthenticatedChannel9::Configure**](idirect3dauthenticatedchannel9-configure.md)
</dt> </dl>

 

 




