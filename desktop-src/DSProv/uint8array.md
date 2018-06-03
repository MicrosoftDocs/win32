---
title: Uint8Array class
description: Models the AD Syntax Octet String.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b61613d2-c203-42fa-8ace-1568ef78364a
ms.prod: windows-server-dev
ms.technology:
- active-directory-domain-services
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Uint8Array class
- Uint8Array class, described
topic_type:
- apiref
api_name:
- Uint8Array
- Uint8Array.value
api_location:
- Dsprov.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Uint8Array class

Models the AD Syntax Octet String.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Uint8Array
{
  uint8 value[];
};
```

## Members

The **Uint8Array** class has these types of members:

-   [Properties](#properties)

### Properties

The **Uint8Array** class has these properties.

<dl> <dt>

**value**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of uint8 values for the Octet String.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Namespace<br/>                | Root\\directory\\LDAP<br/>                                                      |
| MOF<br/>                      | <dl> <dt>DsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Dsprov.dll</dt> </dl> |



 

 





