---
Description: Returns one of the output identifiers that is associated with a specified cryptographic session and Direct3D device.
ms.assetid: 7b56055a-fb36-4e54-9bee-ab9401b09267
title: D3DAUTHENTICATEDQUERY\_OUTPUTID
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DAUTHENTICATEDQUERY\_OUTPUTID

Returns one of the output identifiers that is associated with a specified cryptographic session and Direct3D device.



|             |                                                                                                        |
|-------------|--------------------------------------------------------------------------------------------------------|
| Query GUID  | **D3DAUTHENTICATEDQUERY\_OUTPUTID**                                                                    |
| Input data  | [**D3DAUTHENTICATEDCHANNEL\_QUERYOUTPUTID\_INPUT**](d3dauthenticatedchannel-queryoutputid-input.md)   |
| Return data | [**D3DAUTHENTICATEDCHANNEL\_QUERYOUTPUTID\_OUTPUT**](d3dauthenticatedchannel-queryoutputid-output.md) |



 

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

 

 




