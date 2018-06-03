---
title: Set method of the PS\_BgpRoutingPolicy class
description: Updates a BGP routing policy.
audience: developer
ms.assetid: ee013636-f0e7-4c78-9774-af6d931edcb2
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_BgpRoutingPolicy class
- PS_BgpRoutingPolicy class, Set method
topic_type:
- apiref
api_name:
- PS_BgpRoutingPolicy.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_BgpRoutingPolicy class

Updates a BGP routing policy.

## Syntax


```mof
uint32 Set(
  [in]  string                 Name,
  [in]  boolean                PassThru,
  [in]  uint32                 PolicyType,
  [in]  string                 RoutingDomain,
  [in]  boolean                Force,
  [in]  string                 AddCommunity[],
  [in]  string                 RemoveCommunity[],
  [in]  string                 RemovePolicyClause[],
  [in]  uint32                 MatchASNRange[],
  [in]  string                 IgnorePrefix[],
  [in]  string                 MatchCommunity[],
  [in]  string                 MatchPrefix[],
  [in]  string                 MatchNextHop[],
  [in]  boolean                ClearMED,
  [in]  uint32                 NewLocalPref,
  [in]  uint32                 NewMED,
  [in]  string                 NewNextHop,
  [in]  boolean                RemoveAllCommunities,
  [out] BgpRoutingPolicyConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The unique alphanumeric ID of the routing policy to update.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether *cmdletOutput* parameter returns an output object. **True** to return an output object; otherwise **false**.

</dd> <dt>

*PolicyType* \[in\]
</dt> <dd>

The type of filtering procedure that this routing policy performs. You can set this parameter to one of the following values.

<dt>

<span id="ModifyAttribute"></span><span id="modifyattribute"></span><span id="MODIFYATTRIBUTE"></span>

**ModifyAttribute** (1)


</dt> <dd></dd> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>

**Allow** (2)


</dt> <dd></dd> <dt>

<span id="Deny"></span><span id="deny"></span><span id="DENY"></span>

**Deny** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the routing domain.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether the policy displays a confirmation prompt before adding the specified routing policy to policy store. **True** to display the confirmation prompt; otherwise **false**.

</dd> <dt>

*AddCommunity* \[in\]
</dt> <dd>

An array that contains the community attribute values to add to BGP routes.

</dd> <dt>

*RemoveCommunity* \[in\]
</dt> <dd>

An array that contains the community attribute values to remove from BGP routes.

</dd> <dt>

*RemovePolicyClause* \[in\]
</dt> <dd>

An array that contains the policy clauses to remove from BGP routes.

</dd> <dt>

*MatchASNRange* \[in\]
</dt> <dd>

An array that contains a range of Autonomous System Numbers (ASN) to match with the **AS-PATH** values of BGP route advertisements.

</dd> <dt>

*IgnorePrefix* \[in\]
</dt> <dd>

An array that contains the IP network prefixes to ignore during this procedure.

</dd> <dt>

*MatchCommunity* \[in\]
</dt> <dd>

An array that contains the community attribute values to match with route advertisements.

</dd> <dt>

*MatchPrefix* \[in\]
</dt> <dd>

An array that contains the network prefixes to match with BGP route advertisements.

</dd> <dt>

*MatchNextHop* \[in\]
</dt> <dd>

An array that contains next-hop values to match with BGP route advertisements.

</dd> <dt>

*ClearMED* \[in\]
</dt> <dd>

Indicates whether this routing policy removes the MED value from route advertisements. **True** to remove MED values from BGP route advertisements; otherwise **false**.

</dd> <dt>

*NewLocalPref* \[in\]
</dt> <dd>

The **LOCAL-PREF** attribute for the routing policy.

</dd> <dt>

*NewMED* \[in\]
</dt> <dd>

The multi-exit discriminator (MED) to add to BGP routes.

</dd> <dt>

*NewNextHop* \[in\]
</dt> <dd>

The next-hop value to add to BGP routes.

</dd> <dt>

*RemoveAllCommunities* \[in\]
</dt> <dd>

Set **True** to remove all communities from the BGP route.

**Windows Server 2012 R2:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**BgpRoutingPolicyConfig**](bgproutingpolicyconfig.md) object that receives the updated routing policy.

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

[**PS\_BgpRoutingPolicy**](ps-bgproutingpolicy.md)
</dt> </dl>

 

 





