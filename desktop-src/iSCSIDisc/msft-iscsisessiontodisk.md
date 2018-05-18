---
Description: 'Association between iSCSISession and MSFT\_Disk.'
ms.assetid: '6D9024FE-49FE-4B11-A024-2C9FBBFA34BC'
title: 'MSFT\_iSCSISessionToDisk class'
---

# MSFT\_iSCSISessionToDisk class

Association between [**iSCSISession**](msft-iscsisession.md) and [**MSFT\_Disk**](stormgmt.msft_disk).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSISessionToDisk
{
  MSFT_iSCSISession REF iSCSISession;
  MSFT_Disk         REF Disk;
};
```

## Members

The **MSFT\_iSCSISessionToDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_iSCSISessionToDisk** class has these properties.

<dl> <dt>

[**Disk**](stormgmt.msft_disk)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_Disk**](stormgmt.msft_disk)**
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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Iscsiwmiv2.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Disk**](stormgmt.msft_disk)
</dt> <dt>

[**MSFT\_iSCSISession**](msft-iscsisession.md)
</dt> </dl>

 

 




