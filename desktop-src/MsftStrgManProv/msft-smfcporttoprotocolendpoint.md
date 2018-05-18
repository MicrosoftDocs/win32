---
title: MSFT\_SMFCPortToProtocolEndpoint class
description: Represents a relationship between a Fibre Channel (FC) port and a protocol endpoint.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e5769627-9922-46ef-9cf8-715e1e62d3ad'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMFCPortToProtocolEndpoint class", "MSFT_SMFCPortToProtocolEndpoint class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMFCPortToProtocolEndpoint
- MSFT_SMFCPortToProtocolEndpoint.Parent
- MSFT_SMFCPortToProtocolEndpoint.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMFCPortToProtocolEndpoint class

Represents a relationship between a Fibre Channel (FC) port and a protocol endpoint.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMFCPortToProtocolEndpoint
{
  MSFT_SMFCPort           REF Parent;
  MSFT_SMProtocolEndpoint REF Child;
};
```

## Members

The **MSFT\_SMFCPortToProtocolEndpoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMFCPortToProtocolEndpoint** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMProtocolEndpoint**](msft-smprotocolendpoint.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMProtocolEndpoint**](msft-smprotocolendpoint.md) object that represents the protocol endpoint in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMFCPort**](msft-smfcport.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMFCPort**](msft-smfcport.md) object that represents the FC port in the relationship.

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

 

 





