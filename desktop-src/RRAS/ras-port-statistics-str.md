---
title: RAS_PORT_STATISTICS structure (Rassapi.h)
description: The RAS\_PORT\_STATISTICS structure reports the statistics that a RAS server collects for a connected port.
ms.assetid: c42c7059-ff92-4f49-a86e-2f47a083aa8e
keywords:
- RAS_PORT_STATISTICS structure RAS
- PRAS_PORT_STATISTICS structure pointer RAS
topic_type:
- apiref
api_name:
- RAS_PORT_STATISTICS
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_PORT\_STATISTICS structure

\[The **RAS\_PORT\_STATISTICS** structure is not supported as of Windows Vista.\]

The **RAS\_PORT\_STATISTICS** structure reports the statistics that a RAS server collects for a connected port. The RAS server resets the various statistic counters each time the port is connected. Call the [**RasAdminPortClearStatistics**](rasadminportclearstatistics.md) function to force the RAS server to reset the statistic counters.

For a port that is part of a multilink connection, this structure provides two sets of statistics. The first set contains the cumulative statistics for all ports in the connection. These statistics are the same for all ports in the connection. The second set contains the statistics for just this port. If the port is not part of a multilink connection, both sets of statistics have the same information. To determine whether a port is part of a multilink connection, check the PORT\_MULTILINKED bit in the **Flags** member of the port's [**RAS\_PORT\_0**](ras-port-0-str.md) structure.

## Syntax


```C++
typedef struct _RAS_PORT_STATISTICS {
  DWORD dwBytesXmited;
  DWORD dwBytesRcved;
  DWORD dwFramesXmited;
  DWORD dwFramesRcved;
  DWORD dwCrcErr;
  DWORD dwTimeoutErr;
  DWORD dwAlignmentErr;
  DWORD dwHardwareOverrunErr;
  DWORD dwFramingErr;
  DWORD dwBufferOverrunErr;
  DWORD dwBytesXmitedUncompressed;
  DWORD dwBytesRcvedUncompressed;
  DWORD dwBytesXmitedCompressed;
  DWORD dwBytesRcvedCompressed;
  DWORD dwPortBytesXmited;
  DWORD dwPortBytesRcved;
  DWORD dwPortFramesXmited;
  DWORD dwPortFramesRcved;
  DWORD dwPortCrcErr;
  DWORD dwPortTimeoutErr;
  DWORD dwPortAlignmentErr;
  DWORD dwPortHardwareOverrunErr;
  DWORD dwPortFramingErr;
  DWORD dwPortBufferOverrunErr;
  DWORD dwPortBytesXmitedUncompressed;
  DWORD dwPortBytesRcvedUncompressed;
  DWORD dwPortBytesXmitedCompressed;
  DWORD dwPortBytesRcvedCompressed;
} RAS_PORT_STATISTICS, *PRAS_PORT_STATISTICS;
```



## Members

<dl> <dt>

**dwBytesXmited**
</dt> <dd>

Specifies the total number of bytes transmitted by the connection.

</dd> <dt>

**dwBytesRcved**
</dt> <dd>

Specifies the total number of bytes received by the connection.

</dd> <dt>

**dwFramesXmited**
</dt> <dd>

Specifies the total number of frames transmitted by the connection.

</dd> <dt>

**dwFramesRcved**
</dt> <dd>

Specifies the total number of frames received by the connection.

</dd> <dt>

**dwCrcErr**
</dt> <dd>

Specifies the total number of CRC errors on the connection. CRC errors are caused by the failure of a cyclic redundancy check. A CRC error indicates that one or more characters in the data packet received were found garbled on arrival.

</dd> <dt>

**dwTimeoutErr**
</dt> <dd>

Specifies the total number of time-out errors on the connection. Time-out errors occur when an expected character is not received in time. When this occurs, the software assumes that the data has been lost and requests that it be resent.

</dd> <dt>

**dwAlignmentErr**
</dt> <dd>

Specifies the total number of alignment errors on the connection. Alignment errors occur when a character received is not the one expected. This usually happens when a character is lost or when a time-out error occurs.

</dd> <dt>

**dwHardwareOverrunErr**
</dt> <dd>

Specifies the total number of hardware overrun errors on the connection. These errors indicate the number of times the sending computer has transmitted characters faster than the receiving computer hardware can process them. If this problem persists, reduce the BPS connection rate on the client.

</dd> <dt>

**dwFramingErr**
</dt> <dd>

Specifies the total number of framing errors on the connection. A framing error occurs when an asynchronous character is received with an invalid start or stop bit.

</dd> <dt>

**dwBufferOverrunErr**
</dt> <dd>

