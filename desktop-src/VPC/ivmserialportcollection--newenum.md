---
title: IVMSerialPortCollection _NewEnum property (VPCCOMInterfaces.h)
description: Retrieves an enumerator for the collection. | IVMSerialPortCollection _NewEnum property (VPCCOMInterfaces.h)
ms.assetid: 4bf7bbde-d97f-424e-afa0-ff0e334740b5
keywords:
- _NewEnum property Virtual PC
- _NewEnum property Virtual PC , IVMSerialPortCollection interface
- IVMSerialPortCollection interface Virtual PC , _NewEnum property
topic_type:
- apiref
api_name:
- IVMSerialPortCollection._NewEnum
- IVMSerialPortCollection.get__NewEnum
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMSerialPortCollection::\_NewEnum property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves an enumerator for the collection.

This property is read-only.

## Syntax


```C++
HRESULT get__NewEnum(
  [out, retval] IUnknown **enumerator
);
```



## Property value

The [IEnumVARIANT](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) enumerator.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is NULL.<br/>        |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error occurred.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMSerialPortCollection is defined as dd3c6175-1f04-4341-9f85-104074880289<br/>    |



## See also

<dl> <dt>

[**IVMSerialPortCollection**](ivmserialportcollection.md)
</dt> </dl>

 

