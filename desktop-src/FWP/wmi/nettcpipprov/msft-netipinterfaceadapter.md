---
description: Represents an association between a TCP/IP network interface and a network port.
ms.assetid: 0a9ffc0f-15f4-4d5a-b7c8-77534a285dc7
title: MSFT\_NetIPInterfaceAdapter class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIPInterfaceAdapter
- MSFT_NetIPInterfaceAdapter.Antecedent
- MSFT_NetIPInterfaceAdapter.Dependent
api_type: 
- DllExport
api_location: 
- NetTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIPInterfaceAdapter class

Represents an association between a TCP/IP network interface and a network port.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, UMLPackagePath("CIM::Device::Ports"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
class MSFT_NetIPInterfaceAdapter : CIM_PortImplementsEndpoint
{
  MSFT_NetIPInterface REF Antecedent;
  CIM_NetworkPort     REF Dependent;
};
```

## Members

The **MSFT\_NetIPInterfaceAdapter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetIPInterfaceAdapter** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetIPInterface**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

The [**MSFT\_NetIPInterface**](msft-netipinterface.md) object associated with the network port.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_NetworkPort**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Dependent")
</dt> </dl>

The [**CIM\_NetworkPort**](/previous-versions//cc136873(v=vs.85)) object associated with the IP interface.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PortImplementsEndpoint**](cim-portimplementsendpoint.md)
</dt> <dt>

[**MSFT\_NetIPInterface**](msft-netipinterface.md)
</dt> <dt>

[**CIM\_NetworkPort**](/previous-versions//cc136873(v=vs.85))
</dt> </dl>

 

