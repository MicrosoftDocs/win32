---
title: CustomProtectedInputStream.create synchronous method
description: Synchronously creates an InputStream for reading protected content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: A13A186A-DBA0-4C8A-AD9D-EA6446D91108
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CustomProtectedInputStream.create synchronous method
topic_type:
- apiref
api_name:
- CustomProtectedInputStream.create synchronous method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CustomProtectedInputStream.create synchronous method

Synchronously creates an **InputStream** for reading protected content.

Opens the specified serialized policy and creates a protected stream that can be used to decrypt the actual content. For more information, see the *Remarks* section of this topic.

## Signature

``` syntax
public static CustomProtectedInputStream create(
                                       UserPolicy userPolicy,
                                       InputStream inputStream,
                                       long protectedContentLength,
                                       Context applicationContext)
                             throws ProtectionException
```

## Parameters



| Name                                | Datatype                                               | Notes                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *userPolicy*<br/>             | [**UserPolicy**](userpolicy-class-java.md)<br/> | The custom protection policy.<br/>                                                                                                                                                                                                                                                                                                                |
| *inputStream*<br/>            | **InputStream**<br/>                             | The input stream with the protected content.<br/> The next bytes of available data in *inputStream* (i.e., those returned via the next call to inputStream.Read()) should contain the beginning of the stream's protected content. *inputStream* should have *protectedContentLength* bytes of contiguous protected content available.<br/> |
| *protectedContentLength*<br/> | **long**<br/>                                    | The underlying length of the protected data contained within the stream.<br/>                                                                                                                                                                                                                                                                     |
| *applicationContext*<br/>     | **Context**<br/>                                 |                                                                                                                                                                                                                                                                                                                                                         |



 

## Returns

[**CustomProtectedInputStream**](customprotectedinputstream-class-java.md)

## Throws

[**ProtectionException**](protectionexception-class-java.md)

## Defined in

CustomProtectedInputStream.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Remarks

This method is synchronous as it may require server / client communication. Your app specifies a current stream offset to *protectedContentLength* where the encrypted content is located in the backing stream.

If the range defined by the parameters current stream offset to *protectedContentLength* is not empty (i.e., *protectedContentLength* != 0), it must address an entire segment of encrypted content (i.e. it must start from block 0 (zero) and must have a final block in CBC case, or should be 16 bytes aligned in ECB case).

If the existing content ends at the end of the *InputStream*, your app can specify **Long.MAX\_VALUE** as *protectedContentLength*.

The *protectedContentLength* parameter is needed only for the cases when there is a non-encrypted app specific content after the encrypted content (Multiple segments of protected data). When decrypting it, we need to know where the encrypted content ends. The *protectedContentLength* parameter is specified in terms of the encrypted content, i.e. it includes the size of the CBC padding.

Your app can use [**getEncryptedContentLength**](customprotectedoutputstream-getencryptedcontentlength-method-java.md) to determine the size of the encrypted content given the size of the original content.

This method works in a synchronous manner.

 

 





