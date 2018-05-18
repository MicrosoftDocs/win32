---
Description: 'The RemoveConnection method removes a connection from the specified session.'
ms.assetid: '3d6e880c-5b4d-4e60-8965-efbcfcfe874f'
title: 'RemoveConnection method of the MSIscsiInitiator\_SessionClass class'
---

# RemoveConnection method of the MSIscsiInitiator\_SessionClass class

The **RemoveConnection** method removes a connection from the specified session.

## Syntax


```mof
uint32 RemoveConnection(
  [in] string UniqueConnectionId
);
```



## Parameters

<dl> <dt>

*UniqueConnectionId* \[in\]
</dt> <dd>

The unique ID associated with the connection to be removed.

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

[**MSIscsiInitiator\_SessionClass**](msiscsiinitiator-sessionclass.md)
</dt> </dl>

 

 




