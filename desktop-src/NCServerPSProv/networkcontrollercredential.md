---
title: NetworkControllerCredential class
description: Stores network controller credentials.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0420396b-6db2-40ad-93de-4c622e043ddc'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["NetworkControllerCredential class", "NetworkControllerCredential class, described"]
topic_type:
- apiref
api_name:
- NetworkControllerCredential
- NetworkControllerCredential.UserName
- NetworkControllerCredential.Password
api_location:
- NCServerPSProvider.dll
api_type:
- DllExport
---

# NetworkControllerCredential class

Stores network controller credentials.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("NcServerPSProvider"), AMENDMENT]
class NetworkControllerCredential
{
  string UserName;
  string Password;
};
```

## Members

The **NetworkControllerCredential** class has these types of members:

-   [Properties](#properties)

### Properties

The **NetworkControllerCredential** class has these properties.

<dl> <dt>

**Password**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user password.

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user name.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



 

 





