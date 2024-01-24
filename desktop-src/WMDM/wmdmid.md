---
title: WMDMID structure
description: The WMDMID structure describes serial numbers and group IDs.
ms.assetid: eaa5786e-a2a1-42d7-b527-be83d944cb20
keywords:
- WMDMID structure windows Media Device Manager
- PWMDMID structure pointer windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDMID
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDMID structure

The **WMDMID** structure describes serial numbers and group IDs.

## Syntax


```C++
typedef struct __WMDMID {
  UINT  cbSize;
  DWORD dwVendorID;
  BYTE  pID[WMDMID_LENGTH];
  UINT  SerialNumberLength;
} WMDMID, *PWMDMID;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size of the **WMDMID** structure, in bytes.

</dd> <dt>

**dwVendorID**
</dt> <dd>

**DWORD** containing the registered ID number of the vendor. Contains zero if not in use.

</dd> <dt>

**pID\[WMDMID\_LENGTH\]**
</dt> <dd>

Pointer to an array of bytes containing the serial number. The serial number is a string of byte values that have no standard format. Note that this is not a wide-character value. **WMDMID\_LENGTH** is a constant value defined in mswmdm.h.

</dd> <dt>

**SerialNumberLength**
</dt> <dd>

Actual length of the serial number returned, in bytes.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMDSPDevice::GetSerialNumber**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspdevice-getserialnumber)
</dt> <dt>

[**IMDSPStorageGlobals::GetSerialNumber**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspstorageglobals-getserialnumber)
</dt> <dt>

[**IWMDMDevice::GetSerialNumber**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice-getserialnumber)
</dt> <dt>

[**IWMDMStorageGlobals::GetSerialNumber**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorageglobals-getserialnumber)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





