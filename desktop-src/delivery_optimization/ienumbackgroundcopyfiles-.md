---
title: IEnumBackgroundCopyFiles interface (Deliveryoptimization.h)
description: Use the IEnumBackgroundCopyFiles interface to enumerate the files that a job contains. To get an IEnumBackgroundCopyFiles interface pointer, call the IBackgroundCopyJob EnumFiles method.
ms.assetid: 539973BA-2756-4163-9D8B-4B7C0A708A8D
keywords:
- IEnumBackgroundCopyFiles interface
- IEnumBackgroundCopyFiles interface, described
topic_type:
- apiref
api_name:
- IEnumBackgroundCopyFiles
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IEnumBackgroundCopyFiles interface

Use the **IEnumBackgroundCopyFiles** interface to enumerate the files that a job contains. To get an **IEnumBackgroundCopyFiles** interface pointer, call the [**IBackgroundCopyJob::EnumFiles**](ibackgroundcopyjob-enumfiles.md) method.

## Members

The **IEnumBackgroundCopyFiles** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IEnumBackgroundCopyFiles** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumBackgroundCopyFiles** interface has these methods.



| Method                                                | Description                                                                   |
|:------------------------------------------------------|:------------------------------------------------------------------------------|
| [**GetCount**](ienumbackgroundcopyfiles-getcount.md) | Retrieves the number of items in the enumeration.<br/>                  |
| [**Next**](ienumbackgroundcopyfiles-next.md)         | Retrieves a specified number of items in the enumeration sequence.<br/> |
| [**Reset**](ienumbackgroundcopyfiles-reset.md)       | Resets the enumeration sequence to the beginning.<br/>                  |
| [**Skip**](ienumbackgroundcopyfiles-skip.md)         | Skips a specified number of items in the enumeration sequence.<br/>     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IEnumBackgroundCopyFiles is defined as CA51E165-C365-424C-8D41-24AAA4FF3C40<br/>         |



## See also

<dl> <dt>

[**IBackgroundCopyJob::EnumFiles**](ibackgroundcopyjob-enumfiles.md)
</dt> </dl>

 

