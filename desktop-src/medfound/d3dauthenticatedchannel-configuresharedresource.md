---
description: Contains input data for a D3DAUTHENTICATEDCONFIGURE\_SHAREDRESOURCE command.
ms.assetid: bdeb0cc4-90f0-4174-a859-4b3fecb17bab
title: D3DAUTHENTICATEDCHANNEL_CONFIGURESHAREDRESOURCE structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDCHANNEL_CONFIGURESHAREDRESOURCE
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDCHANNEL\_CONFIGURESHAREDRESOURCE structure

Contains input data for a [**D3DAUTHENTICATEDCONFIGURE\_SHAREDRESOURCE**](d3dauthenticatedconfigure-sharedresource.md) command.

To send this query, call [**IDirect3DAuthenticatedChannel9::Configure**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-configure).

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_CONFIGURESHAREDRESOURCE {
  D3DAUTHENTICATEDCHANNEL_CONFIGURE_INPUT       Parameters;
  D3DAUTHENTICATEDCHANNEL_PROCESSIDENTIFIERTYPE ProcessIdentiferType;
  HANDLE                                        ProcessHandle;
  BOOL                                          AllowAccess;
} D3DAUTHENTICATEDCHANNEL_CONFIGURESHAREDRESOURCE;
```



## Members

<dl> <dt>

**Parameters**
</dt> <dd>

A [**D3DAUTHENTICATEDCHANNEL\_CONFIGURE\_INPUT**](d3dauthenticatedchannel-configure-input.md) structure that contains the command GUID and other data.

</dd> <dt>

**ProcessIdentiferType**
</dt> <dd>

A [**D3DAUTHENTICATEDCHANNEL\_PROCESSIDENTIFIERTYPE**](d3dauthenticatedchannel-processidentifiertype.md) value that specifies the type of process. To specify the Desktop Window Manager (DWM) process, set this member to **PROCESSIDTYPE\_DWM**. Otherwise, set this member to **PROCESSIDTYPE\_HANDLE** and set the **ProcessHandle** member to a valid handle.

</dd> <dt>

**ProcessHandle**
</dt> <dd>

A process handle. If the **ProcessIdentifier** member equals **PROCESSTIDTYPE\_HANDLE**, the **ProcessHandle** member specifies a handle to a process. Otherwise, the value is ignored.

</dd> <dt>

**AllowAccess**
</dt> <dd>

If **TRUE**, the specified process has access to restricted shared resources.

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

 

 




