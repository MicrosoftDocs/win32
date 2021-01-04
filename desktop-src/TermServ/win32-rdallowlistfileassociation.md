---
title: Win32_RDAllowListFileAssociation class
description: Describes a published file type association with a RemoteApp.
ms.assetid: 80cc8f5e-a7f0-458c-b05b-7822306f839a
ms.tgt_platform: multiple
keywords:
- Win32_RDAllowListFileAssociation class Remote Desktop Services
- Win32_RDAllowListFileAssociation class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RDAllowListFileAssociation
- Win32_RDAllowListFileAssociation.ExtName
- Win32_RDAllowListFileAssociation.AppAlias
- Win32_RDAllowListFileAssociation.ProgIdHint
api_location:
- TsPubWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RDAllowListFileAssociation class

Describes a published file type association with a RemoteApp.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_RDAllowListFileAssociation
{
  string ExtName;
  string AppAlias;
  string ProgIdHint;
};
```

## Members

The **Win32\_RDAllowListFileAssociation** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_RDAllowListFileAssociation** class has these properties.

<dl> <dt>

**AppAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Alias of the RemoteApp associated with the extension.

</dd> <dt>

**ExtName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Name of the extension, for example .txt.

</dd> <dt>

**ProgIdHint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Hint to help open documents with this file association

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\cimv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TsAllow.mof</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>TsPubWmi.dll</dt> </dl> |



 

 





