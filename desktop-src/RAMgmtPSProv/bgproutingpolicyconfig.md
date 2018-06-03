---
title: BgpRoutingPolicyConfig class
description: Retrieves the policy configuration of a Border Gateway Protocol (BGP) router.
audience: developer
ms.assetid: 430395e1-4896-4925-b4a7-661d7d588286
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- BgpRoutingPolicyConfig class
- BgpRoutingPolicyConfig class, described
topic_type:
- apiref
api_name:
- BgpRoutingPolicyConfig
- BgpRoutingPolicyConfig.RoutingDomain
- BgpRoutingPolicyConfig.PolicyName
- BgpRoutingPolicyConfig.PolicyType
- BgpRoutingPolicyConfig.MatchPrefix
- BgpRoutingPolicyConfig.IgnorePrefix
- BgpRoutingPolicyConfig.MatchASNRange
- BgpRoutingPolicyConfig.MatchCommunity
- BgpRoutingPolicyConfig.MatchNextHop
- BgpRoutingPolicyConfig.NewNextHop
- BgpRoutingPolicyConfig.NewLocalPref
- BgpRoutingPolicyConfig.NewMED
- BgpRoutingPolicyConfig.ClearMED
- BgpRoutingPolicyConfig.AddCommunity
- BgpRoutingPolicyConfig.RemoveCommunity
- BgpRoutingPolicyConfig.RemoveAllCommunities
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BgpRoutingPolicyConfig class

Retrieves the policy configuration of a Border Gateway Protocol (BGP) router.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class BgpRoutingPolicyConfig
{
  string  RoutingDomain;
  string  PolicyName;
  uint32  PolicyType;
  string  MatchPrefix[];
  string  IgnorePrefix[];
  uint32  MatchASNRange[];
  string  MatchCommunity[];
  string  MatchNextHop[];
  string  NewNextHop;
  uint32  NewLocalPref;
  uint32  NewMED;
  boolean ClearMED;
  string  AddCommunity[];
  string  RemoveCommunity[];
  boolean RemoveAllCommunities;
};
```

## Members

The **BgpRoutingPolicyConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **BgpRoutingPolicyConfig** class has these properties.

<dl> <dt>

**AddCommunity**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The community value to use during BGP route matching.

</dd> <dt>

**ClearMED**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether MED values from route advertisements are to be removed.

</dd> <dt>

**IgnorePrefix**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The list IP addresses to ignore.

</dd> <dt>

**MatchASNRange**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The range of Autonomous System Numbers (ASN) to match with route advertisements.

</dd> <dt>

**MatchCommunity**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The community attribute values to match with route advertisements.

</dd> <dt>

**MatchNextHop**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The next-hop value to match with route advertisements.

</dd> <dt>

**MatchPrefix**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The list IP addresses to match with route advertisements.

</dd> <dt>

**NewLocalPref**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **LOCAL\_PREFERENCE** value of all matched routes.

</dd> <dt>

**NewMED**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The multi-exit discriminator (MED) of all matched routes.

</dd> <dt>

**NewNextHop**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The next-hop value of all matched routes.

</dd> <dt>

**PolicyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-defined alphanumeric ID of the BGP routing policy.

</dd> <dt>

**PolicyType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of the BGP routing policy.

</dd> <dt>

**RemoveAllCommunities**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to remove all communities from the BGP route.

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> <dt>

**RemoveCommunity**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The community value to remove during BGP route matching.

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-defined alphanumeric ID of the BGP routing domain.

> [!Note]  
> This property is only used with multi-tenant deployments.

 

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





