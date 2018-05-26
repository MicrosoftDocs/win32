---
Description: Returns information about a process that is allowed to open shared resources with restricted access.
ms.assetid: 669d9623-3a96-4661-9dae-3f283a990fe8
title: D3DAUTHENTICATEDQUERY\_RESTRICTEDSHAREDRESOURCEPROCESS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DAUTHENTICATEDQUERY\_RESTRICTEDSHAREDRESOURCEPROCESS

Returns information about a process that is allowed to open shared resources with restricted access.



|             |                                                                                                                                                      |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Query GUID  | **D3DAUTHENTICATEDQUERY\_RESTRICTEDSHAREDRESOURCEPROCESS**                                                                                           |
| Input data  | [**D3DAUTHENTICATEDCHANNEL\_QUERYRESTRICTEDSHAREDRESOURCEPROCESS\_INPUT**](d3dauthenticatedchannel-queryrestrictedsharedresourceprocess-input.md)   |
| Return data | [**D3DAUTHENTICATEDCHANNEL\_QUERYRESTRICTEDSHAREDRESOURCEPROCESS\_OUTPUT**](d3dauthenticatedchannel-queryrestrictedsharedresourceprocess-output.md) |



 

## Remarks

The following channel types support this query:

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

[Content Protection Queries](content-protection-queries.md)
</dt> <dt>

[GPU-Based Content Protection](gpu-based-content-protection.md)
</dt> <dt>

[**IDirect3DAuthenticatedChannel9::Query**](/windows/win32/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query?branch=master)
</dt> </dl>

 

 




