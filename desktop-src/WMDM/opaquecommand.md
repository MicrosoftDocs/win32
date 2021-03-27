---
title: OPAQUECOMMAND structure
description: The OPAQUECOMMAND structure contains data for commands that are passed through Windows Media Device Manager to a device but are not intended to be acted upon by Windows Media Device Manager.
ms.assetid: '5b39cf07-2816-4615-a754-e3f0c57bf4ce'
keywords:
- OPAQUECOMMAND structure windows Media Device Manager
- structure windows Media Device Manager
topic_type:
- apiref
api_name:
- OPAQUECOMMAND
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# OPAQUECOMMAND structure

The **OPAQUECOMMAND** structure contains data for commands that are passed through Windows Media Device Manager to a device but are not intended to be acted upon by Windows Media Device Manager.

## Syntax


```C++
typedef struct OPAQUECOMMAND {
  GUID  guidCommand;
  DWORD dwDataLen;
  BYTE  *pData;
  BYTE  abMAC[20];
} ;
```



## Members

<dl> <dt>

**guidCommand**
</dt> <dd>

**GUID** representing the requested command.

</dd> <dt>

**dwDataLen**
</dt> <dd>

Length of the data to which *pData* points, in bytes.

</dd> <dt>

**pData**
</dt> <dd>

Data required to execute the command, and/or data returned by the command.

</dd> <dt>

**abMAC\[20\]**
</dt> <dd>

This message authentication code (MAC) should include the **guidCommand** member, the data to which *pdwDataLen* points, and the data to which *pData* points, if any. If *pData* is **NULL**, it must not be included in the MAC. WMDM\_MAC\_LENGTH is defined as 20.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMDSPDevice::SendOpaqueCommand**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspdevice-sendopaquecommand)
</dt> <dt>

[**IMDSPStorage::SendOpaqueCommands**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspstorage-sendopaquecommand)
</dt> <dt>

[**IWMDMDevice::SendOpaqueCommand**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice-sendopaquecommand)
</dt> <dt>

[**IWMDMStorage::SendOpaqueCommand**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage-sendopaquecommand)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





