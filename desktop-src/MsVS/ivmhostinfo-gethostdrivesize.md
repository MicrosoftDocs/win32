---
title: IVMHostInfo GetHostDriveSize method
description: The GetHostDriveSize method returns the size of a host drive in Megabytes.
ms.assetid: 101251db-3df7-4266-a83c-33d91316527b
keywords:
- GetHostDriveSize method Virtual Server
- GetHostDriveSize method Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , GetHostDriveSize method
- GetHostDriveSize method Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , GetHostDriveSize method
topic_type:
- apiref
api_name:
- IVMHostInfo.GetHostDriveSize
- VMHostInfo.GetHostDriveSize
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

# IVMHostInfo::GetHostDriveSize method

The **GetHostDriveSize** method returns the size of a host drive in Megabytes.

## Syntax


```C++
HRESULT GetHostDriveSize(
  [in]  BSTR hostDriveIdentifier,
  [out] long *hostDriveSizeInMB
);
```



## Parameters

<dl> <dt>

*hostDriveIdentifier* \[in\]
</dt> <dd>

Specifies the desired host drive to check. The [**HostDrives**](ivmhostinfo-hostdrives.md) property is used to retrieve a list of valid drive identifier strings.

</dd> <dt>

*hostDriveSizeInMB* \[out\]
</dt> <dd>

Retrieves the size in megabytes of the host drive specified by the *hostDriveIdentifier* parameter.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                       | Description                                                                                       |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                                                          |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *hostDriveIdentifier* or *hostDriveSizeInMB* parameter is **NULL**.<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *hostDriveIdentifier* parameter is not valid or does not reference a usable drive.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error occurred.<br/>                                                          |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 





