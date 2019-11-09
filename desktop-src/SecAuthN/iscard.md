---
Description: Lets you open and manage a connection to a smart card.
ms.assetid: f49f76e6-eed9-4e85-b48f-29f7bad40218
title: ISCard interface (Scardmgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCard
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCard interface

\[The **ISCard** interface is available for use in the operating systems specified in the Requirements section. The [Smart Card Modules](https://msdn.microsoft.com/en-us/library/Dd627652(v=VS.85).aspx) provide similar functionality.\]

The **ISCard** interface lets you open and manage a connection to a [*smart card*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx). Each connection to a card requires a single, corresponding instance of the **ISCard** interface.

The smart card [*resource manager*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) must be available whenever an instance of **ISCard** is created. If this service is unavailable, creation of the interface will fail.

The following example shows a typical use of the **ISCard** interface. The **ISCard** interface is used to connect to the smart card, submit a [*transaction*](https://msdn.microsoft.com/en-us/library/ms721627(v=VS.85).aspx), and release the smart card.

**To submit a transaction to a specific card**

1.  Create an **ISCard** interface.
2.  Attach to a smart card by specifying a smart card [*reader*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) or by using a previously established, valid handle.
3.  Create transaction commands with [**ISCardCmd**](iscardcmd.md), and [**ISCardISO7816**](iscardiso7816.md) smart card interfaces.
4.  Use **ISCard** to submit the transaction commands for processing by the smart card.
5.  Use **ISCard** to release the smart card.
6.  Release the **ISCard** interface.

## Members

The **ISCard** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) interface. **ISCard** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ISCard** interface has these methods.



| Method                                          | Description                                                                                                                                                                                                                     |
|:------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AttachByHandle**](iscard-attachbyhandle.md) | Attaches an object to an open and configured smart card handle.<br/>                                                                                                                                                      |
| [**AttachByReader**](iscard-attachbyreader.md) | Opens the smart card in the named reader.<br/>                                                                                                                                                                            |
| [**Detach**](iscard-detach.md)                 | Closes the open connection to the smart card.<br/>                                                                                                                                                                        |
| [**LockSCard**](iscard-lockscard.md)           | Claims exclusive access to the smart card.<br/>                                                                                                                                                                           |
| [**ReAttach**](iscard-reattach.md)             | Resets and reinitializes the smart card.<br/>                                                                                                                                                                             |
| [**Transaction**](iscard-transaction.md)       | Executes a write and read operation on the smart card command ([*application protocol data unit*](https://msdn.microsoft.com/en-us/library/ms721532(v=VS.85).aspx)) object.<br/> |
| [**UnlockScard**](iscard-unlockscard.md)       | Releases exclusive access to the smart card.<br/>                                                                                                                                                                         |



 

### Properties

The **ISCard** interface has these properties.



| Property                                               | Access type          | Description                                                                                                                                                                                    |
|:-------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Atr**](iscard-get-atr.md)<br/>               | Read-only<br/> | Retrieves the [*ATR string*](https://msdn.microsoft.com/en-us/library/ms721532(v=VS.85).aspx) of the smart card.<br/>                                                                   |
| [**CardHandle**](iscard-get-cardhandle.md)<br/> | Read-only<br/> | Retrieves the handle for the connected smart card.<br/>                                                                                                                                  |
| [**Context**](iscard-get-context.md)<br/>       | Read-only<br/> | Retrieves the current [*resource manager context*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) handle.<br/>                            |
| [**Protocol**](iscard-get-protocol.md)<br/>     | Read-only<br/> | Retrieves the identifier of the protocol currently in use on the smart card.<br/>                                                                                                        |
| [**Status**](iscard-get-status.md)<br/>         | Read-only<br/> | Retrieves the current [*state*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) the [*smart card*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) is in.<br/> |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardmgr.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardmgr.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCard is defined as 1461AAC3-6810-11D0-918F-00AA00C18068<br/>               |



 

 




