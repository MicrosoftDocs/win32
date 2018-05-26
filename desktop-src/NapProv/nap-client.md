---
Description: Represents information on the NAP Client implemented in the Network Access Protection (NAP) Agent service on a Windows system.
ms.assetid: 7623f0d2-980c-4af5-8031-078121bf72e7
title: NAP\_Client class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NAP\_Client class

Represents information on the NAP Client implemented in the Network Access Protection (NAP) Agent service on a Windows system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class NAP_Client
{
  string  name;
  string  description;
  boolean napEnabled;
  string  napProtocolVersion;
  uint32  systemIsolationState;
  string  probationTime;
  string  fixupURL;
};
```

## Members

The **NAP\_Client** class has these types of members:

-   [Properties](#properties)

### Properties

The **NAP\_Client** class has these properties.

<dl> <dt>

**description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the NAP client.

</dd> <dt>

**fixupURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The fix-up URL if client has restricted access.

</dd> <dt>

**name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The NAP Client name.

</dd> <dt>

**napEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the NAP Agent service is enabled; **TRUE** is enabled, otherwise **FALSE**.

</dd> <dt>

**napProtocolVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the NAP protocol supported by the NAP Client.

</dd> <dt>

**probationTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The absolute time for probation expiration, if the NAP client is in Probation. This value is a string representation of the **ProbationTime** which is a typedef of a [FILETIME](http://go.microsoft.com/fwlink/p/?linkid=90006) structure.

</dd> <dt>

**systemIsolationState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The isolation state of the system. This value can be one of the enumeration values defined in the [**IsolationState**](https://msdn.microsoft.com/library/windows/desktop/aa369699) enumeration.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                           |
| Namespace<br/>                | Root\\NAP<br/>                                                                           |
| MOF<br/>                      | <dl> <dt>Napclientschema.mof</dt> </dl> |



## See also

<dl> <dt>

[**IsolationState**](https://msdn.microsoft.com/library/windows/desktop/aa369699)
</dt> <dt>

[Network Access Protection](https://msdn.microsoft.com/library/windows/desktop/aa369712)
</dt> </dl>

 

 




