---
Description: Returns the current protection level for the device.
ms.assetid: 335d21e8-2a98-4824-a60d-1969a40e8d24
title: D3DAUTHENTICATEDQUERY\_PROTECTION
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DAUTHENTICATEDQUERY\_PROTECTION

Returns the current protection level for the device.



|             |                                                                                                            |
|-------------|------------------------------------------------------------------------------------------------------------|
| Query GUID  | **D3DAUTHENTICATEDQUERY\_PROTECTION**                                                                      |
| Input data  | [**D3DAUTHENTICATEDCHANNEL\_QUERY\_INPUT**](d3dauthenticatedchannel-query-input.md)                       |
| Return data | [**D3DAUTHENTICATEDCHANNEL\_QUERYPROTECTION\_OUTPUT**](d3dauthenticatedchannel-queryprotection-output.md) |



 

## Remarks

This query is valid for all channel types.

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

 

 




