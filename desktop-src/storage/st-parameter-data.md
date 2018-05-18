---
title: ST\_PARAMETER\_DATA structure
description: The ST\_PARAMETER\_DATA structure contains the parameter list for the set timestamp command.
ms.assetid: 'C50F45EC-433C-421D-BD02-4C86CB44D5A4'
keywords: ["ST_PARAMETER_DATA structure Storage Devices", "PST_PARAMETER_DATA structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ST_PARAMETER_DATA
api_location:
- scsi.h
api_type:
- HeaderDef
---

# ST\_PARAMETER\_DATA structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **ST\_PARAMETER\_DATA** structure contains the parameter list for the set timestamp command.

## Syntax


```C++
typedef struct _ST_PARAMETER_DATA {
  UCHAR Reserved1[4];
  UCHAR Timestamp[6];
  UCHAR Reserved2[2];
} ST_PARAMETER_DATA, *PST_PARAMETER_DATA;
```



## Members

<dl> <dt>

**Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Timestamp**
</dt> <dd>

Specifies the value to which a device clock shall be initialized. The timestamp should be the number of milliseconds that have elapsed since midnight, 1 January 1970 UT.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Requirements



|                    |                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows 10, version 1709 and later versions of Windows.<br/>                                      |
| Header<br/>  | <dl> <dt>Scsi.h (include Minitape.h or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**RT\_PARAMETER\_DATA**](rt-parameter-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ST_PARAMETER_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






