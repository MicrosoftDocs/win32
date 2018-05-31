---
title: IVMVirtualNetworkCollection \_NewEnum property
description: The \_NewEnum property contains an IEnumVariant enumerator for the collection.
ms.assetid: 4262bf63-4674-4bcc-bc7d-04e1deccd3ca
keywords:
- _NewEnum property Virtual Server
- _NewEnum property Virtual Server , IVMVirtualNetworkCollection interface
- IVMVirtualNetworkCollection interface Virtual Server , _NewEnum property
topic_type:
- apiref
api_name:
- IVMVirtualNetworkCollection._NewEnum
- IVMVirtualNetworkCollection.get__NewEnum
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualNetworkCollection::\_NewEnum property

The **\_NewEnum** property contains an **IEnumVariant** enumerator for the collection.

This property is read-only.

## Syntax


```C++
HRESULT get__NewEnum(
  [out] IUnknown **enumerator
);
```



## Property value

The **IEnumVariant** enumerator for this collection.

## Error codes



| Name                                                                                          | Meaning                                            |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>           |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *enumerator* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>       |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualNetworkCollection**](ivmvirtualnetworkcollection.md)
</dt> </dl>

 

 





