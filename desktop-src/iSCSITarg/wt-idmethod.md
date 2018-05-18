---
title: WT\_IDMethod class
description: Contains information used by the iSCSI target entry to identify the initiator associated with it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8980ccf6-3360-44fd-84d9-b9fc807a3b97'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["WT_IDMethod class iSCSI Software Target API", "WT_IDMethod class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- WT_IDMethod
- WT_IDMethod.HostName
- WT_IDMethod.Method
- WT_IDMethod.Value
api_location:
- WtWmiProv.dll
api_type:
- DllExport
---

# WT\_IDMethod class

Contains information used by the iSCSI target entry to identify the initiator associated with it.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_IDMethod
{
  string HostName;
  sint32 Method;
  string Value;
};
```

## Members

The **WT\_IDMethod** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_IDMethod** class has these properties.

<dl> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The name of the iSCSI target. There can be more than one **WT\_IDMethod** object with the same **Hostname**. However, the combination of **HostName**, **Method**, and **Value** must be unique.

</dd> <dt>

**Method**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Key**, **Values** (DNSName, IPAddress, MACAddress, IQN, IPv6Address), **ValueMap** (1, 2, 3, 4, 5)
</dt> </dl>

The identification method.

</dd> <dt>

**Value**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The value of the identification method. For example, if the Method is DNSName, *Value* is the DNS name, for example, exchange.contoso.com.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





