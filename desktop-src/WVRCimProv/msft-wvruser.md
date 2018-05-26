---
title: MSFT\_WvrUser class
description: Represents a user account.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ed517dc3-10d2-4b11-9916-374335a30d29
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WvrUser class
- MSFT_WvrUser class, described
topic_type:
- apiref
api_name:
- MSFT_WvrUser
- MSFT_WvrUser.UserName
api_location:
- wvrcimprov.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_WvrUser class

Represents a user account.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("wvrcimprov"), AMENDMENT]
class MSFT_WvrUser
{
  string UserName;
};
```

## Members

The **MSFT\_WvrUser** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WvrUser** class has these properties.

<dl> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Name of the account.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



 

 





