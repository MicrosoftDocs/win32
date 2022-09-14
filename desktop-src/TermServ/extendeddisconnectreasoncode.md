---
title: ExtendedDisconnectReasonCode enumeration
description: Defines extended information about the control's reason for disconnection.
ms.assetid: E73E73B4-6C6B-4270-A1BD-947FA6D7B31B
ms.tgt_platform: multiple
keywords:
- ExtendedDisconnectReasonCode enumeration Remote Desktop Services
topic_type:
- apiref
api_name:
- ExtendedDisconnectReasonCode
api_location:
- MsTscAx.dll
api_type:
- LibDef
ms.topic: reference
ms.date: 05/31/2018
---

# ExtendedDisconnectReasonCode enumeration

Defines extended information about the control's reason for disconnection.

## Syntax


```C++
typedef enum _ExtendedDisconnectReasonCode { 
  exDiscReasonNoInfo                            = 0,
  exDiscReasonAPIInitiatedDisconnect            = 1,
  exDiscReasonAPIInitiatedLogoff                = 2,
  exDiscReasonServerIdleTimeout                 = 3,
  exDiscReasonServerLogonTimeout                = 4,
  exDiscReasonReplacedByOtherConnection         = 5,
  exDiscReasonOutOfMemory                       = 6,
  exDiscReasonServerDeniedConnection            = 7,
  exDiscReasonServerDeniedConnectionFips        = 8,
  exDiscReasonServerInsufficientPrivileges      = 9,
  exDiscReasonServerFreshCredsRequired          = 10,
  exDiscReasonRpcInitiatedDisconnectByUser      = 11,
  exDiscReasonLogoffByUser                      = 2,
  exDiscReasonLicenseInternal                   = 256,
  exDiscReasonLicenseNoLicenseServer            = 257,
  exDiscReasonLicenseNoLicense                  = 258,
  exDiscReasonLicenseErrClientMsg               = 259,
  exDiscReasonLicenseHwidDoesntMatchLicense     = 260,
  exDiscReasonLicenseErrClientLicense           = 261,
  exDiscReasonLicenseCantFinishProtocol         = 262,
  exDiscReasonLicenseClientEndedProtocol        = 263,
  exDiscReasonLicenseErrClientEncryption        = 264,
  exDiscReasonLicenseCantUpgradeLicense         = 265,
  exDiscReasonLicenseNoRemoteConnections        = 266,
  exDiscReasonLicenseCreatingLicStoreAccDenied  = 267,
  exDiscReasonRdpEncInvalidCredentials          = 768,
  exDiscReasonProtocolRangeStart                = 4096,
  exDiscReasonProtocolRangeEnd                  = 32767
} ExtendedDisconnectReasonCode;
```



## Constants

<dl> <dt>

<span id="exDiscReasonNoInfo"></span><span id="exdiscreasonnoinfo"></span><span id="EXDISCREASONNOINFO"></span>**exDiscReasonNoInfo**
</dt> <dd>

No additional information is available.

</dd> <dt>

<span id="exDiscReasonAPIInitiatedDisconnect"></span><span id="exdiscreasonapiinitiateddisconnect"></span><span id="EXDISCREASONAPIINITIATEDDISCONNECT"></span>**exDiscReasonAPIInitiatedDisconnect**
</dt> <dd>

An application initiated the disconnection.

</dd> <dt>

<span id="exDiscReasonAPIInitiatedLogoff"></span><span id="exdiscreasonapiinitiatedlogoff"></span><span id="EXDISCREASONAPIINITIATEDLOGOFF"></span>**exDiscReasonAPIInitiatedLogoff**
</dt> <dd>

An application logged off the client.

</dd> <dt>

<span id="exDiscReasonServerIdleTimeout"></span><span id="exdiscreasonserveridletimeout"></span><span id="EXDISCREASONSERVERIDLETIMEOUT"></span>**exDiscReasonServerIdleTimeout**
</dt> <dd>

The server has disconnected the client because the client has been idle for a period of time longer than the designated time-out period.

</dd> <dt>

