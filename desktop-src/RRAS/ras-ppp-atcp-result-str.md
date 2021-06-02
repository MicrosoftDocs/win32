---
title: RAS_PPP_ATCP_RESULT structure (Rassapi.h)
description: The RAS\_PPP\_ATCP\_RESULT structure is used to report the result of an AppleTalk protocol projection operation for a port.
ms.assetid: ac9df618-f79c-4066-a37e-f92e64e951dd
keywords:
- RAS_PPP_ATCP_RESULT structure RAS
topic_type:
- apiref
api_name:
- RAS_PPP_ATCP_RESULT
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_PPP\_ATCP\_RESULT structure

\[The **RAS\_PPP\_ATCP\_RESULT** structure is not supported as of Windows Vista.\]

The **RAS\_PPP\_ATCP\_RESULT** structure is used to report the result of an AppleTalk protocol projection operation for a port.

## Syntax


```C++
typedef struct _RAS_PPP_ATCP_RESULT {
  DWORD dwError;
  WCHAR wszAddress[RAS_ATADDRESSLEN + 1];
} RAS_PPP_ATCP_RESULT;
```



## Members

<dl> <dt>

**dwError**
</dt> <dd>

Specifies a value that indicates the results of the AppleTalk projection operation. A value of NO\_ERROR indicates success, in which case, the **wszAddress** member is valid. If the projection operation is not successful, **dwError** is an error code from Winerror.h or Raserror.h.

</dd> <dt>

**wszAddress**
</dt> <dd>

Specifies a null-terminated Unicode string that specifies the IP address assigned to the remote client.

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

[**RAS\_PPP\_PROJECTION\_RESULT**](ras-ppp-projection-result-str.md)
</dt> </dl>

 

 





