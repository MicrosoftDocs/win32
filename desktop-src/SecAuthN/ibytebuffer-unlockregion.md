---
description: Removes the access restriction on a range of bytes previously restricted by using IByteBuffer::LockRegion.
ms.assetid: f2a1162e-7fc7-4a55-befb-0b017edb9fe2
title: IByteBuffer::UnlockRegion method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IByteBuffer.UnlockRegion
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# IByteBuffer::UnlockRegion method

\[The **UnlockRegion** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface provides similar functionality.\]

The **UnlockRegion** method removes the access restriction on a range of bytes previously restricted by using [**IByteBuffer::LockRegion**](ibytebuffer-lockregion.md).

## Syntax


```C++
HRESULT UnlockRegion(
  [in] LONG libOffset,
  [in] LONG cb,
  [in] LONG dwLockType
);
```



## Parameters

<dl> <dt>

*libOffset* \[in\]
</dt> <dd>

Byte offset for the beginning of the range.

</dd> <dt>

*cb* \[in\]
</dt> <dd>

Length, in bytes, of the range to be restricted.

</dd> <dt>

*dwLockType* \[in\]
</dt> <dd>

Access restrictions previously placed on the range.

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates the call was successful.

## Remarks

The **IByteBuffer::UnlockRegion** method unlocks a region previously locked by using the [**IByteBuffer::LockRegion**](ibytebuffer-lockregion.md) method. Locked regions must later be explicitly unlocked by calling **IByteBuffer::UnlockRegion** with exactly the same values for the *libOffset*, *cb*, and *dwLockType* parameters. The region must be unlocked before the stream is released. Two adjacent regions cannot be locked separately and then unlocked with a single unlock call.

## Examples

The following example shows unlocking a range of bytes.


```C++
HRESULT  hr;

// Unlock a region.
hr = pIByteBuff->UnlockRegion(0, 10, LOCK_EXCLUSIVE);
if (FAILED(hr))
  printf("Failed IByteBuffer::UnlockRegion\n");
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardssp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardssp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_IByteBuffer is defined as E126F8FE-A7AF-11D0-B88A-00C04FD424B9<br/>          |



 

