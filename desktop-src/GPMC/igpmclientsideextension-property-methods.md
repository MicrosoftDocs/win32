---
title: IGPMClientSideExtension Property Methods
description: The property methods of the IGPMClientSideExtension interface get the properties that are described in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '41ce28c5-fdc4-4bec-b71f-07889048cdb5'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
keywords: ["IGPMClientSideExtension Property Methods GPMC"]
topic_type:
- apiref
api_name:
- IGPMClientSideExtension Property Methods
- IGPMClientSideExtension.ID
- IGPMClientSideExtension.get_ID
- IGPMClientSideExtension.DisplayName
- IGPMClientSideExtension.get_DisplayName
api_location:
- Gpmgmt.dll
api_type:
- COM
---

# IGPMClientSideExtension Property Methods

The property methods of the [**IGPMClientSideExtension**](igpmclientsideextension.md) interface get the properties that are described in the following table. For a general discussion of property methods, see [**Interface Property Methods**](https://msdn.microsoft.com/library/aa746378) in the Active Directory Service Interfaces (ADSI) documentation.

## Properties

<dl> <dt>

**DisplayName**
</dt> <dd> <dl>

Display name of the client-side extension.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DisplayName(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**ID**
</dt> <dd> <dl>

GUID of the client-side extension.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ID(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                             |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>        |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl>      |
| IID<br/>                      | IID\_IGPMClientSideExtension is defined as 69DA7488-B8DB-415E-9266-901BE4D49928<br/> |



## See also

<dl> <dt>

[**IGPM**](igpm.md)
</dt> <dt>

[**IGPMClientSideExtension**](igpmclientsideextension.md)
</dt> <dt>

[**IGPMCSECollection**](igpmcsecollection.md)
</dt> </dl>

 

 





