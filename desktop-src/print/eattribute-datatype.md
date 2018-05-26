---
Description: The EATTRIBUTE\_DATATYPE enumerates the possible data types for a global attribute, feature attribute or option attribute.
ms.assetid: 51d3e768-11b1-411d-89b1-4fec19306b97
title: EATTRIBUTE\_DATATYPE enumeration
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EATTRIBUTE\_DATATYPE enumeration

The EATTRIBUTE\_DATATYPE enumerates the possible data types for a global attribute, feature attribute or option attribute.

## Syntax


```C++
typedef enum _EATTRIBUTE_DATATYPE { 
  kADT_UNKNOWN           = 0,
  kADT_BOOL              = 1,
  kADT_INT               = 2,
  kADT_LONG              = 3,
  kADT_DWORD             = 4,
  kADT_ASCII             = 5,
  kADT_UNICODE           = 6,
  kADT_BINARY            = 7,
  kADT_SIZE              = 8,
  kADT_RECT              = 9,
  kADT_CUSTOMSIZEPARAMS  = 10
} EATTRIBUTE_DATATYPE;
```



## Constants

<dl> <dt>

<span id="kADT_UNKNOWN"></span><span id="kadt_unknown"></span><span id="KADT_UNKNOWN"></span>**kADT\_UNKNOWN**
</dt> <dd>

The attribute is of unknown type.

</dd> <dt>

<span id="kADT_BOOL"></span><span id="kadt_bool"></span><span id="KADT_BOOL"></span>**kADT\_BOOL**
</dt> <dd>

The attribute is of type BOOL.

</dd> <dt>

<span id="kADT_INT"></span><span id="kadt_int"></span><span id="KADT_INT"></span>**kADT\_INT**
</dt> <dd>

The attribute is of type INT.

</dd> <dt>

<span id="kADT_LONG"></span><span id="kadt_long"></span><span id="KADT_LONG"></span>**kADT\_LONG**
</dt> <dd>

The attribute is of type LONG.

</dd> <dt>

<span id="kADT_DWORD"></span><span id="kadt_dword"></span><span id="KADT_DWORD"></span>**kADT\_DWORD**
</dt> <dd>

The attribute is of type DWORD.

</dd> <dt>

<span id="kADT_ASCII"></span><span id="kadt_ascii"></span><span id="KADT_ASCII"></span>**kADT\_ASCII**
</dt> <dd>

The attribute is an ASCII string.

</dd> <dt>

<span id="kADT_UNICODE"></span><span id="kadt_unicode"></span><span id="KADT_UNICODE"></span>**kADT\_UNICODE**
</dt> <dd>

The attribute is a Unicode string.

</dd> <dt>

<span id="kADT_BINARY"></span><span id="kadt_binary"></span><span id="KADT_BINARY"></span>**kADT\_BINARY**
</dt> <dd>

The attribute consists of binary data.

</dd> <dt>

<span id="kADT_SIZE"></span><span id="kadt_size"></span><span id="KADT_SIZE"></span>**kADT\_SIZE**
</dt> <dd>

The attribute is of type SIZE.

</dd> <dt>

<span id="kADT_RECT"></span><span id="kadt_rect"></span><span id="KADT_RECT"></span>**kADT\_RECT**
</dt> <dd>

The attribute is of type RECT.

</dd> <dt>

<span id="kADT_CUSTOMSIZEPARAMS"></span><span id="kadt_customsizeparams"></span><span id="KADT_CUSTOMSIZEPARAMS"></span>**kADT\_CUSTOMSIZEPARAMS**
</dt> <dd>

The attribute is an array containing CUSTOMPARAM\_MAX (a constant defined in printoem.h) elements. Each element is a [**CUSTOMSIZEPARAM**](customsizeparam.md) structure.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**CUSTOMSIZEPARAM**](customsizeparam.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20EATTRIBUTE_DATATYPE%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





