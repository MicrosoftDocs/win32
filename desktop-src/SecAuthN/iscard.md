---
description: Lets you open and manage a connection to a smart card.
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

\[The **ISCard** interface is available for use in the operating systems specified in the Requirements section. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **ISCard** interface lets you open and manage a connection to a [*smart card*](../secgloss/s-gly.md). Each connection to a card requires a single, corresponding instance of the **ISCard** interface.

The smart card [*resource manager*](../secgloss/r-gly.md) must be available whenever an instance of **ISCard** is created. If this service is unavailable, creation of the interface will fail.

The following example shows a typical use of the **ISCard** interface. The **ISCard** interface is used to connect to the smart card, submit a [*transaction*](../secgloss/t-gly.md), and release the smart card.

**To submit a transaction to a specific card**

1.  Create an **ISCard** interface.
2.  Attach to a smart card by specifying a smart card [*reader*](../secgloss/r-gly.md) or by using a previously established, valid handle.
3.  Create transaction commands with [**ISCardCmd**](iscardcmd.md), and [**ISCardISO7816**](iscardiso7816.md) smart card interfaces.
4.  Use **ISCard** to submit the transaction commands for processing by the smart card.
5.  Use **ISCard** to release the smart card.
6.  Release the **ISCard** interface.

## Members

The **ISCard** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ISCard** also has these types of members:

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
| [**Transaction**](iscard-transaction.md)       | Executes a write and read operation on the smart card command ([*application protocol data unit*](../secgloss/a-gly.md)) object.<br/> |
| [**UnlockScard**](iscard-unlockscard.md)       | Releases exclusive access to the smart card.<br/>                                                                                                                                                                         |



 

### Properties

The **ISCard** interface has these properties.



| Property                                               | Access type          | Description                                                                                                                                                                                    |
|:-------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Atr**](iscard-get-atr.md)<br/>               | Read-only<br/> | Retrieves the [*ATR string*](../secgloss/a-gly.md) of the smart card.<br/>                                                                   |
| [**CardHandle**](iscard-get-cardhandle.md)<br/> | Read-only<br/> | Retrieves the handle for the connected smart card.<br/>                                                                                                                                  |
| [**Context**](iscard-get-context.md)<br/>       | Read-only<br/> | Retrieves the current [*resource manager context*](../secgloss/r-gly.md) handle.<br/>                            |
| [**Protocol**](iscard-get-protocol.md)<br/>     | Read-only<br/> | Retrieves the identifier of the protocol currently in use on the smart card.<br/>                                                                                                        |
| [**Status**](iscard-get-status.md)<br/>         | Read-only<br/> | Retrieves the current [*state*](../secgloss/s-gly.md) the [*smart card*](../secgloss/s-gly.md) is in.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardmgr.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardmgr.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCard is defined as 1461AAC3-6810-11D0-918F-00AA00C18068<br/>               |



 

 
