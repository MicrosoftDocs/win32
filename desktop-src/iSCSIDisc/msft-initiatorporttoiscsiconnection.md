---
Description: Association between InitiatorPort and iSCSIConnection.
ms.assetid: 084C1214-65CD-47AC-8FC4-05AFD9CF0389
title: MSFT\_InitiatorPortToiSCSIConnection class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_InitiatorPortToiSCSIConnection class

Association between [**InitiatorPort**](https://msdn.microsoft.com/library/windows/desktop/hh830507) and [**iSCSIConnection**](msft-iscsiconnection.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_InitiatorPortToiSCSIConnection
{
  MSFT_InitiatorPort   REF InitiatorPort;
  MSFT_iSCSIConnection REF iSCSIConnection;
};
```

## Members

The **MSFT\_InitiatorPortToiSCSIConnection** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_InitiatorPortToiSCSIConnection** class has these properties.

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

[**iSCSIConnection**](msft-iscsiconnection.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_iSCSIConnection**](msft-iscsiconnection.md)**
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

[**MSFT\_iSCSIConnection**](msft-iscsiconnection.md)
</dt> </dl>

 

 




