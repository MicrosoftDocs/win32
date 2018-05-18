---
title: SendRNID\_IN structure
description: The SendRNID\_IN structure is used to deliver input parameter data to the SendRNID WMI method.
ms.assetid: '668c4d1a-52e8-49ea-bd19-e789dfa8dfa5'
keywords: ["SendRNID_IN structure Storage Devices", "PSendRNID_IN structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SendRNID_IN
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# SendRNID\_IN structure

The SendRNID\_IN structure is used to deliver input parameter data to the [**SendRNID**](https://msdn.microsoft.com/library/windows/hardware/ff565459) WMI method.

## Syntax


```C++
typedef struct _SendRNID_IN {
  UCHAR wwn[8];
  ULONG wwntype;
} SendRNID_IN, *PSendRNID_IN;
```



## Members

<dl> <dt>

**wwn**
</dt> <dd>

Contains a worldwide name for the port to which the request node identification data (RNID) command is sent.

</dd> <dt>

**wwntype**
</dt> <dd>

Deprecated. Do not use.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SendRNID\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SendRNID**](https://msdn.microsoft.com/library/windows/hardware/ff565459)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SendRNID_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






