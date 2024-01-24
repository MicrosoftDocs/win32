---
title: WMDM_SESSION_TYPE enumeration
description: The WMDM\_SESSION\_TYPE enumeration type defines the session type.
ms.assetid: e4ed41c0-521f-4da0-8361-287b64d74d77
keywords:
- WMDM_SESSION_TYPE enumeration windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDM_SESSION_TYPE
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDM\_SESSION\_TYPE enumeration

The **WMDM\_SESSION\_TYPE** enumeration type defines the session type.

## Syntax


```C++
typedef enum tagWMDM_SESSION_TYPE { 
  WMDM_SESSION_NONE,
  WMDM_SESSION_TRANSFER_TO_DEVICE,
  WMDM_SESSION_TRANSFER_FROM_DEVICE,
  WMDM_SESSION_DELETE,
  WMDM_SESSION_CUSTOM
} WMDM_SESSION_TYPE;
```



## Constants

<dl> <dt>

<span id="WMDM_SESSION_NONE"></span><span id="wmdm_session_none"></span>**WMDM\_SESSION\_NONE**
</dt> <dd>

The session is not defined.

</dd> <dt>

<span id="WMDM_SESSION_TRANSFER_TO_DEVICE"></span><span id="wmdm_session_transfer_to_device"></span>**WMDM\_SESSION\_TRANSFER\_TO\_DEVICE**
</dt> <dd>

The session is defined as transferring data to the device.

</dd> <dt>

<span id="WMDM_SESSION_TRANSFER_FROM_DEVICE"></span><span id="wmdm_session_transfer_from_device"></span>**WMDM\_SESSION\_TRANSFER\_FROM\_DEVICE**
</dt> <dd>

The session is defined as transferring data from the device.

</dd> <dt>

<span id="WMDM_SESSION_DELETE"></span><span id="wmdm_session_delete"></span>**WMDM\_SESSION\_DELETE**
</dt> <dd>

The session is defined as deleting data.

</dd> <dt>

<span id="WMDM_SESSION_CUSTOM"></span><span id="wmdm_session_custom"></span>**WMDM\_SESSION\_CUSTOM**
</dt> <dd>

The session is defined as a custom session.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> </dl>

 

 





