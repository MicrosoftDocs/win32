---
Description: Association between iSCSITarget and iSCSIConnection.
ms.assetid: DED9BDC6-CA89-491C-BD31-8BDDDD7C7D44
title: MSFT\_iSCSITargetToiSCSIConnection class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_iSCSITargetToiSCSIConnection class

Association between [**iSCSITarget**](msft-iscsitarget.md) and [**iSCSIConnection**](msft-iscsiconnection.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSITargetToiSCSIConnection
{
  MSFT_iSCSITarget     REF iSCSITarget;
  MSFT_iSCSIConnection REF iSCSIConnection;
};
```

## Members

The **MSFT\_iSCSITargetToiSCSIConnection** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_iSCSITargetToiSCSIConnection** class has these properties.

<dl> <dt>

[**iSCSIConnection**](msft-iscsiconnection.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_iSCSIConnection**](msft-iscsiconnection.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**iSCSITarget**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_iSCSITarget**](msft-iscsitarget.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Iscsiwmiv2.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_iSCSIConnection**](msft-iscsiconnection.md)
</dt> <dt>

[**MSFT\_iSCSITarget**](msft-iscsitarget.md)
</dt> </dl>

 

 




