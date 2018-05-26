---
title: Error Codes in COM
description: .
ms.assetid: ed430863-f416-4611-81b4-0c31d819944a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Error Codes in COM

To indicate success or failure, COM methods and functions return a value of type **HRESULT**. An **HRESULT** is a 32-bit integer. The high-order bit of the **HRESULT** signals success or failure. Zero (0) indicates success and 1 indicates failure.

This produces the following numeric ranges:

-   Success codes: 0x0–0x7FFFFFFF.
-   Error codes: 0x80000000–0xFFFFFFFF.

A small number of COM methods do not return an **HRESULT** value. For example, the [**AddRef**](https://msdn.microsoft.com/library/windows/desktop/ms691379) and [**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) methods return unsigned long values. But every COM method that returns an error code does so by returning an **HRESULT** value.

To check whether a COM method succeeds, examine the high-order bit of the returned **HRESULT**. The Windows SDK headers provide two macros that make this easier: the [**SUCCEEDED**](https://msdn.microsoft.com/library/windows/desktop/ms687197) macro and the [**FAILED**](https://msdn.microsoft.com/library/windows/desktop/ms693474) macro. The **SUCCEEDED** macro returns **TRUE** if an **HRESULT** is a success code and **FALSE** if it is an error code. The following example checks whether [**CoInitializeEx**](https://msdn.microsoft.com/library/windows/desktop/ms695279) succeeds.


```C++
HRESULT hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED | 
    COINIT_DISABLE_OLE1DDE);

if (SUCCEEDED(hr))
{
    // The function succeeded.
}
else
{
    // Handle the error.
}
```



Sometimes it is more convenient to test the inverse condition. The [**FAILED**](https://msdn.microsoft.com/library/windows/desktop/ms693474) macro does the opposite of [**SUCCEEDED**](https://msdn.microsoft.com/library/windows/desktop/ms687197). It returns **TRUE** for an error code and **FALSE** for a success code.


```C++
HRESULT hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED | 
    COINIT_DISABLE_OLE1DDE);

if (FAILED(hr))
{
    // Handle the error.
}
else
{
    // The function succeeded.
}
```



Later in this module, we will look at some practical advice for how to structure your code to handle COM errors. (See [Error Handling in COM](error-handling-in-com.md).)

## Next

[Creating an Object in COM](creating-an-object-in-com.md)

 

 




