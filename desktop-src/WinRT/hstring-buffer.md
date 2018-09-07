---
Description: A handle to a mutable string buffer that you can use to create an HSTRING.
ms.assetid: D173CE70-ABF3-4703-A229-0753F2AF6F70
title: HSTRING_BUFFER
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HSTRING\_BUFFER

A handle to a mutable string buffer that you can use to create an [**HSTRING**](hstring.md).


```C++
typedef HANDLE HSTRING_BUFFER;
```



## Remarks

**HSTRING\_BUFFER** represents a string buffer that you can modify before converting it to an immutable [**HSTRING**](hstring.md).

Call the [**WindowsPreallocateStringBuffer**](https://msdn.microsoft.com/en-us/library/BR224638(v=VS.85).aspx) function to create an **HSTRING\_BUFFER**. Call the [**WindowsPromoteStringBuffer**](https://msdn.microsoft.com/en-us/library/BR224639(v=VS.85).aspx) to convert an **HSTRING\_BUFFER** to an immutable [**HSTRING**](hstring.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| Header<br/>                   | <dl> <dt>Hstring.h</dt> </dl> |



## See also

<dl> <dt>


</dt> <dt>

[**HSTRING**](hstring.md)
</dt> <dt>

[**WindowsPreallocateStringBuffer**](https://msdn.microsoft.com/en-us/library/BR224638(v=VS.85).aspx)
</dt> <dt>

[**WindowsPromoteStringBuffer**](https://msdn.microsoft.com/en-us/library/BR224639(v=VS.85).aspx)
</dt> </dl>

 

 




