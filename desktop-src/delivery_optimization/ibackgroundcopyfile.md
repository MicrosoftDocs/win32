---
title: IBackgroundCopyFile interface (Deliveryoptimization.h)
description: IBackgroundCopyFile contains information about a file that is part of a job. For example, you can use IBackgroundCopyFile methods to retrieve the local and remote names of the file and transfer progress information.
ms.assetid: 463ED61A-D7C5-4B44-97CF-FDAA138CE9E3
keywords:
- IBackgroundCopyFile interface
- IBackgroundCopyFile interface, described
topic_type:
- apiref
api_name:
- IBackgroundCopyFile
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyFile interface

**IBackgroundCopyFile** contains information about a file that is part of a job. For example, you can use **IBackgroundCopyFile** methods to retrieve the local and remote names of the file and transfer progress information.

To get an **IBackgroundCopyFile** interface pointer, call the [**IBackgroundCopyError::GetFile**](ibackgroundcopyerror-getfile-method.md) method or the [**IEnumBackgroundCopyFiles::Next**](ienumbackgroundcopyfiles-next.md) method.

## Members

The **IBackgroundCopyFile** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IBackgroundCopyFile** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBackgroundCopyFile** interface has these methods.



| Method                                                            | Description                                             |
|:------------------------------------------------------------------|:--------------------------------------------------------|
| [**GetLocalName**](ibackgroundcopyfile-getlocalname-method.md)   | Retrieves the local name of the file.<br/>        |
| [**GetProgress**](ibackgroundcopyfile-getprogress-method.md)     | Retrieves the progress of the file transfer.<br/> |
| [**GetRemoteName**](ibackgroundcopyfile-getremotename-method.md) | Retrieves the remote name of the file.<br/>       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyFile is defined as 01B7BD23-FB88-4A77-8490-5891D3E4653A<br/>              |



## See also

<dl> <dt>

[**IBackgroundCopyError**](ibackgroundcopyerror.md)
</dt> <dt>

[**IBackgroundCopyFile2**](ibackgroundcopyfile2.md)
</dt> <dt>

[**IBackgroundCopyJob**](ibackgroundcopyjob-.md)
</dt> <dt>

[**IEnumBackgroundCopyFiles**](ienumbackgroundcopyfiles-.md)
</dt> </dl>

 

