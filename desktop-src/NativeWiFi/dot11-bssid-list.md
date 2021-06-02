---
description: Contains a list of basic service set (BSS) identifiers.
ms.assetid: 22907f94-1ae8-4938-a816-b406656256c0
title: DOT11_BSSID_LIST structure (Windot11.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DOT11_BSSID_LIST
api_type: 
- HeaderDef
api_location: 
- windot11.h
---

# DOT11\_BSSID\_LIST structure

The **DOT11\_BSSID\_LIST** structure contains a list of basic service set (BSS) identifiers.

## Syntax


```C++
typedef struct _DOT11_BSSID_LIST {
  NDIS_OBJECT_HEADER Header;
  ULONG              uNumOfEntries;
  ULONG              uTotalNumOfEntries;
  DOT11_MAC_ADDRESS  BSSIDs[1];
} DOT11_BSSID_LIST, *PDOT11_BSSID_LIST;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

An [**NDIS\_OBJECT\_HEADER**](ndis-object-header.md) structure that contains the type, version, and, size information of an NDIS structure. For most **DOT11\_BSSID\_LIST** structures, set the **Type** member to **NDIS\_OBJECT\_TYPE\_DEFAULT**, set the **Revision** member to **DOT11\_BSSID\_LIST\_REVISION\_1**, and set the **Size** member to **sizeof(DOT11\_BSSID\_LIST)**.

</dd> <dt>

**uNumOfEntries**
</dt> <dd>

The number of entries in this structure.

</dd> <dt>

**uTotalNumOfEntries**
</dt> <dd>

The total number of entries supported.

</dd> <dt>

**BSSIDs**
</dt> <dd>

A list of BSS identifiers. A BSS identifier is stored as a [**DOT11\_MAC\_ADDRESS**](dot11-mac-address-type.md) type.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                       |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                                                        |
| Header<br/>                   | <dl> <dt>Windot11.h (include Windot11.h)</dt> </dl> |



## See also

<dl> <dt>

[**WLAN\_CONNECTION\_PARAMETERS**](/windows/desktop/api/wlanapi/ns-wlanapi-wlan_connection_parameters)
</dt> </dl>

 

 




