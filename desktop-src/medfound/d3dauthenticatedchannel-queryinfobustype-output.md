---
Description: 'Contains the response to a D3DAUTHENTICATEDQUERY\_ACCESSIBILITYATTRIBUTES query.'
ms.assetid: '9f66a467-ba05-413b-b001-ea4c5ca4a37d'
title: 'D3DAUTHENTICATEDCHANNEL\_QUERYINFOBUSTYPE\_OUTPUT structure'
---

# D3DAUTHENTICATEDCHANNEL\_QUERYINFOBUSTYPE\_OUTPUT structure

Contains the response to a [**D3DAUTHENTICATEDQUERY\_ACCESSIBILITYATTRIBUTES**](d3dauthenticatedquery-accessibilityattributes.md) query.

To send this query, call [**IDirect3DAuthenticatedChannel9::Query**](idirect3dauthenticatedchannel9-query.md).

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_QUERYINFOBUSTYPE_OUTPUT {
  D3DAUTHENTICATEDCHANNEL_QUERY_OUTPUT Output;
  D3DBUSTYPE                           BusType;
  BOOL                                 bAccessibleInContiguousBlocks;
  BOOL                                 bAccessibleInNonContiguousBlocks;
} D3DAUTHENTICATEDCHANNEL_QUERYINFOBUSTYPE_OUTPUT;
```



## Members

<dl> <dt>

**Output**
</dt> <dd>

A [**D3DAUTHENTICATEDCHANNEL\_QUERY\_OUTPUT**](d3dauthenticatedchannel-query-output.md) structure that contains a Message Authentication Code (MAC) and other data.

</dd> <dt>

**BusType**
</dt> <dd>

A bitwise **OR** of flags from the [**D3DBUSTYPE**](d3dbustype.md) enumeration.

</dd> <dt>

**bAccessibleInContiguousBlocks**
</dt> <dd>

If **TRUE**, contiguous blocks of video memory may be accessible to the CPU or the bus.

</dd> <dt>

**bAccessibleInNonContiguousBlocks**
</dt> <dd>

If **TRUE**, non-contiguous blocks of video memory may be accessible to the CPU or the bus.

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

 

 




