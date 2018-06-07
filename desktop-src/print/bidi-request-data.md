---
Description: The BIDI\_REQUEST\_DATA structure holds a single bidi request.
ms.assetid: ef5a89e3-f072-48a7-b2d9-d68e0e27ba9e
title: BIDI\_REQUEST\_DATA structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# BIDI\_REQUEST\_DATA structure

The BIDI\_REQUEST\_DATA structure holds a single bidi request.

## Syntax


```C++
typedef struct _BIDI_REQUEST_DATA {
  DWORD     dwReqNumber;
  LPWSTR    pSchema;
  BIDI_DATA data;
} BIDI_REQUEST_DATA, *PBIDI_REQUEST_DATA, *LPBIDI_REQUEST_DATA;
```



## Members

<dl> <dt>

**dwReqNumber**
</dt> <dd>

Specifies the index of the request, which is used to match a response with a request in a multirequest operation.

</dd> <dt>

**pSchema**
</dt> <dd>

Pointer to a memory location containing the first byte of the schema string.

</dd> <dt>

**data**
</dt> <dd>

Specifies a [**BIDI\_DATA**](bidi-data.md) structure containing the data associated with the schema.

</dd> </dl>

## Remarks

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | This structure is available in Windows XP and later.<br/>                                            |
| Header<br/>  | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl> |



## See also

<dl> <dt>

[**BIDI\_DATA**](bidi-data.md)
</dt> <dt>

[**BIDI\_REQUEST\_CONTAINER**](bidi-request-container.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BIDI_REQUEST_DATA%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





