---
description: Contains input data for the IDirect3DAuthenticatedChannel9::Query method.
ms.assetid: 6a484652-8da2-4074-96b2-6fe49f4d4200
title: D3DAUTHENTICATEDCHANNEL_QUERY_INPUT structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDCHANNEL_QUERY_INPUT
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDCHANNEL\_QUERY\_INPUT structure

Contains input data for the [**IDirect3DAuthenticatedChannel9::Query**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query) method.

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_QUERY_INPUT {
  GUID           QueryType;
  hChannel       HANDLE;
  SequenceNumber UINT;
} D3DAUTHENTICATEDCHANNEL_QUERY_INPUT;
```



## Members

<dl> <dt>

**QueryType**
</dt> <dd>

A GUID that specifies the query. For a list of values, see [Content Protection Queries](content-protection-queries.md).

</dd> <dt>

**HANDLE**
</dt> <dd>

A handle to the authenticated channel. To get the handle, call [**IDirect3DDevice9Video::CreateAuthenticatedChannel**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9video-createauthenticatedchannel).

</dd> <dt>

**UINT**
</dt> <dd>

The query sequence number. At the start of the session, generate a cryptographically secure 32-bit random number to use as the starting sequence number. For each query, increment the sequence number by 1.

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

[**IDirect3DAuthenticatedChannel9::Query**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query)
</dt> </dl>

 

 




