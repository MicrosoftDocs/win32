---
title: OnConnectionTerminated event
description: Called when the clients connection to the server is closed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ea3d3651-3968-40db-bdb3-b812695dc596
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnConnectionTerminated event RDP
topic_type:
- apiref
api_name:
- OnConnectionTerminated
api_location:
- RdpEncom.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnConnectionTerminated event

Called when the client's connection to the server is closed.

## Syntax


```C++
void OnConnectionTerminated(
  [in] long discReason,
  [in] long ExtendedInfo
);
```



## Parameters

<dl> <dt>

*discReason* \[in\]
</dt> <dd>

Reason why the client's connection to the server was closed. The connection was closed for one of the following reasons:

<dt>

<span id="NoInfo"></span><span id="noinfo"></span><span id="NOINFO"></span>

<span id="NoInfo"></span><span id="noinfo"></span><span id="NOINFO"></span>**NoInfo** (0)


</dt> <dd>

No information is available.

</dd> <dt>

<span id="LocalNotError"></span><span id="localnoterror"></span><span id="LOCALNOTERROR"></span>

<span id="LocalNotError"></span><span id="localnoterror"></span><span id="LOCALNOTERROR"></span>**LocalNotError** (1)


</dt> <dd>

Local disconnection. This is not an error code.

</dd> <dt>

<span id="RemoteByUser"></span><span id="remotebyuser"></span><span id="REMOTEBYUSER"></span>

<span id="RemoteByUser"></span><span id="remotebyuser"></span><span id="REMOTEBYUSER"></span>**RemoteByUser** (2)


</dt> <dd>

Remote disconnection by user. This is not an error code.

</dd> <dt>

<span id="ByServer"></span><span id="byserver"></span><span id="BYSERVER"></span>

<span id="ByServer"></span><span id="byserver"></span><span id="BYSERVER"></span>**ByServer** (3)


</dt> <dd>

Remote disconnection by server. This is not an error code.

</dd> <dt>

<span id="DNSLookupFailed"></span><span id="dnslookupfailed"></span><span id="DNSLOOKUPFAILED"></span>

<span id="DNSLookupFailed"></span><span id="dnslookupfailed"></span><span id="DNSLOOKUPFAILED"></span>**DNSLookupFailed** (260)


</dt> <dd>

DNS name lookup failure.

</dd> <dt>

<span id="OutOfMemory"></span><span id="outofmemory"></span><span id="OUTOFMEMORY"></span>

<span id="OutOfMemory"></span><span id="outofmemory"></span><span id="OUTOFMEMORY"></span>**OutOfMemory** (262)


</dt> <dd>

Out of memory.

</dd> <dt>

<span id="ConnectionTimedOut"></span><span id="connectiontimedout"></span><span id="CONNECTIONTIMEDOUT"></span>

<span id="ConnectionTimedOut"></span><span id="connectiontimedout"></span><span id="CONNECTIONTIMEDOUT"></span>**ConnectionTimedOut** (264)


</dt> <dd>

Connection timed out.

</dd> <dt>

<span id="SocketConnectFailed"></span><span id="socketconnectfailed"></span><span id="SOCKETCONNECTFAILED"></span>

<span id="SocketConnectFailed"></span><span id="socketconnectfailed"></span><span id="SOCKETCONNECTFAILED"></span>**SocketConnectFailed** (516)


</dt> <dd>

