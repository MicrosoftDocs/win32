---
title: MSFT\_SMSystemToEndpoint class
description: Represents a relationship between a system and an endpoint.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5a1cb5a4-945b-4e3b-8ba0-d8d3c4893e00'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMSystemToEndpoint class", "MSFT_SMSystemToEndpoint class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMSystemToEndpoint
- MSFT_SMSystemToEndpoint.Parent
- MSFT_SMSystemToEndpoint.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMSystemToEndpoint class

Represents a relationship between a system and an endpoint.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMSystemToEndpoint
{
  MSFT_SMSystem   REF Parent;
  MSFT_SMEndpoint REF Child;
};
```

## Members

The **MSFT\_SMSystemToEndpoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMSystemToEndpoint** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMEndpoint**](msft-smendpoint.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the endpoint in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMSystem**](msft-smsystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the system in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





