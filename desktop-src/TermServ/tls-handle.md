---
title: TLS_HANDLE
description: Represents a handle to a Remote Desktop license server.
ms.assetid: 6da51660-a9fd-4e49-97e3-ba0829b1bbbf
ms.tgt_platform: multiple
keywords:
- TLS_HANDLE
ms.topic: reference
ms.date: 05/31/2018
---

# TLS\_HANDLE

Represents a handle to a Remote Desktop license server. This handle is returned by the [**TLSConnectToLsServer**](tlsconnecttolsserver.md) function.

> [!Note]  
> This data type has no associated header file. To use it, you must define it yourself as shown in this topic.

 


```C++
typedef HANDLE TLS_HANDLE;
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**TLSConnectToLsServer**](tlsconnecttolsserver.md)
</dt> <dt>

[**TLSDisconnectFromServer**](tlsdisconnectfromserver.md)
</dt> </dl>

 

 





