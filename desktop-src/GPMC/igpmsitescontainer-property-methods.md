---
title: IGPMSitesContainer Property Methods
description: The property methods of the IGPMSitesContainer interface get the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation .
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cc1cb43b-2e18-45a7-9fda-b43e5a674b62'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
keywords: ["IGPMSitesContainer Property Methods GPMC"]
topic_type:
- apiref
api_name:
- IGPMSitesContainer Property Methods
- IGPMSitesContainer.Domain
- IGPMSitesContainer.get_Domain
- IGPMSitesContainer.DomainController
- IGPMSitesContainer.get_DomainController
- IGPMSitesContainer.Forest
- IGPMSitesContainer.get_Forest
api_location:
- Gpmgmt.dll
api_type:
- COM
---

# IGPMSitesContainer Property Methods

The property methods of the [**IGPMSitesContainer**](igpmsitescontainer.md) interface get the properties described in the following table. For a general discussion of property methods, see [**Interface Property Methods**](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation .

## Properties

<dl> <dt>

**Domain**
</dt> <dd> <dl>

Name of the domain being used to perform site operations. This is a full DNS name, for example, example.microsoft.com.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Domain(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**DomainController**
</dt> <dd> <dl>

Name of the domain controller being used to perform site operations. This can be a DNS name or a NetBIOS name.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DomainController(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**Forest**
</dt> <dd> <dl>

Full DNS name of the forest in which the [**GPMSitesContainer**](igpmsitescontainer.md) resides; this is the name of the forest root domain.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Forest(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl> |
| IID<br/>                      | IID\_IGPMSitesContainer is defined as 4725A899-2782-4D27-A6BB-D499246FFD72<br/> |



## See also

<dl> <dt>

[**IGPMSitesContainer**](igpmsitescontainer.md)
</dt> <dt>

[**IGPM**](igpm.md)
</dt> </dl>

 

 





