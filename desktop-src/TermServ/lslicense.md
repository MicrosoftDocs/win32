---
title: LSLicense structure
description: Contains information about a specific Remote Desktop Services license.
ms.assetid: 2c7f7b7a-e3b5-4f84-b49f-5f1d6960652d
ms.tgt_platform: multiple
keywords:
- LSLicense structure Remote Desktop Services
- LPLSLicense structure pointer Remote Desktop Services
topic_type:
- apiref
api_name:
- LSLicense
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# LSLicense structure

Contains information about a specific Remote Desktop Services license.

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _LSLicense {
  DWORD dwVersion;
  DWORD dwLicenseId;
  DWORD dwKeyPackId;
  TCHAR szHWID[GUID_MAX_SIZE];
  TCHAR szMachineName[MAXCOMPUTERNAMELENGTH];
  TCHAR szUserName[MAXUSERNAMELENGTH];
  DWORD dwCertSerialLicense;
  DWORD dwLicenseSerialNumber;
  DWORD ftIssueDate;
  DWORD ftExpireDate;
  UCHAR ucLicenseStatus;
} LSLicense, *LPLSLicense;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

Version of the license.

</dd> <dt>

**dwLicenseId**
</dt> <dd>

ID of the license.

</dd> <dt>

**dwKeyPackId**
</dt> <dd>

ID of the [**LSKeyPack**](lskeypack.md) that contains the license.

</dd> <dt>

**szHWID**
</dt> <dd>

Hardware ID of the Remote Desktop Connection (RDC) client that was issued the license.

</dd> <dt>

**szMachineName**
</dt> <dd>

Name of the Remote Desktop Connection (RDC) client that was issued the license.

</dd> <dt>

**szUserName**
</dt> <dd>

Name of the user who was issued the license.

</dd> <dt>

**dwCertSerialLicense**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**dwLicenseSerialNumber**
</dt> <dd>

Serial number of the license.

</dd> <dt>

**ftIssueDate**
</dt> <dd>

Date that the license was issued.

</dd> <dt>

**ftExpireDate**
</dt> <dd>

Date that the license will expire.

</dd> <dt>

**ucLicenseStatus**
</dt> <dd>

Current status of the license.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**LSKeyPack**](lskeypack.md)
</dt> <dt>

[**TLSLicenseEnumBegin**](tlslicenseenumbegin.md)
</dt> <dt>

[**TLSLicenseEnumNext**](tlslicenseenumnext.md)
</dt> <dt>

[**TLSLicenseEnumEnd**](tlslicenseenumend.md)
</dt> </dl>

 

 





