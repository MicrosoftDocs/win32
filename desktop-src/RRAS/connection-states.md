---
title: Connection States
description: During the process of connecting to a remote server, the Remote Access Connection Manager and the RAS server on the remote computer perform several steps to establish the connection.
ms.assetid: 7a8b0086-308b-47d2-888e-69ff473c6015
ms.topic: article
ms.date: 05/31/2018
---

# Connection States

During the process of connecting to a remote server, the Remote Access Connection Manager and the RAS server on the remote computer perform several steps to establish the connection. Each of these steps is identified by a connection state. The [**RASCONNSTATE**](/previous-versions/windows/desktop/legacy/aa376727(v=vs.85)) enumeration is a set of values that correspond to these connection states. The connection states can be divided into the following three groups:

<dl> <dt>

<span id="Running_states"></span><span id="running_states"></span><span id="RUNNING_STATES"></span>Running states
</dt> <dd>

The running states are the parts of the connection operation that RAS handles automatically, such as connecting to the necessary devices, authenticating the user, and waiting for a callback from the remote server. Unless an error occurs, the RAS client need take no action other than to pass the notification on to the user.

</dd> <dt>

<span id="Paused_states"></span><span id="paused_states"></span><span id="PAUSED_STATES"></span>Paused states
</dt> <dd>

The [paused states](paused-states.md) occur when the remote server pauses the connection operation to get additional input from the user. During a paused state, the user can type a [callback](callback-connections.md) number, a different user name and password if the user authentication fails, or a new password if the old one has expired.

</dd> <dt>

<span id="Terminal_states"></span><span id="terminal_states"></span><span id="TERMINAL_STATES"></span>Terminal states
</dt> <dd>

The terminal states occur when the connection has been successfully established, the connection operation has failed, or the connection has been broken by a [**RasHangUp**](/windows/desktop/api/Ras/nf-ras-rashangupa) call.

</dd> </dl>

There are several mechanisms that a RAS client can use to determine the current state of a connection operation. When a RAS client executes the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function asynchronously, the Remote Access Connection Manager sends progress notifications to the client's [notification handler](notification-handlers.md) whenever the connection state changes. In addition, the client can use the [**RasGetConnectStatus**](/windows/desktop/api/Ras/nf-ras-rasgetconnectstatusa) function to get the current state of any RAS connection operation.

 

 