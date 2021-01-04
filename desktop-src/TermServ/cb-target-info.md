---
title: CB_TARGET_INFO structure (Cbclient.h)
description: Contains information about the target computer and IP addresses where incoming connections should be redirected.
ms.assetid: 60612E10-9D82-4F38-87F7-B24F51E6EBDA
ms.tgt_platform: multiple
keywords:
- CB_TARGET_INFO structure Remote Desktop Services
- PCB_TARGET_INFO structure pointer Remote Desktop Services
topic_type:
- apiref
api_name:
- CB_TARGET_INFO
api_location:
- Cbclient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_TARGET\_INFO structure

Contains information about the target computer and IP addresses where incoming connections should be redirected. This structure is used with the [**IConnectionBrokerClient::GetTargetInfo**](iconnectionbrokerclient-gettargetinfo.md) method.

## Syntax


```C++
typedef struct {
  WCHAR ServerName[128];
  DWORD AddressCount;
  WCHAR Addresses[CB_MAX_ADDRESSES][CB_IPADDRESS_LEN];
} CB_TARGET_INFO, *PCB_TARGET_INFO;
```



## Members

<dl> <dt>

**ServerName**
</dt> <dd>

Represents the fully qualified domain name of the target server. For a Remote Desktop virtualization (RDV) scenario, this member is **NULL**. For a Remote Desktop session host (RDSH) scenario, this member contains the server name where the incoming connection is redirected.

</dd> <dt>

**AddressCount**
</dt> <dd>

The number of valid entries in the **Addresses** array.

</dd> <dt>

**Addresses**
</dt> <dd>

An array of strings that contain the IP addresses where the incoming connections are redirected. The number of valid elements in this array is specified in the **AddressCount** member.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Header<br/>                   | <dl> <dt>Cbclient.h</dt> </dl> |



## See also

<dl> <dt>

[**IConnectionBrokerClient::GetTargetInfo**](iconnectionbrokerclient-gettargetinfo.md)
</dt> </dl>

 

 





