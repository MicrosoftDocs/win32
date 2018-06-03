---
title: MSFT\_DfsNamespaceAccess class
description: Controls the access permissions for a DFS folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2eb107c4-5a5a-4cff-925e-4472aa6d635c
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsNamespaceAccess class
- MSFT_DfsNamespaceAccess class, described
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceAccess
- MSFT_DfsNamespaceAccess.AccessType
- MSFT_DfsNamespaceAccess.AccountName
- MSFT_DfsNamespaceAccess.NamespacePath
api_location:
- DfsNCimProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DfsNamespaceAccess class

Controls the access permissions for a DFS folder.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("dfsncimprov"), ClassVersion("1.0"), AMENDMENT]
class MSFT_DfsNamespaceAccess
{
  uint32 AccessType;
  string AccountName;
  string NamespacePath;
};
```

## Members

The **MSFT\_DfsNamespaceAccess** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DfsNamespaceAccess** class has these methods.



| Method                                                                                     | Description                                                                                |
|:-------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| [**GetNamespaceAccessRights**](getnamespaceaccessrights-msft-dfsnamespaceaccess.md)       | Retrieves access permissions for the specified DFS folder.<br/>                      |
| [**GrantNamespaceAccessRights**](grantnamespaceaccessrights-msft-dfsnamespaceaccess.md)   | Grants access permissions for a DFS folder to the specified users or groups.<br/>    |
| [**RemoveNamespaceAccessRights**](removenamespaceaccessrights-msft-dfsnamespaceaccess.md) | Removes access permissions for a DFS folder for the specified users or groups.<br/>  |
| [**RevokeNamespaceAccessRights**](revokenamespaceaccessrights-msft-dfsnamespaceaccess.md) | Revokes access permissions for a DFS folder from the specified users or groups.<br/> |



 

### Properties

The **MSFT\_DfsNamespaceAccess** class has these properties.

<dl> <dt>

**AccessType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets the type of access to be changed for the users or groups on a DFS folder. The default value is "enumerate".

<dt>

<span id="enumerate"></span><span id="ENUMERATE"></span>

<span id="enumerate"></span><span id="ENUMERATE"></span>**"enumerate"** (0)


</dt> <dd>

The right to view and enumerate the contents of a DFS folder.

</dd> </dl>

</dd> <dt>

**AccountName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets or sets the names of users or groups for which to change access permissions on a DFS folder.

</dd> <dt>

**NamespacePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets or sets the Universal Naming Convention (UNC) path of the DFS folder on which to change access permissions. The UNC path has a format of \\\\HostName\\SharedName\[\\ObjectName\]\*, where:

-   The HostName component represents either the host name of a server or the domain name of a domain that hosts resources.
-   The SharedName component represents the share name or the name of the resource that is being accessed.
-   Each ObjectName component represents the name of a directory on the resource that is being accessed.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\dfsn<br/>                                                  |
| MOF<br/>                      | <dl> <dt>DfsNCimProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsNCimProv.dll</dt> </dl> |



 

 





