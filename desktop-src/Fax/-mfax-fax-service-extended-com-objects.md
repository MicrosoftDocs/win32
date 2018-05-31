---
Description: The fax service extended Component Object Model (COM) objects fall into the following functional groupings. For a list of the objects, see Alphabetic List of COM Objects.
ms.assetid: e68f6ef6-a126-4fce-b1b3-4611080f3ace
title: Fax Service Extended COM Objects
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Service Extended COM Objects

The fax service extended Component Object Model (COM) objects fall into the following functional groupings. For a list of the objects, see [Alphabetic List of COM Objects](#alphabetic-list-of-com-objects).

-   [Root Object](#root-object)
-   [Messaging Objects](#messaging-objects)
-   [Configuration Objects](#configuration-objects)
-   [Notification Objects](#notification-objects)
-   [Alphabetic List of COM Objects](#alphabetic-list-of-com-objects)

For more information, see [Fax Service Extended COM Object Model](-mfax-fax-service-extended-com-object-model.md).

> [!Note]  
> There are fax objects and methods that will not function in Windows XP Home Edition, Windows XP Professional, Windows Vista Business, Windows Vista Enterprise, and Windows Vista Ultimate, as follows:

 

-   [**ConnectedSubmit**](-mfax-faxdocument-connectedsubmit.md) and [**IFaxDocument::Submit**](/previous-versions/windows/desktop/api/FaxComex/) are not supported for a remote connection to a fax server that is running on Windows XP Home Edition or Windows XP Professional, Windows Vista Business, Windows Vista Enterprise or Windows Vista Ultimate.
-   Windows Vista Business, Windows Vista Enterprise, Windows Vista Ultimate, Windows XP Home Edition and Windows XP Professional do not support the sending of delivery receipts. If you set [**IFaxReceiptOptions::get\_UseForInboundRouting**](/previous-versions/windows/desktop/api/FaxComex/) equal to **TRUE**, the [**IFaxReceiptOptions::Save**](/previous-versions/windows/desktop/api/FaxComex/) method will fail.
-   Windows Vista Business, Windows Vista Enterprise, Windows Vista Ultimate, Windows XP Home Edition and Windows XP Professional do not support outbound routing features. The [**FaxOutboundRouting**](-mfax-faxoutboundrouting.md) object and its subordinate objects are therefore not available for programmatic use.
-   You cannot add inbound routing extensions to the fax service running on Windows XP Home Edition or Windows XP Professional, Windows Vista Business, Windows Vista Enterprise or Windows Vista Ultimate. Therefore, [**IFaxServer::RegisterInboundRoutingExtension**](/previous-versions/windows/desktop/api/FaxComex/) is not available.
-   You cannot reassign inbox faxes on Windows Vista Business, Windows Vista Enterprise or Windows Vista Ultimate.

If you use any of the methods that are unavailable, you will receive a [FAX\_E\_NOT\_SUPPORTED\_ON\_THIS\_SKU](-mfax-fax-error-codes.md) error.

## Root Object

A fax client application must create an instance of a [**FaxServer**](-mfax-faxserver.md) object and connect to an active fax server before accessing most other fax service extended COM objects. After you obtain a connection, you can create other messaging objects and configuration objects you need.

You do not have to create the [**FaxServer**](-mfax-faxserver.md) object to send a single fax using the [**FaxDocument**](-mfax-faxdocument.md) object.



| Object                               | Description                                                                                                                                                                                                                                             |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxServer**](-mfax-faxserver.md) | Permits a fax client application to connect to and disconnect from an active fax server. After you obtain a connection to a fax server, you can create the other objects you need to manage fax jobs, view fax archives, and configure the fax service. |



 

## Messaging Objects

Includes objects used to create, track, and manage fax documents, messages, and jobs.



| Object                                                                 | Description                                                                                           |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**FaxDocument**](-mfax-faxdocument.md)                               | Permits a fax client application to compose and submit a new fax message to one or more recipients.   |
| [**FaxIncomingJob**](-mfax-faxincomingjob.md)                         | Describes an individual incoming fax job in a fax server's queue.                                     |
| [**FaxIncomingJobs**](-mfax-faxincomingjobs.md)                       | Contains a collection of incoming fax jobs in a fax server's queue.                                   |
| [**FaxIncomingMessage**](-mfax-faxincomingmessage.md)                 | Describes an individual message in the archived inbound fax messages that were successfully received. |
| [**FaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator.md) | Forward iterator for archived fax messages that were successfully received.                           |
| [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)                         | Describes an individual outbound fax job in a fax server's queue.                                     |
| [**FaxOutgoingJobs**](-mfax-faxoutgoingjobs.md)                       | Contains a collection of outbound fax jobs in a fax server's queue.                                   |
| [**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md)                 | Describes an individual message in the archived fax messages that were successfully transmitted.      |
| [**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md) | Forward iterator for archived fax messages that were successfully transmitted.                        |
| [**FaxRecipient**](-mfax-faxrecipient.md)                             | Contains information about an individual fax recipient.                                               |
| [**FaxRecipients**](-mfax-faxrecipients.md)                           | A collection of objects containing information about the recipients of a fax transmission.            |
| [**FaxSender**](-mfax-faxsender.md)                                   | Contains information about an individual fax sender.                                                  |



 

## Configuration Objects

Includes objects used to configure the fax service.



| Object                                                                                  | Description                                                                                                       |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [**FaxActivity**](-mfax-faxactivity.md)                                                | Permits reporting of the activity and status of a fax server.                                                     |
| [**FaxActivityLogging**](-mfax-faxactivitylogging.md)                                  | Permits configuration of the activity logging options that the fax service uses.                                  |
| [**FaxDevice**](-mfax-faxdevice.md)                                                    | Represents a single fax device on a fax server.                                                                   |
| [**FaxDeviceIds**](-mfax-faxdeviceids.md)                                              | Contains an ordered collection of fax device IDs.                                                                 |
| [**FaxDeviceProvider**](-mfax-faxdeviceprovider.md)                                    | Represents an individual fax device provider on a fax server.                                                     |
| [**FaxDeviceProviders**](-mfax-faxdeviceproviders.md)                                  | Contains a collection of the fax device providers on a fax server.                                                |
| [**FaxDevices**](-mfax-faxdevices.md)                                                  | Contains a collection of fax devices.                                                                             |
| [**FaxEventLogging**](-mfax-faxeventlogging.md)                                        | Permits configuration of the event logging categories that the fax service uses.                                  |
| [**FaxFolders**](-mfax-faxfolders.md)                                                  | Permits users to access the folders, jobs, and messages on a fax server.                                          |
| [**FaxInboundRouting**](-mfax-faxinboundrouting.md)                                    | Permits access to an inbound fax routing extension and its methods.                                               |
| [**FaxInboundRoutingExtension**](-mfax-faxinboundroutingextension.md)                  | Represents an individual fax routing extension on a fax server.                                                   |
| [**FaxInboundRoutingExtensions**](-mfax-faxinboundroutingextensions.md)                | Contains a collection of the fax routing extensions on a fax server.                                              |
| [**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md)                        | Represents an individual fax routing method on a fax server.                                                      |
| [**FaxInboundRoutingMethods**](-mfax-faxinboundroutingmethods.md)                      | Contains an ordered collection of fax routing methods.                                                            |
| [**FaxIncomingArchive**](-mfax-faxincomingarchive.md)                                  | Permits configuration of parameters related to the archived inbound faxes on a fax server.                        |
| [**FaxIncomingQueue**](-mfax-faxincomingqueue.md)                                      | Permits configuration of the inbound fax queue on a fax server.                                                   |
| [**FaxLoggingOptions**](-mfax-faxloggingoptions.md)                                    | Permits configuration of both the activity logging options and the event logging categories the fax service uses. |
| [**FaxOutboundRouting**](-mfax-faxoutboundrouting.md)                                  | Permits users to configure outbound routing groups and rules.                                                     |
| [**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md)                        | Represents an individual outbound routing group.                                                                  |
| [**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md)                      | Contains a collection of the outbound routing groups on a fax server.                                             |
| [**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md)                          | Represents an individual outbound fax routing rule.                                                               |
| [**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md)                        | Contains a collection of outbound fax routing rules.                                                              |
| [**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md)                                  | Permits configuration of parameters related to the archived inbound faxes on a fax server.                        |
| [**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md)                                      | Permits configuration of the outbound queue on a fax server.                                                      |
| [**FaxReceiptOptions**](-mfax-faxreceiptoptions.md)                                    | Permits setting and retrieving the mail configuration the fax service uses to send fax receipts.                  |
| [**FaxSecurity**](-mfax-faxsecurity.md) and [**FaxSecurity2**](-mfax-faxsecurity2.md) | Represents the security configuration on a fax server.                                                            |
| [**FaxConfiguration**](-mfax-faxconfiguration.md)                                      | Represents various objects that provide configuration options for the fax service.                                |



 

## Notification Objects

Includes objects for event notification callbacks.



| Object                                               | Description                                                                                                                                                                                |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IFaxServerNotify**](/previous-versions/windows/desktop/api/FaxComex/)   | [**FaxServer**](-mfax-faxserver.md) interface used for fax notifications. For more information, see [Registering for Event Notifications](-mfax-registering-for-event-notifications.md). |
| [**FaxJobStatus**](-mfax-faxjobstatus.md)           | Retrieves dynamic information about a fax job.                                                                                                                                             |
| [**IFaxServerNotify2**](/previous-versions/windows/desktop/api/FaxComex/) | Used for fax notifications. For more information, see Registering for Event Notifications.                                                                                                 |
| [**IFaxAccountNotify**](/previous-versions/windows/desktop/api/FaxComex/) | [**FaxAccount**](-mfax-faxaccount.md) interface used for fax account notifications. For more information, see Registering for Event Notifications.                                        |



 

## Alphabetic List of COM Objects

The fax service extended COM object model includes the following objects, listed alphabetically:

-   [**FaxAccount**](-mfax-faxaccount.md)
-   [**FaxAccountFolders**](-mfax-faxaccountfolders.md)
-   [**FaxAccountIncomingArchive**](-mfax-faxaccountincomingarchive.md)
-   [**FaxAccountIncomingQueue**](-mfax-faxaccountincomingqueue.md)
-   [**FaxAccountNotify (interface)**](/previous-versions/windows/desktop/api/FaxComex/)
-   [**FaxAccountOutgoingArchive**](-mfax-faxaccountoutgoingarchive.md)
-   [**FaxAccountOutgoingQueue**](-mfax-faxaccountoutgoingqueue.md)
-   [**FaxAccounts**](-mfax-faxaccounts.md)
-   [**FaxAccountSet**](-mfax-faxaccountset.md)
-   [**FaxActivity**](-mfax-faxactivity.md)
-   [**FaxActivityLogging**](-mfax-faxactivitylogging.md)
-   [**FaxDevice**](-mfax-faxdevice.md)
-   [**FaxDeviceIds**](-mfax-faxdeviceids.md)
-   [**FaxDeviceProvider**](-mfax-faxdeviceprovider.md)
-   [**FaxDeviceProviders**](-mfax-faxdeviceproviders.md)
-   [**FaxDevices**](-mfax-faxdevices.md)
-   [**FaxDocument**](-mfax-faxdocument.md)
-   [**FaxEventLogging**](-mfax-faxeventlogging.md)
-   [**FaxFolders**](-mfax-faxfolders.md)
-   [**FaxInboundRouting**](-mfax-faxinboundrouting.md)
-   [**FaxInboundRoutingExtension**](-mfax-faxinboundroutingextension.md)
-   [**FaxInboundRoutingExtensions**](-mfax-faxinboundroutingextensions.md)
-   [**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md)
-   [**FaxInboundRoutingMethods**](-mfax-faxinboundroutingmethods.md)
-   [**FaxIncomingArchive**](-mfax-faxincomingarchive.md)
-   [**FaxIncomingJob**](-mfax-faxincomingjob.md)
-   [**FaxIncomingJobs**](-mfax-faxincomingjobs.md)
-   [**FaxIncomingMessage**](-mfax-faxincomingmessage.md)
-   [**FaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator.md)
-   [**FaxIncomingQueue**](-mfax-faxincomingqueue.md)
-   [**FaxJobStatus**](-mfax-faxjobstatus.md)
-   [**FaxLoggingOptions**](-mfax-faxloggingoptions.md)
-   [**FaxOutboundRouting**](-mfax-faxoutboundrouting.md)
-   [**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md)
-   [**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md)
-   [**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md)
-   [**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md)
-   [**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md)
-   [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
-   [**FaxOutgoingJobs**](-mfax-faxoutgoingjobs.md)
-   [**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md)
-   [**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md)
-   [**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md)
-   [**FaxReceiptOptions**](-mfax-faxreceiptoptions.md)
-   [**FaxRecipient**](-mfax-faxrecipient.md)
-   [**FaxRecipients**](-mfax-faxrecipients.md)
-   [**FaxSecurity**](-mfax-faxsecurity.md)
-   [**FaxSecurity2**](-mfax-faxsecurity2.md)
-   [**FaxSender**](-mfax-faxsender.md)
-   [**FaxServer**](-mfax-faxserver.md)
-   [**FaxServerNotify (interface)**](/previous-versions/windows/desktop/api/FaxComex/)
-   [**FaxServerNotify2 (interface)**](/previous-versions/windows/desktop/api/FaxComex/)

 

 



