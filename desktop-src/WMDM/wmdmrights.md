---
title: WMDMRIGHTS structure
description: The WMDMRIGHTS structure describes content-use rights.
ms.assetid: 1be9167b-0d20-4a17-a42b-9696ada2b539
keywords:
- WMDMRIGHTS structure windows Media Device Manager
- PWMDMRIGHTS structure pointer windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDMRIGHTS
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDMRIGHTS structure

The **WMDMRIGHTS** structure describes content-use rights.

## Syntax


```C++
typedef struct __WMDMRIGHTS {
  UINT         cbSize;
  DWORD        dwContentType;
  DWORD        fuFlags;
  DWORD        fuRights;
  DWORD        dwAppSec;
  DWORD        dwPlaybackCount;
  WMDMDATETIME ExpirationDate;
} WMDMRIGHTS, *PWMDMRIGHTS;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size of the structure, in bytes.

</dd> <dt>

**dwContentType**
</dt> <dd>

**DWORD** containing the type of content.

</dd> <dt>

**fuFlags**
</dt> <dd>

Bit field specifying the rights options in use for the content.



| Value                        | Description                                  |
|------------------------------|----------------------------------------------|
| WMDM\_RIGHTS\_PLAYBACKCOUNT  | Number of times that the file can be played. |
| WMDM\_RIGHTS\_EXPIRATIONDATE | Expiration date of the file.                 |
| WMDM\_RIGHTS\_FREESERIALIDS  | Free serial identifier of the file.          |
| WMDM\_RIGHTS\_GROUPID Group  | Identifier of the file.                      |
| WMDM\_RIGHTS\_NAMEDSERIALIDS | Named serial identifier of the file.         |



 

</dd> <dt>

**fuRights**
</dt> <dd>

Bit field containing the rights bits for the content.



| Value                                     | Description                                   |
|-------------------------------------------|-----------------------------------------------|
| WMDM\_RIGHTS\_PLAY\_ON\_PC                | Content can be played on a personal computer. |
| WMDM\_RIGHTS\_COPY\_TO\_NON\_SDMI\_DEVICE | Content can be copied to a non-SDMI device.   |
| WMDM\_RIGHTS\_COPY\_TO\_CD                | Content can be copied to a CD.                |
| WMDM\_RIGHTS\_COPY\_TO\_SDMI\_DEVICE      | Content can be copied to an SDMI device.      |



 

</dd> <dt>

**dwAppSec**
</dt> <dd>

Byte array that specifies the minimum level of application security.

</dd> <dt>

**dwPlaybackCount**
</dt> <dd>

**DWORD** containing the number of remaining times that the content can be rendered.

</dd> <dt>

**ExpirationDate**
</dt> <dd>

[**WMDMDATETIME**](wmdmdatetime.md) structure containing the expiration date and time for the content. If the license has no expiration date, the **wYear** member is set to 0xFFFF, and all other members of **WMDMDATETIME** are ignored.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMDSPStorage::GetRights**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspstorage-getrights)
</dt> <dt>

[**IWMDMStorage::GetRights**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage-getrights)
</dt> <dt>

[**WMDMDATETIME**](wmdmdatetime.md)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





