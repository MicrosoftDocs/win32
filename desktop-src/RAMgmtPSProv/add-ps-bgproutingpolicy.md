---
title: Add method of the PS\_BgpRoutingPolicy class
description: Adds a new BGP routing policy to the policy store.
audience: developer
ms.assetid: 5ea11549-9f07-4044-959e-2ecb20b3b5bb
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_BgpRoutingPolicy class
- PS_BgpRoutingPolicy class, Add method
topic_type:
- apiref
api_name:
- PS_BgpRoutingPolicy.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_BgpRoutingPolicy class

Adds a new BGP routing policy to the policy store.

## Syntax


```mof
uint32 Add(
  [in]  boolean                PassThru,
  [in]  string                 RoutingDomain,
  [in]  string                 IgnorePrefix[],
  [in]  string                 Name,
  [in]  string                 MatchCommunity[],
  [in]  uint32                 NewLocalPref,
  [in]  string                 AddCommunity[],
  [in]  boolean                Force,
  [in]  uint32                 NewMED,
  [in]  uint32                 PolicyType,
  [in]  string                 NewNextHop,
  [in]  string                 RemoveCommunity[],
  [in]  string                 MatchPrefix[],
  [in]  uint32                 MatchASNRange[],
  [in]  string                 MatchNextHop[],
  [in]  boolean                ClearMED,
  [in]  boolean                RemoveAllCommunities,
  [out] BgpRoutingPolicyConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether *cmdletOutput* parameter returns an output object. **True** to return an output object; otherwise **false**.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the routing domain.

</dd> <dt>

*IgnorePrefix* \[in\]
</dt> <dd>

An array that contains the IP network prefixes to ignore during this procedure.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The unique alphanumeric ID of the routing policy.

</dd> <dt>

*MatchCommunity* \[in\]
</dt> <dd>

An array that contains the community attribute values to match with route advertisements.

</dd> <dt>

*NewLocalPref* \[in\]
</dt> <dd>

The **LOCAL-PREF** attribute for the routing policy.

</dd> <dt>

*AddCommunity* \[in\]
</dt> <dd>

An array that contains the community attribute values to add to BGP routes.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether the policy displays a confirmation prompt before adding the specified routing policy to policy store. **True** to display the confirmation prompt; otherwise **false**.

</dd> <dt>

*NewMED* \[in\]
</dt> <dd>

The multi-exit discriminator (MED) to add to BGP routes.

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

*NewNextHop* \[in\]
</dt> <dd>

The next-hop value to add to BGP routes.

</dd> <dt>

*RemoveCommunity* \[in\]
</dt> <dd>

An array that contains the community attribute values to remove from BGP routes.

</dd> <dt>

*MatchPrefix* \[in\]
</dt> <dd>

An array that contains the network prefixes to match with BGP route advertisements.

</dd> <dt>

*MatchASNRange* \[in\]
</dt> <dd>

An array that contains a range of Autonomous System Numbers (ASN) to match with the **AS-PATH** values of BGP route advertisements.

</dd> <dt>

*MatchNextHop* \[in\]
</dt> <dd>

An array that contains next-hop values to match with BGP route advertisements.

</dd> <dt>

*ClearMED* \[in\]
</dt> <dd>

Indicates whether this routing policy removes the MED value from route advertisements. **True** to remove MED values from BGP route advertisements; otherwise **false**.

</dd> <dt>

*RemoveAllCommunities* \[in\]
</dt> <dd>

Set **True** to remove all communities from the BGP route.

**Windows Server 2012 R2:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**BgpRoutingPolicyConfig**](bgproutingpolicyconfig.md) object that receives the new routing policy.

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

 

 





