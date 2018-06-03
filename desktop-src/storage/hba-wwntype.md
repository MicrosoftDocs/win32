---
title: HBA\_wwntype enumeration
description: The HBA\_wwntype enumerator indicates whether a worldwide name specifies a port or a node (machine).
ms.assetid: 30ce30db-e030-43c3-bf8d-2f6ef86087ab
keywords:
- HBA_wwntype enumeration Storage Devices
- HBA_WWNTYPE enumeration Storage Devices
topic_type:
- apiref
api_name:
- HBA_WWNTYPE
api_location:
- hbaapi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# HBA\_wwntype enumeration

The HBA\_wwntype enumerator indicates whether a worldwide name specifies a port or a node (machine).

## Syntax


```C++
typedef enum HBA_wwntype { 
  NODE_WWN  = 0,
  PORT_WWN  = 1
} HBA_WWNTYPE;
```



## Constants

<dl> <dt>

<span id="NODE_WWN"></span><span id="node_wwn"></span>**NODE\_WWN**
</dt> <dd>

Indicates that the world wide name specifies a node..

</dd> <dt>

<span id="PORT_WWN"></span><span id="port_wwn"></span>**PORT\_WWN**
</dt> <dd>

Indicates that the world wide name specifies a port.

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_SendRNID**](hba-sendrnid.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_wwntype%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






