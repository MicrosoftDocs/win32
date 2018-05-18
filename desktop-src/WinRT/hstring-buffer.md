---
Description: 'A handle to a mutable string buffer that you can use to create an HSTRING.'
ms.assetid: 'D173CE70-ABF3-4703-A229-0753F2AF6F70'
title: 'HSTRING\_BUFFER'
---

# HSTRING\_BUFFER

A handle to a mutable string buffer that you can use to create an [**HSTRING**](hstring.md).


```C++
typedef HANDLE HSTRING_BUFFER;
```



## Remarks

**HSTRING\_BUFFER** represents a string buffer that you can modify before converting it to an immutable [**HSTRING**](hstring.md).

Call the [**WindowsPreallocateStringBuffer**](windowspreallocatestringbuffer.md) function to create an **HSTRING\_BUFFER**. Call the [**WindowsPromoteStringBuffer**](windowspromotestringbuffer.md) to convert an **HSTRING\_BUFFER** to an immutable [**HSTRING**](hstring.md).

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

[**WindowsPreallocateStringBuffer**](windowspreallocatestringbuffer.md)
</dt> <dt>

[**WindowsPromoteStringBuffer**](windowspromotestringbuffer.md)
</dt> </dl>

 

 




