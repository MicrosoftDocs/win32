---
description: Contains the table of key information for all wireless LAN interfaces managed by the Wireless Configuration Service.
ms.assetid: 5d5fe222-6ca1-4778-9f64-1c6a63467a6c
title: INTFS_KEY_TABLE structure (Wzcsapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- INTFS_KEY_TABLE
api_type: 
- HeaderDef
api_location: 
- Wzcsapi.h
---

# INTFS\_KEY\_TABLE structure

\[**INTFS\_KEY\_TABLE** is no longer supported as of Windows Vista and Windows Server 2008. Instead, use the [Native Wifi API](native-wifi-reference.md), which provides similar functionality. For more information, see [About the Native Wifi API](about-the-native-wifi-api.md).\]

The **INTFS\_KEY\_TABLE** structure contains the table of key information for all wireless LAN interfaces managed by the Wireless Configuration Service.

## Syntax


```C++
typedef struct {
  DWORD           dwNumIntfs;
  PINTF_KEY_ENTRY pIntfs;
} INTFS_KEY_TABLE, *PINTFS_KEY_TABLE;
```



## Members

<dl> <dt>

**dwNumIntfs**
</dt> <dd>

Total number of interfaces.

</dd> <dt>

**pIntfs**
</dt> <dd>

Pointer to the [**INTF\_KEY\_ENTRY**](intf-key-entry.md) structure.

</dd> </dl>

## Remarks

> [!Note]  
> The *Wzcsapi.h* header file is not available in the Windows SDK.

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP with SP3<br/>                                                       |
| End of server support<br/>    | Windows Server 2003<br/>                                                       |
| Header<br/>                   | <dl> <dt>Wzcsapi.h</dt> </dl> |



 

 




