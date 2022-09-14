---
title: Change Notifications in Active Directory Domain Services
description: Active Directory Domain Services provide a mechanism for a client application to register with a domain controller to receive change notifications.
ms.assetid: 27f6c7c1-b32e-457a-9be5-47836d097ab1
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Change Notifications in Active Directory Domain Services

Active Directory Domain Services provide a mechanism for a client application to register with a domain controller to receive change notifications. To do this, the client specifies the LDAP change notification control in an asynchronous LDAP search operation. The client also specifies the following search parameters.



| Parameter             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope<br/>      | Specify either **LDAP\_SCOPE\_BASE** to monitor just the object, or **LDAP\_SCOPE\_ONELEVEL** to monitor the immediate children of the object, not including the object itself. Do not specify **LDAP\_SCOPE\_SUBTREE**. Although the subtree scope is supported if the base object is the root of a naming context, its use can severely impact server performance, because it generates an LDAP search result message every time an object in the naming context is modified. You cannot specify **LDAP\_SCOPE\_SUBTREE** for an arbitrary subtree.<br/> |
| Filter<br/>     | Specify a search filter of "(objectclass=\*)", which means you receive notifications for changes to any object in the specified scope.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                |
| Attributes<br/> | Specify a list of attributes to return when a change occurs. Be aware that you receive notifications when any attribute is modified, not just the specified attributes.<br/>                                                                                                                                                                                                                                                                                                                                                                               |



 

You can register up to five notification requests on a single LDAP connection. You must have a dedicated thread that waits for the notifications and processes them quickly. When you call the ldap\_search\_ext function to register a notification request, the function returns a message identifier that identifies that request. You then use the [**ldap\_result**](/previous-versions/windows/desktop/api/winldap/nf-winldap-ldap_result) function to wait for change notifications. When a change occurs, the server sends you an LDAP message that contains the message identifier for the notification request that generated the notification. This causes the **ldap\_result** function to return with search results that identify the object that changed.

The client application must determine the initial state of the object monitored. To do this, you must first register the notification request and then read the current state.

The client application must also determine the cause of the change. For a base level search, a notification occurs when any attribute changes, or when the object is deleted or moved. For a one-level search, a notification occurs when a child object is created, deleted, moved, or modified. Be aware that moving or renaming an object in the hierarchy above a target object does not generate a notification even though the distinguished name of the target changed as a result. For example, if monitoring changes to the child objects in a container, you will not receive notifications if the container itself is moved or renamed.

When the client processes the search results, it can use the ldap\_get\_dn function to get the distinguished name of the object that changed. Do not rely on distinguished names to identify the objects tracked, because distinguished names can change. Instead, include the **objectGUID** attribute in the list of attributes to retrieve. Each object's **objectGUID** remains unchanged regardless of where the object is moved within the enterprise forest.

If an object within the search scope is deleted, the client receives a change notification and the **isDeleted** attribute of the object is set to **TRUE**. In this case, the search results report the new distinguished name of the object in the Deleted Objects container of its partition. It is not necessary to specify the tombstone control ([LDAP\_SERVER\_SHOW\_DELETED\_OID](/previous-versions/windows/desktop/ldap/ldap-server-show-deleted-oid)) to get notifications of object deletions. For more information, see [Retrieving Deleted Objects](retrieving-deleted-objects.md).

When a client has registered a notification request, the client continues to receive notifications until the connection is broken or the client abandons the search by calling the ldap\_abandon function. If the client or server disconnects, for example, if the server fails, the notification request is terminated. When the client reconnects, it must register for notifications again, and then read the current state of the objects of interest in case there were changes while the client was disconnected.

The client can use the value of an object's **uSNChanged** attribute to determine whether the current state of the object on the server reflects the latest changes that the client has received. The system increases an object's **uSNChanged** attribute when the object is moved or modified. For example, if the server fails and the directory partition is restored from a backup, the server's replica of an object may not reflect changes previously reported to the client, in which case the **uSNChanged** value on the server will be lower than the value stored by the client.

For more information and a code example that uses the LDAP change notification control in an asynchronous LDAP search operation, see [Example Code for Receiving Change Notifications](example-code-for-receiving-change-notifications.md).

For more information about when to use the LDAP change notification control, see [Overview of Change Tracking Techniques](overview-of-change-tracking-techniques.md).

 

