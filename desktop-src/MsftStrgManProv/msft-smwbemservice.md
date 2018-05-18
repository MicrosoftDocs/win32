---
title: MSFT\_SMWbemService class
description: Represents a Web-Based Enterprise Management (WBEM) service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'da52436d-5ca4-424c-b42e-6b8b31b7f1a7'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMWbemService class", "MSFT_SMWbemService class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMWbemService
- MSFT_SMWbemService.ServiceURI
- MSFT_SMWbemService.ServiceURI_ip
- MSFT_SMWbemService.InteropNamespace
- MSFT_SMWbemService.Namespaces
- MSFT_SMWbemService.CommunicationMechanisms
- MSFT_SMWbemService.ProtocolVersion
- MSFT_SMWbemService.ProviderDescription
- MSFT_SMWbemService.RegisteredProfilesSupported
- MSFT_SMWbemService.AuthenticationMechanisms
- MSFT_SMWbemService.MultipleOperationsSupported
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMWbemService class

Represents a Web-Based Enterprise Management (WBEM) service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMWbemService
{
  String  ServiceURI;
  String  ServiceURI_ip;
  String  InteropNamespace;
  String  Namespaces[];
  String  CommunicationMechanisms[];
  String  ProtocolVersion;
  String  ProviderDescription;
  String  RegisteredProfilesSupported[];
  String  AuthenticationMechanisms[];
  Boolean MultipleOperationsSupported;
};
```

## Members

The **MSFT\_SMWbemService** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMWbemService** class has these properties.

<dl> <dt>

**AuthenticationMechanisms**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the authentication mechanisms supported by the provider.

</dd> <dt>

**CommunicationMechanisms**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the names of the communication mechanisms that are supported on the provider.

</dd> <dt>

**InteropNamespace**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The namespace that provides interoperation types for the provider.

</dd> <dt>

**MultipleOperationsSupported**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if multiple operations are supported on the provider; otherwise, **False**.

</dd> <dt>

**Namespaces**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the vendor specific namespaces of the service.

</dd> <dt>

**ProtocolVersion**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The protocol version supported on the provider.

</dd> <dt>

**ProviderDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The provider description.

</dd> <dt>

**RegisteredProfilesSupported**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the registered profiles supported on the provider.

</dd> <dt>

**ServiceURI**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The URI of the service.

</dd> <dt>

**ServiceURI\_ip**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address of the service URI.

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

 

 





