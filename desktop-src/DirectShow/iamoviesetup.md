---
Description: 'Note  This interface has been deprecated.'
ms.assetid: 'b200dbee-bab7-43d7-a204-751592fa2405'
title: IAMovieSetup interface
---

# IAMovieSetup interface

> [!Note]  
> This interface has been deprecated. It is used by two obsolete functions, [**AMovieDllRegisterServer**](amoviedllregisterserver.md) and [**AMovieDllUnregisterServer**](amoviedllunregisterserver.md). These functions are now replaced by [**AMovieDllRegisterServer2**](amoviedllregisterserver2.md), which does not require **IAMovieSetup**. However, **IAMovieSetup** will continue to be supported for backward compatibility with existing applications.

 

## Members

The **IAMovieSetup** interface inherits from the [**IUnknown**](com.iunknown) interface. **IAMovieSetup** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMovieSetup** interface has these methods.



| Method                                        | Description                                      |
|:----------------------------------------------|:-------------------------------------------------|
| [**Register**](iamoviesetup-register.md)     | Adds the filter to the registry.<br/>      |
| [**Unregister**](iamoviesetup-unregister.md) | Removes the filter from the registry.<br/> |



 

## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




