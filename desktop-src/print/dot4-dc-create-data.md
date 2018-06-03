---
Description: Defines the DOT4\_DC\_CREATE\_DATA construct.
ms.assetid: 9C21732B-0AB1-4F3E-8F3D-F0B12007920A
title: DOT4\_DC\_CREATE\_DATA structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DOT4\_DC\_CREATE\_DATA structure

Defines the **DOT4\_DC\_CREATE\_DATA** construct.

## Syntax


```C++
typedef struct _DOT4_DC_CREATE_DATA {
  unsigned char bPsid;
  CHAR          pServiceName[MAX_SERVICE_LENGTH + 1];
  unsigned char bType;
  ULONG         ulBufferSize;
  USHORT        usMaxHtoPPacketSize;
  USHORT        usMaxPtoHPacketSize;
  unsigned char bHsid;
} DOT4_DC_CREATE_DATA, *PDOT4_DC_CREATE_DATA;
```



## Members

<dl> <dt>

**bPsid**
</dt> <dd>

Specifies this or the service name sent.

</dd> <dt>

**pServiceName**
</dt> <dd>

Describes the **CHAR** member **pServiceName**.

</dd> <dt>

**bType**
</dt> <dd>

Specifies the type, stream or packet, of channels on the socket.

</dd> <dt>

**ulBufferSize**
</dt> <dd>

Specifies the size of the read buffer for channels on socket.

</dd> <dt>

**usMaxHtoPPacketSize**
</dt> <dd>

Describes the **USHORT** member **usMaxHtoPPacketSize**.

</dd> <dt>

**usMaxPtoHPacketSize**
</dt> <dd>

Describes the **USHORT** member **usMaxPtoHPacketSize**.

</dd> <dt>

**bHsid**
</dt> <dd>

Specifies the host socket ID returned.

</dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D4drvif.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DOT4_DC_CREATE_DATA%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




