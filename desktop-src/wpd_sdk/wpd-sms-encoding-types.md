---
Description: The WPD\_SMS\_ENCODING\_TYPES enumeration type describes the encoding type of a short message service (SMS) message.
ms.assetid: 5a9752e5-4e09-42a4-8fed-b4ea551fa36f
title: WPD\_SMS\_ENCODING\_TYPES enumeration
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WPD\_SMS\_ENCODING\_TYPES enumeration

The **WPD\_SMS\_ENCODING\_TYPES** enumeration type describes the encoding type of a short message service (SMS) message.

## Syntax


```C++
typedef enum WPD_SMS_ENCODING_TYPES { 
  SMS_ENCODING_7_BIT   = 0,
  SMS_ENCODING_8_BIT   = 1,
  SMS_ENCODING_UTF_16  = 2
} ;
```



## Constants

<dl> <dt>

<span id="SMS_ENCODING_7_BIT"></span><span id="sms_encoding_7_bit"></span>**SMS\_ENCODING\_7\_BIT**
</dt> <dd>

Seven-bit encoding.

</dd> <dt>

<span id="SMS_ENCODING_8_BIT"></span><span id="sms_encoding_8_bit"></span>**SMS\_ENCODING\_8\_BIT**
</dt> <dd>

Eight-bit encoding.

</dd> <dt>

<span id="SMS_ENCODING_UTF_16"></span><span id="sms_encoding_utf_16"></span>**SMS\_ENCODING\_UTF\_16**
</dt> <dd>

Sixteen-bit encoding (UTF).

</dd> </dl>

## Remarks

This enumeration is used by the [WPD\_SMS\_ENCODING](sms-properties.md#wpd-sms-encoding) property.

## Requirements



|                   |                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




