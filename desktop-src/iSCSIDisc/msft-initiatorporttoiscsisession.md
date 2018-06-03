---
Description: Association between InitiatorPort and iSCSISession.
ms.assetid: ECE175F3-CFD8-41C1-93BB-83B5E7639EE5
title: MSFT\_InitiatorPortToiSCSISession class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_InitiatorPortToiSCSISession class

Association between [**InitiatorPort**](https://msdn.microsoft.com/library/windows/desktop/hh830507) and [**iSCSISession**](msft-iscsisession.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_InitiatorPortToiSCSISession
{
  MSFT_InitiatorPort REF InitiatorPort;
  MSFT_iSCSISession  REF iSCSISession;
};
```

## Members

The **MSFT\_InitiatorPortToiSCSISession** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_InitiatorPortToiSCSISession** class has these properties.

<dl> <dt>

[**InitiatorPort**](https://msdn.microsoft.com/library/windows/desktop/hh830507)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_InitiatorPort**](https://msdn.microsoft.com/library/windows/desktop/hh830507)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

[**iSCSISession**](msft-iscsisession.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_iSCSISession**](msft-iscsisession.md)**
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

[**MSFT\_InitiatorPort**](https://msdn.microsoft.com/library/windows/desktop/hh830507)
</dt> <dt>

[**MSFT\_iSCSISession**](msft-iscsisession.md)
</dt> </dl>

 

 




