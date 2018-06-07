---
Description: Lets you open and manage a connection to a smart card.
ms.assetid: f49f76e6-eed9-4e85-b48f-29f7bad40218
title: ISCard interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ISCard interface

\[The **ISCard** interface is available for use in the operating systems specified in the Requirements section. The [Smart Card Modules](https://msdn.microsoft.com/a33e4e23-5f0d-4d03-ae3b-8727cdf57ab7) provide similar functionality.\]

The **ISCard** interface lets you open and manage a connection to a [*smart card*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50). Each connection to a card requires a single, corresponding instance of the **ISCard** interface.

The smart card [*resource manager*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd) must be available whenever an instance of **ISCard** is created. If this service is unavailable, creation of the interface will fail.

The following example shows a typical use of the **ISCard** interface. The **ISCard** interface is used to connect to the smart card, submit a [*transaction*](https://msdn.microsoft.com/11f2e098-1d1e-473b-90ff-7b86eb923e9f), and release the smart card.

**To submit a transaction to a specific card**

1.  Create an **ISCard** interface.
2.  Attach to a smart card by specifying a smart card [*reader*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd) or by using a previously established, valid handle.
3.  Create transaction commands with [**ISCardCmd**](iscardcmd.md), and [**ISCardISO7816**](iscardiso7816.md) smart card interfaces.
4.  Use **ISCard** to submit the transaction commands for processing by the smart card.
5.  Use **ISCard** to release the smart card.
6.  Release the **ISCard** interface.

## Members

The **ISCard** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISCard** also has these types of members:

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
| [**Transaction**](iscard-transaction.md)       | Executes a write and read operation on the smart card command ([*application protocol data unit*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02)) object.<br/> |
| [**UnlockScard**](iscard-unlockscard.md)       | Releases exclusive access to the smart card.<br/>                                                                                                                                                                         |



 

### Properties

The **ISCard** interface has these properties.



| Property                                               | Access type          | Description                                                                                                                                                                                    |
|:-------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Atr**](iscard-get-atr.md)<br/>               | Read-only<br/> | Retrieves the [*ATR string*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02) of the smart card.<br/>                                                                   |
| [**CardHandle**](iscard-get-cardhandle.md)<br/> | Read-only<br/> | Retrieves the handle for the connected smart card.<br/>                                                                                                                                  |
| [**Context**](iscard-get-context.md)<br/>       | Read-only<br/> | Retrieves the current [*resource manager context*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd) handle.<br/>                            |
| [**Protocol**](iscard-get-protocol.md)<br/>     | Read-only<br/> | Retrieves the identifier of the protocol currently in use on the smart card.<br/>                                                                                                        |
| [**Status**](iscard-get-status.md)<br/>         | Read-only<br/> | Retrieves the current [*state*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) the [*smart card*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) is in.<br/> |



 

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



 

 