<span id="exDiscReasonServerLogonTimeout"></span><span id="exdiscreasonserverlogontimeout"></span><span id="EXDISCREASONSERVERLOGONTIMEOUT"></span>**exDiscReasonServerLogonTimeout**
</dt> <dd>

The server has disconnected the client because the client has exceeded the period designated for connection.

</dd> <dt>

<span id="exDiscReasonReplacedByOtherConnection"></span><span id="exdiscreasonreplacedbyotherconnection"></span><span id="EXDISCREASONREPLACEDBYOTHERCONNECTION"></span>**exDiscReasonReplacedByOtherConnection**
</dt> <dd>

The client's connection was replaced by another connection.

</dd> <dt>

<span id="exDiscReasonOutOfMemory"></span><span id="exdiscreasonoutofmemory"></span><span id="EXDISCREASONOUTOFMEMORY"></span>**exDiscReasonOutOfMemory**
</dt> <dd>

No memory is available.

</dd> <dt>

<span id="exDiscReasonServerDeniedConnection"></span><span id="exdiscreasonserverdeniedconnection"></span><span id="EXDISCREASONSERVERDENIEDCONNECTION"></span>**exDiscReasonServerDeniedConnection**
</dt> <dd>

The server denied the connection.

</dd> <dt>

<span id="exDiscReasonServerDeniedConnectionFips"></span><span id="exdiscreasonserverdeniedconnectionfips"></span><span id="EXDISCREASONSERVERDENIEDCONNECTIONFIPS"></span>**exDiscReasonServerDeniedConnectionFips**
</dt> <dd>

The server denied the connection for security reasons.

</dd> <dt>

<span id="exDiscReasonServerInsufficientPrivileges"></span><span id="exdiscreasonserverinsufficientprivileges"></span><span id="EXDISCREASONSERVERINSUFFICIENTPRIVILEGES"></span>**exDiscReasonServerInsufficientPrivileges**
</dt> <dd>

The server denied the connection for security reasons.

</dd> <dt>

<span id="exDiscReasonServerFreshCredsRequired"></span><span id="exdiscreasonserverfreshcredsrequired"></span><span id="EXDISCREASONSERVERFRESHCREDSREQUIRED"></span>**exDiscReasonServerFreshCredsRequired**
</dt> <dd>

Fresh credentials are required.

</dd> <dt>

<span id="exDiscReasonRpcInitiatedDisconnectByUser"></span><span id="exdiscreasonrpcinitiateddisconnectbyuser"></span><span id="EXDISCREASONRPCINITIATEDDISCONNECTBYUSER"></span>**exDiscReasonRpcInitiatedDisconnectByUser**
</dt> <dd>

User activity has initiated the disconnect.

</dd> <dt>

<span id="exDiscReasonLogoffByUser"></span><span id="exdiscreasonlogoffbyuser"></span><span id="EXDISCREASONLOGOFFBYUSER"></span>**exDiscReasonLogoffByUser**
</dt> <dd>

The user logged off, disconnecting the session.

</dd> <dt>

<span id="exDiscReasonLicenseInternal"></span><span id="exdiscreasonlicenseinternal"></span><span id="EXDISCREASONLICENSEINTERNAL"></span>**exDiscReasonLicenseInternal**
</dt> <dd>

Internal licensing error.

</dd> <dt>

<span id="exDiscReasonLicenseNoLicenseServer"></span><span id="exdiscreasonlicensenolicenseserver"></span><span id="EXDISCREASONLICENSENOLICENSESERVER"></span>**exDiscReasonLicenseNoLicenseServer**
</dt> <dd>

No license server was available.

</dd> <dt>

<span id="exDiscReasonLicenseNoLicense"></span><span id="exdiscreasonlicensenolicense"></span><span id="EXDISCREASONLICENSENOLICENSE"></span>**exDiscReasonLicenseNoLicense**
</dt> <dd>

No valid software license was available.

</dd> <dt>

<span id="exDiscReasonLicenseErrClientMsg"></span><span id="exdiscreasonlicenseerrclientmsg"></span><span id="EXDISCREASONLICENSEERRCLIENTMSG"></span>**exDiscReasonLicenseErrClientMsg**
</dt> <dd>

The remote computer received a licensing message that was not valid.

