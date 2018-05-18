---
Description: 'Enables a process to open a shared resource, or disables a process from opening shared resources.'
ms.assetid: '5fa2b88f-e946-436c-953e-04e0e338146c'
title: 'D3DAUTHENTICATEDCONFIGURE\_SHAREDRESOURCE'
---

# D3DAUTHENTICATEDCONFIGURE\_SHAREDRESOURCE

Enables a process to open a shared resource, or disables a process from opening shared resources.



|              |                                                                                                             |
|--------------|-------------------------------------------------------------------------------------------------------------|
| Command GUID | **D3DAUTHENTICATEDCONFIGURE\_SHAREDRESOURCE**                                                               |
| Input data   | [**D3DAUTHENTICATEDCHANNEL\_CONFIGURESHAREDRESOURCE**](d3dauthenticatedchannel-configuresharedresource.md) |



 

## Remarks

The following channel types support this query:

-   **D3DAUTHENTICATEDCHANNEL\_DRIVER\_D3D9**
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

 

 




