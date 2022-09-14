---
description: Contains input data for the IDirect3DAuthenticatedChannel9::Configure method.
ms.assetid: 7646100e-f768-4935-9e71-1d9db0d69c52
title: D3DAUTHENTICATEDCHANNEL_CONFIGURE_INPUT structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDCHANNEL_CONFIGURE_INPUT
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDCHANNEL\_CONFIGURE\_INPUT structure

Contains input data for the [**IDirect3DAuthenticatedChannel9::Configure**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-configure) method.

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_CONFIGURE_INPUT {
  D3D_OMAC omac;
  GUID     ConfigureType;
  HANDLE   hChannel;
  UINT     SequenceNumber;
} D3DAUTHENTICATEDCHANNEL_CONFIGURE_INPUT;
```



## Members

<dl> <dt>

**omac**
</dt> <dd>

A [**D3D\_OMAC**](d3d-omac.md) structure that contains a Message Authentication Code (MAC) of the data. The driver uses AES-based one-key CBC MAC (OMAC) to calculate this value for the block of data that appears after this structure member.

</dd> <dt>

**ConfigureType**
</dt> <dd>

A GUID that specifies the command. For a list of values, see [Content Protection Commands](content-protection-commands.md).

</dd> <dt>

**hChannel**
</dt> <dd>

A handle to the authenticated channel. To get the handle, call [**IDirect3DDevice9Video::CreateAuthenticatedChannel**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9video-createauthenticatedchannel).

</dd> <dt>

**SequenceNumber**
</dt> <dd>

The query sequence number. At the start of the session, generate a cryptographically secure 32-bit random number to use as the starting sequence number. For each command, increment the sequence number by 1.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Video Structures](direct3d-video-structures.md)
</dt> <dt>

[**IDirect3DAuthenticatedChannel9::Configure**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-configure)
</dt> </dl>

 

 




