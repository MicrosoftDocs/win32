---
title: RT\_PARAMETER\_DATA structure
description: The RT\_PARAMETER\_DATA structure contains the parameter data for the report timestamp command.
ms.assetid: 'EB23D502-87E4-48B1-B1DC-0B215AB361C8'
keywords: ["RT_PARAMETER_DATA structure Storage Devices", "PRT_PARAMETER_DATA structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- RT_PARAMETER_DATA
api_location:
- scsi.h
api_type:
- HeaderDef
---

# RT\_PARAMETER\_DATA structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **RT\_PARAMETER\_DATA** structure contains the parameter data for the report timestamp command.

## Syntax


```C++
typedef struct _RT_PARAMETER_DATA {
  UCHAR     ParameterDataLength[2];
  UCHAR Origin  :3;
  UCHAR Reserved1  :5;
  UCHAR Reserved2;
  UCHAR Timestamp[6];
  UCHAR Reserved3[2];
} RT_PARAMETER_DATA, *PRT_PARAMETER_DATA;
```



## Members

<dl> <dt>

 **ParameterDataLength**
</dt> <dd>

Indicates the number of bytes that follow in the parameter data.

</dd> <dt>

**Origin**
</dt> <dd>

Indicates the most recent event that initialized the returned device clock.



| Value                                                                                                                                   | Meaning                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>                                                            | Device clock initialized to zero at power on or as the result of a hard reset.<br/> |
| <dl> <dt>1</dt> </dl>                                                            | Reserved for future use.<br/>                                                       |
| <dl> <dt>2</dt> </dl>                                                            | Device clock initialized by the SET TIMESTAMP command.<br/>                         |
| <dl> <dt>3</dt> </dl>                                                            | Device clock initialized by an unknown method.<br/>                                 |
| <dl> <dt></dt> <dt>4 to 7</dt> </dl> | Reserved for future use.<br/>                                                       |



 

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Timestamp**
</dt> <dd>

Contains the current value of a device clock.

</dd> <dt>

**Reserved3**
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

[**ST\_PARAMETER\_DATA**](st-parameter-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20RT_PARAMETER_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






