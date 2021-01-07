---
description: Contains the response to a D3DAUTHENTICATEDQUERY\_CRYPTOSESSION query.
ms.assetid: df9d9b41-8188-4597-9e83-d14065eb7fc7
title: D3DAUTHENTICATEDCHANNEL_QUERYCRYPTOSESSION_OUTPUT structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDCHANNEL_QUERYCRYPTOSESSION_OUTPUT
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDCHANNEL\_QUERYCRYPTOSESSION\_OUTPUT structure

Contains the response to a [**D3DAUTHENTICATEDQUERY\_CRYPTOSESSION**](d3dauthenticatedquery-cryptosession.md) query.

To send this query, call [**IDirect3DAuthenticatedChannel9::Query**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query).

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_QUERYCRYPTOSESSION_OUTPUT {
  D3DAUTHENTICATEDCHANNEL_QUERY_OUTPUT Output;
  HANDLE                               DXVA2DecodeHandle;
  HANDLE                               CryptoSessionHandle;
  HANDLE                               DeviceHandle;
} D3DAUTHENTICATEDCHANNEL_QUERYCRYPTOSESSION_OUTPUT;
```



## Members

<dl> <dt>

**Output**
</dt> <dd>

A [**D3DAUTHENTICATEDCHANNEL\_QUERY\_OUTPUT**](d3dauthenticatedchannel-query-output.md) structure that contains a Message Authentication Code (MAC) and other data.

</dd> <dt>

**DXVA2DecodeHandle**
</dt> <dd>

A handle to a DirectX Video Acceleration 2 (DXVA-2) decoder device.

</dd> <dt>

**CryptoSessionHandle**
</dt> <dd>

A handle to the cryptographic session that is associated with the decoder device.

</dd> <dt>

**DeviceHandle**
</dt> <dd>

A handle to the Direct3D device that is associated with the decoder device.

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

 

 




