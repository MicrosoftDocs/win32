---
Description: Contains input data for a D3DAUTHENTICATEDCONFIGURE\_PROTECTION command.
ms.assetid: 44f37e78-7218-42be-a07a-5ab911f2ba21
title: D3DAUTHENTICATEDCHANNEL\_CONFIGUREPROTECTION structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DAUTHENTICATEDCHANNEL\_CONFIGUREPROTECTION structure

Contains input data for a [**D3DAUTHENTICATEDCONFIGURE\_PROTECTION**](d3dauthenticatedconfigure-protection.md) command.

To send this query, call [**IDirect3DAuthenticatedChannel9::Configure**](/windows/win32/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-configure?branch=master).

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_CONFIGUREPROTECTION {
  D3DAUTHENTICATEDCHANNEL_CONFIGURE_INPUT  Parameters;
  D3DAUTHENTICATEDCHANNEL_PROTECTION_FLAGS Protections;
} D3DAUTHENTICATEDCHANNEL_CONFIGUREPROTECTION;
```



## Members

<dl> <dt>

**Parameters**
</dt> <dd>

A [**D3DAUTHENTICATEDCHANNEL\_CONFIGURE\_INPUT**](d3dauthenticatedchannel-configure-input.md) structure that contains the command GUID and other data.

</dd> <dt>

**Protections**
</dt> <dd>

A [**D3DAUTHENTICATEDCHANNEL\_PROTECTION\_FLAGS**](d3dauthenticatedchannel-protection-flags.md) structure that specifies the protection level.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Video Structures](direct3d-video-structures.md)
</dt> <dt>

[**IDirect3DAuthenticatedChannel9::Configure**](/windows/win32/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-configure?branch=master)
</dt> </dl>

 

 




