---
Description: The BIDI\_REQUEST\_CONTAINER structure is a container for a list of bidi requests.
ms.assetid: 9892cf0e-23ee-496f-9078-4a2a1fdb19d9
title: BIDI\_REQUEST\_CONTAINER structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# BIDI\_REQUEST\_CONTAINER structure

The BIDI\_REQUEST\_CONTAINER structure is a container for a list of bidi requests.

## Syntax


```C++
typedef struct _BIDI_REQUEST_CONTAINER {
  DWORD             Version;
  DWORD             Flags;
  DWORD             Count;
  BIDI_REQUEST_DATA aData[1];
} BIDI_REQUEST_CONTAINER, *PBIDI_REQUEST_CONTAINER, *LPBIDI_REQUEST_CONTAINER;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Specifies the version of the bidi API Schema, which is currently 1.

</dd> <dt>

**Flags**
</dt> <dd>

Is a set of flags reserved for system use. This must be zero.

</dd> <dt>

**Count**
</dt> <dd>

Specifies the number of bidi requests in the **aData** member. A container can contain zero or more requests, although a value of zero is valid only if the action is BIDI\_ACTION\_ENUM\_SCHEMA.

</dd> <dt>

**aData**
</dt> <dd>

Is an array of [**BIDI\_REQUEST\_DATA**](bidi-request-data.md) structures, each holding a single bidi request.

</dd> </dl>

## Remarks

Even though the **aData** member of this structure is an array with only a single array element, **aData**\[0\] should be thought of as the first element of an array of (possibly) an arbitrarily large size.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | This structure is available in Windows XP and later.<br/>                                            |
| Header<br/>  | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl> |



## See also

<dl> <dt>

[**BIDI\_REQUEST\_DATA**](bidi-request-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BIDI_REQUEST_CONTAINER%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





