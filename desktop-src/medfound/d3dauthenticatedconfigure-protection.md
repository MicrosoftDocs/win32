---
description: Enables or disables protection for the device.
ms.assetid: 120d940f-39a0-4ad5-bd3e-c108b3f98ace
title: D3DAUTHENTICATEDCONFIGURE_PROTECTION (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDCONFIGURE_PROTECTION
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDCONFIGURE\_PROTECTION

Enables or disables protection for the device.



| Requirement | Value |
|--------------|-----------------------------------------------------------------------------------------------------|
| Command GUID | **D3DAUTHENTICATEDCONFIGURE\_PROTECTION**                                                           |
| Input data   | [**D3DAUTHENTICATEDCHANNEL\_CONFIGUREPROTECTION**](d3dauthenticatedchannel-configureprotection.md) |



 

## Remarks

This command is valid for all channel types.

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

 

 




