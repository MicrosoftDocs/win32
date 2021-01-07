---
description: Contains the response to a call to the IDirect3DAuthenticatedChannel9::Configure method.
ms.assetid: 6f33d3f7-a883-4aca-a058-b656d745f2b1
title: D3DAUTHENTICATEDCHANNEL_CONFIGURE_OUTPUT structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDCHANNEL_CONFIGURE_OUTPUT
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDCHANNEL\_CONFIGURE\_OUTPUT structure

Contains the response to a call to the [**IDirect3DAuthenticatedChannel9::Configure**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-configure) method.

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_CONFIGURE_OUTPUT {
  D3D_OMAC omac;
  GUID     ConfigureType;
  HANDLE   hChannel;
  UINT     SequenceNumber;
  HRESULT  ReturnCode;
} D3DAUTHENTICATEDCHANNEL_CONFIGURE_OUTPUT;
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

A handle to the authenticated channel.

</dd> <dt>

**SequenceNumber**
</dt> <dd>

The command sequence number.

</dd> <dt>

**ReturnCode**
</dt> <dd>

The result code for the command.

</dd> </dl>

## Remarks

For the **ConfigureType**, **hChannel**, and **SequenceNumber** members, the driver uses the same values that the application provided in the [**D3DAUTHENTICATEDCHANNEL\_CONFIGURE\_INPUT**](d3dauthenticatedchannel-configure-input.md) structure. The application should verify that these values match.

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

 

 




