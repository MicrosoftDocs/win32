---
description: Contains input data for a D3DAUTHENTICATEDCONFIGURE\_INITIALIZE command.
ms.assetid: 08677cb3-6f08-49d5-a3b6-c48c88516273
title: D3DAUTHENTICATEDCHANNEL_CONFIGUREINITIALIZE structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDCHANNEL_CONFIGUREINITIALIZE
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDCHANNEL\_CONFIGUREINITIALIZE structure

Contains input data for a [**D3DAUTHENTICATEDCONFIGURE\_INITIALIZE**](d3dauthenticatedconfigure-initialize.md) command.

To send this query, call [**IDirect3DAuthenticatedChannel9::Configure**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-configure).

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_CONFIGUREINITIALIZE {
  D3DAUTHENTICATEDCHANNEL_CONFIGURE_INPUT Parameters;
  UINT                                    StartSequenceQuery;
  UINT                                    StartSequenceConfigure;
} D3DAUTHENTICATEDCHANNEL_CONFIGUREINITIALIZE;
```



## Members

<dl> <dt>

**Parameters**
</dt> <dd>

A [**D3DAUTHENTICATEDCHANNEL\_CONFIGURE\_INPUT**](d3dauthenticatedchannel-configure-input.md) structure that contains the command GUID and other data.

</dd> <dt>

**StartSequenceQuery**
</dt> <dd>

The initial sequence number for queries.

</dd> <dt>

**StartSequenceConfigure**
</dt> <dd>

The initial sequence number for commands.

</dd> </dl>

## Remarks

The **StartSequenceQuery** and **StartSequenceConfigure** members each contain a cryptographically secure 32-bit random number.

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

 

 




