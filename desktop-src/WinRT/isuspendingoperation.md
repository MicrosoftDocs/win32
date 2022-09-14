---
description: Provides information about an app suspending operation.
ms.assetid: B380AEA2-6486-46CC-AD0A-CF25C144DC01
title: ISuspendingOperation interface (Windows.ApplicationModel.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ISuspendingOperation
api_type:
- COM
api_location:
- Windows.ApplicationModel.h
---

# ISuspendingOperation interface

Provides information about an app suspending operation.

## Members

The **ISuspendingOperation** interface inherits from [**IInspectable**](/windows/win32/api/inspectable/nn-inspectable-iinspectable). **ISuspendingOperation** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ISuspendingOperation** interface has these methods.



| Method                                                  | Description                                                       |
|:--------------------------------------------------------|:------------------------------------------------------------------|
| [**GetDeferral**](isuspendingoperation-getdeferral.md) | Requests that the app suspending operation be delayed.<br/> |



 

### Properties

The **ISuspendingOperation** interface has these properties.



| Property                                                     | Access type           | Description                                                                             |
|:-------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------|
| [**Deadline**](isuspendingoperation-deadline.md)<br/> | Read/write<br/> | Gets the time remaining before a delayed app suspending operation continues.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Header<br/>                   | <dl> <dt>Windows.ApplicationModel.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.ApplicationModel.idl</dt> </dl> |



## See also

<dl> <dt>

[**IInspectable**](/windows/win32/api/inspectable/nn-inspectable-iinspectable)
</dt> <dt>

[**ISuspendingDeferral**](isuspendingdeferral.md)
</dt> <dt>

[**ISuspendingEventArgs**](isuspendingeventargs.md)
</dt> </dl>

 

 
