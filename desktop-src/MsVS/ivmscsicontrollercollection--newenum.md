---
title: IVMSCSIControllerCollection \_NewEnum property
description: The \_NewEnum property contains an IEnumVariant enumerator for the collection.
ms.assetid: 'afe1953a-5000-402a-bcbe-5d43eb8ac31b'
keywords: ["_NewEnum property Virtual Server", "_NewEnum property Virtual Server , IVMSCSIControllerCollection interface", "IVMSCSIControllerCollection interface Virtual Server , _NewEnum property"]
topic_type:
- apiref
api_name:
- IVMSCSIControllerCollection._NewEnum
- IVMSCSIControllerCollection.get__NewEnum
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMSCSIControllerCollection::\_NewEnum property

The **\_NewEnum** property contains an **IEnumVariant** enumerator for the collection.

This property is read-only.

## Syntax


```C++
HRESULT get__NewEnum(
  [out] IUnknown **enumerator
);
```



## Property value

The **IEnumVariant** enumerator for this collection.

## Error codes



| Name                                                                                          | Meaning                                          |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>         |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter is **NULL** or invalid.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>         |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSCSIControllerCollection**](ivmscsicontrollercollection.md)
</dt> </dl>

 

 





