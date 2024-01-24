---
title: BITS_FILE_PROPERTY_ID enumeration (Deliveryoptimization.h)
description: The BITS_FILE_PROPERTY_ID enumeration specifies values that define ID values corresponding to BackgroundCopyFile properties.
ms.assetid: 47EFD160-7CA8-48E6-A18E-38D85F7C6E47
keywords:
- BITS_FILE_PROPERTY_ID enumeration
- BITS_FILE_PROPERTY_ID enumeration
topic_type:
- apiref
api_name:
- BITS_FILE_PROPERTY_ID
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# BITS_FILE_PROPERTY_ID enumeration

The **BITS_FILE_PROPERTY_ID** enumeration specifies values that define ID values corresponding to **BackgroundCopyFile** properties.

## Syntax


```C++
typedef enum _BITS_FILE_PROPERTY_ID { 
  BITS_FILE_PROPERTY_ID_HTTP_RESPONSE_HEADERS  = 1
} BITS_FILE_PROPERTY_ID;
```



## Constants

<dl> <dt>

<span id="BITS_FILE_PROPERTY_ID_HTTP_RESPONSE_HEADERS"></span><span id="bits_file_property_id_http_response_headers"></span>**BITS_FILE_PROPERTY_ID_HTTP_RESPONSE_HEADERS**
</dt> <dd>

The full set of HTTP response headers from the server's last HTTP response packet.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl> |



 

 





