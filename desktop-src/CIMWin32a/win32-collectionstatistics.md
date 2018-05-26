---
title: Win32\_CollectionStatistics class
description: The Win32\_CollectionStatistics abstract association WMI class relates a managed system element collection and the class that represents statistical information about the collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9006e77e-55c4-42b9-b0f5-c63626e8d43e
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_CollectionStatistics class
- Win32_CollectionStatistics class, described
topic_type:
- apiref
api_name:
- Win32_CollectionStatistics
- Win32_CollectionStatistics.Stats
- Win32_CollectionStatistics.Collection
api_location:
- Wmipcima.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_CollectionStatistics class

The **Win32\_CollectionStatistics** abstract association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a managed system element collection and the class that represents statistical information about the collection.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, Association, UUID("{13FFA73F-25AA-4b66-B63C-B635514678C5}"), AMENDMENT]
class Win32_CollectionStatistics
{
  CIM_StatisticalInformation REF Stats;
  CIM_CollectionOfMSEs       REF Collection;
};
```

## Members

The **Win32\_CollectionStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_CollectionStatistics** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to an instance of a [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) object that represents the collection of managed system elements.

</dd> <dt>

**Stats**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StatisticalInformation**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to an instance of a [**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483) object that represents statistical information about a collection.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





