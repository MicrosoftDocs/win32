---
Description: 'The BIDI\_RESPONSE\_CONTAINER structure is a container for a list of bidi responses.'
ms.assetid: '26924dd2-ac67-408c-87e0-5cfb3281fe75'
title: 'BIDI\_RESPONSE\_CONTAINER structure'
---

# BIDI\_RESPONSE\_CONTAINER structure

The BIDI\_RESPONSE\_CONTAINER structure is a container for a list of bidi responses.

## Syntax


```C++
typedef struct _BIDI_RESPONSE_CONTAINER {
  DWORD              Version;
  DWORD              Flags;
  DWORD              Count;
  BIDI_RESPONSE_DATA aData[1];
} BIDI_RESPONSE_CONTAINER, *PBIDI_RESPONSE_CONTAINER, *LPBIDI_RESPONSE_CONTAINER;
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

Specifies the number of responses in the **aData** member.

</dd> <dt>

**aData**
</dt> <dd>

Is an array of [**BIDI\_RESPONSE\_DATA**](bidi-response-data.md) structures, each containing a single bidi response.

</dd> </dl>

## Remarks

Even though the **aData** member of this structure is an array with only a single array element, **aData**\[0\] should be thought of as the first element of an array of (possibly) an arbitrarily large size.

The spooler's [**RouterAllocBidiResponseContainer**](routerallocbidiresponsecontainer.md) function allocates the memory needed for this structure, which is then used to hold an array of BIDI\_RESPONSE\_DATA structures. When a BIDI\_RESPONSE\_CONTAINER structure is no longer needed, it should be freed by a call to [**RouterFreeBidiResponseContainer**](routerfreebidiresponsecontainer.md).

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | This structure is available in Windows XP and later operating systems.<br/>                          |
| Header<br/>  | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl> |



## See also

<dl> <dt>

[**BIDI\_RESPONSE\_DATA**](bidi-response-data.md)
</dt> <dt>

[**RouterAllocBidiResponseContainer**](routerallocbidiresponsecontainer.md)
</dt> <dt>

[**RouterFreeBidiResponseContainer**](routerfreebidiresponsecontainer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BIDI_RESPONSE_CONTAINER%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





