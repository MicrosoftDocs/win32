---
Description: 'Represents the status of a MSFT\_SomFilter object.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '9D9824BB-9A07-40DC-973F-B38FF175A404'
ms.prod: 'windows-server-dev'
ms.technology:
- 'group-policy'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'MSFT\_SomFilterStatus class'
---

# MSFT\_SomFilterStatus class

Represents the status of a [**MSFT\_SomFilter**](msft-somfilter.md) object.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("PolicStatus")]
class MSFT_SomFilterStatus
{
  string  Domain;
  boolean SchemaAvailable;
  boolean ContainerAvailable;
};
```

## Members

The **MSFT\_SomFilterStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SomFilterStatus** class has these properties.

<dl> <dt>

**ContainerAvailable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the container of the [**MSFT\_SomFilter**](msft-somfilter.md) object is available. True if the container is available; otherwise false.

</dd> <dt>

**Domain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the domain of the [**MSFT\_SomFilter**](msft-somfilter.md) object in DNS format. For example, "microsoft.com".

</dd> <dt>

**SchemaAvailable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the schema of the [**MSFT\_SomFilter**](msft-somfilter.md) object is available. True if the schema is available; otherwise false.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\policy<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>PolicMan.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PolicMan.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Rule**](msft-rule.md)
</dt> </dl>

 

 




