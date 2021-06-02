---
description: The SCARD\_IO\_REQUEST structure begins a protocol control information structure.
ms.assetid: 80fd7c6e-e768-42db-8302-29e92c9552f0
title: SCARD_IO_REQUEST structure (Winsmcrd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SCARD_IO_REQUEST
api_type: 
- HeaderDef
api_location: 
- Winsmcrd.h
---

# SCARD\_IO\_REQUEST structure

The **SCARD\_IO\_REQUEST** structure begins a protocol control information structure. Any protocol-specific information then immediately follows this structure. The entire length of the structure must be aligned with the underlying hardware architecture word size. For example, in Win32 the length of any PCI information must be a multiple of four bytes so that it aligns on a 32-bit boundary.

## Syntax


```C++
typedef struct {
  DWORD dwProtocol;
  DWORD cbPciLength;
} SCARD_IO_REQUEST;
```



## Members

<dl> <dt>

**dwProtocol**
</dt> <dd>

Protocol in use.

</dd> <dt>

**cbPciLength**
</dt> <dd>

Length, in bytes, of the **SCARD\_IO\_REQUEST** structure plus any following PCI-specific information.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Winsmcrd.h</dt> </dl> |



## See also

<dl> <dt>

[**SCardTransmit**](/windows/desktop/api/Winscard/nf-winscard-scardtransmit)
</dt> </dl>

 

 




