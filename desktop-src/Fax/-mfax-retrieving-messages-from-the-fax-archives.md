---
Description: 'A fax archive can hold potentially hundreds of thousands of fax messages.'
ms.assetid: 'b7fd8059-34ae-408c-a807-8b826b394d09'
title: Retrieving Messages from the Fax Archives
---

# Retrieving Messages from the Fax Archives

A fax archive can hold potentially hundreds of thousands of fax messages. Because fax archives tend to get large, the fax service extended Component Object Model (COM) implementation does not expose the contents of the fax archives as a collection of fax messages. Instead, you can either retrieve an individual message from the archive using its message ID or access messages in the archive in a sequential manner by using a forward-iterating cursor object.

**Using a message ID.** If you need to retrieve an individual fax message, and you know the message's ID, you can access the message directly in the archive without creating an iterator object. For more information, see [**FaxIncomingArchive**](-mfax-faxincomingarchive.md), [**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md), [**IFaxIncomingArchive::GetMessage**](-mfax-faxincomingarchive-cpp-mfax-faxincomingarchive-getmessage-cpp.md), and [**GetMessage**](-mfax-faxoutgoingarchive-getmessage.md). For Windows Vista, see [**FaxAccountIncomingArchive**](-mfax-faxaccountincomingarchive.md), [**FaxAccountOutgoingArchive**](-mfax-faxaccountoutgoingarchive.md), [**IFaxAccountIncomingArchive::GetMessage**](-mfax-faxaccountincomingarchive-cpp-mfax-faxaccountincomingarchive-getmessage-cpp.md), and [**IFaxAccountOutgoingArchive::GetMessage**](-mfax-faxaccountoutgoingarchive-cpp-mfax-faxaccountoutgoingarchive-getmessage-cpp.md).

**Using a forward-iterating cursor.** If you do not know a particular fax message's ID, if you need to scan the archive, or if you need to access multiple messages in the archive, use the [**FaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator.md) and [**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md) objects that the extended fax COM implementation provides. These objects are called forward iterators because the functionality they provide is unidirectional movement through the fax archive, from beginning to end, one message at a time. The access these objects provide is called cursor-based because you can access only one message at a time, the message where you position the archive cursor. The **FaxIncomingMessageIterator** and **FaxOutgoingMessageIterator** interfaces include methods to set the archive cursor at the first message in the archive, to move the archive cursor to the next message in the archive, and to retrieve the properties of the message under the archive cursor. The interfaces also include a method to retrieve the **AtEOF** property (the end-of-file marker) for the archive.

To determine the size of the archive, after you create an iterator object, position the archive cursor at the first message in the archive. Then continue to move through the succeeding messages in a sequential manner, counting the messages as you go, until you reach the end of the archive.

For more information, see [Fax Folders](-mfax-fax-folders.md). The Microsoft Visual Basic example [Opening a Fax from the Outgoing Archive](-mfax-opening-a-fax-from-the-outgoing-archive.md) demonstrates how to use the message iterator.

 

 