Windows Sockets [**connect**](https://msdn.microsoft.com/library/windows/desktop/ms737625) failed.

</dd> <dt>

<span id="OutOfMemory2"></span><span id="outofmemory2"></span><span id="OUTOFMEMORY2"></span>

<span id="OutOfMemory2"></span><span id="outofmemory2"></span><span id="OUTOFMEMORY2"></span>**OutOfMemory2** (518)


</dt> <dd>

Out of memory.

</dd> <dt>

<span id="HostNotFound"></span><span id="hostnotfound"></span><span id="HOSTNOTFOUND"></span>

<span id="HostNotFound"></span><span id="hostnotfound"></span><span id="HOSTNOTFOUND"></span>**HostNotFound** (520)


</dt> <dd>

Host not found error.

</dd> <dt>

<span id="WinsockSendFailed"></span><span id="winsocksendfailed"></span><span id="WINSOCKSENDFAILED"></span>

<span id="WinsockSendFailed"></span><span id="winsocksendfailed"></span><span id="WINSOCKSENDFAILED"></span>**WinsockSendFailed** (772)


</dt> <dd>

Windows Sockets [**send**](https://msdn.microsoft.com/library/windows/desktop/ms740149) call failed.

</dd> <dt>

<span id="OutOfMemory3"></span><span id="outofmemory3"></span><span id="OUTOFMEMORY3"></span>

<span id="OutOfMemory3"></span><span id="outofmemory3"></span><span id="OUTOFMEMORY3"></span>**OutOfMemory3** (774)


</dt> <dd>

Out of memory.

</dd> <dt>

<span id="InvalidIPAddr"></span><span id="invalidipaddr"></span><span id="INVALIDIPADDR"></span>

<span id="InvalidIPAddr"></span><span id="invalidipaddr"></span><span id="INVALIDIPADDR"></span>**InvalidIPAddr** (776)


</dt> <dd>

Invalid IP address specified.

</dd> <dt>

<span id="SocketRecvFailed"></span><span id="socketrecvfailed"></span><span id="SOCKETRECVFAILED"></span>

<span id="SocketRecvFailed"></span><span id="socketrecvfailed"></span><span id="SOCKETRECVFAILED"></span>**SocketRecvFailed** (1028)


</dt> <dd>

Windows Sockets [**recv**](https://msdn.microsoft.com/library/windows/desktop/ms740121) call failed.

</dd> <dt>

<span id="InvalidSecurityData"></span><span id="invalidsecuritydata"></span><span id="INVALIDSECURITYDATA"></span>

<span id="InvalidSecurityData"></span><span id="invalidsecuritydata"></span><span id="INVALIDSECURITYDATA"></span>**InvalidSecurityData** (1030)


</dt> <dd>

Invalid security data.

</dd> <dt>

<span id="InternalError"></span><span id="internalerror"></span><span id="INTERNALERROR"></span>

<span id="InternalError"></span><span id="internalerror"></span><span id="INTERNALERROR"></span>**InternalError** (1032)


</dt> <dd>

Internal error.

</dd> <dt>

<span id="InvalidEncryption"></span><span id="invalidencryption"></span><span id="INVALIDENCRYPTION"></span>

<span id="InvalidEncryption"></span><span id="invalidencryption"></span><span id="INVALIDENCRYPTION"></span>**InvalidEncryption** (1286)


</dt> <dd>

Invalid encryption method specified.

</dd> <dt>

<span id="DNSLookupFailed2"></span><span id="dnslookupfailed2"></span><span id="DNSLOOKUPFAILED2"></span>

<span id="DNSLookupFailed2"></span><span id="dnslookupfailed2"></span><span id="DNSLOOKUPFAILED2"></span>**DNSLookupFailed2** (1288)


</dt> <dd>

DNS lookup failed.

</dd> <dt>

<span id="GetHostByNameFailed"></span><span id="gethostbynamefailed"></span><span id="GETHOSTBYNAMEFAILED"></span>

<span id="GetHostByNameFailed"></span><span id="gethostbynamefailed"></span><span id="GETHOSTBYNAMEFAILED"></span>**GetHostByNameFailed** (1540)


</dt> <dd>

Windows Sockets [**gethostbyname**](https://msdn.microsoft.com/library/windows/desktop/ms738524) call failed.

</dd> <dt>

<span id="InvalidServerSecurityInfo"></span><span id="invalidserversecurityinfo"></span><span id="INVALIDSERVERSECURITYINFO"></span>

<span id="InvalidServerSecurityInfo"></span><span id="invalidserversecurityinfo"></span><span id="INVALIDSERVERSECURITYINFO"></span>**InvalidServerSecurityInfo** (1542)


</dt> <dd>

Invalid server security data.

</dd> <dt>

<span id="TimerError"></span><span id="timererror"></span><span id="TIMERERROR"></span>

<span id="TimerError"></span><span id="timererror"></span><span id="TIMERERROR"></span>**TimerError** (1544)


</dt> <dd>

Internal timer error.

</dd> <dt>

<span id="NoTimeoutOccurred"></span><span id="notimeoutoccurred"></span><span id="NOTIMEOUTOCCURRED"></span>

<span id="NoTimeoutOccurred"></span><span id="notimeoutoccurred"></span><span id="NOTIMEOUTOCCURRED"></span>**NoTimeoutOccurred** (1796)


</dt> <dd>

Time-out occurred.

</dd> <dt>

<span id="ServerCertificateUnpackErr"></span><span id="servercertificateunpackerr"></span><span id="SERVERCERTIFICATEUNPACKERR"></span>

<span id="ServerCertificateUnpackErr"></span><span id="servercertificateunpackerr"></span><span id="SERVERCERTIFICATEUNPACKERR"></span>**ServerCertificateUnpackErr** (1798)


</dt> <dd>

Failed to unpack server certificate.

</dd> <dt>

<span id="InvalidIP"></span><span id="invalidip"></span><span id="INVALIDIP"></span>

<span id="InvalidIP"></span><span id="invalidip"></span><span id="INVALIDIP"></span>**InvalidIP** (2052)


</dt> <dd>

Bad IP address specified.

</dd> <dt>

<span id="LicensingFailed"></span><span id="licensingfailed"></span><span id="LICENSINGFAILED"></span>

<span id="LicensingFailed"></span><span id="licensingfailed"></span><span id="LICENSINGFAILED"></span>**LicensingFailed** (2056)


</dt> <dd>

License negotiation failed.

</dd> <dt>

<span id="InternalSecurityError"></span><span id="internalsecurityerror"></span><span id="INTERNALSECURITYERROR"></span>

<span id="InternalSecurityError"></span><span id="internalsecurityerror"></span><span id="INTERNALSECURITYERROR"></span>**InternalSecurityError** (2310)


</dt> <dd>

Internal security error.

</dd> <dt>

<span id="AtClientWinsockFDCLOSE"></span><span id="atclientwinsockfdclose"></span><span id="ATCLIENTWINSOCKFDCLOSE"></span>

<span id="AtClientWinsockFDCLOSE"></span><span id="atclientwinsockfdclose"></span><span id="ATCLIENTWINSOCKFDCLOSE"></span>**AtClientWinsockFDCLOSE** (2308)


</dt> <dd>

Socket closed.

</dd> <dt>

<span id="LicensingTimeout"></span><span id="licensingtimeout"></span><span id="LICENSINGTIMEOUT"></span>

<span id="LicensingTimeout"></span><span id="licensingtimeout"></span><span id="LICENSINGTIMEOUT"></span>**LicensingTimeout** (2312)


</dt> <dd>

Licensing time-out.

</dd> <dt>

<span id="InternalSecurityError2"></span><span id="internalsecurityerror2"></span><span id="INTERNALSECURITYERROR2"></span>

<span id="InternalSecurityError2"></span><span id="internalsecurityerror2"></span><span id="INTERNALSECURITYERROR2"></span>**InternalSecurityError2** (2566)


</dt> <dd>

Internal security error.

</dd> <dt>

<span id="EncryptionError"></span><span id="encryptionerror"></span><span id="ENCRYPTIONERROR"></span>

<span id="EncryptionError"></span><span id="encryptionerror"></span><span id="ENCRYPTIONERROR"></span>**EncryptionError** (2822)


</dt> <dd>

Encryption error.

</dd> <dt>

<span id="DecryptionError"></span><span id="decryptionerror"></span><span id="DECRYPTIONERROR"></span>

<span id="DecryptionError"></span><span id="decryptionerror"></span><span id="DECRYPTIONERROR"></span>**DecryptionError** (3078)


</dt> <dd>

Decryption error.

</dd> <dt>

<span id="ClientDecompressionError"></span><span id="clientdecompressionerror"></span><span id="CLIENTDECOMPRESSIONERROR"></span>

<span id="ClientDecompressionError"></span><span id="clientdecompressionerror"></span><span id="CLIENTDECOMPRESSIONERROR"></span>**ClientDecompressionError** (3080)


</dt> <dd>

Decompression error.

</dd> </dl> </dd> <dt>

*ExtendedInfo* \[in\]
</dt> <dd>

Additional information as to why the connection was closed. Possible values include the following:

<dt>

<span id="NoInfo"></span><span id="noinfo"></span><span id="NOINFO"></span>

<span id="NoInfo"></span><span id="noinfo"></span><span id="NOINFO"></span>**NoInfo** (0x0000)


</dt> <dd>

No additional information is available.

</dd> <dt>

<span id="APIInitiatedDisconnect"></span><span id="apiinitiateddisconnect"></span><span id="APIINITIATEDDISCONNECT"></span>

<span id="APIInitiatedDisconnect"></span><span id="apiinitiateddisconnect"></span><span id="APIINITIATEDDISCONNECT"></span>**APIInitiatedDisconnect** (0x0001)


</dt> <dd>

An application initiated the disconnection.

</dd> <dt>

<span id="APIInitiatedLogoff"></span><span id="apiinitiatedlogoff"></span><span id="APIINITIATEDLOGOFF"></span>

<span id="APIInitiatedLogoff"></span><span id="apiinitiatedlogoff"></span><span id="APIINITIATEDLOGOFF"></span>**APIInitiatedLogoff** (0x0002)


</dt> <dd>

An application logged off the client.

</dd> <dt>

<span id="ServerIdleTimeout"></span><span id="serveridletimeout"></span><span id="SERVERIDLETIMEOUT"></span>

<span id="ServerIdleTimeout"></span><span id="serveridletimeout"></span><span id="SERVERIDLETIMEOUT"></span>**ServerIdleTimeout** (0x0003)


</dt> <dd>

The server has disconnected the client because the client has been idle for a period of time longer than the designated time-out period.

</dd> <dt>

<span id="ServerLogonTimeout"></span><span id="serverlogontimeout"></span><span id="SERVERLOGONTIMEOUT"></span>

<span id="ServerLogonTimeout"></span><span id="serverlogontimeout"></span><span id="SERVERLOGONTIMEOUT"></span>**ServerLogonTimeout** (0x0004)


</dt> <dd>

The server has disconnected the client because the client has exceeded the period designated for connection.

</dd> <dt>

<span id="ReplacedByOtherConnection"></span><span id="replacedbyotherconnection"></span><span id="REPLACEDBYOTHERCONNECTION"></span>

<span id="ReplacedByOtherConnection"></span><span id="replacedbyotherconnection"></span><span id="REPLACEDBYOTHERCONNECTION"></span>**ReplacedByOtherConnection** (0x0005)


</dt> <dd>

The client's connection was replaced by another connection.

</dd> <dt>

<span id="OutOfMemory"></span><span id="outofmemory"></span><span id="OUTOFMEMORY"></span>

<span id="OutOfMemory"></span><span id="outofmemory"></span><span id="OUTOFMEMORY"></span>**OutOfMemory** (0x0006)


</dt> <dd>

No memory is available.

</dd> <dt>

<span id="ServerDeniedConnection"></span><span id="serverdeniedconnection"></span><span id="SERVERDENIEDCONNECTION"></span>

<span id="ServerDeniedConnection"></span><span id="serverdeniedconnection"></span><span id="SERVERDENIEDCONNECTION"></span>**ServerDeniedConnection** (0x0007)


</dt> <dd>

The server denied the connection.

</dd> <dt>

<span id="ServerDeniedConnectionFips"></span><span id="serverdeniedconnectionfips"></span><span id="SERVERDENIEDCONNECTIONFIPS"></span>

<span id="ServerDeniedConnectionFips"></span><span id="serverdeniedconnectionfips"></span><span id="SERVERDENIEDCONNECTIONFIPS"></span>**ServerDeniedConnectionFips** (0x0008)


</dt> <dd>

The server denied the connection for security reasons.

</dd> <dt>

<span id="ServerInsufficientPrivileges"></span><span id="serverinsufficientprivileges"></span><span id="SERVERINSUFFICIENTPRIVILEGES"></span>

<span id="ServerInsufficientPrivileges"></span><span id="serverinsufficientprivileges"></span><span id="SERVERINSUFFICIENTPRIVILEGES"></span>**ServerInsufficientPrivileges** (0x0009)


</dt> <dd>

The connection was denied because the user account is not authorized for remote logon.

</dd> <dt>

<span id="LicenseInternal"></span><span id="licenseinternal"></span><span id="LICENSEINTERNAL"></span>

<span id="LicenseInternal"></span><span id="licenseinternal"></span><span id="LICENSEINTERNAL"></span>**LicenseInternal** (0x0100)


</dt> <dd>

Internal licensing error.

</dd> <dt>

<span id="LicenseNoLicenseServer"></span><span id="licensenolicenseserver"></span><span id="LICENSENOLICENSESERVER"></span>

<span id="LicenseNoLicenseServer"></span><span id="licensenolicenseserver"></span><span id="LICENSENOLICENSESERVER"></span>**LicenseNoLicenseServer** (0x0101)


</dt> <dd>

No license server was available.

</dd> <dt>

<span id="LicenseNoLicense"></span><span id="licensenolicense"></span><span id="LICENSENOLICENSE"></span>

<span id="LicenseNoLicense"></span><span id="licensenolicense"></span><span id="LICENSENOLICENSE"></span>**LicenseNoLicense** (0x0102)


</dt> <dd>

No valid software license was available.

</dd> <dt>

<span id="LicenseErrClientMsg"></span><span id="licenseerrclientmsg"></span><span id="LICENSEERRCLIENTMSG"></span>

<span id="LicenseErrClientMsg"></span><span id="licenseerrclientmsg"></span><span id="LICENSEERRCLIENTMSG"></span>**LicenseErrClientMsg** (0x0103)


</dt> <dd>

The remote computer received an invalid licensing message.

</dd> <dt>

<span id="LicenseHwidDoesntMatchLicense"></span><span id="licensehwiddoesntmatchlicense"></span><span id="LICENSEHWIDDOESNTMATCHLICENSE"></span>

<span id="LicenseHwidDoesntMatchLicense"></span><span id="licensehwiddoesntmatchlicense"></span><span id="LICENSEHWIDDOESNTMATCHLICENSE"></span>**LicenseHwidDoesntMatchLicense** (0x0104)


</dt> <dd>

The hardware ID does not match the one designated on the software license.

</dd> <dt>

<span id="LicenseErrClientLicense"></span><span id="licenseerrclientlicense"></span><span id="LICENSEERRCLIENTLICENSE"></span>

<span id="LicenseErrClientLicense"></span><span id="licenseerrclientlicense"></span><span id="LICENSEERRCLIENTLICENSE"></span>**LicenseErrClientLicense** (0x0105)


</dt> <dd>

Client license error.

</dd> <dt>

<span id="LicenseCantFinishProtocol"></span><span id="licensecantfinishprotocol"></span><span id="LICENSECANTFINISHPROTOCOL"></span>

<span id="LicenseCantFinishProtocol"></span><span id="licensecantfinishprotocol"></span><span id="LICENSECANTFINISHPROTOCOL"></span>**LicenseCantFinishProtocol** (0x0106)


</dt> <dd>

Network problems occurred during the licensing protocol.

</dd> <dt>

<span id="LicenseClientEndedProtocol"></span><span id="licenseclientendedprotocol"></span><span id="LICENSECLIENTENDEDPROTOCOL"></span>

<span id="LicenseClientEndedProtocol"></span><span id="licenseclientendedprotocol"></span><span id="LICENSECLIENTENDEDPROTOCOL"></span>**LicenseClientEndedProtocol** (0x0107)


</dt> <dd>

The client ended the licensing protocol prematurely.

</dd> <dt>

<span id="LicenseErrClientEncryption"></span><span id="licenseerrclientencryption"></span><span id="LICENSEERRCLIENTENCRYPTION"></span>

<span id="LicenseErrClientEncryption"></span><span id="licenseerrclientencryption"></span><span id="LICENSEERRCLIENTENCRYPTION"></span>**LicenseErrClientEncryption** (0x0108)


</dt> <dd>

A licensing message was encrypted incorrectly.

</dd> <dt>

<span id="LicenseCantUpgradeLicense"></span><span id="licensecantupgradelicense"></span><span id="LICENSECANTUPGRADELICENSE"></span>

<span id="LicenseCantUpgradeLicense"></span><span id="licensecantupgradelicense"></span><span id="LICENSECANTUPGRADELICENSE"></span>**LicenseCantUpgradeLicense** (0x0109)


</dt> <dd>

The local computer's client access license could not be upgraded or renewed.

</dd> <dt>

<span id="LicenseNoRemoteConnections"></span><span id="licensenoremoteconnections"></span><span id="LICENSENOREMOTECONNECTIONS"></span>

<span id="LicenseNoRemoteConnections"></span><span id="licensenoremoteconnections"></span><span id="LICENSENOREMOTECONNECTIONS"></span>**LicenseNoRemoteConnections** (0x010A)


</dt> <dd>

The remote computer is not licensed to accept remote connections.

</dd> <dt>

<span id="RdpEncInvalidCredentials"></span><span id="rdpencinvalidcredentials"></span><span id="RDPENCINVALIDCREDENTIALS"></span>

<span id="RdpEncInvalidCredentials"></span><span id="rdpencinvalidcredentials"></span><span id="RDPENCINVALIDCREDENTIALS"></span>**RdpEncInvalidCredentials** (0x0300)


</dt> <dd>

The connection was denied because the sharer was not able to authenticate the viewer.

</dd> <dt>

<span id="ProtocolRangeStart_through_ProtocolRangeEnd"></span><span id="protocolrangestart_through_protocolrangeend"></span><span id="PROTOCOLRANGESTART_THROUGH_PROTOCOLRANGEEND"></span>

<span id="ProtocolRangeStart_through_ProtocolRangeEnd"></span><span id="protocolrangestart_through_protocolrangeend"></span><span id="PROTOCOLRANGESTART_THROUGH_PROTOCOLRANGEEND"></span>**ProtocolRangeStart through ProtocolRangeEnd** (0x1000 - 0x7FFF)


</dt> <dd>

Values in this range represent internal protocol errors. Check the server event log for additional details.

</dd> </dl> </dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>RdpEncomAPI.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>RdpEncomAPI.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>RdpEncomAPI.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RdpEncom.dll</dt> </dl>    |



## See also

<dl> <dt>

[**\_IRDPSessionEvents**](/windows/win32/RdpEncomAPI/?branch=master)
</dt> </dl>

 

 





