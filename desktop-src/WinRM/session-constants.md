---
title: Session Constants
description: The session constants in the \_\_WSManSessionFlags enumeration specify authentication and other information for WSMan.CreateSession or IWSMan CreateSession calls that connect to a remote computer.
ms.assetid: 5df52696-ac2c-42b7-8b0f-99a27b58575b
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Session Constants

The session constants in the **\_\_WSManSessionFlags** enumeration specify authentication and other information for [**WSMan.CreateSession**](wsman-createsession.md) or [**IWSMan::CreateSession**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsman-createsession) calls that connect to a remote computer. These constants are also closely related to **Winrm** command-line tool switches.

## Using Session Constants

You can set the Session flags for the call to [**WSMan.CreateSession**](wsman-createsession.md) in two different ways. One is shorter and simpler. The longer way, as is shown in the following example, is to locate the value of the flag you want to use and create a constant in your script with that value. Then the constant is used to set the value of the *iFlags* parameter.

``` syntax
Const SessionFlagUseNegotiate = 131072
Const SessionFlagCredUserNamePassword = 4096
iFlags = SessionFlagUseNegotiate Or SessionFlagCredUserNamePassword
```

The recommended way, as shown in the following example, is to use the [**WSMan**](wsman.md) object method associated with the flag.

``` syntax
iFlags = Wsman.SessionFlagUseNegotiate Or Wsman.SessionFlagCredUserNamePassword
```

<dl> <dt>

<span id="Authentication_Constants"></span><span id="authentication_constants"></span><span id="AUTHENTICATION_CONSTANTS"></span>[**Authentication Constants**](authentication-constants.md)
</dt> <dd>

Specify the authentication method and how to handle certificate servers.

</dd> <dt>

<span id="Other_Session_Constants"></span><span id="other_session_constants"></span><span id="OTHER_SESSION_CONSTANTS"></span>[**Other Session Constants**](other-session-constants.md)
</dt> <dd>

Specify the encoding, encryption, and service principal name port.

</dd> </dl>

## Related topics

<dl> <dt>

[WinRM Constants and Enumerations](winrm-constants-and-enumerations.md)
</dt> <dt>

[**WSMan.CreateSession**](wsman-createsession.md)
</dt> <dt>

[Authentication for Remote Connections](authentication-for-remote-connections.md)
</dt> </dl>

 

 




