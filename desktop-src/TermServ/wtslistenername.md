---
title: WTSLISTENERNAME (WtsApi32.h)
description: Represents the name of a Remote Desktop Services listeners on a Remote Desktop Session Host (RD Session Host) server.
ms.assetid: 3C41F507-6A67-4244-860F-E89B0F9E33B0
ms.tgt_platform: multiple
keywords:
- WTSLISTENERNAMEW
- WTSLISTENERNAMEA
- WTSLISTENERNAME
- PWTSLISTENERNAME
- WTSLISTENERNAME
- PWTSLISTENERNAME
ms.topic: reference
ms.date: 05/31/2018
---

# WTSLISTENERNAME

Represents the name of a Remote Desktop Services listeners on a Remote Desktop Session Host (RD Session Host) server.


```C++
typedef WCHAR WTSLISTENERNAMEW[WTS_LISTENER_NAME_LENGTH + 1 ], *PWTSLISTENERNAMEW;
typedef CHAR WTSLISTENERNAMEA[WTS_LISTENER_NAME_LENGTH + 1 ], *PWTSLISTENERNAMEA;
#if UNICODE
typedef WTSLISTENERNAMEW WTSLISTENERNAME;
typedef PWTSLISTENERNAMEW PWTSLISTENERNAME;
#else 
typedef WTSLISTENERNAMEA WTSLISTENERNAME;
typedef PWTSLISTENERNAMEA PWTSLISTENERNAME;
#endif 
```



<dl> <dt>

**WTSLISTENERNAMEW**
</dt> <dd>

The Unicode name of the listener.

</dd> <dt>

**WTSLISTENERNAMEA**
</dt> <dd>

A pointer to the ANSI name of the listener.

</dd> <dt>

**WTSLISTENERNAME**
</dt> <dd>

The name of the listener.

</dd> <dt>

**PWTSLISTENERNAME**
</dt> <dd>

A pointer to the name of the listener.

</dd> <dt>

**WTSLISTENERNAME**
</dt> <dd>

The name of the listener.

</dd> <dt>

**PWTSLISTENERNAME**
</dt> <dd>

A pointer to the name of the listener.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>WtsApi32.h</dt> </dl> |



 

 





