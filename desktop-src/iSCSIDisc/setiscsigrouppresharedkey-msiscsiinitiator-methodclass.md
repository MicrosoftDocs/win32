---
Description: 'The SetIscsiGroupPresharedKey method sets the iSCSI group Preshared Key for the Initiator.'
ms.assetid: 'a7bb20a6-3e4b-4b3e-973c-f23f584f7d24'
title: 'SetIscsiGroupPresharedKey method of the MSiSCSIInitiator\_MethodClass class'
---

# SetIscsiGroupPresharedKey method of the MSiSCSIInitiator\_MethodClass class

The **SetIscsiGroupPresharedKey** method sets the iSCSI group Preshared Key for the Initiator.

## Syntax


```mof
uint32 SetIscsiGroupPresharedKey(
  [in] uint8   Key[],
  [in] boolean Persist
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

The key to associate with the Initiator.

</dd> <dt>

*Persist* \[in\]
</dt> <dd>

Indicates if the key will persist.

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

 

 




