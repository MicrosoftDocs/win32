---
description: Provides the methods needed to construct and manage a smart card application protocol data unit (APDU).
ms.assetid: fd84bb2e-27da-4670-b8e8-56c7948b78bb
title: ISCardCmd interface (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardCmd
- ISCardCmd.Type
- ISCardCmd.get_Type
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardCmd interface

\[The **ISCardCmd** interface is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **ISCardCmd** interface provides the methods needed to construct and manage a [*smart card*](../secgloss/s-gly.md) [*application protocol data unit*](../secgloss/a-gly.md) (APDU). This interface encapsulates two buffers:

-   The APDU buffer contains the command sequence that will be sent to the card.
-   The APDUReply buffer contains data returned from the card after execution of the APDU command (this data is also referred to as the return APDU).

The following example shows a typical use of the **ISCardCmd** interface. The **ISCardCmd** interface is used to build an APDU.

**To submit a transaction to a specific card**

1.  Create an [**ISCard**](iscard.md) interface and connect to a smart card.
2.  Create an **ISCardCmd** interface.
3.  Build a smart card APDU command by using the [**ISCardISO7816**](iscardiso7816.md) interface or one of **ISCardCmd** build methods.
4.  Execute the command on the smart card by calling the appropriate [**ISCard**](iscard.md) interface method.
5.  Evaluate the returned response.
6.  Repeat the procedure as needed.
7.  Release the **ISCardCmd** interface and others as needed.

## Members

The **ISCardCmd** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ISCardCmd** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ISCardCmd** interface has these methods.



| Method                                       | Description                                                                                                |
|:---------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**BuildCmd**](iscardcmd-buildcmd.md)       | Constructs a valid command APDU for transmission to a smart card.<br/>                               |
| [**Clear**](iscardcmd-clear.md)             | Clears the APDU and the reply APDU message buffers.<br/>                                             |
| [**Encapsulate**](iscardcmd-encapsulate.md) | Encapsulates the given command APDU into another command APDU for transmission to a smart card.<br/> |



 

### Properties

The **ISCardCmd** interface has these properties.



| Property                                                              | Access type           | Description                                                                                                                                                         |
|:----------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AlternateClassId**](iscardcmd-get-alternateclassid.md)<br/> | Read/write<br/> | Current alternate class ID value.<br/>                                                                                                                        |
| [**Apdu**](iscardcmd-get-apdu.md)<br/>                         | Read/write<br/> | Raw [*application protocol data unit*](../secgloss/a-gly.md) (APDU).<br/> |
| [**ApduLength**](iscardcmd-get-apdulength.md)<br/>             | Read-only<br/>  | Length of the APDU.<br/>                                                                                                                                      |
| [**ApduReply**](iscardcmd-get-apdureply.md)<br/>               | Read/write<br/> | [*Reply APDU*](../secgloss/r-gly.md).<br/>                                                                        |
| [**ApduReplyLength**](iscardcmd-get-apdureplylength.md)<br/>   | Read/write<br/> | Length of the reply APDU.<br/>                                                                                                                                |
| [**ClassId**](iscardcmd-get-classid.md)<br/>                   | Read/write<br/> | Class ID of the APDU.<br/>                                                                                                                                    |
| [**Data**](iscardcmd-get-data.md)<br/>                         | Read-only<br/>  | Data field of the APDU.<br/>                                                                                                                                  |
| [**InstructionId**](iscardcmd-get-instructionid.md)<br/>       | Read/write<br/> | Instruction ID byte from the APDU.<br/>                                                                                                                       |
| [**LeField**](iscardcmd-get-lefield.md)<br/>                   | Read-only<br/>  | Le field of the APDU.<br/>                                                                                                                                    |
| [**Nad**](iscardcmd-put-nad.md)<br/>                           | Read/write<br/> | Node address.<br/>                                                                                                                                            |
| [**P1**](iscardcmd-get-p1.md)<br/>                             | Read/write<br/> | First parameter byte of the APDU.<br/>                                                                                                                        |
| [**P2**](iscardcmd-get-p2.md)<br/>                             | Read/write<br/> | Second parameter byte of the APDU.<br/>                                                                                                                       |
| [**P3**](iscardcmd-get-p3.md)<br/>                             | Read-only<br/>  | Third parameter byte of the APDU.<br/>                                                                                                                        |
| [**ReplyNad**](iscardcmd-get-replynad.md)<br/>                 | Read/write<br/> | Node address used by the card in the reply message.<br/>                                                                                                      |
| [**ReplyStatus**](iscardcmd-get-replystatus.md)<br/>           | Read/write<br/> | [*Reply APDU*](../secgloss/r-gly.md) message status word.<br/>                                                    |
| [**ReplyStatusSW1**](iscardcmd-get-replystatussw1.md)<br/>     | Read-only<br/>  | Reply APDU's message SW1 status byte.<br/>                                                                                                                    |
| [**ReplyStatusSW2**](iscardcmd-get-replystatussw2.md)<br/>     | Read-only<br/>  | Reply APDU's message SW2 status byte.<br/>                                                                                                                    |
| **Type**<br/>                                                   | Read-only<br/>  | Reserved for future use.<br/>                                                                                                                                 |



 

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
| IID<br/>                      | IID\_ISCardCmd is defined as D5778AE3-43DE-11D0-9171-00AA00C18068<br/>            |



 

 
