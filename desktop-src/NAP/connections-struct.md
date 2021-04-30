---
title: Connections structure (NapEnforcementClient.h)
description: Contains information about the list of connections maintained by an enforcer.
ms.assetid: 79466099-b567-4268-b9bf-d5e57f4d4900
keywords:
- Connections structure NAP
topic_type:
- apiref
api_name:
- Connections
api_location:
- NapEnforcementClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Connections structure

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **Connections** structure contains information about the list of connections maintained by an enforcer.

## Syntax


```C++
typedef struct tagConnections {
  UINT16                          count;
  INapEnforcementClientConnection **connections;
} Connections;
```



## Members

<dl> <dt>

**count**
</dt> <dd>

The number of active connections currently maintained by an enforcer within the range 0 (zero) to [**maxConnectionCountPerEnforcer**](nap-type-constants.md).

</dd> <dt>

**connections**
</dt> <dd>

A COM pointer to a list of [**INapEnforcementClientConnection**](inapenforcementclientconnection.md) interfaces that represent client connections.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapEnforcementClient.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapEnforcementClient.idl</dt> </dl> |



## See also

<dl> <dt>

[NAP Reference](nap-reference.md)
</dt> <dt>

[NAP Structures](nap-structures.md)
</dt> <dt>

[**INapEnforcementClientConnection**](inapenforcementclientconnection.md)
</dt> </dl>

 

 





