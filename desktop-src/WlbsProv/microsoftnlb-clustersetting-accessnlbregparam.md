---
title: AccessNLBRegParam method of the MicrosoftNLB\_ClusterSetting class
description: Gets and sets the following instance-specific/global NLB registry parameters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 36a2e7dd-717e-4c07-ba36-cf0d460262bf
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AccessNLBRegParam method
- AccessNLBRegParam method, MicrosoftNLB_ClusterSetting class
- MicrosoftNLB_ClusterSetting class, AccessNLBRegParam method
topic_type:
- apiref
api_name:
- MicrosoftNLB_ClusterSetting.AccessNLBRegParam
api_location:
- WlbsProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AccessNLBRegParam method of the MicrosoftNLB\_ClusterSetting class

Gets and sets the following instance-specific/global NLB registry parameters. For the instance-specific parameters to take effect, call the [**LoadAllSettings**](microsoftnlb-clustersetting-loadallsettings.md) method after calling this method. The global parameters will take effect upon the next boot-up of the system.

## Syntax


```mof
boolean AccessNLBRegParam(
  [in]      boolean Get = ,
  [in]      boolean InstanceOnly = ,
  [in]      string  Name,
  [in, out] uint32  Value
);
```



## Parameters

<dl> <dt>

*Get* \[in\]
</dt> <dd>

Indicates whether the value is being retrieved or set. **VARIANT\_TRUE** indicates that the value is being retrieved.

</dd> <dt>

*InstanceOnly* \[in\]
</dt> <dd>

Indicates whether to use the instance-specific or global value of the setting. **VARIANT\_TRUE** indicates that the instance-specific value should be used.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the setting to retrieve or set. Supported values include:

<dt>

<span id="UnicastInterHostCommSupport"></span><span id="unicastinterhostcommsupport"></span><span id="UNICASTINTERHOSTCOMMSUPPORT"></span>

<span id="UnicastInterHostCommSupport"></span><span id="unicastinterhostcommsupport"></span><span id="UNICASTINTERHOSTCOMMSUPPORT"></span>**UnicastInterHostCommSupport**


</dt> <dd>

Indicates whether nodes operating in unicast mode can communicate with each other. One (1) enables inter-host communications, and zero (0) disables interhost communication. This setting is instance-specific.

</dd> <dt>

<span id="EnableTCPNotification"></span><span id="enabletcpnotification"></span><span id="ENABLETCPNOTIFICATION"></span>

<span id="EnableTCPNotification"></span><span id="enabletcpnotification"></span><span id="ENABLETCPNOTIFICATION"></span>**EnableTCPNotification**


</dt> <dd>

Enables an different methods of tracking TCP connections to ensure affinity between the host that received the original connection and the client. This setting is global. Possible value are 0, 1, and 2.

</dd> </dl> </dd> <dt>

*Value* \[in, out\]
</dt> <dd>

Value to be set

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md)
</dt> </dl>

 

 





