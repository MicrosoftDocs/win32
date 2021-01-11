---
description: Identifies the host type of the WLDP caller.
ms.assetid: E8E603CC-9CB2-4C3B-9F06-9B06C7B5D752
title: WLDP_HOST_ID enumeration (Wldp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WLDP_HOST_ID
api_type: 
- HeaderDef
api_location: 
- wldp.h
---

# WLDP\_HOST\_ID enumeration

Identifies the host type of the WLDP caller.

## Syntax


```C++
typedef enum _WLDP_HOST_ID { 
   WLDP_HOST_ID_UNKNOWN     = 0,
   WLDP_HOST_ID_GLOBAL      = 1,
  WLDP_HOST_ID_VBA          = 2,
   WLDP_HOST_ID_WSH         = 3,
   WLDP_HOST_ID_POWERSHELL  = 4,
   WLDP_HOST_ID_IE          = 5,
   WLDP_HOST_ID_MSI         = 6,
   WLDP_HOST_ID_MAX         = 7
} WLDP_HOST_ID, *PWLDP_HOST_ID;
```



## Constants

<dl> <dt>

<span id="_WLDP_HOST_ID_UNKNOWN_"></span><span id="_wldp_host_id_unknown_"></span> **WLDP\_HOST\_ID\_UNKNOWN** 
</dt> <dd>

The host type is unknown.

</dd> <dt>

<span id="_WLDP_HOST_ID_GLOBAL"></span><span id="_wldp_host_id_global"></span> **WLDP\_HOST\_ID\_GLOBAL**
</dt> <dd>

The host type is global policy.

</dd> <dt>

<span id="WLDP_HOST_ID_VBA"></span><span id="wldp_host_id_vba"></span>**WLDP\_HOST\_ID\_VBA**
</dt> <dd>

The host type is VBScript.

</dd> <dt>

<span id="_WLDP_HOST_ID_WSH"></span><span id="_wldp_host_id_wsh"></span> **WLDP\_HOST\_ID\_WSH**
</dt> <dd>

The host type is Windows Script Host.

</dd> <dt>

<span id="_WLDP_HOST_ID_POWERSHELL"></span><span id="_wldp_host_id_powershell"></span> **WLDP\_HOST\_ID\_POWERSHELL**
</dt> <dd>

The host type is Windows Powershell.

</dd> <dt>

<span id="_WLDP_HOST_ID_IE"></span><span id="_wldp_host_id_ie"></span> **WLDP\_HOST\_ID\_IE**
</dt> <dd>

The host type is Internet Explorer.

</dd> <dt>

<span id="_WLDP_HOST_ID_MSI"></span><span id="_wldp_host_id_msi"></span> **WLDP\_HOST\_ID\_MSI**
</dt> <dd>

The host type is the Microsoft Windows Installer.

</dd> <dt>

<span id="_WLDP_HOST_ID_MAX__"></span><span id="_wldp_host_id_max__"></span> **WLDP\_HOST\_ID\_MAX** 
</dt> <dd>

The maximum enumeration value.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Wldp.h</dt> </dl> |



 

 




