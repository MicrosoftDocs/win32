---
title: ProtectedFileStream class
description: Used to access a protected file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: T:Microsoft.RightsManagement.ProtectedFileStream
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ProtectedFileStream class
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ProtectedFileStream
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ProtectedFileStream class

Used to access a protected file.

## Syntax


```C++
public ref class ProtectedFileStream sealed : IRandomAccessStream
```



## Members

The **ProtectedFileStream** class inherits from [**IRandomAccessStream**](https://msdn.microsoft.com/library/windows/apps/br241731). **ProtectedFileStream** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ProtectedFileStream** class has these methods. It also inherits methods from the **Object** class.



| Method                                                             | Description                                                                            |
|:-------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| [**AcquireAsync**](protectedfilestream-acquireasync.md)           | Creates a ProtectedFileStream object from a backing stream.                            |
| [**CloneStream**](protectedfilestream-clonestream.md)             | Creates a new instance of ProtectedFileStream over the protected file.                 |
| [**CreateAsync**](protectedfilestream-createasync.md)             | Creates a ProtectedFileStream from a UserPolicy object and a backing stream.           |
| [**FlushAsync**](protectedfilestream-flushasync.md)               | Flushes the data asynchronously to the protected file.                                 |
| [**GetInputStreamAt**](protectedfilestream-getinputstreamat.md)   | Returns an input stream at the specified position in the protected file.               |
| [**GetOutputStreamAt**](protectedfilestream-getoutputstreamat.md) | Returns an output stream at the specified location in the protected file.              |
| [**ReadAsync**](protectedfilestream-readasync.md)                 | Returns an asynchronous byte reader object.                                            |
| [**Seek**](protectedfilestream-seek.md)                           | Sets the current position to the specified number of bytes from the start of the file. |
| [**WriteAsync**](protectedfilestream-writeasync.md)               | Writes data asynchronously to the protected file.                                      |



 

### Properties

The **ProtectedFileStream** class has these properties.



| Property                                                                              | Access type           | Description                                                                                                           |
|:--------------------------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**CanRead**](protectedfilestream-canread.md)<br/>                             | Read-only<br/>  | Gets a value that indicates whether the file can be read from. Implements the IRandomAccessStream.CanRead property.   |
| [**CanWrite**](protectedfilestream-canwrite.md)<br/>                           | Read-only<br/>  | Gets a value that indicates whether the file can be written to. Implements the IRandomAccessStream.CanWrite property. |
| [**OriginalFileExtension**](protectedfilestream-originalfileextension.md)<br/> | Read-only<br/>  | Gets the filename extension of the original (unprotected) file.                                                       |
| [**Policy**](protectedfilestream-policy.md)<br/>                               | Read-only<br/>  | Gets user policy associated with this ProtectedFileStream object.                                                     |
| [**Position**](protectedfilestream-position.md)<br/>                           | Read-only<br/>  | Gets the current file position in bytes.                                                                              |
| [**Size**](protectedfilestream-size.md)<br/>                                   | Read/write<br/> | Gets or sets the size of the protected data in bytes.                                                                 |



 

## Remarks

**ProtectedFileStream** objects are used to open and create protected files and to read and write protected content from and to protected files. The **ProtectedFileStream** class implements the [Windows.Storage.Streams.IRandomAccessStream](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.aspx) interface so that apps can read and write from and to protected files as they would by using standard Windows Runtime streams. When you create a **ProtectedFileStream**, you specify a backing stream, an object of IRandomAccessStream, where the actual protected file is or should be stored.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



## See also

<dl> <dt>

[**IRandomAccessStream**](https://msdn.microsoft.com/library/windows/apps/br241731)
</dt> </dl>

 

 





