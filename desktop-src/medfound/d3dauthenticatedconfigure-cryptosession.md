---
Description: Associates a cryptographic session with a DirectX Video Acceleration 2 (DXVA-2) decoder device and a Direct3D device.
ms.assetid: d40fead7-8a86-426e-933e-13df21cdf50b
title: D3DAUTHENTICATEDCONFIGURE\_CRYPTOSESSION
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DAUTHENTICATEDCONFIGURE\_CRYPTOSESSION

Associates a cryptographic session with a DirectX Video Acceleration 2 (DXVA-2) decoder device and a Direct3D device.



|              |                                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------|
| Command GUID | **D3DAUTHENTICATEDCONFIGURE\_CRYPTOSESSION**                                                              |
| Input data   | [**D3DAUTHENTICATEDCHANNEL\_CONFIGURECRYPTOSESSION**](d3dauthenticatedchannel-configurecryptosession.md) |



 

## Remarks

After this command is sent, you can send the [D3DAUTHENTICATEDQUERY\_OUTPUTID](d3dauthenticatedquery-outputid.md) query to find out which video outputs are associated with the cryptographic session.

The following channel types support this command:

-   **D3DAUTHENTICATEDCHANNEL\_D3D9**
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

[**IDirect3DAuthenticatedChannel9::Configure**](/windows/win32/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-configure?branch=master)
</dt> </dl>

 

 




