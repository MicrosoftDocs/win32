---
title: Fragment
description: Use the Fragment packet to send a fragment of the upload file to the server.
ms.assetid: 'd6df7e47-a240-4be2-a9c4-24a13e622861'
keywords:
- Fragment BITS
topic_type:
- apiref
api_name:
- Fragment
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Fragment

Use the **Fragment** packet to send a fragment of the upload file to the server.

``` syntax
BITS_POST remote-URL HTTP/1.1
BITS-Packet-Type: Fragment
BITS-Session-Id: {guid}
Content-Name: filename
Content-Length: length
Content-Range: Bytes range/total-length
Content-Encoding: encoding
```

## Headers

<dl> <dt>

<span id="BITS_POST"></span><span id="bits_post"></span>BITS\_POST
</dt> <dd>

BITS-specific verb that identifies this packet to the BITS server.

Replace remote-URL with the absolute or relative URI. Typically, replace remote-URL with the remote file name of the job. For network load balancing considerations, see the BITS-Host-Id header in the [**Create-Session**](create-session.md) packet.

</dd> <dt>

<span id="BITS-Packet-Type"></span><span id="bits-packet-type"></span><span id="BITS-PACKET-TYPE"></span>BITS-Packet-Type
</dt> <dd>

Identifies this request packet as a Fragment packet.

</dd> <dt>

<span id="BITS-Session-Id"></span><span id="bits-session-id"></span><span id="BITS-SESSION-ID"></span>BITS-Session-Id
</dt> <dd>

String GUID that identifies the session to the server. Replace {guid} with the session identifier that the server returns in the [**Ack for Create-Session**](ack-for-create-session.md) response packet.

</dd> <dt>

<span id="Content-Name"></span><span id="content-name"></span><span id="CONTENT-NAME"></span>Content-Name
</dt> <dd>

Specify this header only with the initial fragment. Replace filename with the name of the local file name from the job. The name does not include the path.

</dd> <dt>

<span id="Content-Length"></span><span id="content-length"></span><span id="CONTENT-LENGTH"></span>Content-Length
</dt> <dd>

Replace length with the number of bytes sent in the fragment body.

</dd> <dt>

<span id="Content-Range"></span><span id="content-range"></span><span id="CONTENT-RANGE"></span>Content-Range
</dt> <dd>

Tells the server where to apply the range in the destination file. Replace range with the start and end offsets of the range in the destination file. The offsets are zero-based. If the given range overlaps an existing range, BITS writes only the non-overlapping portion of the range; BITS does not overwrite existing content. For example, if the first packet contained the range 0 through 100 and the second packet contained the range 50 through 150, BITS writes only bytes 101 through 150 from the second packet. Replace total-length with the total number of bytes in the file.

</dd> <dt>

<span id="Content-Encoding"></span><span id="content-encoding"></span><span id="CONTENT-ENCODING"></span>Content-Encoding
</dt> <dd>

Replace encoding with the type of encoding the client uses on the fragment. The client must use the encoding that the server identifies in the Accept-Encoding header of the [**Ack for Create-Session**](ack-for-create-session.md) response packet. The server uses the encoding type to decode the fragment. All fragments must specify the same encoding.

Do not send this header if the encoding type is Identity. The BITS server supports only Identity encoding.

</dd> </dl>

## Remarks

The fragment is a range of bytes sent in the body of the packet. The client sends the fragments in sequential order starting with offset zero; the server does not keep track of non-contiguous ranges. If the client sends non-contiguous ranges, the server returns an HTTP 416 (range-not-satisfiable) return code in the [**Ack for Fragment**](ack-for-fragment.md) response.

The Content-*xxxx* headers are standard HTTP 1.1 headers. For more details on the Content-*xxxx* headers, see the [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) specification.

## See also

<dl> <dt>

[**Ack for Fragment**](ack-for-fragment.md)
</dt> <dt>

[**Close-Session**](close-session.md)
</dt> <dt>

[**Create-Session**](create-session.md)
</dt> </dl>

 

 




