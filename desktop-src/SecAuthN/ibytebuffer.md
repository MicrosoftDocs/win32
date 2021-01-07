---
description: The IByteBuffer interface is provided to read, write and manage stream objects. This object essentially is a wrapper for the IStream object.
ms.assetid: dbc46d53-a421-45c0-a86b-b8a0a212a672
title: IByteBuffer interface (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IByteBuffer
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# IByteBuffer interface

\[The **IByteBuffer** interface is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface provides similar functionality.\]

The **IByteBuffer** interface is provided to read, write and manage stream objects. This object essentially is a wrapper for the **IStream** object.

## Members

The **IByteBuffer** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IByteBuffer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IByteBuffer** interface has these methods.



| Method                                           | Description                                                                                               |
|:-------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| [**Clone**](ibytebuffer-clone.md)               | Clones an **IByteBuffer** object.<br/>                                                              |
| [**Commit**](ibytebuffer-commit.md)             | Commits a [*transaction*](/windows/desktop/SecGloss/t-gly).<br/> |
| [**CopyTo**](ibytebuffer-copyto.md)             | Copies bytes to another object.<br/>                                                                |
| [**Initialize**](ibytebuffer-initialize.md)     | Initializes the **IByteBuffer** object.<br/>                                                        |
| [**LockRegion**](ibytebuffer-lockregion.md)     | Restricts access to a range of bytes.<br/>                                                          |
| [**Read**](ibytebuffer-read.md)                 | Reads bytes into memory.<br/>                                                                       |
| [**Revert**](ibytebuffer-revert.md)             | Discards changes since the last [**Commit**](ibytebuffer-commit.md) call.<br/>                     |
| [**Seek**](ibytebuffer-seek.md)                 | Changes the seek pointer.<br/>                                                                      |
| [**SetSize**](ibytebuffer-setsize.md)           | Changes the size of the stream object.<br/>                                                         |
| [**Stat**](ibytebuffer-stat.md)                 | Retrieves statistical information about a stream.<br/>                                              |
| [**UnlockRegion**](ibytebuffer-unlockregion.md) | Removes access restriction previously set by [**LockRegion**](ibytebuffer-lockregion.md).<br/>     |
| [**Write**](ibytebuffer-write.md)               | Writes bytes to the stream.<br/>                                                                    |



 

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



 

