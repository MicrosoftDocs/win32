---
title: Remote Access Service Data Types
description: The following data types are used by the Remote Access Service API.
ms.assetid: 'aaa7f971-9c23-4738-a386-9b7db859f6be'
keywords: ["RASIPV4ADDR", "RASIPV6ADDR"]
---

# Remote Access Service Data Types

The following data types are used by the Remote Access Service API.


```C++
typedef in_addr RASIPV4ADDR;
typedef in6_addr RASIPV6ADDR;
```



<dl> <dt>

**RASIPV4ADDR**
</dt> <dd>

A [**in\_addr**](https://msdn.microsoft.com/library/windows/desktop/ms738571) that contains an IPv4 address.

> [!Note]  
> Supported in Windows Vista or later versions of Windows.

 

</dd> <dt>

**RASIPV6ADDR**
</dt> <dd>

A [**in6\_addr**](https://msdn.microsoft.com/library/windows/desktop/ms738560) that contains an IPv6 address.

> [!Note]  
> Supported in Windows Vista or later versions of Windows.

 

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Ras.h</dt> </dl> |



 

 





