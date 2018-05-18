---
title: DhcpServerv4Superscope class
description: Dhcp Server v4 Superscope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '600a37db-4c89-4735-b12f-df72e2be2a70'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv4Superscope class", "DhcpServerv4Superscope class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv4Superscope
- DhcpServerv4Superscope.SuperscopeName
- DhcpServerv4Superscope.ScopeId
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv4Superscope class

Dhcp Server v4 Superscope.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4Superscope
{
  string SuperscopeName;
  string ScopeId[];
};
```

## Members

The **DhcpServerv4Superscope** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4Superscope** class has these properties.

<dl> <dt>

**ScopeId**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

List of scopes that belong to given superscope on Dhcp server

</dd> <dt>

**SuperscopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of superscope on Dhcp server

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





