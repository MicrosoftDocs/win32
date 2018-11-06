---
title: IAgentNotifySinkEx ListeningState
description: IAgentNotifySinkEx ListeningState
ms.assetid: e303b299-0dd0-419a-87a9-1490fe6cf54a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySinkEx::ListeningState

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT ListeningState(
   long dwCharacterID,  // character ID
   long bListening,     // listening mode state
   long dwCause         // cause  
);
```

Notifies a client application when the Listening mode changes.

-   No return value.

<dl> <dt>

<span id="dwCharacterID"></span><span id="dwcharacterid"></span><span id="DWCHARACTERID"></span>*dwCharacterID*
</dt> <dd>

The character for which the listening state changed.

</dd> <dt>

<span id="bListening"></span><span id="blistening"></span><span id="BLISTENING"></span>*bListening*
</dt> <dd>

The Listening mode state. **True** indicates that Listening mode has started; **False**, that Listening mode has ended.

</dd> <dt>

<span id="dwCause"></span><span id="dwcause"></span><span id="DWCAUSE"></span>*dwCause*
</dt> <dd>

The cause for the event, which may be one of the following values.



| Value                                                                             | Description                                                                    |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **const unsigned long** **LSCOMPLETE\_CAUSE\_PROGRAMDISABLED = 1;**<br/>    | Listening mode was turned off by program code.                                 |
| **const unsigned long** **LSCOMPLETE\_CAUSE\_PROGRAMTIMEDOUT = 2;**<br/>    | Listening mode (turned on by program code) timed out.                          |
| **const unsigned long** **LSCOMPLETE\_CAUSE\_USERTIMEDOUT = 3;**<br/>       | Listening mode (turned on by the Listening key) timed out.                     |
| **const unsigned long** **LSCOMPLETE\_CAUSE\_USERRELEASEDKEY = 4;**<br/>    | Listening mode was turned off because the user released the Listening key.     |
| **const unsigned long** **LSCOMPLETE\_CAUSE\_USERUTTERANCEENDED = 5;**<br/> | Listening mode was turned off because the user finished speaking.              |
| **const unsigned long** **LSCOMPLETE\_CAUSE\_CLIENTDEACTIVATED = 6;**<br/>  | Listening mode was turned off because the input active client was deactivated. |
| **const unsigned long** **LSCOMPLETE\_CAUSE\_DEFAULTCHARCHANGE = 7**<br/>   | Listening mode was turned off because the default character was changed.       |
| **const unsigned long** **LSCOMPLETE\_CAUSE\_USERDISABLED = 8**<br/>        | Listening mode was turned off because the user disabled speech input.          |



 

</dd> </dl>

This event is sent to all clients when the Listening mode begins after the user presses the Listening key or when its time-out ends, or when the input-active client calls the [**IAgentCharacterEx::Listen**](iagentcharacterex--listen.md) method with **True** or **False**.

The event returns values to the clients that currently have this character loaded. All other clients receive a null character (empty string).

## See Also

[**IAgentCharacterEx::Listen**](iagentcharacterex--listen.md)


 

 





