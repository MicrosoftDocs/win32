---
title: DN\_With\_Binary class
description: Models the DN\_With\_Binary AD Syntax.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'd3959171-65f9-4b22-bd41-9b212a73fdd9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'active-directory-domain-services'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DN_With_Binary class", "DN_With_Binary class, described"]
topic_type:
- apiref
api_name:
- DN_With_Binary
- DN_With_Binary.dnString
- DN_With_Binary.value
api_location:
- Dsprov.dll
api_type:
- DllExport
---

# DN\_With\_Binary class

Models the DN\_With\_Binary AD Syntax.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class DN_With_Binary
{
  string dnString;
  uint8  value[];
};
```

## Members

The **DN\_With\_Binary** class has these types of members:

-   [Properties](#properties)

### Properties

The **DN\_With\_Binary** class has these properties.

<dl> <dt>

**dnString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The DN string component of the tuple.

</dd> <dt>

**value**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Value component of the tuple.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Namespace<br/>                | Root\\directory\\LDAP<br/>                                                      |
| MOF<br/>                      | <dl> <dt>DsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Dsprov.dll</dt> </dl> |



 

 





