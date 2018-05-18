---
Description: 'Contains input data for a D3DAUTHENTICATEDQUERY\_OUTPUTIDCOUNT query.'
ms.assetid: 'cc68b39f-4645-46a6-a752-549b070cf23b'
title: 'D3DAUTHENTICATEDCHANNEL\_QUERYOUTPUTIDCOUNT\_INPUT structure'
---

# D3DAUTHENTICATEDCHANNEL\_QUERYOUTPUTIDCOUNT\_INPUT structure

Contains input data for a [**D3DAUTHENTICATEDQUERY\_OUTPUTIDCOUNT**](d3dauthenticatedquery-outputidcount.md) query.

To send this query, call [**IDirect3DAuthenticatedChannel9::Query**](idirect3dauthenticatedchannel9-query.md).

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_QUERYOUTPUTIDCOUNT_INPUT {
  D3DAUTHENTICATEDCHANNEL_QUERY_INPUT Input;
  HANDLE                              DeviceHandle;
  HANDLE                              CryptoSessionHandle;
} D3DAUTHENTICATEDCHANNEL_QUERYOUTPUTIDCOUNT_INPUT;
```



## Members

<dl> <dt>

**Input**
</dt> <dd>

A [**D3DAUTHENTICATEDCHANNEL\_QUERY\_INPUT**](d3dauthenticatedchannel-query-input.md) structure that contains the GUID for the query and other data.

</dd> <dt>

**DeviceHandle**
</dt> <dd>

A handle to the device.

</dd> <dt>

**CryptoSessionHandle**
</dt> <dd>

A handle to the cryptographic session.

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

[**IDirect3DAuthenticatedChannel9::Query**](idirect3dauthenticatedchannel9-query.md)
</dt> </dl>

 

 




