---
title: OPAQUECOMMAND structure
description: The OPAQUECOMMAND structure contains data for commands that are passed through Windows Media Device Manager to a device but are not intended to be acted upon by Windows Media Device Manager.
ms.assetid: d7b60187-84d1-4ff3-ab58-e6b8ea75ee37
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
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMDSPDevice::SendOpaqueCommand**](/windows/win32/mswmdm/nf-mswmdm-imdspdevice-sendopaquecommand?branch=master)
</dt> <dt>

[**IMDSPStorage::SendOpaqueCommands**](/windows/win32/mswmdm/nf-mswmdm-imdspstorage-sendopaquecommand?branch=master)
</dt> <dt>

[**IWMDMDevice::SendOpaqueCommand**](/windows/win32/mswmdm/nf-mswmdm-iwmdmdevice-sendopaquecommand?branch=master)
</dt> <dt>

[**IWMDMStorage::SendOpaqueCommand**](/windows/win32/mswmdm/nf-mswmdm-iwmdmstorage-sendopaquecommand?branch=master)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





