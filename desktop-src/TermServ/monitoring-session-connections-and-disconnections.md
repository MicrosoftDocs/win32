---
title: Monitoring session connections and disconnections
description: To register an application with Remote Desktop Services, store the name of the virtual channel server application in the registry by adding a subkey.
ms.assetid: 8524cb7a-a930-431a-bc5f-b0793781de15
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring session connections and disconnections

For a service application, such as a virtual channel server application, to monitor session connections and disconnections, you must register it with Remote Desktop Services. To register the application with Remote Desktop Services, store the name of the virtual channel server application in the registry by adding a subkey under the following location:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**TerminalServer**\\**Addins**

The subkey can have any name. It must have a **REG\_SZ** value, **Name**, that contains the symbolic name of the application.

``` syntax
Name = AddinName
```

The maximum length of both the subkey and the value of **Name** is 99 characters.

The subkey must also have a **REG\_DWORD** value that indicates the type of server application.

``` syntax
Type = AddinType
```

*AddinType* must be the following value.



| Value | Meaning                               |
|-------|---------------------------------------|
| 3     | User-mode application, session space. |



 

Registration of the service application takes effect only in sessions created after the registration was performed.

For each registered service application, Remote Desktop Services will signal a set of event objects when a client connects or disconnects from the session. Each virtual channel plug-in must register itself and create the notification events by calling [**CreateEvent**](/windows/desktop/api/synchapi/nf-synchapi-createeventa). The names of these event objects adhere to the following format.

``` syntax
AddinName-Reconnect

AddinName-Disconnect
```

*AddinName* is the string specified in the **Name** value of the registry subkey under which the server application is registered. Creating these events under a session causes them to be created in a special per-session event directory. The event directory provides added security by preventing applications in other sessions from modifying the state of these events.

To control whether RECONNECT and DISCONNECT events are received on the server, you can place the **RemoteControlPersistent** flag in the registry under the following key:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**TerminalServer**\\**Addins**\\*addinname*

The flag enables or disables RECONNECT and DISCONNECT events from being signaled when a client session starts or stops. The syntax of the **REG\_DWORD** value is the following.

``` syntax
RemoteControlPersistent = flag
```

The value of *flag* can be one or zero. Zero is the default value. If set to one, the service application will not be notified if the client session is started or stopped. If set to zero, a RECONNECT event is signaled when the client session starts, and a DISCONNECT event is signaled when the client session stops.

The previous event-object name format is still supported in Windows Server 2008 for backward compatibility. It is recommended that you use the newer Windows Server 2008 format because it is more secure.

The previous event format is as follows.

``` syntax
Global\AddinName-SessionId-Reconnect
 
Global\AddinName-SessionId-Disconnect
```

*AddinName* is the string specified in the **Name** value of the registry subkey under which the server application is registered. *SessionId* is the session identifier of a client session.

 

 