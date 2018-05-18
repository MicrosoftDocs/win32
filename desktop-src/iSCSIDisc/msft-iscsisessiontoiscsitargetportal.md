---
Description: 'Association between iSCSISession and iSCSITargetPortal.'
ms.assetid: '61D081D5-16CE-4523-9F4D-587D556FC679'
title: 'MSFT\_iSCSISessionToiSCSITargetPortal class'
---

# MSFT\_iSCSISessionToiSCSITargetPortal class

Association between [**iSCSISession**](msft-iscsisession.md) and [**iSCSITargetPortal**](msft-iscsitargetportal.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSISessionToiSCSITargetPortal
{
  MSFT_iSCSISession      REF iSCSISession;
  MSFT_iSCSITargetPortal REF iSCSITargetPortal;
};
```

## Members

The **MSFT\_iSCSISessionToiSCSITargetPortal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_iSCSISessionToiSCSITargetPortal** class has these properties.

<dl> <dt>

[**iSCSISession**](msft-iscsisession.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_iSCSISession**](msft-iscsisession.md)**
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

[**MSFT\_iSCSISession**](msft-iscsisession.md)
</dt> <dt>

[**MSFT\_iSCSITargetPortal**](msft-iscsitargetportal.md)
</dt> </dl>

 

 




