---
Description: Association between iSCSITarget and iSCSISession.
ms.assetid: 5B716F63-0E6B-430E-8DD6-E50AB1C4AB9F
title: MSFT\_iSCSITargetToiSCSISession class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_iSCSITargetToiSCSISession class

Association between [**iSCSITarget**](msft-iscsitarget.md) and [**iSCSISession**](msft-iscsisession.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSITargetToiSCSISession
{
  MSFT_iSCSITarget  REF iSCSITarget;
  MSFT_iSCSISession REF iSCSISession;
};
```

## Members

The **MSFT\_iSCSITargetToiSCSISession** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_iSCSITargetToiSCSISession** class has these properties.

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

[**MSFT\_iSCSISession**](msft-iscsisession.md)
</dt> <dt>

[**MSFT\_iSCSITarget**](msft-iscsitarget.md)
</dt> </dl>

 

 




