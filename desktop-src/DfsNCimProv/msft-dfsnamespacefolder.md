---
title: MSFT\_DfsNamespaceFolder class
description: Represents a DFS folder. This class can be used for the creation, modification, deletion, and movement of DFS folders.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a4c4799e-25e9-45b4-9db0-deaef423caea
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsNamespaceFolder class
- MSFT_DfsNamespaceFolder class, described
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceFolder
- MSFT_DfsNamespaceFolder.Description
- MSFT_DfsNamespaceFolder.Flags
- MSFT_DfsNamespaceFolder.NamespacePath
- MSFT_DfsNamespaceFolder.State
- MSFT_DfsNamespaceFolder.TimeToLive
api_location:
- DfsNCimProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DfsNamespaceFolder class

Represents a DFS folder. This class can be used for the creation, modification, deletion, and movement of DFS folders.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("dfsncimprov"), ClassVersion("1.0"), AMENDMENT]
class MSFT_DfsNamespaceFolder : MSFT_DfsNamespaceLinkBase
{
  string Description;
  uint32 Flags;
  string NamespacePath;
  uint32 State;
  uint32 TimeToLive;
};
```

## Members

The **MSFT\_DfsNamespaceFolder** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DfsNamespaceFolder** class has these methods.



| Method                                                                         | Description                                                                  |
|:-------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| [**GetNamespaceFolder**](getnamespacefolder-msft-dfsnamespacefolder.md)       | Retrieves the properties of a DFS folder.<br/>                         |
| [**MoveNamespaceFolder**](movenamespacefolder-msft-dfsnamespacefolder.md)     | Moves a DFS folder to another location within the same namespace.<br/> |
| [**NewNamespaceFolder**](newnamespacefolder-msft-dfsnamespacefolder.md)       | Creates a new DFS folder in the existing namespace.<br/>               |
| [**RemoveNamespaceFolder**](removenamespacefolder-msft-dfsnamespacefolder.md) | Removes a DFS folder.<br/>                                             |
| [**SetNamespaceFolder**](setnamespacefolder-msft-dfsnamespacefolder.md)       | Updates the properties of a DFS folder.<br/>                           |



 

### Properties

The **MSFT\_DfsNamespaceFolder** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets a short description of the purpose of the DFS-N root or the DFS-N link.

This property is inherited from [**MSFT\_DfsNamespaceLinkBase**](msft-dfsnamespacelinkbase.md).

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**BitMap**](https://msdn.microsoft.com/library/aa393650) ("0", "3"), [**BitValues**](https://msdn.microsoft.com/library/aa393650) ("InsiteReferrals", "TargetFailback")
</dt> </dl>

Gets or sets a bitwise combination of the enumeration values that represent the properties of the DFS-N root or the DFS-N link.

This property is inherited from [**MSFT\_DfsNamespaceLinkBase**](msft-dfsnamespacelinkbase.md).

<dt>

<span id="InsiteReferrals"></span><span id="insitereferrals"></span><span id="INSITEREFERRALS"></span>

<span id="InsiteReferrals"></span><span id="insitereferrals"></span><span id="INSITEREFERRALS"></span>**"InsiteReferrals"** ("0")


</dt> <dd>

**True** if in-site referrals are enabled for the DFS-N root or the DFS-N link; otherwise, **false**. The default value is **false**.

</dd> <dt>

<span id="TargetFailback"></span><span id="targetfailback"></span><span id="TARGETFAILBACK"></span>

<span id="TargetFailback"></span><span id="targetfailback"></span><span id="TARGETFAILBACK"></span>**"TargetFailback"** ("3")


</dt> <dd>

**True** if target failback is enabled for the DFS-N root or the DFS-N link; otherwise, **false**. The default value is **false**.

</dd> </dl>

</dd> <dt>

**NamespacePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets or sets the Universal Naming Convention (UNC) path of the DFS-N root or the DFS-N link.

A DFS-N root or a DFS-N link can have one of the following UNC path formats:



|            | Server Format                     | Domain Format                     |
|------------|-----------------------------------|-----------------------------------|
| DFS-N Root | \\\\ServerName\\DFSName           | \\\\DomainName\\DFSName           |
| DFS-N Link | \\\\ServerName\\DFSName\\LinkPath | \\\\DomainName\\DFSName\\LinkPath |



 

where:

-   The ServerName component represents the host name of a DFS root target of a DFS namespace.
-   The DomainName component represents the domain name of the domain that hosts the domain-based DFS namespace.
-   The DFSName component represents the DFS-N name.
-   The LinkPath component represents the path of the DFS-N link relative to the DFS root target share.

Stand-alone DFS namespaces must have links and roots with the formats shown in the first column, as they must contain a server name. Domain-based DFS namespaces can have links and roots with the formats from either column, although the second column's formats (which contain a domain name instead of a server name) are the preferred format.

This property is inherited from [**MSFT\_DfsNamespaceLinkBase**](msft-dfsnamespacelinkbase.md).

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets the state of the DFS-N root or the DFS-N link. The default value is "ONLINE".

This property is inherited from [**MSFT\_DfsNamespaceLinkBase**](msft-dfsnamespacelinkbase.md).

<dt>

<span id="OFFLINE"></span><span id="offline"></span>

<span id="OFFLINE"></span><span id="offline"></span>**"OFFLINE"** (3)


</dt> <dd>

Not online.

</dd> <dt>

<span id="ONLINE"></span><span id="online"></span>

<span id="ONLINE"></span><span id="online"></span>**"ONLINE"** (4)


</dt> <dd>

Online.

</dd> </dl>

</dd> <dt>

**TimeToLive**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets the interval time, in seconds, of the time to live (TTL) of the referral. A referral TTL determines the amount of time that clients cache (store) referrals for this DFS-N root or DFS-N link. The default value is 300.

This property is inherited from [**MSFT\_DfsNamespaceLinkBase**](msft-dfsnamespacelinkbase.md).

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\dfsn<br/>                                                  |
| MOF<br/>                      | <dl> <dt>DfsNCimProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsNCimProv.dll</dt> </dl> |



 

 





