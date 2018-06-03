---
Description: The MSFT\_Rule class represents a single rule in a MSFT\_SomFilter object. The rule is expressed as a query. The MSFT\_Rule class is compiled in the \\root\\policy namespace.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 81e2a8b9-201a-4e38-90a3-163d589dbdfe
ms.prod: windows-server-dev
ms.technology:
- group-policy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_Rule class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_Rule class

The **MSFT\_Rule** class represents a single rule in a [**MSFT\_SomFilter**](msft-somfilter.md) object. The rule is expressed as a query. The **MSFT\_Rule** class is compiled in the \\root\\policy namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{D157AAFD-D42F-45cd-B30B-F67CF152C9F9}"), AMENDMENT]
class MSFT_Rule
{
  string QueryLanguage = "WQL";
  string TargetNamespace;
  string Query;
};
```

## Members

The **MSFT\_Rule** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_Rule** class has these properties.

<dl> <dt>

**Query**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**NOT\_NULL**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Query that defines the scope of the rule.

</dd> <dt>

**QueryLanguage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**NOT\_NULL**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Language in which the query is expressed. The property value must be "WQL".

</dd> <dt>

**TargetNamespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**NOT\_NULL**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Namespace in which the query is evaluated.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\policy<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>PolicMan.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PolicMan.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SomFilter**](msft-somfilter.md)
</dt> </dl>

 

 




