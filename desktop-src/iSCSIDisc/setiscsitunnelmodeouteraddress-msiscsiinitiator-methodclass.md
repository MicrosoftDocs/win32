---
Description: The SetIscsiTunnelModeOuterAddress method sets the iSCSI Tunnel Outer Mode address for the initiator.
ms.assetid: 4715107e-dddc-479a-89b2-c00175fc1247
title: SetIscsiTunnelModeOuterAddress method of the MSIscsiInitiator\_MethodClass class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetIscsiTunnelModeOuterAddress method of the MSIscsiInitiator\_MethodClass class

The **SetIscsiTunnelModeOuterAddress** method sets the iSCSI Tunnel Outer Mode address for the initiator.

## Syntax


```mof
uint32 SetIscsiTunnelModeOuterAddress(
  [in] string  InitiatorName,
  [in] uint32  InitiatorPortNumber,
  [in] string  DestinationAddress,
  [in] string  OuterModeAddress,
  [in] boolean Persist
);
```



## Parameters

<dl> <dt>

*InitiatorName* \[in\]
</dt> <dd>

The name of the Initiator with which the tunnel-mode outer address will be associated. If this parameter is **NULL**, all HBA initiators are configured to use the indicated tunnel-mode outer address.

</dd> <dt>

*InitiatorPortNumber* \[in\]
</dt> <dd>

Indicates the number of the port with which the tunnel-mode outer address is associated.

</dd> <dt>

*DestinationAddress* \[in\]
</dt> <dd>

The destination address to associate with the tunnel-mode outer address indicated by *OuterModeAddress*.

</dd> <dt>

*OuterModeAddress* \[in\]
</dt> <dd>

The Outer Mode address of the Initiator.

</dd> <dt>

*Persist* \[in\]
</dt> <dd>

When **TRUE**, this parameter indicates that the iSCSI initiator service stores the Tunnel-Mode Outer Address in non-volatile memory and that the address will persist across restarts of the Initiator and the iSCSI Initiator Service.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSIscsiInitiator\_MethodClass**](msiscsiinitiator-methodclass.md)
</dt> </dl>

 

 




