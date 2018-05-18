---
title: IVMFloppyDriveCollection \_NewEnum property
description: Retrieves an enumerator for the collection.
ms.assetid: '06de9560-cba9-4c64-907e-83e77781cafc'
keywords: ["_NewEnum property Virtual PC", "_NewEnum property Virtual PC , IVMFloppyDriveCollection interface", "IVMFloppyDriveCollection interface Virtual PC , _NewEnum property"]
topic_type:
- apiref
api_name:
- IVMFloppyDriveCollection._NewEnum
- IVMFloppyDriveCollection.get__NewEnum
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
---

# IVMFloppyDriveCollection::\_NewEnum property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](https://msdn.microsoft.com/library/windows/desktop/hh850319).\]

Retrieves an enumerator for the collection.

This property is read-only.

## Syntax


```C++
HRESULT get__NewEnum(
  [out, retval] IUnknown **enumerator
);
```



## Property value

The [IEnumVARIANT](http://go.microsoft.com/fwlink/p/?linkid=120799) enumerator.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>    |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error occurred.<br/> |



## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMFloppyDriveCollection is defined as 8ba70a25-f698-4ee5-85ce-3cc93a925516<br/>   |



## See also

<dl> <dt>

[**IVMFloppyDriveCollection**](ivmfloppydrivecollection.md)
</dt> </dl>

 

 





