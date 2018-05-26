---
title: DASiteAddresses class
description: Defines the list of IPAddresses corresponding to all the codes of a DirectAccess site.
audience: developer
ms.assetid: 58e23841-c527-45e0-ae40-1ce307cb96ff
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DASiteAddresses class
- DASiteAddresses class, described
topic_type:
- apiref
api_name:
- DASiteAddresses
- DASiteAddresses.Addresses
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DASiteAddresses class

Defines the list of IPAddresses corresponding to all the codes of a DirectAccess site.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class DASiteAddresses
{
  string Addresses[];
};
```

## Members

The **DASiteAddresses** class has these types of members:

-   [Properties](#properties)

### Properties

The **DASiteAddresses** class has these properties.

<dl> <dt>

**Addresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of addresses for the site.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





