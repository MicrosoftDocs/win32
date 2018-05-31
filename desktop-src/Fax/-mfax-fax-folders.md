---
Description: The fax service provides four folders that allow you to manage incoming and outgoing faxes.
ms.assetid: 60cc6263-cfd0-431c-8346-22ca3f374916
title: Fax Folders
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Folders

The fax service provides four folders that allow you to manage incoming and outgoing faxes.

-   The incoming queue, represented by the [**FaxIncomingQueue**](-mfax-faxincomingqueue.md) object (and [**FaxAccountIncomingQueue**](-mfax-faxaccountincomingqueue.md) object in Windows Vista)
-   The outgoing queue, represented by the [**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md) object (and [**FaxAccountOutgoingQueue**](-mfax-faxaccountoutgoingqueue.md) object in Windows Vista)
-   The incoming archive, represented by the [**FaxIncomingArchive**](-mfax-faxincomingarchive.md) object (and [**FaxAccountIncomingArchive**](-mfax-faxaccountincomingarchive.md) object in Windows Vista)
-   The outgoing archive, represented by the [**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md) object (and [**FaxAccountOutgoingArchive**](-mfax-faxaccountoutgoingarchive.md) object in Windows Vista)

## Fax Queues

A fax queue is a collection of faxes that the fax service is processing. Faxes in a queue are referred to as fax *jobs*.

The fax service provides two fax queues, an *incoming* queue and an *outgoing* queue. The incoming queue contains faxes that the fax service is receiving, known as incoming jobs. The outgoing queue contains faxes that the fax service is sending, or will attempt to send, known as outgoing jobs.

For more information about queues, see the [**FaxIncomingQueue**](-mfax-faxincomingqueue.md), [**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md), [**FaxIncomingJob**](-mfax-faxincomingjob.md), and [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md) objects.

In Windows Vista, refer to the [**FaxAccountIncomingQueue**](-mfax-faxaccountincomingqueue.md), [**FaxAccountOutgoingQueue**](-mfax-faxaccountoutgoingqueue.md), [**FaxIncomingJob**](-mfax-faxincomingjob.md), and [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md) objects.

## Fax Archives

A fax *archive* is a collection of faxes that the fax service has processed successfully. Faxes in an archive are referred to as fax messages.

The fax service provides two fax archives, an incoming archive and an outgoing archive. The incoming archive contains faxes that the fax service has received successfully, known as incoming messages. The outgoing archive contains faxes that the fax service has sent successfully, known as outgoing messages.

For more information, see the [**FaxIncomingArchive**](-mfax-faxincomingarchive.md), [**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md), [**FaxIncomingMessage**](-mfax-faxincomingmessage.md), and [**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md) objects (In Windows Vista, refer to [**FaxAccountIncomingArchive**](-mfax-faxaccountincomingarchive.md), [**FaxAccountOutgoingArchive**](-mfax-faxaccountoutgoingarchive.md), [**FaxIncomingMessage**](-mfax-faxincomingmessage.md), and [**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md) objects) and the following topics:

-   [Archived Broadcast Messages](-mfax-archived-broadcast-messages.md)
-   [Retrieving Messages from the Fax Archives](-mfax-retrieving-messages-from-the-fax-archives.md)

The archiving of fax messages is optional, and can be set using the [**IFaxIncomingArchive::get\_UseArchive**](-mfax-faxincomingarchive-cpp-mfax-faxincomingarchive-usearchive-cpp.md) and [**IFaxOutgoingArchive::get\_UseArchive**](-mfax-faxoutgoingarchive-cpp-mfax-faxoutgoingarchive-usearchive-cpp.md) methods. (In Windows Vista, [**IFaxConfiguration:UseArchive**](-mfax-ifaxconfiguration-usearchive.md) method.)

## Archived Message Iterator

The Fax Service Extended Component Object Model (COM) implementation does not expose fax archives as a collection of fax messages. This is because fax archives tend to get large. Instead, the service uses a forward-iterating cursor object to access individual messages in the archive. For more information, see [**FaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator.md) and [**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md).

 

 



