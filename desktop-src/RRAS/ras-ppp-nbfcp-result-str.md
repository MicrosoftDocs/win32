---
title: RAS_PPP_NBFCP_RESULT structure (Rassapi.h)
description: The RAS\_PPP\_NBFCP\_RESULT structure is used to report the result of a PPP NetBEUI Framer (NBF) projection operation for a port.
ms.assetid: 670bf125-cad5-481f-89e4-858e636316bd
keywords:
- RAS_PPP_NBFCP_RESULT structure RAS
topic_type:
- apiref
api_name:
- RAS_PPP_NBFCP_RESULT
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_PPP\_NBFCP\_RESULT structure

\[The **RAS\_PPP\_NBFCP\_RESULT** structure is not supported as of Windows Vista.\]

The **RAS\_PPP\_NBFCP\_RESULT** structure is used to report the result of a PPP NetBEUI Framer (NBF) projection operation for a port.

## Syntax


```C++
typedef struct _RAS_PPP_NBFCP_RESULT {
  DWORD dwError;
  DWORD dwNetBiosError;
  CHAR  szName[NETBIOS_NAME_LEN + 1];
  WCHAR wszWksta[NETBIOS_NAME_LEN + 1];
} RAS_PPP_NBFCP_RESULT;
```



## Members

<dl> <dt>

**dwError**
</dt> <dd>

Indicates the results of the NBF projection operation. A value of NO\_ERROR indicates success, in which case, the **wszWksta** member contains the name of the remote computer. If the projection operation was not successful, **dwError** is an error code from Winerror.h or Raserror.h.

</dd> <dt>

**dwNetBiosError**
</dt> <dd>

Ignore this member on the server; it is relevant only on the client.

</dd> <dt>

**szName**
</dt> <dd>

Ignore this member on the server; it is relevant only on the client.

</dd> <dt>

**wszWksta**
</dt> <dd>

A null-terminated Unicode string that specifies the NetBIOS name of the RAS client workstation.

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

 

 





