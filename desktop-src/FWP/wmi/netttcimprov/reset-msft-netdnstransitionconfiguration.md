---
description: Resets the configuration for DNS64.
ms.assetid: 04603286-947c-4708-8cd3-468f9142e27f
title: Reset method of the MSFT\_NetDnsTransitionConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetDnsTransitionConfiguration.Reset
api_type: 
- COM
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# Reset method of the MSFT\_NetDnsTransitionConfiguration class

Resets the configuration for DNS64.

## Syntax


```mof
uint32 Reset(
  [in]  boolean                            State,
  [in]  boolean                            OnlySendAQuery,
  [in]  boolean                            Latency,
  [in]  boolean                            AlwaysSynthesize,
  [in]  boolean                            PrefixMapping,
  [in]  boolean                            SendInterface,
  [in]  boolean                            AcceptInterface,
  [in]  boolean                            PassThru,
  [out] MSFT_NetDnsTransitionConfiguration OutputObject
);
```



## Parameters

<dl> <dt>

*State* \[in\]
</dt> <dd>

Indicates whether to reset the **State** property of the [**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md) object.

</dd> <dt>

*OnlySendAQuery* \[in\]
</dt> <dd>

Indicates whether to reset the **OnlySendAQuery** property of the [**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md) object.

</dd> <dt>

*Latency* \[in\]
</dt> <dd>

Indicates whether to reset the **Latency** property of the [**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md) object.

</dd> <dt>

*AlwaysSynthesize* \[in\]
</dt> <dd>

Indicates whether to reset the **AlwaysSynthesize** property of the [**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md) object.

</dd> <dt>

*PrefixMapping* \[in\]
</dt> <dd>

Indicates whether to reset the **PrefixMapping** property of the [**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md) object.

</dd> <dt>

*SendInterface* \[in\]
</dt> <dd>

Indicates whether to reset the **SendInterface** property of the [**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md) object.

</dd> <dt>

*AcceptInterface* \[in\]
</dt> <dd>

Indicates whether to reset the **AcceptInterface** property of the [**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md) object.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output the an object that represents the reset DNS64 configuration in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives the reset [**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md)
</dt> </dl>

 

 




