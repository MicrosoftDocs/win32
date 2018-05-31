---
title: IVMVirtualServer VMRCCreateEncryptionCertificateRequest method
description: The VMRCCreateEncryptionCertificateRequest method creates a new security certificate request.
ms.assetid: 81a2bea6-a869-4e78-a4c3-3e4980947305
keywords:
- VMRCCreateEncryptionCertificateRequest method Virtual Server
- VMRCCreateEncryptionCertificateRequest method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VMRCCreateEncryptionCertificateRequest method
topic_type:
- apiref
api_name:
- IVMVirtualServer.VMRCCreateEncryptionCertificateRequest
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

# IVMVirtualServer::VMRCCreateEncryptionCertificateRequest method

The **VMRCCreateEncryptionCertificateRequest** method creates a new security certificate request.

## Syntax


```C++
HRESULT VMRCCreateEncryptionCertificateRequest(
  [in]  BSTR distinguishedName,
  [in]  long keyLength,
  [out] BSTR *request
);
```



## Parameters

<dl> <dt>

*distinguishedName* \[in\]
</dt> <dd>

The distinguished name of the host computer.

</dd> <dt>

*keyLength* \[in\]
</dt> <dd>

The key length in bits.

</dd> <dt>

*request* \[out\]
</dt> <dd>

The Base-64 encoded security certificate request.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                        | Description                                               |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>              | The operation was successful.<br/>                  |
| <dl> <dt>**E\_POINTER** </dt> </dl>         | *distinguishedName* or *request* is **NULL**.<br/>  |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>      | *distinguishedName* or *keyLength* is invalid.<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error occurred.<br/>                  |



 

## Remarks

This method creates a request for a new security certificate.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





