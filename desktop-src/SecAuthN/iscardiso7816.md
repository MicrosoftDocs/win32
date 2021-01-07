---
description: The ISCardISO7816 interface provides methods for implementing ISO 7816-4 functionality.
ms.assetid: c940c44f-0556-48ef-91f4-502f4c0dfc02
title: ISCardISO7816 interface (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardISO7816
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardISO7816 interface

\[The **ISCardISO7816** interface is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **ISCardISO7816** interface provides methods for implementing ISO 7816-4 functionality. With the exception of [**SetDefaultClassId**](iscardiso7816-setdefaultclassid.md), these methods create an [*application protocol data unit*](../secgloss/a-gly.md) (APDU) command that is encapsulated in a [**ISCardCmd**](iscardcmd.md) object.

The ISO 7816-4 specification defines standard commands available on [*smart cards*](../secgloss/s-gly.md). The specification also defines how a smart card APDU command should be constructed and sent to the smart card for execution. This interface automates the building process.

The following example shows a typical use of the **ISCardISO7816** interface. In this case, the **ISCardISO7816** interface is used to build an APDU command.

**To submit a transaction to a specific card**

1.  Create an **ISCardISO7816** and [**ISCardCmd**](iscardcmd.md) interface.

    The [**ISCardCmd**](iscardcmd.md) interface is used to encapsulate the APDU.

2.  Call the appropriate method of the **ISCardISO7816** interface, passing the required parameters and the [**ISCardCmd**](iscardcmd.md) interface pointer.

    The ISO 7816-4 APDU command will be built and encapsulated in the [**ISCardCmd**](iscardcmd.md) interface.

3.  Release the **ISCardISO7816** and [**ISCardCmd**](iscardcmd.md) interfaces.

> [!Note]  
> In the method reference pages, if a bit sequence in a table is not defined, assume that bit sequence is reserved for future use or proprietary to a specific vendor.

 

## Members

The **ISCardISO7816** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ISCardISO7816** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISCardISO7816** interface has these methods.



| Method                                                             | Description                                                                                                                                                                                                                                                                                                        |
|:-------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AppendRecord**](iscardiso7816-appendrecord.md)                 | Constructs a command that appends a record to the end of an elementary file (EF).<br/>                                                                                                                                                                                                                       |
| [**EraseBinary**](iscardiso7816-erasebinary.md)                   | Sets part of the content of an EF to its logical erased state, sequentially, starting from a given offset.<br/>                                                                                                                                                                                              |
| [**ExternalAuthenticate**](iscardiso7816-externalauthenticate.md) | Conditionally updates the security status using the result of the computation by the card, based on a challenge previously issued by the card (for example, by the INS\_GET\_CHALLENGE command), a possibly secret key stored in the card, and authentication data transmitted by the interface device.<br/> |
| [**GetChallenge**](iscardiso7816-getchallenge.md)                 | Requires the issuing of a challenge for use in a security-related procedure.<br/>                                                                                                                                                                                                                            |
| [**GetData**](iscardiso7816-getdata.md)                           | Retrieves a single primitive data object or a set of data objects contained in a constructed data object, based on the type of file specified.<br/>                                                                                                                                                          |
| [**GetResponse**](iscardiso7816-getresponse.md)                   | Transmits from the card to the interface device APDUs that otherwise could not be transmitted by the available protocols.<br/>                                                                                                                                                                               |
| [**InternalAuthenticate**](iscardiso7816-internalauthenticate.md) | Initiates the computation of the authentication data by the card using the challenge data sent from the interface device and a relevant secret stored in the card.<br/>                                                                                                                                      |
| [**ManageChannel**](iscardiso7816-managechannel.md)               | Opens and closes logical channels.<br/>                                                                                                                                                                                                                                                                      |
| [**PutData**](iscardiso7816-putdata.md)                           | Stores one primitive data object, or one or more data objects contained in a constructed data object, within the current [*resource manager context*](../secgloss/r-gly.md).<br/>                                                    |
| [**ReadBinary**](iscardiso7816-readbinary.md)                     | Constructs a command that acquires a response message that gives that part of the contents of an EF with transparent structure.<br/>                                                                                                                                                                         |
| [**ReadRecord**](iscardiso7816-readrecord.md)                     | Constructs a command that reads the contents of the specified records of an elementary file.<br/>                                                                                                                                                                                                            |
| [**SelectFile**](iscardiso7816-selectfile.md)                     | Sets a current file within a logical channel.<br/>                                                                                                                                                                                                                                                           |
| [**SetDefaultClassId**](iscardiso7816-setdefaultclassid.md)       | Assigns a standard class ID byte that will be used in all operations when constructing an ISO 7816-4 command APDU.<br/>                                                                                                                                                                                      |
| [**UpdateBinary**](iscardiso7816-updatebinary.md)                 | Initiates the update of the bits already present in an EF with the bits given in the command APDU.<br/>                                                                                                                                                                                                      |
| [**UpdateRecord**](iscardiso7816-updaterecord.md)                 | Constructs a command that initiates the updating of a specific record.<br/>                                                                                                                                                                                                                                  |
| [**Verify**](iscardiso7816-verify.md)                             | Initiates the comparison in the card of the verification data sent from the interface device with the reference data stored in the card.<br/>                                                                                                                                                                |
| [**WriteBinary**](iscardiso7816-writebinary.md)                   | Initiates the writing of binary values into an EF.<br/>                                                                                                                                                                                                                                                      |
| [**WriteRecord**](iscardiso7816-writerecord.md)                   | Constructs a command that writes a record.<br/>                                                                                                                                                                                                                                                              |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardssp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardsrv.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardISO7816 is defined as 53B6AA68-3F56-11D0-916B-00AA00C18068<br/>        |



 

 
