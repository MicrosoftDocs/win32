---
Description: Association between InitiatorPort and iSCSITarget.
ms.assetid: 966D2C5B-1AC6-4AD7-83F2-FB0854CBB5EB
title: MSFT\_InitiatorPortToiSCSITarget class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_InitiatorPortToiSCSITarget class

Association between [**InitiatorPort**](https://msdn.microsoft.com/library/windows/desktop/hh830507) and [**iSCSITarget**](msft-iscsitarget.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_InitiatorPortToiSCSITarget
{
  MSFT_InitiatorPort REF InitiatorPort;
  MSFT_iSCSITarget   REF iSCSITarget;
};
```

## Members

The **MSFT\_InitiatorPortToiSCSITarget** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_InitiatorPortToiSCSITarget** class has these properties.

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

[**iSCSITarget**](msft-iscsitarget.md)
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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Iscsiwmiv2.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_InitiatorPort**](https://msdn.microsoft.com/library/windows/desktop/hh830507)
</dt> <dt>

[**MSFT\_iSCSITarget**](msft-iscsitarget.md)
</dt> </dl>

 

 




