---
description: There are five types of events that can be logged. All of these have well-defined common data and can optionally include event-specific data.
ms.assetid: 4ab4a284-a4cd-4cf7-a9d2-e4a75fce01b9
title: Event Types
ms.topic: article
ms.date: 05/31/2018
---

# Event Types

There are five types of events that can be logged. All of these have well-defined common data and can optionally include event-specific data.

The application indicates the event type when it reports an event. Each event must be of a single type. The Event Viewer displays a different icon for each type in the list view of the event log.

The following table describes the five event types used in event logging.



| Event type        | Description                                                                                                                                                                                                                                                                                              |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Error**         | An event that indicates a significant problem such as loss of data or loss of functionality. For example, if a service fails to load during startup, an Error event is logged.                                                                                                                           |
| **Warning**       | An event that is not necessarily significant, but may indicate a possible future problem. For example, when disk space is low, a Warning event is logged. If an application can recover from an event without loss of functionality or data, it can generally classify the event as a Warning event.     |
| **Information**   | An event that describes the successful operation of an application, driver, or service. For example, when a network driver loads successfully, it may be appropriate to log an Information event. Note that it is generally inappropriate for a desktop application to log an event each time it starts. |
| **Success Audit** | An event that records an audited security access attempt that is successful. For example, a user's successful attempt to log on to the system is logged as a Success Audit event.                                                                                                                        |
| **Failure Audit** | An event that records an audited security access attempt that fails. For example, if a user tries to access a network drive and fails, the attempt is logged as a Failure Audit event.                                                                                                                   |



 

Selected activities of users can be tracked by auditing security events and then placing entries in a computer's security log.

 

 



