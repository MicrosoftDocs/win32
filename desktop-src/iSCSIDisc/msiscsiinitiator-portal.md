---
Description: 'The MSIscsiInitiator\_Portal structure describes the characteristics of an iSCSI Initiator portal.'
ms.assetid: 'ccfd3e6b-df8c-4a87-b392-662ced2f3594'
title: 'MSIscsiInitiator\_Portal class'
---

# MSIscsiInitiator\_Portal class

The **MSIscsiInitiator\_Portal** structure describes the characteristics of an iSCSI Initiator portal.

## Syntax

``` syntax
class MSIscsiInitiator_Portal
{
  uint32 Index;
  string SymbolicName;
  string Address;
  uint16 Port;
};
```

## Members

The **MSIscsiInitiator\_Portal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_Portal** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address or DNS name associated with the portal.

</dd> <dt>

**Index**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The index number associated with the portal.

</dd> <dt>

**Port**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port associated with the portal.

</dd> <dt>

**SymbolicName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The symbolic name of the portal.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



 

 




