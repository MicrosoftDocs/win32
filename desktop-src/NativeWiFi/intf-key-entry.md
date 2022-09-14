---
description: Stores the key information about a wireless LAN interface managed by the Wireless Configuration Service.
ms.assetid: 5e689fd0-27d9-48eb-8983-96d7918be1cd
title: INTF_KEY_ENTRY structure (Wzcsapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- INTF_KEY_ENTRY
api_type: 
- HeaderDef
api_location: 
- wzcsapi.h
---

# INTF\_KEY\_ENTRY structure

\[**INTF\_KEY\_ENTRY** is no longer supported as of Windows Vista and Windows Server 2008. Instead, use the [Native Wifi API](native-wifi-reference.md), which provides similar functionality. For more information, see [About the Native Wifi API](about-the-native-wifi-api.md).\]

The **INTF\_KEY\_ENTRY** structure stores the key information about a wireless LAN interface managed by the Wireless Configuration Service.

## Syntax


```C++
typedef struct {
  LPWSTR wszGuid;
} INTF_KEY_ENTRY, *PINTF_KEY_ENTRY;
```



## Members

<dl> <dt>

**wszGuid**
</dt> <dd>

A pointer to the interface GUID represented as a Unicode string in the following format: "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}".

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



## See also

<dl> <dt>

[**INTFS\_KEY\_TABLE**](intfs-key-table.md)
</dt> <dt>

[**WZCEnumInterfaces**](wzcenuminterfaces.md)
</dt> </dl>

 

 