Specifies the total number of buffer overrun errors on the connection. A buffer overrun error occurs when the sending computer is transmitting characters faster than the receiving computer can accommodate them. If this problem persists, reduce the BPS connection rate on the client.

</dd> <dt>

**dwBytesXmitedUncompressed**
</dt> <dd>

Specifies the total number of bytes transmitted uncompressed by the connection.

</dd> <dt>

**dwBytesRcvedUncompressed**
</dt> <dd>

Specifies the total number of bytes received uncompressed by the connection.

</dd> <dt>

**dwBytesXmitedCompressed**
</dt> <dd>

Specifies the total number of bytes transmitted compressed by the connection.

</dd> <dt>

**dwBytesRcvedCompressed**
</dt> <dd>

Specifies the total number of bytes received compressed by the connection.

</dd> <dt>

**dwPortBytesXmited**
</dt> <dd>

Specifies the total number of bytes transmitted by the port.

</dd> <dt>

**dwPortBytesRcved**
</dt> <dd>

Specifies the total number of bytes received by the port.

</dd> <dt>

**dwPortFramesXmited**
</dt> <dd>

Specifies the total number of frames transmitted by the port.

</dd> <dt>

**dwPortFramesRcved**
</dt> <dd>

Specifies the total number of frames received by the port.

</dd> <dt>

**dwPortCrcErr**
</dt> <dd>

Specifies the total number of CRC errors on the port. CRC errors are caused by the failure of a cyclic redundancy check. A CRC error indicates that one or more characters in the data packet received were found garbled on arrival.

</dd> <dt>

**dwPortTimeoutErr**
</dt> <dd>

Specifies the total number of time-out errors on the port. Time-out errors occur when an expected character is not received in time. When this occurs, the software assumes that the data has been lost and requests that it be resent.

</dd> <dt>

**dwPortAlignmentErr**
</dt> <dd>

Specifies the total number of alignment errors on the port. Alignment errors occur when a character received is not the one expected. This usually happens when a character is lost or when a time-out error occurs.

</dd> <dt>

**dwPortHardwareOverrunErr**
</dt> <dd>

Specifies the total number of hardware overrun errors on the port. These errors indicate the number of times the sending computer has transmitted characters faster than the receiving computer hardware can process them. If this problem persists, reduce the BPS connection rate on the client.

</dd> <dt>

**dwPortFramingErr**
</dt> <dd>

Specifies the total number of framing errors on the port. A framing error occurs when an asynchronous character is received with an invalid start or stop bit.

</dd> <dt>

**dwPortBufferOverrunErr**
</dt> <dd>

Specifies the total number of buffer overrun errors on the port. A buffer overrun error occurs when the sending computer is transmitting characters faster than the receiving computer can accommodate them. If this problem persists, reduce the BPS connection rate on the client.

</dd> <dt>

**dwPortBytesXmitedUncompressed**
</dt> <dd>

Specifies the total number of bytes transmitted uncompressed by the port. If the port is part of a multilink connection, this member is not valid. Use the compression statistics for the connection instead.

</dd> <dt>

**dwPortBytesRcvedUncompressed**
</dt> <dd>

Specifies the total number of bytes received uncompressed by the port. If the port is part of a multilink connection, this member is not valid. Use the compression statistics for the connection instead.

</dd> <dt>

**dwPortBytesXmitedCompressed**
</dt> <dd>

Specifies the total number of bytes transmitted compressed by the port. If the port is part of a multilink connection, this member is not valid. Use the compression statistics for the connection instead.

</dd> <dt>

**dwPortBytesRcvedCompressed**
</dt> <dd>

Specifies the total number of bytes received compressed by the port. If the port is part of a multilink connection, this member is not valid. Use the compression statistics for the connection instead.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP<br/>                                                                |
| End of server support<br/>    | Windows Server 2003<br/>                                                       |
| Header<br/>                   | <dl> <dt>Rassapi.h</dt> </dl> |



## See also

<dl> <dt>

[Remote Access Service (RAS) Overview](about-remote-access-service.md)
</dt> <dt>

[RAS Server Administration Structures](ras-server-administration-structures.md)
</dt> <dt>

[**RAS\_PORT\_0**](ras-port-0-str.md)
</dt> <dt>

[**RasAdminAcceptNewConnection**](rasadminacceptnewconnection.md)
</dt> <dt>

[**RasAdminConnectionHangupNotification**](rasadminconnectionhangupnotification.md)
</dt> <dt>

[**RasAdminPortClearStatistics**](rasadminportclearstatistics.md)
</dt> <dt>

[**RasAdminPortGetInfo**](rasadminportgetinfo.md)
</dt> </dl>

 

 





