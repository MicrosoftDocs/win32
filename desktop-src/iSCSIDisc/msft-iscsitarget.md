---
Description: Represents an iSCSI target.
ms.assetid: CCB86833-2F8C-41CE-B5F9-A14F79DEE3D3
title: MSFT\_iSCSITarget class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_iSCSITarget class

Represents an iSCSI target.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSITarget
{
  string  NodeAddress;
  Boolean IsConnected;
};
```

## Members

The **MSFT\_iSCSITarget** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_iSCSITarget** class has these methods.



| Method                                            | Description                                                                                  |
|:--------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**Connect**](msft-iscsitarget-connect.md)       | Creates a session between an iSCSI initiator and an iSCSI target.<br/>                 |
| [**Disconnect**](msft-iscsitarget-disconnect.md) | Disconnects the specified session between an iSCSI initiator and an iSCSI target.<br/> |
| [**Update**](msft-iscsitarget-update.md)         | Refreshes the information about connected iSCSI targets.<br/>                          |



 

### Properties

The **MSFT\_iSCSITarget** class has these properties.

<dl> <dt>

**IsConnected**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, there is an active connection to the target.

</dd> <dt>

**NodeAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The iSCSI qualified name (IQN) of the target.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Iscsiwmiv2.mof</dt> </dl> |



 

 




