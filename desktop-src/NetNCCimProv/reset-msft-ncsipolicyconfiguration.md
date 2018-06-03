---
Description: Resets the NCSI configuration.
ms.assetid: 790a1121-9bd5-4541-9550-8320b0d55d15
title: Reset method of the MSFT\_NCSIPolicyConfiguration class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Reset method of the MSFT\_NCSIPolicyConfiguration class

Resets the NCSI configuration.

## Syntax


```mof
uint32 Reset(
  [in]  boolean                         CorporateDNSProbeHostAddress,
  [in]  boolean                         CorporateDNSProbeHostName,
  [in]  boolean CorporateSitePrefixList In,
  [in]  boolean                         DomainLocationDeterminationURL,
  [in]  boolean                         PassThru,
  [out] MSFT_NCSIPolicyConfiguration    OutputObject
);
```



## Parameters

<dl> <dt>

*CorporateDNSProbeHostAddress* \[in\]
</dt> <dd>

Specifies whether to reset the **CorporateDNSProbeHostAddress** of the [**MSFT\_NCSIPolicyConfiguration**](msft-ncsipolicyconfiguration.md) object.

</dd> <dt>

*CorporateDNSProbeHostName* \[in\]
</dt> <dd>

Specifies whether to reset the **CorporateDNSProbeHostName** of the [**MSFT\_NCSIPolicyConfiguration**](msft-ncsipolicyconfiguration.md) object.

</dd> <dt>

*In* \[in\]
</dt> <dd>

Specifies whether to reset the **CorporateSitePrefixList** of the [**MSFT\_NCSIPolicyConfiguration**](msft-ncsipolicyconfiguration.md) object.

</dd> <dt>

*DomainLocationDeterminationURL* \[in\]
</dt> <dd>

Specifies whether to reset the **DomainLocationDeterminationURL** of the [**MSFT\_NCSIPolicyConfiguration**](msft-ncsipolicyconfiguration.md) object.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output an object that represents the reset NCSI configuration in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives the reset [**MSFT\_NCSIPolicyConfiguration**](msft-ncsipolicyconfiguration.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetNCCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetNCCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NCSIPolicyConfiguration**](msft-ncsipolicyconfiguration.md)
</dt> </dl>

 

 




