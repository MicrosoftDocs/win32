---
title: ITsSbTargetEx interface
description: Exposes properties that store configuration and state information about a target.
ms.assetid: 3f0f26fb-e8bc-47eb-8038-e51792ad4376
ms.tgt_platform: multiple
keywords:
- ITsSbTargetEx interface Remote Desktop Services
- ITsSbTargetEx interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- ITsSbTargetEx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ITsSbTargetEx interface

Exposes properties that store configuration and state information about a target.

This interface is only available on Windows Server 2012 R2 with [KB3091411](https://support.microsoft.com/kb/3091411) installed. The [**TargetLoad**](itssbtarget-targetload.md) property of the [**ITsSbTarget**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtarget) interface is available starting with Windows Server 2016.

## Members

The **ITsSbTargetEx** interface inherits from [**ITsSbTarget**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtarget). **ITsSbTargetEx** also has these types of members:

-   [Properties](#properties)

### Properties

The **ITsSbTargetEx** interface has these properties.



| Property                                                                      | Access type           | Description                                                                               |
|:------------------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------|
| [**EnvironmentName**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtarget-get_environmentname)<br/>             | Read/write<br/> | Retrieves or specifies the name of the environment associated with the target.<br/> |
| [**FarmName**](itssbtarget-farmname.md)<br/>                           | Read/write<br/> | Specifies or retrieves the name of the farm to which this target is joined.<br/>    |
| [**IpAddresses**](itssbtarget-ipaddresses.md)<br/>                     | Read/write<br/> | Retrieves or specifies the external IP addresses of the target.<br/>                |
| [**NumPendingConnections**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtarget-get_numpendingconnections)<br/> | Read-only<br/>  | Retrieves the number of pending user connections for the target.<br/>               |
| [**NumSessions**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtarget-get_numsessions)<br/>                     | Read-only<br/>  | Retrieves the number of sessions maintained by broker for the target.<br/>          |
| [**TargetFQDN**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtarget-get_targetfqdn)<br/>                       | Read/write<br/> | Specifies or retrieves the fully qualified domain name of the target.<br/>          |
| [**TargetLoad**](/previous-versions/windows/desktop/legacy/mt703468(v=vs.85))<br/>                     | Read-only<br/>  | Retrieves the relative load on a target.<br/>                                       |
| [**TargetName**](itssbtarget-targetname.md)<br/>                       | Read/write<br/> | Specifies or retrieves the name of the target.<br/>                                 |
| [**TargetNetbios**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtarget-get_targetnetbios)<br/>                 | Read/write<br/> | Specifies or retrieves the NetBIOS name of the target.<br/>                         |
| [**TargetPropertySet**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtarget-get_targetpropertyset)<br/>         | Read/write<br/> | Specifies or retrieves the property set for the target.<br/>                        |
| [**TargetState**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtarget-get_targetstate)<br/>                     | Read/write<br/> | Specifies or retrieves the target state.<br/>                                       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                |
| IID<br/>                      | IID\_ITsSbTargetEx is defined as 74f99987-625d-11e5-bea1-a0481c7e9064<br/> |



## See also

<dl> <dt>

[**ITsSbTarget**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtarget)
</dt> <dt>

[Remote Desktop Virtualization Interfaces](remote-desktop-virtualization-interfaces.md)
</dt> </dl>

 

