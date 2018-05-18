---
title: MSFT\_SMProtocolEndpoint class
description: Represents a protocol endpoint.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7183aef5-428f-486e-9f36-3449dac87a05'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMProtocolEndpoint class", "MSFT_SMProtocolEndpoint class, described"]
---

# MSFT\_SMProtocolEndpoint class

Represents a protocol endpoint.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage")]
class MSFT_SMProtocolEndpoint
{
  String ObjectId;
  string Name;
  string NameFormat;
  string SystemName;
  string ConnectedName;
  string ConnectedNameFormat;
  string ConnectedSystemName;
};
```

## Members

The **MSFT\_SMProtocolEndpoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMProtocolEndpoint** class has these properties.

<dl> <dt>

**ConnectedName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**ConnectedNameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The format of the **ConnectedName** property.

</dd> <dt>

**ConnectedSystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the endpoint. The **NameFormat** property describes the format of the endpoint name.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The format of the **Name** value.

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the system that hosts the endpoint.

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

 

 





