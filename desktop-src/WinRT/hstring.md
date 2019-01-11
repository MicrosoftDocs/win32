---
Description: A handle to a Windows Runtime string.
ms.assetid: 763ACE57-EFDD-482E-851E-668D7756C5DF
title: HSTRING
ms.topic: article
ms.date: 05/31/2018
---

# HSTRING

A handle to a Windows Runtime string.


```C++
typedef HSTRING__* HSTRING;
```



## Remarks

Use **HSTRING** to represent immutable strings in the Windows Runtime.

JavaScript and other languages, such as C\#, and Microsoft Visual Basic, can use strings that are represented by using **HSTRING**. The following table shows how an **HSTRING** is represented in other languages.



| Programming Language                                                                    | String Representation                                      |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------|
| [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt)              | [winrt::hstring](/uwp/cpp-ref-for-winrt/hstring) class     |
| Visual C++ component extensions ([C++/CX](/cpp/cppcx/visual-c-language-reference-c-cx)) | [Platform::String](/cpp/cppcx/platform-string-class) class |
| JavaScript                                                                              | String object                                              |
| .NET Framework                                                                          | System.String class                                        |



 

The **HSTRING** handle is a standard handle type. Semantically, an **HSTRING** containing the value **NULL** represents the empty string, which consists of zero content characters and a terminating **NULL** character. Creating a string via [**WindowsCreateString**](https://msdn.microsoft.com/en-us/library/BR224630(v=VS.85).aspx) with zero characters will produce the handle value **NULL**. When calling [**WindowsGetStringRawBuffer**](https://msdn.microsoft.com/en-us/library/BR224636(v=VS.85).aspx) with the value **NULL**, a pointer to an empty string followed only by the **NUL** terminating character will be returned. No distinct value exists to represent an **HSTRING** that is uninitialized.

Call the [**WindowsCreateString**](https://msdn.microsoft.com/en-us/library/BR224630(v=VS.85).aspx) function to create a new **HSTRING**, and call the [**WindowsDeleteString**](https://msdn.microsoft.com/en-us/library/BR224632(v=VS.85).aspx) function to release the reference to the backing string memory. Call the [**WindowsCreateStringReference**](https://msdn.microsoft.com/en-us/library/BR224631(v=VS.85).aspx) function to create a string reference, which is also called a *fast-pass string*.

Copy an **HSTRING** by calling the [**WindowsDuplicateString**](https://msdn.microsoft.com/en-us/library/BR224634(v=VS.85).aspx) function.

Concatenate two strings by calling the [**WindowsConcatString**](https://msdn.microsoft.com/en-us/library/BR224629(v=VS.85).aspx) function.

Access the backing string memory by calling the [**WindowsGetStringRawBuffer**](https://msdn.microsoft.com/en-us/library/BR224636(v=VS.85).aspx) function.

**HSTRING** can store and use embedded **NUL** characters. Use the [**WindowsStringHasEmbeddedNull**](https://msdn.microsoft.com/en-us/library/BR224641(v=VS.85).aspx) function to check for embedded **NUL** characters before using any functions which may produce unexpected results. For example, most of the Windows functions use **LPCWSTR** as an input parameter, and they compute the length of the string only until the first **NUL** is encountered.

The backing string must remain immutable and null-terminated. When calling code creates a string reference by using the [**WindowsCreateStringReference**](https://msdn.microsoft.com/en-us/library/BR224631(v=VS.85).aspx) function, the memory containing the backing string representation is owned by the caller. The Windows Runtime relies on the contents of the original string to remain unchanged. When passing a string reference into the Windows Runtime, it is the caller’s responsibility to ensure that the string’s contents are unchanging and **NUL** terminated for the duration of the call. The Windows Runtime releases all references to the string reference when the call returns.

When you receive an **HSTRING** as an out parameter, it is good practice to set the handle to **NULL** when you are finished with it.

Call the [**WindowsPreallocateStringBuffer**](https://msdn.microsoft.com/en-us/library/BR224638(v=VS.85).aspx) function to allocate a mutable string buffer that you can use to create an immutable **HSTRING**. When you have finished populating the buffer, you call the [**WindowsPromoteStringBuffer**](https://msdn.microsoft.com/en-us/library/BR224639(v=VS.85).aspx) function to create the **HSTRING**. This two-phase construction pattern enables functionality that is similar to a "string builder."

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| Header<br/>                   | <dl> <dt>Hstring.h</dt> </dl> |



## See also

<dl> <dt>


</dt> <dt>

[**WindowsCreateString**](https://msdn.microsoft.com/en-us/library/BR224630(v=VS.85).aspx)
</dt> <dt>

[**WindowsDeleteString**](https://msdn.microsoft.com/en-us/library/BR224632(v=VS.85).aspx)
</dt> <dt>

[**WindowsDuplicateString**](https://msdn.microsoft.com/en-us/library/BR224634(v=VS.85).aspx)
</dt> <dt>

[**WindowsPreallocateStringBuffer**](https://msdn.microsoft.com/en-us/library/BR224638(v=VS.85).aspx)
</dt> </dl>

 

 




