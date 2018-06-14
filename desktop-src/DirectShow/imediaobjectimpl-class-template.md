---
Description: The IMediaObjectImpl class template provides a base implementation for the IMediaObject interface. For more information on using this template, see Using the DMO Class Template.
ms.assetid: 81d45b8d-8373-4e42-b768-f6126feb935d
title: IMediaObjectImpl Class Template
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMediaObjectImpl Class Template

The `IMediaObjectImpl` class template provides a base implementation for the [**IMediaObject**](/windows/desktop/api/Mediaobj/nn-mediaobj-imediaobject) interface. For more information on using this template, see [Using the DMO Class Template](using-the-dmo-class-template.md).

This `IMediaObjectImpl` template exposes the following members.



| Nested Class                              | Description                                  |
|-------------------------------------------|----------------------------------------------|
| [**LockIt**](imediaobjectimpl-lockit.md) | Helper class that locks and unlocks the DMO. |



 



| Method                                                                      | Description                                                          |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**CheckTypesSet**](/windows/desktop/api/Dmoimpl/nf-dmoimpl-imediaobjectimpl-checktypesset)                     | Determines whether all of the non-optional streams have media types. |
| [**InputType**](/windows/desktop/api/Dmoimpl/nf-dmoimpl-imediaobjectimpl-inputtype)                             | Retrieves the current media type for a specified input stream.       |
| [**InputTypeSet**](/windows/desktop/api/Dmoimpl/nf-dmoimpl-imediaobjectimpl-inputtypeset)                       | Queries whether the media type was set on an input stream.           |
| [**InternalAcceptingInput**](https://msdn.microsoft.com/en-us/library/Dd406931(v=VS.85).aspx)   | Queries whether an input stream can accept more input.               |
| [**InternalCheckInputType**](https://msdn.microsoft.com/en-us/library/Dd406932(v=VS.85).aspx)   | Queries whether an input stream can accept a given media type.       |
| [**InternalCheckOutputType**](https://msdn.microsoft.com/en-us/library/Dd406933(v=VS.85).aspx) | Queries whether an output stream can accept a given media type.      |
| [**Lock**](https://msdn.microsoft.com/en-us/library/Dd406934(v=VS.85).aspx)                                       | Locks the DMO                                                        |
| [**OutputType**](/windows/desktop/api/Dmoimpl/nf-dmoimpl-imediaobjectimpl-outputtype)                           | Retrieves the current media type for a specified output stream.      |
| [**OutputTypeSet**](/windows/desktop/api/Dmoimpl/nf-dmoimpl-imediaobjectimpl-outputtypeset)                     | Queries whether the media type was set on an output stream.          |
| [**Unlock**](https://msdn.microsoft.com/en-us/library/Dd406938(v=VS.85).aspx)                                   | Unlocks the DMO                                                      |



 

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

 

 




