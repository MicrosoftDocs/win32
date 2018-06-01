---
title: IVMRCAuthenticatorCollection \_NewEnum property
description: The \_NewEnum property contains an IEnumVariant enumerator for the collection.
ms.assetid: 4c20bcde-a8d2-484d-9561-b6cee40ba824
keywords:
- _NewEnum property Virtual Server
- _NewEnum property Virtual Server , IVMRCAuthenticatorCollection interface
- IVMRCAuthenticatorCollection interface Virtual Server , _NewEnum property
topic_type:
- apiref
api_name:
- IVMRCAuthenticatorCollection._NewEnum
- IVMRCAuthenticatorCollection.get__NewEnum
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

# IVMRCAuthenticatorCollection::\_NewEnum property

The **\_NewEnum** property contains an [**IEnumVariant**](https://msdn.microsoft.com/windows/desktop/139e3c93-faef-4003-9079-e0e94494db3e) enumerator for the collection.

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
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>           |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMRCAuthenticatorCollection**](ivmrcauthenticatorcollection.md)
</dt> </dl>

 

 





