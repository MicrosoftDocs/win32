---
title: DN\_With\_String class
description: Models the DN\_With\_String AD syntax.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'c2d9d423-c515-4bcf-8fe9-f118405490be'
ms.prod: 'windows-server-dev'
ms.technology:
- 'active-directory-domain-services'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DN_With_String class", "DN_With_String class, described"]
topic_type:
- apiref
api_name:
- DN_With_String
- DN_With_String.dnString
- DN_With_String.value
api_location:
- Dsprov.dll
api_type:
- DllExport
---

# DN\_With\_String class

Models the DN\_With\_String AD syntax.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class DN_With_String
{
  string dnString;
  string value;
};
```

## Members

The **DN\_With\_String** class has these types of members:

-   [Properties](#properties)

### Properties

The **DN\_With\_String** class has these properties.

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

Data type: **string**
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



 

 





