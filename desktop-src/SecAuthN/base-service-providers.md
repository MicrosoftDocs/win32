---
description: These service providers provide the basic smart card capabilities.
ms.assetid: 1d887c4c-095c-4e1e-8b9a-7761acda2cbf
title: Base Service Providers
ms.topic: article
ms.date: 05/31/2018
---

# Base Service Providers

These [*service providers*](/windows/desktop/SecGloss/c-gly) provide the basic [*smart card*](/windows/desktop/SecGloss/s-gly) capabilities. They can be used to access a single smart card capability, or their COM interfaces can be combined to provide several capabilities within a single service provider. These service providers are the building blocks for developing additional functionality to other service providers.

The following tasks can be performed by base service provider interfaces supplied by the Smart Card SDK.



| Task                                                                                                                   | Base service provider interfaces         | DLL      |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------|----------|
| Connect to a smart card, implement transactions, close connections, and so on.                                         | [**ISCard**](iscard.md)                 | SCardSSP |
| Maintain a command APDU and [*reply APDU*](/windows/desktop/SecGloss/r-gly).          | [**ISCardCmd**](iscardcmd.md)           | SCardSSP |
| Query the [*smart card database*](/windows/desktop/SecGloss/s-gly). | [**ISCardDatabase**](iscarddatabase.md) | SCardSSP |
| Locate a smart card or reader.                                                                                         | [**ISCardLocate**](iscardlocate.md)     | SCardSSP |
| Build an ISO7816-4 command APDU.                                                                                       | [**ISCardISO7816**](iscardiso7816.md)   | SCardSSP |
| Wrap an Istream buffer by using Visual Basic–compatible types.                                                         | [**IByteBuffer**](ibytebuffer.md)       | SCardSSP |



 

The following procedure shows a typical use of these base service provider interfaces. In this example, the [**ISCard**](iscard.md), [**ISCardISO7816**](iscardiso7816.md), and [**ISCardCmd**](iscardcmd.md) interfaces are used to perform a transaction.

**To perform a transaction**

1.  Create an instance for all base service provider interfaces needed (for example, [**ISCard**](iscard.md), [**ISCardISO7816**](iscardiso7816.md), and [**ISCardCmd**](iscardcmd.md)).
2.  Connect to a particular smart card by using the methods in the [**ISCard**](iscard.md) interface.
3.  Using [**ISCardISO7816**](iscardiso7816.md) and an [**ISCardCmd**](iscardcmd.md) object, build an ISO 7816-4 command by calling the **ISCardISO7816** method. The command is contained in **ISCardCmd** as the command APDU.
4.  Do a transaction with the card by calling the [**ISCard**](iscard.md) transaction method and passing the created [**ISCardCmd**](iscardcmd.md) object. When the transaction is complete, the results are stored in the **ISCardCmd** reply APDU.
5.  Interpret the [**ISCardCmd**](iscardcmd.md) reply APDU and repeat.
6.  Release all interfaces when operations are complete.

For information about the APDU command built within the DLLs, see [Building an ISO7816-4 APDU Command](building-an-iso7816-4-apdu-command.md).

 

 
