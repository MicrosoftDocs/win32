---
title: LSKeyPack structure
description: Contains information about a specific Remote Desktop Services licensing key pack.
ms.assetid: c26d27ee-7dd3-49f0-a79c-752d23693a2a
ms.tgt_platform: multiple
keywords:
- LSKeyPack structure Remote Desktop Services
- LPLSKeyPack structure pointer Remote Desktop Services
topic_type:
- apiref
api_name:
- LSKeyPack
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# LSKeyPack structure

Contains information about a specific Remote Desktop Services licensing key pack.

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _LSKeyPack {
  DWORD dwVersion;
  UCHAR ucKeyPackType;
  TCHAR szCompanyName[256];
  TCHAR szKeyPackId[256];
  TCHAR szProductName[256];
  TCHAR szProductId[256];
  TCHAR szProductDesc[256];
  WORD  wMajorVersion;
  WORD  wMinorVersion;
  DWORD dwPlatformType;
  UCHAR ucLicenseType;
  DWORD dwLanguageId;
  UCHAR ucChannelOfPurchase;
  TCHAR szBeginSerialNumber[256];
  DWORD dwTotalLicenseInKeyPack;
  DWORD dwProductFlags;
  DWORD dwKeyPackId;
  UCHAR ucKeyPackStatus;
  DWORD dwActivateDate;
  DWORD dwExpirationDate;
  DWORD dwNumberOfLicenses;
} LSKeyPack, *LPLSKeyPack;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

Version of the key pack.

</dd> <dt>

**ucKeyPackType**
</dt> <dd>

Type of key pack.

</dd> <dt>

**szCompanyName**
</dt> <dd>

Name of the company that issued the key pack.

</dd> <dt>

**szKeyPackId**
</dt> <dd>

ID of the key pack.

</dd> <dt>

**szProductName**
</dt> <dd>

Name of the product to which this key pack belongs.

</dd> <dt>

**szProductId**
</dt> <dd>

ID of the product to which this key pack belongs.

</dd> <dt>

**szProductDesc**
</dt> <dd>

Description of the product to which this key pack belongs.

</dd> <dt>

**wMajorVersion**
</dt> <dd>

Major version of the product to which this key pack belongs.

</dd> <dt>

**wMinorVersion**
</dt> <dd>

Minor version of the product to which this key pack belongs.

</dd> <dt>

**dwPlatformType**
</dt> <dd>

Platform type.

</dd> <dt>

**ucLicenseType**
</dt> <dd>

Type of licenses in the key pack.

</dd> <dt>

**dwLanguageId**
</dt> <dd>

Language ID.

</dd> <dt>

**ucChannelOfPurchase**
</dt> <dd>

Channel of purchase.

</dd> <dt>

**szBeginSerialNumber**
</dt> <dd>

Serial number for the first license.

</dd> <dt>

**dwTotalLicenseInKeyPack**
</dt> <dd>

Total number of licenses in the key pack.

</dd> <dt>

**dwProductFlags**
</dt> <dd>

Flags.

</dd> <dt>

**dwKeyPackId**
</dt> <dd>

ID of the key pack.

</dd> <dt>

**ucKeyPackStatus**
</dt> <dd>

Status of the key pack.

</dd> <dt>

**dwActivateDate**
</dt> <dd>

Activation date for the key pack.

</dd> <dt>

**dwExpirationDate**
</dt> <dd>

Expiration date for the key pack.

</dd> <dt>

**dwNumberOfLicenses**
</dt> <dd>

Number of licenses.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**TLSKeyPackEnumBegin**](tlskeypackenumbegin.md)
</dt> <dt>

[**TLSKeyPackEnumNext**](tlskeypackenumnext.md)
</dt> <dt>

[**TLSKeyPackEnumEnd**](tlskeypackenumend.md)
</dt> </dl>

 

 





