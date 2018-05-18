---
title: MSFT\_DfsNamespaceLinkBase class
description: Represents the base functionality of a DFS namespace (DFS-N) root or a DFS-N link.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6c2829a9-d6eb-490a-aec6-05be2ea185d6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-namespace'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_DfsNamespaceLinkBase class", "MSFT_DfsNamespaceLinkBase class, described"]
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceLinkBase
- MSFT_DfsNamespaceLinkBase.Description
- MSFT_DfsNamespaceLinkBase.Flags
- MSFT_DfsNamespaceLinkBase.NamespacePath
- MSFT_DfsNamespaceLinkBase.State
- MSFT_DfsNamespaceLinkBase.TimeToLive
api_location:
- DfsNCimProv.dll
api_type:
- DllExport
---

# MSFT\_DfsNamespaceLinkBase class

Represents the base functionality of a DFS namespace (DFS-N) root or a DFS-N link.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, ClassVersion("1.0"), AMENDMENT]
class MSFT_DfsNamespaceLinkBase
{
  string Description;
  uint32 Flags;
  string NamespacePath;
  uint32 State;
  uint32 TimeToLive;
};
```

## Members

The **MSFT\_DfsNamespaceLinkBase** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DfsNamespaceLinkBase** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets a short description of the purpose of the DFS-N root or the DFS-N link.

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

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets the state of the DFS-N root or the DFS-N link. The default value is "ONLINE".

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

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\dfsn<br/>                                                  |
| MOF<br/>                      | <dl> <dt>DfsNCimProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsNCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DFSNamespace**](msft-dfsnamespace.md)
</dt> <dt>

[**MSFT\_DFSNamespaceFolder**](msft-dfsnamespacefolder.md)
</dt> </dl>

 

 





