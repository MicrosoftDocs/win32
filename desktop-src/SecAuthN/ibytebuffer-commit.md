---
description: The Commit method ensures that any changes made to an object open in transacted mode are reflected in the parent storage.
ms.assetid: 00986e48-c5b9-4ac9-a204-a0774cb5e03e
title: IByteBuffer::Commit method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IByteBuffer.Commit
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# IByteBuffer::Commit method

\[The **Commit** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface provides similar functionality.\]

The **Commit** method ensures that any changes made to an object open in transacted mode are reflected in the parent storage.

## Syntax


```C++
HRESULT Commit(
  [in] LONG grfCommitFlags
);
```



## Parameters

<dl> <dt>

*grfCommitFlags* \[in\]
</dt> <dd>

Controls how the changes for the stream object are committed. For a definition of these values, see the STGC enumeration.

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates the call was successful.

## Remarks

This method ensures that changes to a stream object opened in transacted mode are reflected in the parent storage. Changes that have been made to the stream since it was opened or last committed are reflected to the parent storage object. If the parent is opened in transacted mode, the parent may still revert at a later time rolling back the changes to this stream object. The compound file implementation does not support opening streams in transacted mode, so this method has very little effect other than to flush memory buffers.

## Examples

The following example shows committing changes to storage.


```C++
HRESULT  hr;

// Commit the buffer.
hr = pIByteBuff->Commit(STGC_DEFAULT | STGC_CONSOLIDATE);
if (FAILED(hr))
  printf("Failed IByteBuffer::Commit\n");
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



 

