---
title: CB_RESOURCE_TYPE enumeration (Cbclient.h)
description: Specifies the type of resource that the incoming connection is connecting to.
ms.assetid: 80D921BF-2D84-4A18-9544-50087B81F177
ms.tgt_platform: multiple
keywords:
- CB_RESOURCE_TYPE enumeration Remote Desktop Services
topic_type:
- apiref
api_name:
- CB_RESOURCE_TYPE
api_location:
- Cbclient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_RESOURCE\_TYPE enumeration

Specifies the type of resource that the incoming connection is connecting to. This enumeration is used with the [**CB\_CONNECTION\_INFO**](cb-connection-info.md) structure.

## Syntax


```C++
typedef enum _CB_RESOURCE_TYPE { 
  CB_RESOURCE_UNDEFINED  = 0,
  CB_RESOURCE_SESSION    = 1,
  CB_RESOURCE_VM
} CB_RESOURCE_TYPE;
```



## Constants

<dl> <dt>

<span id="CB_RESOURCE_UNDEFINED"></span><span id="cb_resource_undefined"></span>**CB\_RESOURCE\_UNDEFINED**
</dt> <dd>

The resource type is not defined.

</dd> <dt>

<span id="CB_RESOURCE_SESSION"></span><span id="cb_resource_session"></span>**CB\_RESOURCE\_SESSION**
</dt> <dd>

The resource is a remote session.

</dd> <dt>

<span id="CB_RESOURCE_VM"></span><span id="cb_resource_vm"></span>**CB\_RESOURCE\_VM**
</dt> <dd>

The resource is a virtual machine.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Header<br/>                   | <dl> <dt>Cbclient.h</dt> </dl> |



## See also

<dl> <dt>

[**CB\_CONNECTION\_INFO**](cb-connection-info.md)
</dt> </dl>

 

 





