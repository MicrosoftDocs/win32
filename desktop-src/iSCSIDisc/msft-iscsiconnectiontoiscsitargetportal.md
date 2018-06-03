---
Description: Association between iSCSIConnection and iSCSITargetPortal.
ms.assetid: 53A00446-AE06-4567-91B5-FA6FC768C6FA
title: MSFT\_iSCSIConnectionToiSCSITargetPortal class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_iSCSIConnectionToiSCSITargetPortal class

Association between [**iSCSIConnection**](msft-iscsiconnection.md) and [**iSCSITargetPortal**](msft-iscsitargetportal.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSIConnectionToiSCSITargetPortal
{
  MSFT_iSCSIConnection   REF iSCSIConnection;
  MSFT_iSCSITargetPortal REF iSCSITargetPortal;
};
```

## Members

The **MSFT\_iSCSIConnectionToiSCSITargetPortal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_iSCSIConnectionToiSCSITargetPortal** class has these properties.

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

[**iSCSITargetPortal**](msft-iscsitargetportal.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_iSCSITargetPortal**](msft-iscsitargetportal.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Iscsiwmiv2.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_iSCSIConnection**](msft-iscsiconnection.md)
</dt> <dt>

[**MSFT\_iSCSITargetPortal**](msft-iscsitargetportal.md)
</dt> </dl>

 

 




