---
title: Overview of Change Tracking Techniques
description: There are several ways that change tracking mechanisms can differ Scope for tracking changes An application can track changes to a single attribute of a single object, to all objects in a domain, and so on.
ms.assetid: 7359e851-61b7-420d-beb0-f7f33f79b007
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Change Tracking Techniques

There are several ways that change tracking mechanisms can differ:

-   Scope for tracking changes: An application can track changes to a single attribute of a single object, to all objects in a domain, and so on. If the mechanism matches the requirements of the application, the application receives a minimum of irrelevant data, and thus this enhances performance.
-   Timeliness: An application is notified of every change as it happens, or can be notified of the net effect of changes over a period of minutes or hours.

    Processing less timely data may be more efficient, because several changes may be collapsed into one. For example, if an attribute changes three times within a one hour interval, an application notified of changes accumulated over an hour will be notified of just one attribute change, not three.

    When thinking about timeliness, consider the effect of replication latency. An update that originates on one domain controller does not replicate to another domain controller instantly. Requiring change-tracking timeliness much better than the expected replication latency often gives no real benefit to the application.

-   Polling versus notification: With polling, an application periodically makes a request to a domain controller to receive change tracking data. With notification the domain controller sends changes to the application only when changes occur.

    The overhead of polling is obvious: The application may request change tracking data when nothing significant has occurred. The overhead of notification is more subtle. The server must maintain data about notification requests and must consult this data to decide whether or not to send a notification. This can add overhead to normal update requests.

-   Expressing the application's knowledge: persistent versus temporary: Every change tracking mechanism must include some method for the server holding the data tracked to understand the application's state of knowledge, so that the idea of "change" is well defined. For example, the application's state of knowledge might be expressed as "Updated with all changes that occurred on DC d before time t." A mechanism based on this way of expressing an application's state of knowledge would provide an efficient way for the application to obtain changes that have occurred later than a specified time.

    If the expression of the application's knowledge can be persisted, that is, stored recoverably, as in a file or database, application restart is less resource intensive than if it cannot. In the example above, the expression of the application's knowledge can be persisted by recording the DC d and the time t. Some change notification mechanisms do not allow this data to be persisted. The server and application must synchronize with some other mechanism when the application starts. This is resource-intensive if multiple objects are involved, and can involve complex programming.

Use the following techniques to track changes in Active Directory Domain Services:

-   Use the change notification control to initiate a persistent asynchronous search for changes that match a specified filter. For more information, see [Change Notifications in Active Directory Domain Services](change-notifications-in-active-directory-domain-services.md).
-   Use a directory synchronization (DirSync) search to retrieve changes that have occurred since the previous DirSync search. For more information, see [Polling for Changes Using the DirSync Control](polling-for-changes-using-the-dirsync-control.md).
-   Use the USNChanged attribute to search for objects that have changed since the previous search. For more information, see [Polling for Changes Using USNChanged](polling-for-changes-using-usnchanged.md).

The change notification control is designed for applications or services that require reasonably prompt notification of infrequent changes. An example is a service or program that stores configuration data on the Active Directory server and must be notified promptly when a change occurs. Be aware that there are limitations of the notification control.

-   The promptness of notifications depends on replication latency and where the change occurred. You may be notified promptly when a change replicates into the replica you are monitoring, but the change may have originated much earlier on some other replica.
-   The control is restricted to monitoring a single object or the immediate children of a container. Applications that must monitor multiple containers or unrelated objects can register up to five notification requests.
-   If too many clients are listening for changes that occur frequently, it will impact the performance of the server. In general, applications should limit their use of this control for performance reasons on the server. If you do not need to know about changes immediately, it may be best to periodically poll for changes instead of using change notification.

The DirSync and USNChanged search techniques are designed for applications that maintain consistency between data on the Active Directory server and corresponding data in some other storage. These techniques are used by applications that periodically poll for changes. The DirSync technique is based on an LDAP server control that you can use through ADSI or LDAP APIs. The disadvantages of the DirSync control are that it can only be used by a highly privileged account, such as a domain administrator. The following is a list of limitations of DirSync control:

-   The DirSync control can only be used by a highly privileged account, such as a domain administrator.
-   The DirSync control can only monitor an entire naming context. You cannot limit the scope of a DirSync search to monitor only a specific subtree, container, or object in a naming context.

The USNChanged technique does not have these limitations, although it is somewhat more complicated to use than DirSync.

 

 




