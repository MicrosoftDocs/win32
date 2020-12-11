---
title: MPRESOURCE_INFO structure (MpClient.h)
description: Resource information structure.
ms.assetid: 2D645722-3DE3-4748-B532-3E522464EA1E
keywords:
- MPRESOURCE_INFO structure Legacy Windows Environment Features
- PMPRESOURCE_INFO structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPRESOURCE_INFO
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPRESOURCE\_INFO structure

Resource information structure.

## Syntax


```C++
typedef struct tagMPRESOURCE_INFO {
  MP_MIDL_STRING LPWSTR Scheme;
  MP_MIDL_STRING LPWSTR Path;
  MPRESOURCE_CLASS      Class;
} MPRESOURCE_INFO, *PMPRESOURCE_INFO;
```



## Members

<dl> <dt>

**Scheme**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Resource scheme identifier such as "file" or "dir".

</dd> <dt>

**Path**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Absolute path of resource, based on **Scheme**.

</dd> <dt>

**Class**
</dt> <dd>

Type: **MPRESOURCE\_CLASS**

</dd> <dd>

This field is set when the resource is identified as part of the threat. It specifies the resource class, mainly concrete vs. latent. It can be a combination of these possible values:



| Value                                                                                                                                                                                                                                                                        | Meaning                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <span id="MP_RESOURCE_CLASS_UNKNOWN"></span><span id="mp_resource_class_unknown"></span><dl> <dt>**MP\_RESOURCE\_CLASS\_UNKNOWN**</dt> <dt>0x0000</dt> </dl>              |                                                                       |
| <span id="MP_RESOURCE_CLASS_CONCRETE"></span><span id="mp_resource_class_concrete"></span><dl> <dt>**MP\_RESOURCE\_CLASS\_CONCRETE**</dt> <dt>0x0001</dt> </dl>           | Mutually exclusive with **MP\_RESOURCE\_CLASS\_LATENT**.<br/>   |
| <span id="MP_RESOURCE_CLASS_LATENT"></span><span id="mp_resource_class_latent"></span><dl> <dt>**MP\_RESOURCE\_CLASS\_LATENT**</dt> <dt>0x0002</dt> </dl>                 | Mutually exclusive with **MP\_RESOURCE\_CLASS\_CONCRETE**.<br/> |
| <span id="MP_RESOURCE_CLASS_SAMPLE_FILE"></span><span id="mp_resource_class_sample_file"></span><dl> <dt>**MP\_RESOURCE\_CLASS\_SAMPLE\_FILE**</dt> <dt>0x0004</dt> </dl> |                                                                       |
| <span id="MP_RESOURCE_CLASS_SHARED"></span><span id="mp_resource_class_shared"></span><dl> <dt>**MP\_RESOURCE\_CLASS\_SHARED**</dt> <dt>0x0100</dt> </dl>                 |                                                                       |



 

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





