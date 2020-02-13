---
Description: The IMediaObjectImpl class template provides a base implementation for the IMediaObject interface. For more information on using this template, see Using the DMO Class Template.
ms.assetid: 81d45b8d-8373-4e42-b768-f6126feb935d
title: IMediaObjectImpl Class Template (Dmoimpl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMediaObjectImpl Class Template

The `IMediaObjectImpl` class template provides a base implementation for the [**IMediaObject**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-imediaobject) interface. For more information on using this template, see [Using the DMO Class Template](using-the-dmo-class-template.md).

This `IMediaObjectImpl` template exposes the following members.



| Nested Class                              | Description                                  |
|-------------------------------------------|----------------------------------------------|
| [**LockIt**](imediaobjectimpl-lockit.md) | Helper class that locks and unlocks the DMO. |



 



| Method                                                                      | Description                                                          |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**CheckTypesSet**](https://msdn.microsoft.com/library/Dd406927(v=VS.85).aspx)                     | Determines whether all of the non-optional streams have media types. |
| [**InputType**](https://msdn.microsoft.com/library/Dd406929(v=VS.85).aspx)                             | Retrieves the current media type for a specified input stream.       |
| [**InputTypeSet**](https://msdn.microsoft.com/library/Dd406930(v=VS.85).aspx)                       | Queries whether the media type was set on an input stream.           |
| [**InternalAcceptingInput**](https://msdn.microsoft.com/library/Dd406931(v=VS.85).aspx)   | Queries whether an input stream can accept more input.               |
| [**InternalCheckInputType**](https://msdn.microsoft.com/library/Dd406932(v=VS.85).aspx)   | Queries whether an input stream can accept a given media type.       |
| [**InternalCheckOutputType**](https://msdn.microsoft.com/library/Dd406933(v=VS.85).aspx) | Queries whether an output stream can accept a given media type.      |
| [**Lock**](https://msdn.microsoft.com/library/Dd406934(v=VS.85).aspx)                                       | Locks the DMO                                                        |
| [**OutputType**](https://msdn.microsoft.com/library/Dd406936(v=VS.85).aspx)                           | Retrieves the current media type for a specified output stream.      |
| [**OutputTypeSet**](https://msdn.microsoft.com/library/Dd406937(v=VS.85).aspx)                     | Queries whether the media type was set on an output stream.          |
| [**Unlock**](https://msdn.microsoft.com/library/Dd406938(v=VS.85).aspx)                                   | Unlocks the DMO                                                      |



 

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

 

 




