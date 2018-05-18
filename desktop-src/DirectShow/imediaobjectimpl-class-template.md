---
Description: 'The IMediaObjectImpl class template provides a base implementation for the IMediaObject interface. For more information on using this template, see Using the DMO Class Template.'
ms.assetid: '81d45b8d-8373-4e42-b768-f6126feb935d'
title: IMediaObjectImpl Class Template
---

# IMediaObjectImpl Class Template

The `IMediaObjectImpl` class template provides a base implementation for the [**IMediaObject**](imediaobject.md) interface. For more information on using this template, see [Using the DMO Class Template](using-the-dmo-class-template.md).

This `IMediaObjectImpl` template exposes the following members.



| Nested Class                              | Description                                  |
|-------------------------------------------|----------------------------------------------|
| [**LockIt**](imediaobjectimpl-lockit.md) | Helper class that locks and unlocks the DMO. |



 



| Method                                                                      | Description                                                          |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**CheckTypesSet**](imediaobjectimpl-checktypesset.md)                     | Determines whether all of the non-optional streams have media types. |
| [**InputType**](imediaobjectimpl-inputtype.md)                             | Retrieves the current media type for a specified input stream.       |
| [**InputTypeSet**](imediaobjectimpl-inputtypeset.md)                       | Queries whether the media type was set on an input stream.           |
| [**InternalAcceptingInput**](imediaobjectimpl-internalacceptinginput.md)   | Queries whether an input stream can accept more input.               |
| [**InternalCheckInputType**](imediaobjectimpl-internalcheckinputtype.md)   | Queries whether an input stream can accept a given media type.       |
| [**InternalCheckOutputType**](imediaobjectimpl-internalcheckoutputtype.md) | Queries whether an output stream can accept a given media type.      |
| [**Lock**](imediaobjectimpl-lock.md)                                       | Locks the DMO                                                        |
| [**OutputType**](imediaobjectimpl-outputtype.md)                           | Retrieves the current media type for a specified output stream.      |
| [**OutputTypeSet**](imediaobjectimpl-outputtypeset.md)                     | Queries whether the media type was set on an output stream.          |
| [**Unlock**](imediaobjectimpl-unlock.md)                                   | Unlocks the DMO                                                      |



 

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

 

 




