---
Description: The SetIscsiIKEInfo method sets the iSCSI IKE authentication information for the initiator.
ms.assetid: 670f2788-6379-4f7e-9ee3-4ae46249074c
title: SetIscsiIKEInfo method of the MSIscsiInitiator\_MethodClass class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetIscsiIKEInfo method of the MSIscsiInitiator\_MethodClass class

The **SetIscsiIKEInfo** method sets the iSCSI IKE authentication information for the initiator.

## Syntax


```mof
uint32 SetIscsiIKEInfo(
  [in] string                                             InitiatorName,
  [in] uint32                                             InitiatorPortNumber,
  [in] MSIscsiInitiator_IKEPresharedKeyAuthenticationInfo AuthInfo,
  [in] boolean                                            Persist
);
```



## Parameters

<dl> <dt>

*InitiatorName* \[in\]
</dt> <dd>

The Initiator name.

</dd> <dt>

*InitiatorPortNumber* \[in\]
</dt> <dd>

The port number associated with the Initiator.

</dd> <dt>

*AuthInfo* \[in\]
</dt> <dd>

An [**MSIscsiInitiator\_IKEPresharedKeyAuthenticationInfo**](msiscsiinitiator-ikepresharedkeyauthenticationinfo.md) structure containing IKE Authentication information.

</dd> <dt>

*Persist* \[in\]
</dt> <dd>

Indicates if the IKE information will persist.

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

 

 




