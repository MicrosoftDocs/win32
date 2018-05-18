---
Description: 'The SetIscsiInitiatorCHAPSharedSecret function sets the iSCSI CHAP Shared Secret for the Initiator.'
ms.assetid: '93bffe27-2b63-4748-901e-1a2f4f80f165'
title: 'SetIscsiInitiatorCHAPSharedSecret method of the MSIscsiInitiator\_MethodClass class'
---

# SetIscsiInitiatorCHAPSharedSecret method of the MSIscsiInitiator\_MethodClass class

The **SetIscsiInitiatorCHAPSharedSecret** function sets the iSCSI CHAP Shared Secret for the Initiator.

## Syntax


```mof
uint32 SetIscsiInitiatorCHAPSharedSecret(
  [in] uint8 SharedSecret[]
);
```



## Parameters

<dl> <dt>

*SharedSecret* \[in\]
</dt> <dd>

The iSCSI CHAP Shared Secret to associate with the Initiator.

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

 

 




