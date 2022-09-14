---
title: Ack for Create-Session
description: Use the Ack for Create-Session packet to acknowledge the client's Create-Session request.
ms.assetid: eeb8ff83-2a7f-4fef-9df7-8c12febfcf36
keywords:
- Ack for Create-Session BITS
topic_type:
- apiref
api_name:
- Ack for Create-Session
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Ack for Create-Session

Use the **Ack for Create-Session** packet to acknowledge the client's [**Create-Session**](create-session.md) request.

``` syntax
reason-code reason-description
BITS-Packet-Type: Ack
BITS-Protocol: {guid}
BITS-Session-Id: {guid}
BITS-Host-Id: PublicHostName
BITS-Host-Id-Fallback-Timeout: Timeout
Accept-Encoding: Identity
Content-Length: length
BITS-Error-Code: error-code
BITS-Error-Context: error-context
```

## Headers

<dl> <dt>

<span id="reason-code"></span><span id="REASON-CODE"></span>reason-code
</dt> <dd>

Replace reason-code with the HTTP reason code. The following table shows the typical reason codes for a response to a [**Create-Session**](create-session.md) request. For a list of HTTP reason codes, see [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt).



| Reason code    | Description                                                                         |
|----------------|-------------------------------------------------------------------------------------|
| 200<br/> | OK. The request was successful.<br/>                                          |
| 201<br/> | Created. The session was created.<br/>                                        |
| 403<br/> | Forbidden. The user is not allowed to upload files to the specified URL.<br/> |
| 404<br/> | Not Found. The specified URL does not exist.<br/>                             |
| 409<br/> | Conflict. The file exists on the server and cannot be overwritten.<br/>       |



 

</dd> <dt>

<span id="reason-description"></span><span id="REASON-DESCRIPTION"></span>reason-description
</dt> <dd>

Replace reason-description with the HTTP description associated with the reason code. For example, set reason-description to OK if reason-code is 200.

</dd> <dt>

<span id="BITS-Packet-Type"></span><span id="bits-packet-type"></span><span id="BITS-PACKET-TYPE"></span>BITS-Packet-Type
</dt> <dd>

Identifies this response packet as an Ack packet.

</dd> <dt>

<span id="BITS-Protocol"></span><span id="bits-protocol"></span><span id="BITS-PROTOCOL"></span>BITS-Protocol
</dt> <dd>

String GUID that identifies the protocol that the server wants to use for this session. Replace {guid} with the protocol identifier from the list of protocols the client includes in the [**Create-Session**](create-session.md) request; the BITS-Supported-Protocol header contains the list. Include this header only if the reason-code is 200 or 201.

</dd> <dt>

<span id="BITS-Session-Id"></span><span id="bits-session-id"></span><span id="BITS-SESSION-ID"></span>BITS-Session-Id
</dt> <dd>

String GUID that identifies this session to the client. Replace {guid} with the session identifier that the client sends in all subsequent request packets.

BITS uses a GUID to identify the session, but you can use any HTTP-legal string up to 100 characters.

</dd> <dt>

<span id="BITS-Host-Id"></span><span id="bits-host-id"></span><span id="BITS-HOST-ID"></span>BITS-Host-Id
</dt> <dd>

Optional. Include this header only if the [BITS IIS extension property](bits-iis-extension-properties.md), BITSHostId, is set. Replace PublicHostName with the server name or IP address from the BITSHostId property.

The client must replace the server portion of the remote-URL on all subsequent packets. If the client does not specify this host name on subsequent packets, it is possible that the job will begin again on another server in the farm, leaving a partial upload file on the previous server.

</dd> <dt>

<span id="BITS-Host-Id-Fallback-Timeout"></span><span id="bits-host-id-fallback-timeout"></span><span id="BITS-HOST-ID-FALLBACK-TIMEOUT"></span>BITS-Host-Id-Fallback-Timeout
</dt> <dd>

Optional. Include this header only if the BITS-Host-Id header is specified. Replace Timeout with the time-out value from the BITSHostIdFallbackTimeout property. The BITSHostIdFallbackTimeout property is one of the [BITS IIS extension properties](bits-iis-extension-properties.md).

The client uses the time-out period to determine how long it tries to reconnect to the server name specified in the BITS-Host-Id header before reverting to the host name specified in the remote file name of the job. The timer begins when BITS is unable to connect to the BITS-Host-Id server. The timer is reset when a connection to the server is restored. If a time-out period is not specified, the client never reverts to the host name specified in the remote file name.

</dd> <dt>

<span id="Accept-Encoding"></span><span id="accept-encoding"></span><span id="ACCEPT-ENCODING"></span>Accept-Encoding
</dt> <dd>

Identifies the encoding scheme to use on the fragments sent to the server. The Fragment packet contains the encoded fragment in the body of the packet. The BITS server requires Identity encoding (plaintext). Include this header only if the Reason-code is 200 or 201.

</dd> <dt>

<span id="Content-Length"></span><span id="content-length"></span><span id="CONTENT-LENGTH"></span>Content-Length
</dt> <dd>

Replace length with the number of bytes included in the body of the response. Required even if the body of the response does not include content.

</dd> <dt>

<span id="BITS-Error-Code"></span><span id="bits-error-code"></span><span id="BITS-ERROR-CODE"></span>BITS-Error-Code
</dt> <dd>

Replace error-code with a hexadecimal number that represents an HRESULT value associated with a server-side error. Include this header only if reason-code is not 200 or 201.

</dd> <dt>

<span id="BITS-Error-Context"></span><span id="bits-error-context"></span><span id="BITS-ERROR-CONTEXT"></span>BITS-Error-Context
</dt> <dd>

Replace error-context with a hexadecimal number that represents the context in which the error occurred. Specify the hexadecimal number for [**BG\_ERROR\_CONTEXT\_REMOTE\_FILE**](/windows/win32/api/bits/ne-bits-bg_error_context) (0x5) if the server generated the error. Otherwise, specify the hexadecimal number for **BG\_ERROR\_CONTEXT\_REMOTE\_APPLICATION** (0x7) if the error was generated by the application to which the upload file is passed. Include this header only if the reason-code is not 200 or 201.

</dd> </dl>

## See also

<dl> <dt>

[**Create-Session**](create-session.md)
</dt> </dl>

 

 





