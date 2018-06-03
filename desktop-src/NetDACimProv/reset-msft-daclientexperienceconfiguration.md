---
Description: Resets the DirectAccess client experience settings.
ms.assetid: 8199c7dc-8ab3-48cd-b23f-1333b2f243d4
title: Reset method of the MSFT\_DAClientExperienceConfiguration class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Reset method of the MSFT\_DAClientExperienceConfiguration class

Resets the DirectAccess client experience settings.

## Syntax


```mof
uint32 Reset(
  [in]  boolean                              CorporateResources,
  [in]  boolean                              IPsecTunnelEndpoints,
  [in]  boolean PreferLocalNamesAllowed      In,
  [in]  boolean                              SupportEmail,
  [in]  boolean                              FriendlyName,
  [in]  boolean                              PassiveMode,
  [in]  boolean                              CustomCommands,
  [in]  boolean                              ManualEntryPointSelectionAllowed,
  [in]  boolean                              GslbFqdn,
  [in]  boolean                              ForceTunneling,
  [in]  boolean                              PassThru,
  [out] MSFT_DAClientExperienceConfiguration OutputObject
);
```



## Parameters

<dl> <dt>

*CorporateResources* \[in\]
</dt> <dd>

Specifies whether to reset the **CorporateResources** property of the [**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md) object.

</dd> <dt>

*IPsecTunnelEndpoints* \[in\]
</dt> <dd>

Specifies whether to reset the **IPsecTunnelEndpoints** property of the [**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md) object.

</dd> <dt>

*In* \[in\]
</dt> <dd>

Specifies whether to reset the **PreferLocalNamesAllowed** property of the [**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md) object.

</dd> <dt>

*SupportEmail* \[in\]
</dt> <dd>

Specifies whether to reset the **SupportEmail** property of the [**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md) object.

</dd> <dt>

*FriendlyName* \[in\]
</dt> <dd>

Specifies whether to reset the **FriendlyName** property of the [**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md) object.

</dd> <dt>

*PassiveMode* \[in\]
</dt> <dd>

Specifies whether to reset the **PassiveMode** property of the [**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md) object.

</dd> <dt>

*CustomCommands* \[in\]
</dt> <dd>

Specifies whether to reset the **CustomCommands** property of the [**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md) object.

</dd> <dt>

*ManualEntryPointSelectionAllowed* \[in\]
</dt> <dd>

Specifies whether to reset the **ManualEntryPointSelectionAllowed** property of the [**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md) object.

</dd> <dt>

*GslbFqdn* \[in\]
</dt> <dd>

Specifies whether to reset the **GslbFqdn** property of the [**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md) object.

</dd> <dt>

*ForceTunneling* \[in\]
</dt> <dd>

Specifies whether to reset the **ForceTunneling** property of the [**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md) object.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output an object that represents the reset settings in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives a [**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md) object that contains the reset DirectAccess client experience settings.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetDACim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetDACim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DAClientExperienceConfiguration**](msft-daclientexperienceconfiguration.md)
</dt> </dl>

 

 




