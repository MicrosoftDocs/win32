---
description: Specifies the timeout value used for sample locking operations in XVP.
title: MF_XVP_SAMPLE_LOCK_TIMEOUT attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_XVP\_SAMPLE\_LOCK\_TIMEOUT attribute

Specifies the timeout value used for sample locking operations in XVP.

## Data type

**UINT32**

## Remarks

The timeout value is in milliseconds. The timeout applies to an [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample) that uses a lock to protect access to the buffer. For example, if the **IMFSample** references a shared D3D texture that is protected by [IDXGIKeyedMutex](/windows/win32/api/dxgi/nn-dxgi-idxgikeyedmutex), then the timeout is used when trying to acquire the **IDXGIKeyedMutex**.


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 version 1803                                         |
| Minimum supported server<br/> | Windows Server version 1803                             |
| Header                   | Mfidl.h |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




