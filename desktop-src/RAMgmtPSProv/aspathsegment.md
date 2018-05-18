---
title: ASPathSegment class
description: Retrieves Border Gateway Protocol (BGP) routing information about a path segment to an autonomous system (AS).
audience: developer
ms.assetid: '0adb3c02-9dee-4d19-8de9-24397fbf6514'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ASPathSegment class", "ASPathSegment class, described"]
topic_type:
- apiref
api_name:
- ASPathSegment
- ASPathSegment.PathType
- ASPathSegment.ASN
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# ASPathSegment class

Retrieves Border Gateway Protocol (BGP) routing information about a path segment to an autonomous system (AS).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class ASPathSegment
{
  string PathType;
  uint32 ASN[];
};
```

## Members

The **ASPathSegment** class has these types of members:

-   [Properties](#properties)

### Properties

The **ASPathSegment** class has these properties.

<dl> <dt>

**ASN**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of Autonomous System Numbers (ASN) of the segment path.

</dd> <dt>

**PathType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of the path segment.

The possible values are.

<dt>

<span id="AS_SET"></span><span id="as_set"></span>

**AS\_SET** ("AS\_SET")


</dt> <dd></dd> <dt>

<span id="AS_SEQUENCE"></span><span id="as_sequence"></span>

**AS\_SEQUENCE** ("AS\_SEQUENCE")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





