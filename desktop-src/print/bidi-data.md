---
Description: The BIDI\_DATA structure is used to store the values of a bidi schema.
ms.assetid: 9e0f3044-01c0-4dec-b34c-0f33ccfe3300
title: BIDI\_DATA structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BIDI\_DATA structure

The BIDI\_DATA structure is used to store the values of a bidi schema.

## Syntax


```C++
typedef struct _BIDI_DATA {
  DWORD dwBidiType;
  union {
    BOOL             bData;
    LONG             iData;
    LPWSTR           sData;
    FLOAT            fData;
    BINARY_CONTAINER biData;
  } u;
} BIDI_DATA, *PBIDI_DATA, *LPBIDI_DATA;
```



## Members

<dl> <dt>

**dwBidiType**
</dt> <dd>

Specifies the type of data in a bidi request as one of the values listed in the [**BIDI\_TYPE**](bidi-type.md) enumeration. The value of this member determines which one of the following five union members is valid.

</dd> <dt>

**u**
</dt> <dd> <dl> <dt>

**bData**
</dt> <dd>

Specifies the Boolean value. This member is valid only if the value of **dwBidiType** is BIDI\_BOOL, one of the BIDI\_TYPE enumerators.

</dd> <dt>

**iData**
</dt> <dd>

Specifies the integer value. This member is valid only if the value of **dwBidiType** is BIDI\_INT, one of the BIDI\_TYPE enumerators.

</dd> <dt>

**sData**
</dt> <dd>

Pointer to a memory location at which the first byte of the string is stored. This member is valid only if the value of **dwBidiType** is BIDI\_STRING or BIDI\_TEXT, two of the BIDI\_TYPE enumerators.

</dd> <dt>

**fData**
</dt> <dd>

Specifies the floating-point value. This member is valid only if the value of **dwBidiType** is BIDI\_FLOAT, one of the BIDI\_TYPE enumerators.

</dd> <dt>

**biData**
</dt> <dd>

Specifies a [**BINARY\_CONTAINER**](binary-container.md) structure that holds the binary data. This member is valid only if the value of **dwBidiType** is BIDI\_BLOB, one of the BIDI\_TYPE enumerators.

</dd> </dl> </dd> </dl>

## Remarks

The [**BIDI\_REQUEST\_DATA**](bidi-request-data.md) and [**BIDI\_RESPONSE\_DATA**](bidi-response-data.md) structures each have a member of this type, which holds the bidi data for the request or response.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | This structure is available in Windows XP and later.<br/>                                            |
| Header<br/>  | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl> |



## See also

<dl> <dt>

[**BINARY\_CONTAINER**](binary-container.md)
</dt> <dt>

[**BIDI\_TYPE**](bidi-type.md)
</dt> <dt>

[**BIDI\_REQUEST\_DATA**](bidi-request-data.md)
</dt> <dt>

[**BIDI\_RESPONSE\_DATA**](bidi-response-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BIDI_DATA%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





