---
description: A structure identifying the host and source file to be evaluated.
ms.assetid: 547EF59E-7DE5-45E4-948F-109547FAAEE7
title: WLDP_HOST_INFORMATION structure (Wldp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WLDP_HOST_INFORMATION
api_type: 
- HeaderDef
api_location: 
- wldp.h
---

# WLDP\_HOST\_INFORMATION structure

A structure identifying the host and source file to be evaluated.

## Syntax


```C++
typedef struct _WLDP_HOST_INFORMATION {
  DWORD        dwRevision;
  WLDP_HOST_ID dwHostId;
  PCWSTR       szSource;
  HANDLE       hSource;
} WLDP_HOST_INFORMATION, *PWLDP_HOST_INFORMATION;
```



## Members

<dl> <dt>

**dwRevision**
</dt> <dd>

Must be **WLDP\_HOST\_INFORMATION\_REVISION**.

</dd> <dt>

**dwHostId**
</dt> <dd>

Enumeration value from [**WLDP\_HOST\_ID**](wldp-host-id.md) that describes the host ID.

</dd> <dt>

**szSource**
</dt> <dd>

Full path and script name with the extension. NULL for **WLDP\_HOST\_ID\_GLOBAL**, or manual script execution.

</dd> <dt>

**hSource**
</dt> <dd>

In addition to the name, the caller can specify a handle to the file used for validation.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Wldp.h</dt> </dl> |



 

 




