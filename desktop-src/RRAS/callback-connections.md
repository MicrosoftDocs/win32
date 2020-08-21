---
title: Callback Connections
description: RAS supports connections in which the remote server hangs up and then calls back to the client to establish the connection.
ms.assetid: 25f0e84d-8900-4efe-b07d-59f25186c976
ms.topic: article
ms.date: 05/31/2018
---

# Callback Connections

RAS supports connections in which the remote server hangs up and then calls back to the client to establish the connection.

For each user that can connect to a RAS server, the server stores a callback attribute that controls how the connection is made. The default attribute is No Callback, which means that the user can connect to the RAS server without a callback. Alternatively, the administrator of the RAS server can assign to a user either the Preset or Set-By-Caller callback attribute.

For a user assigned the Preset restriction, the administrator specifies a phone number that the RAS server must call back to establish a connection. The user cannot specify a different number, and the connection cannot be made without a callback.

A Preset callback operation is handled automatically by the Remote Access Connection Manager and the remote server. The RAS client application does not need to do anything other than provide feedback to the user when the notification handler is called during the various states of the callback operation.

A user assigned the Set By Caller privilege can choose to connect either with or without a callback. The [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call uses the **szCallbackNumber** member of the [**RASDIALPARAMS**](/previous-versions/windows/desktop/legacy/aa377238(v=vs.85)) structure to indicate the choice.

The **szCallbackNumber** member can simply specify the callback number; or, to establish the connection without a callback, **szCallbackNumber** can point to an empty string, "". In either of these cases, the Remote Access Connection Manager handles the connection operation automatically. As with a Preset callback operation, the RAS client does not need to perform any action other than to provide feedback to the user.

If the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call enables [paused states](paused-states.md), **szCallbackNumber** can point to an asterisk string, "\*", to indicate that the connection operation should enter a paused state to allow the user to type in the callback number. In this case, the connection operation for a Set By Caller user enters a paused state after the remote server has authenticated the user. During the paused state, the RAS client gets the callback number input from the user. The client then resumes the connection operation by making a second **RasDial** call in which **szCallbackNumber** specifies the number supplied by the user.

> [!Note]  
> If paused states are not enabled there is a different meaning when **szCallbackNumber** points to an asterisk string, "\*". In this case, the asterisk indicates that the callback number is stored in the phone-book file specified by the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call.

 

In the event of a callback, the call to [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) does not return until after the server has called back the client.

 

 