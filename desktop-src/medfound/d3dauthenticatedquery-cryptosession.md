---
Description: Returns handles to the cryptographic session and Direct3D device that are associated with a specified DirectX Video Acceleration 2 (DXVA-2) decoder device.
ms.assetid: 90b3bcf3-2988-48de-8acd-62e385d4fdf0
title: D3DAUTHENTICATEDQUERY\_CRYPTOSESSION
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DAUTHENTICATEDQUERY\_CRYPTOSESSION

Returns handles to the cryptographic session and Direct3D device that are associated with a specified DirectX Video Acceleration 2 (DXVA-2) decoder device.



|             |                                                                                                                  |
|-------------|------------------------------------------------------------------------------------------------------------------|
| Query GUID  | **D3DAUTHENTICATEDQUERY\_CRYPTOSESSION**                                                                         |
| Input data  | [**D3DAUTHENTICATEDCHANNEL\_QUERY\_INPUT**](d3dauthenticatedchannel-query-input.md)                             |
| Return data | [**D3DAUTHENTICATEDCHANNEL\_QUERYCRYPTOSESSION\_OUTPUT**](d3dauthenticatedchannel-querycryptosession-output.md) |



 

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

[**IDirect3DAuthenticatedChannel9::Query**](/windows/win32/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query?branch=master)
</dt> </dl>

 

 




