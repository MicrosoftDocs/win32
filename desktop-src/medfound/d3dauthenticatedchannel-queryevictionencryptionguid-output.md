---
description: Contains the response to a D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUID query.
ms.assetid: afe73f8e-3304-470c-a37a-17b6c767b2c0
title: D3DAUTHENTICATEDCHANNEL_QUERYEVICTIONENCRYPTIONGUID_OUTPUT structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDCHANNEL_QUERYEVICTIONENCRYPTIONGUID_OUTPUT
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDCHANNEL\_QUERYEVICTIONENCRYPTIONGUID\_OUTPUT structure

Contains the response to a [**D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUID**](d3dauthenticatedquery-encryptionwhenaccessibleguid.md) query.

To send this query, call [**IDirect3DAuthenticatedChannel9::Query**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query).

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_QUERYEVICTIONENCRYPTIONGUID_OUTPUT {
  Output D3DAUTHENTICATEDCHANNEL_QUERY_OUTPUT;
  UINT   EncryptionGuidIndex;
  GUID   EncryptionGuid;
} D3DAUTHENTICATEDCHANNEL_QUERYEVICTIONENCRYPTIONGUID_OUTPUT;
```



## Members

<dl> <dt>

**D3DAUTHENTICATEDCHANNEL\_QUERY\_OUTPUT**
</dt> <dd>

A [**D3DAUTHENTICATEDCHANNEL\_QUERY\_OUTPUT**](d3dauthenticatedchannel-query-output.md) structure that contains a Message Authentication Code (MAC) and other data.

</dd> <dt>

**EncryptionGuidIndex**
</dt> <dd>

The index of the encryption GUID.

</dd> <dt>

**EncryptionGuid**
</dt> <dd>

A GUID that specifies a supported encryption type.

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

 

 




