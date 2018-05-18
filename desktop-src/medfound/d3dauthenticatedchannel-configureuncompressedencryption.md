---
Description: 'Contains input data for the D3DAUTHENTICATEDCONFIGURE\_ENCRYPTIONWHENACCESSIBLE command.'
ms.assetid: 'd2d0adff-5d4d-4af3-b6b8-b8c60a506142'
title: 'D3DAUTHENTICATEDCHANNEL\_CONFIGUREUNCOMPRESSEDENCRYPTION structure'
---

# D3DAUTHENTICATEDCHANNEL\_CONFIGUREUNCOMPRESSEDENCRYPTION structure

Contains input data for the [**D3DAUTHENTICATEDCONFIGURE\_ENCRYPTIONWHENACCESSIBLE**](d3dauthenticatedconfigure-encryptionwhenaccessible.md) command.

To send this query, call [**IDirect3DAuthenticatedChannel9::Configure**](idirect3dauthenticatedchannel9-configure.md).

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_CONFIGUREUNCOMPRESSEDENCRYPTION {
  D3DAUTHENTICATEDCHANNEL_CONFIGURE_INPUT Parameters;
  GUID                                    EncryptionGuid;
} D3DAUTHENTICATEDCHANNEL_CONFIGUREUNCOMPRESSEDENCRYPTION;
```



## Members

<dl> <dt>

**Parameters**
</dt> <dd>

A [**D3DAUTHENTICATEDCHANNEL\_CONFIGURE\_INPUT**](d3dauthenticatedchannel-configure-input.md) structure that contains the command GUID and other data.

</dd> <dt>

**EncryptionGuid**
</dt> <dd>

A GUID that specifies the type of encryption to apply.

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

[**IDirect3DAuthenticatedChannel9::Configure**](idirect3dauthenticatedchannel9-configure.md)
</dt> </dl>

 

 




