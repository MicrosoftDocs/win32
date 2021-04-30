---
title: IBackgroundCopyFile2 interface (Deliveryoptimization.h)
description: Use the IBackgroundCopyFile2 interface to specify a new remote name for the file and retrieve the list of ranges to download.
ms.assetid: 28233310-9F2A-4567-B0B1-B549F862F3C8
keywords:
- IBackgroundCopyFile2 interface
- IBackgroundCopyFile2 interface, described
topic_type:
- apiref
api_name:
- IBackgroundCopyFile2
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyFile2 interface

Use the **IBackgroundCopyFile2** interface to specify a new remote name for the file and retrieve the list of ranges to download.

The **IBackgroundCopyFile2** interface inherits from the [**IBackgroundCopyFile**](ibackgroundcopyfile.md) interface.

To get an **IBackgroundCopyFile2** interface pointer, call the **IBackgroundCopyFile::QueryInterface** method using __uuidof(IBackgroundCopyFile2) for the interface identifier. Use the **IBackgroundCopyFile2** interface pointer to call both the [**IBackgroundCopyFile**](ibackgroundcopyfile.md) and **IBackgroundCopyFile2** methods.

## Members

The **IBackgroundCopyFile2** interface inherits from [**IBackgroundCopyFile**](ibackgroundcopyfile.md). **IBackgroundCopyFile2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBackgroundCopyFile2** interface has these methods.



| Method                                                             | Description                                                                      |
|:-------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**GetFileRanges**](ibackgroundcopyfile2-getfileranges-method.md) | Retrieves the array of ranges that you want to download from the URL.<br/> |
| [**SetRemoteName**](ibackgroundcopyfile2-setremotename-method.md) | Changes the remote name to a new URL.<br/>                                 |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyFile2 is defined as 83E81B93-0873-474D-8A8C-F2018B1A939C<br/>             |



## See also

<dl> <dt>

[**IBackgroundCopyFile**](ibackgroundcopyfile.md)
</dt> </dl>

 

 





