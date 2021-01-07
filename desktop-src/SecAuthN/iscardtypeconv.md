---
description: Provides the methods needed to support the users of the other smart card COM interfaces.
ms.assetid: ce81706b-9201-432e-b9d0-c758769e1040
title: ISCardTypeConv interface (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardTypeConv
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardTypeConv interface

\[The **ISCardTypeConv** interface is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **ISCardTypeConv** interface provides the methods needed to support the users of the other [*smart card*](../secgloss/s-gly.md) COM interfaces. This interface is provided for backward compatibility only and should no longer be used.

## Members

The **ISCardTypeConv** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ISCardTypeConv** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISCardTypeConv** interface has these methods.



| Method                                                                              | Description                                                                                                                             |
|:------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| [**ConvertByteArrayToByteBuffer**](iscardtypeconv-convertbytearraytobytebuffer.md) | Converts a typical C/C++ byte array into a universal buffer of bytes (**IStream** object).<br/>                                   |
| [**ConvertByteBufferToByteArray**](iscardtypeconv-convertbytebuffertobytearray.md) | Converts a byte array mapped into a universal buffer of bytes (**IStream** object) into a typical C/C++ byte array.<br/>          |
| [**ConvertByteBufferToSafeArray**](iscardtypeconv-convertbytebuffertosafearray.md) | Converts a byte array mapped into a universal buffer of bytes (**IStream** object) into a SAFEARRAY of unsigned char (byte).<br/> |
| [**ConvertSafeArrayToByteBuffer**](iscardtypeconv-convertsafearraytobytebuffer.md) | Converts a byte array defined as a SAFEARRAY into a universal buffer of bytes (**IStream** object).<br/>                          |
| [**CreateByteArray**](iscardtypeconv-createbytearray.md)                           | Creates an array of bytes.<br/>                                                                                                   |
| [**CreateByteBuffer**](iscardtypeconv-createbytebuffer.md)                         | Creates a universal buffer of bytes mapped into an **IStream** ([**IByteBuffer**](ibytebuffer.md)) object.<br/>                  |
| [**CreateSafeArray**](iscardtypeconv-createsafearray.md)                           | Creates an Automation SAFEARRAY of unsigned characters (bytes).<br/>                                                              |
| [**FreeIStreamMemoryPtr**](iscardtypeconv-freeistreammemoryptr.md)                 | Frees a memory pointer to the HGLOBAL memory block managed by an **IStream** COM interface.<br/>                                  |
| [**GetAtIStreamMemory**](iscardtypeconv-getatistreammemory.md)                     | Acquires a byte pointer to the HGLOBAL memory block that is managed by the **IStream** COM interface.<br/>                        |
| [**SizeOfIStream**](iscardtypeconv-sizeofistream.md)                               | Determines the size (number of bytes) of an **IStream** COM interface.<br/>                                                       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scarddat.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scarddat.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardTypeConv is defined as 53B6AA63-3F56-11D0-916B-00AA00C18068<br/>       |



 

 
