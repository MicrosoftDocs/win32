---
title: WMDM_FIND_SCOPE enumeration
description: The WMDM\_FIND\_SCOPE enumeration type defines the scope of the storage object.
ms.assetid: 971f84d5-8383-4b38-a201-b21100b2f37e
keywords:
- WMDM_FIND_SCOPE enumeration windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDM_FIND_SCOPE
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDM\_FIND\_SCOPE enumeration

The **WMDM\_FIND\_SCOPE** enumeration type defines the scope of the storage object.

## Syntax


```C++
typedef enum tagWMDM_FIND_SCOPE { 
  WMDM_FIND_SCOPE_GLOBAL,
  WMDM_FIND_SCOPE_IMMEDIATE_CHILDREN
} WMDM_FIND_SCOPE;
```



## Constants

<dl> <dt>

<span id="WMDM_FIND_SCOPE_GLOBAL"></span><span id="wmdm_find_scope_global"></span>**WMDM\_FIND\_SCOPE\_GLOBAL**
</dt> <dd>

Looking for the matching object anywhere on the device.

</dd> <dt>

<span id="WMDM_FIND_SCOPE_IMMEDIATE_CHILDREN"></span><span id="wmdm_find_scope_immediate_children"></span>**WMDM\_FIND\_SCOPE\_IMMEDIATE\_CHILDREN**
</dt> <dd>

Looking for the matching object within this storage and its children.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> </dl>

 

 





