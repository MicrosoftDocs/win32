---
description: Initializes the authenticated channel.
ms.assetid: a74edbaa-af57-4f8e-9974-f6053f59377f
title: D3DAUTHENTICATEDCONFIGURE_INITIALIZE (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDCONFIGURE_INITIALIZE
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDCONFIGURE\_INITIALIZE

Initializes the authenticated channel.



| Requirement | Value |
|--------------|-----------------------------------------------------------------------------------------------------|
| Command GUID | **D3DAUTHENTICATEDCONFIGURE\_INITIALIZE**                                                           |
| Input data   | [**D3DAUTHENTICATEDCHANNEL\_CONFIGUREINITIALIZE**](d3dauthenticatedchannel-configureinitialize.md) |



 

## Remarks

Send this command once, at the start of the session. This command can be sent only one time for each authenticated channel. The input sequence number is ignored for this command.

The following channel types support this command:

-   **D3DAUTHENTICATEDCHANNEL\_DRIVER\_HARDWARE**
-   **D3DAUTHENTICATEDCHANNEL\_DRIVER\_SOFTWARE**

## Requirements



| Requirement | Value |
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

[**IDirect3DAuthenticatedChannel9::Configure**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-configure)
</dt> </dl>

 

 




