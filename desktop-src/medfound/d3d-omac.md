---
description: Contains a Message Authentication Code (MAC).
ms.assetid: be5515fd-1936-46b8-9fc8-8d1f87048c38
title: D3D_OMAC structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3D_OMAC
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3D\_OMAC structure

Contains a Message Authentication Code (MAC).

## Syntax


```C++
typedef struct _D3D_OMAC {
  BYTE Omac[D3D_OMAC_SIZE];
} D3D_OMAC;
```



## Members

<dl> <dt>

**Omac**
</dt> <dd>

A byte array that contains the cryptographic MAC value of the message.

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
</dt> </dl>

 

 




