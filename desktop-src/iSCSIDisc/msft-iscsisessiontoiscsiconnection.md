---
Description: 'Association between iSCSISession and iSCSIConnection.'
ms.assetid: '4C4C2035-D8D0-46D0-B9C2-A3189871A525'
title: 'MSFT\_iSCSISessionToiSCSIConnection class'
---

# MSFT\_iSCSISessionToiSCSIConnection class

Association between [**iSCSISession**](msft-iscsisession.md) and [**iSCSIConnection**](msft-iscsiconnection.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSISessionToiSCSIConnection
{
  MSFT_iSCSISession    REF iSCSISession;
  MSFT_iSCSIConnection REF iSCSIConnection;
};
```

## Members

The **MSFT\_iSCSISessionToiSCSIConnection** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_iSCSISessionToiSCSIConnection** class has these properties.

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

[**MSFT\_iSCSIConnection**](msft-iscsiconnection.md)
</dt> <dt>

[**MSFT\_iSCSISession**](msft-iscsisession.md)
</dt> </dl>

 

 




