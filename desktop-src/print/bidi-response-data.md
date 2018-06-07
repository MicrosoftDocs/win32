---
Description: The BIDI\_RESPONSE\_DATA structure holds a single bidi response.
ms.assetid: 8e56ef0a-c652-4fca-ad87-4a0495c8de2e
title: BIDI\_RESPONSE\_DATA structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# BIDI\_RESPONSE\_DATA structure

The BIDI\_RESPONSE\_DATA structure holds a single bidi response.

## Syntax


```C++
typedef struct _BIDI_RESPONSE_DATA {
  DWORD     dwResult;
  DWORD     dwReqNumber;
  LPWSTR    pSchema;
  BIDI_DATA data;
} BIDI_RESPONSE_DATA, *PBIDI_RESPONSE_DATA, *LPBIDI_RESPONSE_DATA;
```



## Members

<dl> <dt>

**dwResult**
</dt> <dd>

Specifies the last error of the response.

</dd> <dt>

**dwReqNumber**
</dt> <dd>

Specifies a number used to match a response and a request in a multirequest operation.

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

The spooler's [**RouterAllocBidiResponseContainer**](routerallocbidiresponsecontainer.md) function is used to allocate the memory needed for a [**BIDI\_RESPONSE\_CONTAINER**](bidi-response-container.md) structure, which is then used to hold an array of BIDI\_RESPONSE\_DATA structures. When a BIDI\_RESPONSE\_CONTAINER structure is no longer needed, it should be freed by a call to [**RouterFreeBidiResponseContainer**](routerfreebidiresponsecontainer.md).

When the bidi action is BIDI\_ACTION\_GETALL, the **dwReqNumber** member holds the ID of the matching request in the [**BIDI\_REQUEST\_CONTAINER**](bidi-request-container.md) structure, the **pSchema** member points to the schema string associated with the data, and the **data** member holds the bidi data. If the bidi action is BIDI\_ACTION\_ENUM\_SCHEMA, **pSchema** should be set to **NULL**, and the **data** member will hold the supported schema string. In this case, **data.dwDataType** is set to BIDI\_TEXT (a [**BIDI\_DATA**](bidi-data.md) enumerator). For information about the BIDI\_ACTION\_*Xxx* constants, see IBidiSpooler::MultiSendRecv in the Microsoft Windows SDK documentation.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | This structure is available in Windows XP and later operating systems.<br/>                          |
| Header<br/>  | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl> |



## See also

<dl> <dt>

[**BIDI\_RESPONSE\_CONTAINER**](bidi-response-container.md)
</dt> <dt>

[**RouterAllocBidiResponseContainer**](routerallocbidiresponsecontainer.md)
</dt> <dt>

[**RouterFreeBidiResponseContainer**](routerfreebidiresponsecontainer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BIDI_RESPONSE_DATA%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





