---
Description: The SetIscsiInitiatorRADIUSSharedSecret function sets the RADIUS shared secret for the Initiator.
ms.assetid: 6ec10834-a2df-499b-ace3-01600f4a3140
title: SetIscsiInitiatorRADIUSSharedSecret method of the MSIscsiInitiator\_MethodClass class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetIscsiInitiatorRADIUSSharedSecret method of the MSIscsiInitiator\_MethodClass class

The **SetIscsiInitiatorRADIUSSharedSecret** function sets the RADIUS shared secret for the Initiator.

## Syntax


```mof
uint32 SetIscsiInitiatorRADIUSSharedSecret(
  [in] uint8 SharedSecret[]
);
```



## Parameters

<dl> <dt>

*SharedSecret* \[in\]
</dt> <dd>

The Shared Secret to associate with the initiator.

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

 

 




