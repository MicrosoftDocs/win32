---
title: DACorpPrefixConfiguration class
description: Defines an object that contains the Corp Prefix, base Prefix, and a Boolean value that indicates whether native IPv6 is deployed.
audience: developer
ms.assetid: bdc29e31-ebf3-4330-aab8-39e4836476dc
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DACorpPrefixConfiguration class
- DACorpPrefixConfiguration class, described
topic_type:
- apiref
api_name:
- DACorpPrefixConfiguration
- DACorpPrefixConfiguration.corpIPv6Prefix
- DACorpPrefixConfiguration.basePrefix
- DACorpPrefixConfiguration.IPv6State
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DACorpPrefixConfiguration class

Defines an object that contains the Corp Prefix, base Prefix, and a Boolean value that indicates whether native IPv6 is deployed.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class DACorpPrefixConfiguration
{
  string corpIPv6Prefix[];
  string basePrefix;
  uint32 IPv6State;
};
```

## Members

The **DACorpPrefixConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **DACorpPrefixConfiguration** class has these properties.

<dl> <dt>

**basePrefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The base prefix.

</dd> <dt>

**corpIPv6Prefix**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Native IPV6 prefix or ISATAP prefix based on the **IsNativev6deployed** value.

</dd> <dt>

**IPv6State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration which indicates the IPv6 state:

<dt>

0
</dt> <dd>

Indicates IPv4 only.

</dd> <dt>

1
</dt> <dd>

Indicates External Isatap is deployed.

</dd> <dt>

2
</dt> <dd>

Indicates native IPv6 is deployed.

</dd> <dt>

3
</dt> <dd>

Indicates IPv6 only.

</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





