---
description: PNRP uses the WSANSPIoctl function to receive notifications about changes to the following.
ms.assetid: e5509be1-5294-4696-ab5b-fa2217ae0956
title: PNRP and WSANSPIoctl
ms.topic: article
ms.date: 05/31/2018
---

# PNRP and WSANSPIoctl

PNRP uses the [**WSANSPIoctl**](winsock-nsp-reference-links.md) function to receive notifications about changes to the following:

-   A network cloud list
-   Availability of results of a name resolution request

The first call to [**WSALookupServiceBegin**](winsock-nsp-reference-links.md) defines the type of information that a client is notified about. A client can be notified with a Windows message, a completion routine, a handle to a WSAEVENT object, or a port. For more information about options and setting the *lpCompletion* parameter, see **WSANSPIoctl**.

To continue receiving notifications after a call to [**WSALookupServiceNext**](winsock-nsp-reference-links.md), an application must call **WSANSPIoctl** again.

The [**WSALookupServiceNext**](winsock-nsp-reference-links.md) function blocks even if **WSANSPIoctl** is called. Before calling **WSALookupServiceNext**, an application must wait until it receives a notification—if blocking is an issue.

When calling this function, the parameters must have the following values:

<dl> <dt>

<span id="hLookup"></span><span id="hlookup"></span><span id="HLOOKUP"></span>*hLookup*
</dt> <dd>

Specifies the handle that [**WSALookupServiceBegin**](winsock-nsp-reference-links.md) returns.

</dd> <dt>

<span id="dwControlCode"></span><span id="dwcontrolcode"></span><span id="DWCONTROLCODE"></span>*dwControlCode*
</dt> <dd>

Must be **SIO\_NSP\_NOTIFY\_CHANGE**.

</dd> <dt>

<span id="lpvInBuffer"></span><span id="lpvinbuffer"></span><span id="LPVINBUFFER"></span>*lpvInBuffer*
</dt> <dd>

Must be **NULL**.

</dd> <dt>

<span id="cbInBuffer"></span><span id="cbinbuffer"></span><span id="CBINBUFFER"></span>*cbInBuffer*
</dt> <dd>

Must be zero (0).

</dd> <dt>

<span id="lpvOutBuffer"></span><span id="lpvoutbuffer"></span><span id="LPVOUTBUFFER"></span>*lpvOutBuffer*
</dt> <dd>

Must be **NULL**.

</dd> <dt>

<span id="cbOutBuffer"></span><span id="cboutbuffer"></span><span id="CBOUTBUFFER"></span>*cbOutBuffer*
</dt> <dd>

Must be zero (0).

</dd> <dt>

<span id="lpcbBytesReturned"></span><span id="lpcbbytesreturned"></span><span id="LPCBBYTESRETURNED"></span>*lpcbBytesReturned*
</dt> <dd>

Must be **NULL**.

</dd> <dt>

<span id="lpCompletion"></span><span id="lpcompletion"></span><span id="LPCOMPLETION"></span>*lpCompletion*
</dt> <dd>

Specifies either **NULL** or a pointer to a [**WSACOMPLETION**](winsock-nsp-reference-links.md) structure.

</dd> </dl>

After a notification is received, call [**WSALookupServiceNext**](winsock-nsp-reference-links.md) one time to obtain the results.

To end a search, call [**WSALookupServiceEnd**](winsock-nsp-reference-links.md).

## Resolution Notifications

A client can be notified any time that a name resolution entry is added. The client then calls [**WSALookupServiceNext**](winsock-nsp-reference-links.md) to obtain the resolution data.

If the client does not use this technique, a call to [**WSALookupServiceNext**](winsock-nsp-reference-links.md) can be blocked until the specified timeout occurs.

## Cloud List Notifications

A client can be notified any time there is a change to a set of clouds.

The [**WSALookupServiceNext**](winsock-nsp-reference-links.md) function returns **WSA\_E\_NO\_MORE** as a set delimiter. The client application must enumerate existing clouds until this message is returned, and then use a notification scheme to retrieve subsequent changes as they occur. A client application can also call **WSALookupServiceNext**, but the call is blocked until a change occurs.

The [**WSALookupServiceNext**](winsock-nsp-reference-links.md) function returns a cloud in a **WSAQUERYSET** structure. One of the following flags is returned in the **dwOutputFlags** member.



| Value               | Description                                             |
|---------------------|---------------------------------------------------------|
| RESULT\_IS\_ADDED   | The cloud that is returned is added.                    |
| RESULT\_IS\_CHANGED | The cloud that is returned is changed.                  |
| RESULT\_IS\_DELETED | The cloud that is returned is deleted and is not valid. |



 

## Related topics

<dl> <dt>

[PNRP and WSALookupServiceBegin](pnrp-and-wsalookupservicebegin.md)
</dt> <dt>

[PNRP and WSALookupServiceEnd](pnrp-and-wsalookupserviceend.md)
</dt> <dt>

[PNRP and WSAQUERYSET](pnrp-and-wsaqueryset.md)
</dt> <dt>

[PNRP NSP Error Codes](pnrp-nsp-error-codes.md)
</dt> <dt>

[**WSANSPIoctl**](winsock-nsp-reference-links.md)
</dt> <dt>

**WSALookupServiceBegin**
</dt> <dt>

**WSALookupServiceEnd**
</dt> <dt>

**WSAQUERYSET**
</dt> </dl>

 

 



