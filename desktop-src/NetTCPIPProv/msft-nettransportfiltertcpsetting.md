---
Description: Represents an association between a.
ms.assetid: 6b602398-2e04-42e4-a7b1-1e48afdb7465
title: MSFT\_NetTransportFilterTCPSetting class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_NetTransportFilterTCPSetting class

Represents an association between a transport filter and a TCP setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, UMLPackagePath("CIM::Core::CoreElements"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
class MSFT_NetTransportFilterTCPSetting : CIM_Dependency
{
  MSFT_NetTransportFilter REF Antecedent;
  MSFT_NetTCPSetting      REF Dependent;
};
```

## Members

The **MSFT\_NetTransportFilterTCPSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetTransportFilterTCPSetting** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetTransportFilter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**MSFT\_NetTransportFilter**](msft-nettransportfilter.md) object for the filter associated with the TCP setting.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetTCPSetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**MSFT\_NetTCPSetting**](msft-nettcpsetting.md) object fo the TCP setting associated with the filter.

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

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[**MSFT\_NetTransportFilter**](msft-nettransportfilter.md)
</dt> <dt>

[**MSFT\_NetTCPSetting**](msft-nettcpsetting.md)
</dt> </dl>

 

 




