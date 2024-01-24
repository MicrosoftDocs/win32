---
title: RAS_PPP_PROJECTION_RESULT structure (Rassapi.h)
description: The RAS\_PPP\_PROJECTION\_RESULT structure is used to report the results of the various PPP projection operations for a port.
ms.assetid: 061b1b51-4b6f-4127-8ee5-8a1913a2aa99
keywords:
- RAS_PPP_PROJECTION_RESULT structure RAS
topic_type:
- apiref
api_name:
- RAS_PPP_PROJECTION_RESULT
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_PPP\_PROJECTION\_RESULT structure

\[The **RAS\_PPP\_PROJECTION\_RESULT** structure is not supported as of Windows Vista.\]

The **RAS\_PPP\_PROJECTION\_RESULT** structure is used to report the results of the various PPP projection operations for a port.

## Syntax


```C++
typedef struct _RAS_PPP_PROJECTION_RESULT {
  RAS_PPP_NBFCP_RESULT nbf;
  RAS_PPP_IPCP_RESULT  ip;
  RAS_PPP_IPXCP_RESULT ipx;
  RAS_PPP_ATCP_RESULT  at;
} RAS_PPP_PROJECTION_RESULT;
```



## Members

<dl> <dt>

**nbf**
</dt> <dd>

A [**RAS\_PPP\_NBFCP\_RESULT**](ras-ppp-nbfcp-result-str.md) structure that reports the result of a PPP NetBEUI Framer (NBF) projection operation.

</dd> <dt>

**ip**
</dt> <dd>

A [**RAS\_PPP\_IPCP\_RESULT**](ras-ppp-ipcp-result-str.md) structure that reports the result of a PPP Internet Protocol (IP) projection operation.

</dd> <dt>

**ipx**
</dt> <dd>

A [**RAS\_PPP\_IPXCP\_RESULT**](ras-ppp-ipxcp-result-str.md) structure that reports the result of a PPP Internetwork Packet Exchange (IPX) projection operation.

</dd> <dt>

**at**
</dt> <dd>

A [**RAS\_PPP\_ATCP\_RESULT**](ras-ppp-atcp-result-str.md) structure.

</dd> </dl>

## Remarks

This structure reports the projection results for NetBEUI, TCP/IP, and IPX protocols. Each PPP structure has a **dwError** member that indicates whether the other information in the structure is valid. If **dwError** is NO\_ERROR, the other information is valid. If **dwError** is one of the error codes in Winerror.h or Raserror.h, the other information is not valid.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP<br/>                                                                |
| End of server support<br/>    | Windows Server 2003<br/>                                                       |
| Header<br/>                   | <dl> <dt>Rassapi.h</dt> </dl> |



## See also

<dl> <dt>

[Remote Access Service (RAS) Overview](about-remote-access-service.md)
</dt> <dt>

[RAS Server Administration Structures](ras-server-administration-structures.md)
</dt> <dt>

[**RAS\_PORT\_1**](ras-port-1-str.md)
</dt> <dt>

[**RAS\_PPP\_ATCP\_RESULT**](ras-ppp-atcp-result-str.md)
</dt> <dt>

[**RAS\_PPP\_IPCP\_RESULT**](ras-ppp-ipcp-result-str.md)
</dt> <dt>

[**RAS\_PPP\_IPXCP\_RESULT**](ras-ppp-ipxcp-result-str.md)
</dt> <dt>

[**RAS\_PPP\_NBFCP\_RESULT**](ras-ppp-nbfcp-result-str.md)
</dt> <dt>

[**RasAdminPortGetInfo**](rasadminportgetinfo.md)
</dt> </dl>

 

 





