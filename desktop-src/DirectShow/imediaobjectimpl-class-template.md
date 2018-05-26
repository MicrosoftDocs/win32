---
Description: The IMediaObjectImpl class template provides a base implementation for the IMediaObject interface. For more information on using this template, see Using the DMO Class Template.
ms.assetid: 81d45b8d-8373-4e42-b768-f6126feb935d
title: IMediaObjectImpl Class Template
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMediaObjectImpl Class Template

The `IMediaObjectImpl` class template provides a base implementation for the [**IMediaObject**](/windows/win32/Mediaobj/nn-mediaobj-imediaobject?branch=master) interface. For more information on using this template, see [Using the DMO Class Template](using-the-dmo-class-template.md).

This `IMediaObjectImpl` template exposes the following members.



| Nested Class                              | Description                                  |
|-------------------------------------------|----------------------------------------------|
| [**LockIt**](imediaobjectimpl-lockit.md) | Helper class that locks and unlocks the DMO. |



 



| Method                                                                      | Description                                                          |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**CheckTypesSet**](/windows/win32/Dmoimpl/nf-dmoimpl-imediaobjectimpl-checktypesset?branch=master)                     | Determines whether all of the non-optional streams have media types. |
| [**InputType**](/windows/win32/Dmoimpl/nf-dmoimpl-imediaobjectimpl-inputtype?branch=master)                             | Retrieves the current media type for a specified input stream.       |
| [**InputTypeSet**](/windows/win32/Dmoimpl/nf-dmoimpl-imediaobjectimpl-inputtypeset?branch=master)                       | Queries whether the media type was set on an input stream.           |
| [**InternalAcceptingInput**](/windows/win32/Dmoimpl/?branch=master)   | Queries whether an input stream can accept more input.               |
| [**InternalCheckInputType**](/windows/win32/Dmoimpl/?branch=master)   | Queries whether an input stream can accept a given media type.       |
| [**InternalCheckOutputType**](/windows/win32/Dmoimpl/?branch=master) | Queries whether an output stream can accept a given media type.      |
| [**Lock**](/windows/win32/Dmoimpl/?branch=master)                                       | Locks the DMO                                                        |
| [**OutputType**](/windows/win32/Dmoimpl/nf-dmoimpl-imediaobjectimpl-outputtype?branch=master)                           | Retrieves the current media type for a specified output stream.      |
| [**OutputTypeSet**](/windows/win32/Dmoimpl/nf-dmoimpl-imediaobjectimpl-outputtypeset?branch=master)                     | Queries whether the media type was set on an output stream.          |
| [**Unlock**](/windows/win32/Dmoimpl/?branch=master)                                   | Unlocks the DMO                                                      |



 

## Requirements



|                    |                                                                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dmoimpl.h</dt> </dl>                                                                     |
| Library<br/> | <dl> <dt>Dmoguids.lib; </dt> <dt>Msdmo.lib</dt> </dl> |



## See also

<dl> <dt>

[DMO Reference](dmo-reference.md)
</dt> <dt>

[Using the DMO Class Template](using-the-dmo-class-template.md)
</dt> </dl>

 

 




