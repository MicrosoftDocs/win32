---
title: RAS_PPP_IPXCP_RESULT structure (Rassapi.h)
description: The RAS\_PPP\_IPXCP\_RESULT structure is used to report the result of a PPP Internetwork Packet Exchange (IPX) projection operation for a port.
ms.assetid: e1236e1b-f0ef-46cf-a12f-35529215752c
keywords:
- RAS_PPP_IPXCP_RESULT structure RAS
topic_type:
- apiref
api_name:
- RAS_PPP_IPXCP_RESULT
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_PPP\_IPXCP\_RESULT structure

\[The **RAS\_PPP\_IPXCP\_RESULT** structure is not supported as of Windows Vista.\]

The **RAS\_PPP\_IPXCP\_RESULT** structure is used to report the result of a PPP Internetwork Packet Exchange (IPX) projection operation for a port.

## Syntax


```C++
typedef struct _RAS_PPP_IPXCP_RESULT {
  DWORD dwError;
  WCHAR wszAddress[RAS_IPXADDRESSLEN + 1];
} RAS_PPP_IPXCP_RESULT;
```



## Members

<dl> <dt>

**dwError**
</dt> <dd>

Indicates the results of the IPX projection operation. A value of NO\_ERROR indicates success, in which case, the **wszAddress** member is valid. If the projection operation was not successful, **dwError** is an error code from Winerror.h or Raserror.h.

</dd> <dt>

**wszAddress**
</dt> <dd>

A null-terminated Unicode string that specifies the IPX address assigned to the remote client. This string has the *net***.***node* form.

</dd> </dl>

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

[**RAS\_PPP\_PROJECTION\_RESULT**](ras-ppp-projection-result-str.md)
</dt> <dt>

[**RasAdminPortGetInfo**](rasadminportgetinfo.md)
</dt> </dl>

 

 





