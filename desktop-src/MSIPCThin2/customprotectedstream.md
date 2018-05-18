---
title: CustomProtectedStream class
description: Used to access files that use a custom protection format.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'T:Microsoft.RightsManagement.CustomProtection.CustomProtectedStream'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["CustomProtectedFileStream class"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CustomProtectedFileStream
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# CustomProtectedStream class

Used to access files that use a custom protection format.

> \[!Important\]  
> RMS applications that use **CustomProtectedStream** may be incompatible with SharePoint, Exchange, and other RMS applications. For most applications, it is recommended that you use [**ProtectedFileStream**](protectedfilestream.md) instead.

 

## Syntax


```C++
public ref class CustomProtectedFileStream sealed : IRandomAccessStream
```



## Members

The **CustomProtectedFileStream** class inherits from [**IRandomAccessStream**](https://msdn.microsoft.com/library/windows/apps/br241731). **CustomProtectedStream** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CustomProtectedFileStream** class has these methods. It also inherits methods from the **Object** class.



| Method                                                                               | Description                                                                                           |
|:-------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**CloneStream**](customprotectedstream-clonestream.md)                             | Creates a new instance of CustomProtectedStream over the protected content.                           |
| [**CreateAsync**](customprotectedstream-createasync-cpp.md)                         | Creates a CustomProtectedStream object based on the specified protection policy and a backing stream. |
| [**FlushAsync**](customprotectedstream-flushasync.md)                               | Flushes the data asynchronously to the backing file.                                                  |
| [**GetEncryptedContentLength**](customprotectedstream-getencryptedcontentlength.md) | Calculates the length of the encrypted content from the length of the clear content.                  |
| [**GetInputStreamAt**](customprotectedstream-getinputstreamat.md)                   | Returns an input stream at the specified position in the protected file.                              |
| [**GetOutputStreamAt**](customprotectedstream-getoutputstreamat.md)                 | Returns an output stream at the specified location in the protected file.                             |
| [**ReadAsync**](customprotectedstream-readasync.md)                                 | Returns an asynchronous byte reader object.                                                           |
| [**Seek**](customprotectedstream-seek.md)                                           | Sets the current position to the specified number of bytes from the start of the file.                |
| [**WriteAsync**](customprotectedstream-writeasync.md)                               | Writes data asynchronously to the backing file.                                                       |



 

### Properties

The **CustomProtectedFileStream** class has these properties.



| Property                                                      | Access type           | Description                                                                                                         |
|:--------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------|
| [**CanRead**](customprotectedstream-canread.md)<br/>   | Read-only<br/>  | Gets a value that indicates whether the file can be read from. Implements the IRandomAccessStream.CanRead property. |
| [**CanWrite**](customprotectedstream-canwrite.md)<br/> | Read-only<br/>  | Gets a value that indicates whether the file can be written to.                                                     |
| [**Position**](customprotectedstream-position.md)<br/> | Read-only<br/>  | Gets the current file position in bytes.                                                                            |
| [**Size**](customprotectedstream-size.md)<br/>         | Read/write<br/> | Gets or sets the size of the protected data in bytes. Implements the IRandomAccessStream.Size property.             |



 

## Remarks

**CustomProtectedStream** objects are used to open and create files that are protected with a custom format and to read and write protected content from and to such files. The **CustomProtectedStream** class implements the [Windows.Storage.Streams.IRandomAccessStream](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.aspx) interface so that apps can read and write from and to a protected file as they would by using standard Windows Runtime streams. When you create a **CustomProtectedStream**, you specify a backing stream, an object of IRandomAccessStream, where the actual protected content is or should be stored.

Data written to streams created using this class must be 16-byte aligned.

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

 

 





