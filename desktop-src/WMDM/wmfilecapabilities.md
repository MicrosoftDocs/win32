---
title: WMFILECAPABILITIES structure
description: The WMFILECAPABILITIES structure describes the MIME type.
ms.assetid: '30307343-f55e-4695-9ae8-b938617d749d'
keywords: ["WMFILECAPABILITIES structure windows Media Device Manager"]
topic_type:
- apiref
api_name:
- WMFILECAPABILITIES
api_location:
- wmdm.idl
api_type:
- HeaderDef
---

# WMFILECAPABILITIES structure

The **WMFILECAPABILITIES** structure describes the MIME type.

## Syntax


```C++
typedef struct _tagWMFILECAPABILITIES {
  LPWSTR pwszMimeType;
  DWORD  dwReserved;
} WMFILECAPABILITIES;
```



## Members

<dl> <dt>

**pwszMimeType**
</dt> <dd>

MIME type.

</dd> <dt>

**dwReserved**
</dt> <dd>

**DWORD** reserved for future use. Set to zero (0).

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWMDMDevice2::GetFormatSupport2**](iwmdmdevice2-getformatsupport2.md)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





