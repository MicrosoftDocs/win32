---
title: VMSerialPortType enumeration
description: The VMSerialPortType enumeration specifies the type of serial port.
ms.assetid: '01ac8f48-fc7e-4b8f-9214-551a8526774d'
keywords: ["VMSerialPortType enumeration Virtual Server"]
topic_type:
- apiref
api_name:
- VMSerialPortType
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
---

# VMSerialPortType enumeration

The **VMSerialPortType** enumeration specifies the type of serial port.

## Syntax


```C++
typedef enum  { 
  vmSerialPort_HostPort   = 0,
  vmSerialPort_TextFile   = 1,
  vmSerialPort_NamedPipe  = 2,
  vmSerialPort_Null       = 3
} VMSerialPortType;
```



## Constants

<dl> <dt>

<span id="vmSerialPort_HostPort"></span><span id="vmserialport_hostport"></span><span id="VMSERIALPORT_HOSTPORT"></span>**vmSerialPort\_HostPort**
</dt> <dd>

Host serial port.

</dd> <dt>

<span id="vmSerialPort_TextFile"></span><span id="vmserialport_textfile"></span><span id="VMSERIALPORT_TEXTFILE"></span>**vmSerialPort\_TextFile**
</dt> <dd>

Host text file.

</dd> <dt>

<span id="vmSerialPort_NamedPipe"></span><span id="vmserialport_namedpipe"></span><span id="VMSERIALPORT_NAMEDPIPE"></span>**vmSerialPort\_NamedPipe**
</dt> <dd>

Named pipe.

</dd> <dt>

<span id="vmSerialPort_Null"></span><span id="vmserialport_null"></span><span id="VMSERIALPORT_NULL"></span>**vmSerialPort\_Null**
</dt> <dd>

NULL serial port that discards all bits sent to it.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





