---
description: The Revert method discards all changes that have been made to a transacted stream since the last IByteBuffer::Commit call.
ms.assetid: da3d9810-6511-43d5-af87-03a392f8be75
title: IByteBuffer::Revert method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IByteBuffer.Revert
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# IByteBuffer::Revert method

\[The **Revert** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface provides similar functionality.\]

The **Revert** method discards all changes that have been made to a transacted stream since the last [**IByteBuffer::Commit**](ibytebuffer-commit.md) call.

## Syntax


```C++
HRESULT Revert();
```



## Parameters

This method has no parameters.

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates the call was successful and the stream was reverted to its previous version.

## Remarks

This method discards changes made to a transacted stream since the last commit operation.

## Examples

The following example shows reverting a transacted stream to the last-committed operation.


```C++
HRESULT  hr;

hr = pIByteBuff->Revert();
if (FAILED(hr))
  printf("Failed IByteBuffer::Revert\n");
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



 

