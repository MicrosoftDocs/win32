---
Description: Association between iSCSIConnection and MSFT\_Disk.
ms.assetid: 9319361C-9337-473F-96BA-F0167183D914
title: MSFT\_iSCSIConnectionToDisk class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_iSCSIConnectionToDisk class

Association between [**iSCSIConnection**](msft-iscsiconnection.md) and [**MSFT\_Disk**](https://msdn.microsoft.com/library/windows/desktop/hh830493).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSIConnectionToDisk
{
  MSFT_iSCSIConnection REF iSCSIConnection;
  MSFT_Disk            REF Disk;
};
```

## Members

The **MSFT\_iSCSIConnectionToDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_iSCSIConnectionToDisk** class has these properties.

<dl> <dt>

[**Disk**](https://msdn.microsoft.com/library/windows/desktop/hh830493)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_Disk**](https://msdn.microsoft.com/library/windows/desktop/hh830493)**
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

[**MSFT\_Disk**](https://msdn.microsoft.com/library/windows/desktop/hh830493)
</dt> <dt>

[**MSFT\_iSCSIConnection**](msft-iscsiconnection.md)
</dt> </dl>

 

 




