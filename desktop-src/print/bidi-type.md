---
Description: The BIDI\_TYPE enumeration lists the possible values of data transferred in a bidi operation.
ms.assetid: ebb79ad6-91a1-4bdf-a6f6-7e04ed2358d9
title: BIDI\_TYPE enumeration
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BIDI\_TYPE enumeration

The BIDI\_TYPE enumeration lists the possible values of data transferred in a bidi operation.

## Syntax


```C++
typedef enum  { 
  BIDI_NULL    = 0,
  BIDI_INT     = 1,
  BIDI_FLOAT   = 2,
  BIDI_BOOL    = 3,
  BIDI_STRING  = 4,
  BIDI_TEXT    = 5,
  BIDI_ENUM    = 6,
  BIDI_BLOB    = 7
} BIDI_TYPE;
```



## Constants

<dl> <dt>

<span id="BIDI_NULL"></span><span id="bidi_null"></span>**BIDI\_NULL**
</dt> <dd>

Indicates that there is no data.

</dd> <dt>

<span id="BIDI_INT"></span><span id="bidi_int"></span>**BIDI\_INT**
</dt> <dd>

Indicates that the bidi data is an integer.

</dd> <dt>

<span id="BIDI_FLOAT"></span><span id="bidi_float"></span>**BIDI\_FLOAT**
</dt> <dd>

Indicates that the bidi data is a floating-point number.

</dd> <dt>

<span id="BIDI_BOOL"></span><span id="bidi_bool"></span>**BIDI\_BOOL**
</dt> <dd>

Indicates that the bidi data is either **TRUE** or **FALSE**.

</dd> <dt>

<span id="BIDI_STRING"></span><span id="bidi_string"></span>**BIDI\_STRING**
</dt> <dd>

Indicates that the bidi data is a Unicode character string.

</dd> <dt>

<span id="BIDI_TEXT"></span><span id="bidi_text"></span>**BIDI\_TEXT**
</dt> <dd>

Indicates that the bidi data is a nonlocalizable Unicode string.

</dd> <dt>

<span id="BIDI_ENUM"></span><span id="bidi_enum"></span>**BIDI\_ENUM**
</dt> <dd>

Indicates that the bidi data value is a Unicode string.

</dd> <dt>

<span id="BIDI_BLOB"></span><span id="bidi_blob"></span>**BIDI\_BLOB**
</dt> <dd>

Indicates that the bidi data is binary data.

</dd> </dl>

## Remarks

The following correspondence applies between Simple Network Management Protocol (SNMP) types and bidi types defined in the BIDI\_TYPE enumeration.



| SNMP type                                                                                                                                                        | Bidi type                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| SNMP\_SYNTAX\_CNTR32<br/> SNMP\_SYNTAX\_GAUGE32<br/> SNMP\_SYNTAX\_INT<br/> SNMP\_SYNTAX\_TIMETICKS<br/> SNMP\_SYNTAX\_UINT32<br/> | BIDI\_BOOL<br/> BIDI\_INT<br/>                          |
| SNMP\_SYNTAX\_IPADDR<br/> SNMP\_SYNTAX\_OCTETS<br/> SNMP\_SYNTAX\_OID<br/>                                                                     | BIDI\_ENUM<br/> BIDI\_STRING<br/> BIDI\_TEXT<br/> |
| SNMP\_SYNTAX\_CNTR64<br/> SNMP\_SYNTAX\_OCTETS<br/> SNMP\_SYNTAX\_OPAQUE<br/>                                                                  | BIDI\_BLOB<br/>                                               |
| (none)<br/>                                                                                                                                                | BIDI\_FLOAT<br/>                                              |



 

See the smiValue structure in the Microsoft Windows SDK documentation for descriptions of the WinSNMP data types.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | This enumeration is available in Windows XP and later operating systems.<br/>                        |
| Header<br/>  | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BIDI_TYPE%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




