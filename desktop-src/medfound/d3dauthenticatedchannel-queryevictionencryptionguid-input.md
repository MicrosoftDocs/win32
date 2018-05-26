---
Description: Contains input data for a D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUID query.
ms.assetid: 0e24e393-3f63-4c6f-aca1-f73ced3490ba
title: D3DAUTHENTICATEDCHANNEL\_QUERYEVICTIONENCRYPTIONGUID\_INPUT structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DAUTHENTICATEDCHANNEL\_QUERYEVICTIONENCRYPTIONGUID\_INPUT structure

Contains input data for a [**D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUID**](d3dauthenticatedquery-encryptionwhenaccessibleguid.md) query.

To send this query, call [**IDirect3DAuthenticatedChannel9::Query**](/windows/win32/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query?branch=master).

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_QUERYEVICTIONENCRYPTIONGUID_INPUT {
  D3DAUTHENTICATEDCHANNEL_QUERY_INPUT Input;
  UINT                                EncryptionGuidIndex;
} D3DAUTHENTICATEDCHANNEL_QUERYEVICTIONENCRYPTIONGUID_INPUT;
```



## Members

<dl> <dt>

**Input**
</dt> <dd>

A [**D3DAUTHENTICATEDCHANNEL\_QUERY\_INPUT**](d3dauthenticatedchannel-query-input.md) structure that contains the GUID for the query and other data.

</dd> <dt>

**EncryptionGuidIndex**
</dt> <dd>

The index of the encryption GUID.

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

[**IDirect3DAuthenticatedChannel9::Query**](/windows/win32/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query?branch=master)
</dt> </dl>

 

 




