---
Description: Association between iSCSITarget and iSCSITargetPortal.
ms.assetid: 1066A33B-8D4B-4D8A-973B-BDAA14B441CF
title: MSFT\_iSCSITargetToiSCSITargetPortal class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_iSCSITargetToiSCSITargetPortal class

Association between [**iSCSITarget**](msft-iscsitarget.md) and [**iSCSITargetPortal**](msft-iscsitargetportal.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSITargetToiSCSITargetPortal
{
  MSFT_iSCSITarget       REF iSCSITarget;
  MSFT_iSCSITargetPortal REF iSCSITargetPortal;
};
```

## Members

The **MSFT\_iSCSITargetToiSCSITargetPortal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_iSCSITargetToiSCSITargetPortal** class has these properties.

<dl> <dt>

**iSCSITarget**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_iSCSITarget**](msft-iscsitarget.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**iSCSITargetPortal**
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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Iscsiwmiv2.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_iSCSITarget**](msft-iscsitarget.md)
</dt> <dt>

[**MSFT\_iSCSITargetPortal**](msft-iscsitargetportal.md)
</dt> </dl>

 

 