</dd> <dt>

<span id="exDiscReasonLicenseHwidDoesntMatchLicense"></span><span id="exdiscreasonlicensehwiddoesntmatchlicense"></span><span id="EXDISCREASONLICENSEHWIDDOESNTMATCHLICENSE"></span>**exDiscReasonLicenseHwidDoesntMatchLicense**
</dt> <dd>

The hardware ID does not match the one designated on the software license.

</dd> <dt>

<span id="exDiscReasonLicenseErrClientLicense"></span><span id="exdiscreasonlicenseerrclientlicense"></span><span id="EXDISCREASONLICENSEERRCLIENTLICENSE"></span>**exDiscReasonLicenseErrClientLicense**
</dt> <dd>

Client license error.

</dd> <dt>

<span id="exDiscReasonLicenseCantFinishProtocol"></span><span id="exdiscreasonlicensecantfinishprotocol"></span><span id="EXDISCREASONLICENSECANTFINISHPROTOCOL"></span>**exDiscReasonLicenseCantFinishProtocol**
</dt> <dd>

Network problems occurred during the licensing protocol.

</dd> <dt>

<span id="exDiscReasonLicenseClientEndedProtocol"></span><span id="exdiscreasonlicenseclientendedprotocol"></span><span id="EXDISCREASONLICENSECLIENTENDEDPROTOCOL"></span>**exDiscReasonLicenseClientEndedProtocol**
</dt> <dd>

The client ended the licensing protocol prematurely.

</dd> <dt>

<span id="exDiscReasonLicenseErrClientEncryption"></span><span id="exdiscreasonlicenseerrclientencryption"></span><span id="EXDISCREASONLICENSEERRCLIENTENCRYPTION"></span>**exDiscReasonLicenseErrClientEncryption**
</dt> <dd>

A licensing message was encrypted incorrectly.

</dd> <dt>

<span id="exDiscReasonLicenseCantUpgradeLicense"></span><span id="exdiscreasonlicensecantupgradelicense"></span><span id="EXDISCREASONLICENSECANTUPGRADELICENSE"></span>**exDiscReasonLicenseCantUpgradeLicense**
</dt> <dd>

The local computer's client access license could not be upgraded or renewed.

</dd> <dt>

<span id="exDiscReasonLicenseNoRemoteConnections"></span><span id="exdiscreasonlicensenoremoteconnections"></span><span id="EXDISCREASONLICENSENOREMOTECONNECTIONS"></span>**exDiscReasonLicenseNoRemoteConnections**
</dt> <dd>

The remote computer is not licensed to accept remote connections.

</dd> <dt>

<span id="exDiscReasonLicenseCreatingLicStoreAccDenied"></span><span id="exdiscreasonlicensecreatinglicstoreaccdenied"></span><span id="EXDISCREASONLICENSECREATINGLICSTOREACCDENIED"></span>**exDiscReasonLicenseCreatingLicStoreAccDenied**
</dt> <dd>

An access denied error was received while creating a registry key for the license store.

</dd> <dt>

<span id="exDiscReasonRdpEncInvalidCredentials"></span><span id="exdiscreasonrdpencinvalidcredentials"></span><span id="EXDISCREASONRDPENCINVALIDCREDENTIALS"></span>**exDiscReasonRdpEncInvalidCredentials**
</dt> <dd>

Invalid credentials were encountered.

</dd> <dt>

<span id="exDiscReasonProtocolRangeStart"></span><span id="exdiscreasonprotocolrangestart"></span><span id="EXDISCREASONPROTOCOLRANGESTART"></span>**exDiscReasonProtocolRangeStart**
</dt> <dd>

Beginning the range of internal protocol errors. Check the server event log for additional details.

</dd> <dt>

<span id="exDiscReasonProtocolRangeEnd"></span><span id="exdiscreasonprotocolrangeend"></span><span id="EXDISCREASONPROTOCOLRANGEEND"></span>**exDiscReasonProtocolRangeEnd**
</dt> <dd>

Ending the range of internal protocol errors.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExtendedDisconnectReason**](imsrdpclient-extendeddisconnectreason.md)
</dt> </dl>

 

 





