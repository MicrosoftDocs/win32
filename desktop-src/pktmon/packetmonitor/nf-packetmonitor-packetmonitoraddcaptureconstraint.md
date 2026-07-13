---
title: PacketMonitorAddCaptureConstraint
description: This function is used to apply constraints to packets which are reported by packet monitor.
ms.topic: reference
ms.date: 07/05/2024
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - Pktmonapi.dll
api_name:
 - PacketMonitorAddCaptureConstraint
---

# PacketMonitorAddCaptureConstraint function

## Description

This function is used to apply constraints to packets which are reported by packet monitor.

This function is used to specify constraints/filters on packet capture for a Packet Monitor Session. Only those packets which satisfy the constraints added to a session will be captured by Packet Monitor. Multiple constraints can be added to a session in which case a packet will be captured if it matches any one of the added constraints. If no constraints have been added to a session, all packets will be captured.

## Syntax

```cpp
HRESULT
WINAPI
PacketMonitorAddCaptureConstraint(
    _In_ PACKETMONITOR_SESSION session,
    _In_ PACKETMONITOR_PROTOCOL_CONSTRAINT const* captureConstraint
    );
```

## Parameters

### [in] session

Packet Monitor Session to which this constraint will be applied as filter for Packet Monitoring. A session object can be created by calling PacketMonitorCreateLiveSession. 

### [in] captureConstraint

Pointer to variable of type PACKETMONITOR_PROTOCOL_CONSTRAINT specifying the constraint to be applied on the packets for the session. Packet monitor will only report packets for which the header data matches with all the fields set in this struct.

```cpp
typedef struct PACKETMONITOR_PROTOCOL_CONSTRAINT
{
    WCHAR Name[PACKETMONITOR_MAX_NAME_LENGTH];

    union
    {
        struct
        {
            UINT Mac1 : 1;
            UINT Mac2 : 1;
            UINT VlanId : 1;
            UINT EtherType : 1;

            UINT DSCP : 1;
            UINT TransportProtocol : 1;
            UINT Ip1 : 1;
            UINT Ip2 : 1;
            UINT IPv6 : 1; // indicate IP version

            UINT PrefixLength1 : 1;
            UINT PrefixLength2 : 1;

            UINT Port1 : 1;
            UINT Port2 : 1;
            UINT TCPFlags : 1;
            UINT EncapType : 1;
            UINT VxLanPort : 1;

            UINT ClusterHeartbeat : 1;

        } IsPresent;

        UINT IsPresentValue;
    };

    // Ethernet frame
    UCHAR Mac1[PACKETMONITOR_MAC_ADDRESS_SIZE];
    UCHAR Mac2[PACKETMONITOR_MAC_ADDRESS_SIZE];

    USHORT VlanId;

    USHORT EtherType; 

    // IP header
    USHORT DSCP;
    UCHAR TransportProtocol;

    PACKETMONITOR_IP_ADDRESS Ip1;
    PACKETMONITOR_IP_ADDRESS Ip2;

    UCHAR PrefixLength1;
    UCHAR PrefixLength2;

    // TCP or UDP header
    USHORT Port1;
    USHORT Port2;

    UCHAR TCPFlags;

    // Encapsulation
    ULONG EncapType;
    USHORT VxLanPort;

    // Counters
    UINT64 Packets;
    UINT64 Bytes;
} PACKETMONITOR_PROTOCOL_CONSTRAINT;

typedef union PACKETMONITOR_IP_ADDRESS
{
    ULONG IPv4;
    UCHAR IPv4_bytes[PACKETMONITOR_IPV4_ADDRESS_SIZE];
 
    ULONGLONG IPv6[PACKETMONITOR_IPV6_ADDRESS_SIZE / sizeof(ULONGLONG)];
    UCHAR IPv6_bytes[PACKETMONITOR_IPV6_ADDRESS_SIZE];
} PACKETMONITOR_IP_ADDRESS;
```

* Mac1 – Mac Address of Source if IsPresent.Mac1 is TRUE. 
* Mac2 – Mac Address of Destination if IsPresent.Mac2 is TRUE.
* EtherType – Ethernet Type Value if IsPresent.EtherType is TRUE.
* DSCP – Field in the IP header if IsPresent.DSCP is TRUE. 
* TransportProtocol – Type of Protocol (UDP – 17, TCP – 6, etc.)
* Ip1 – Ip Address of Source if IsPresent.Ip1 is TRUE.
* Ip2 – Ip Address of Destination if IsPresent.Ip2 is TRUE. 
* Port1 – Source Port Number if IsPresent.Port1 is TRUE.
* Port2 – Destination Port Number if IsPresent.Port1 is TRUE.
* TCPFlags – TCP Flags if IsPresent.TCPFlags is TRUE.
* VxLanPort – VxLanPort if IsPresent. VxLanPort is TRUE
* EncapType – Encapsulation type for packets. Supported Values are:
  * 0x00 – No Encapsulation (Default)
  * 0x01 – VxLan Encapsulation
  * 0x02 – GRE(Generic Routing Encapsulation) encapsulation
  * 0x04 – IP inside IP packet Encapsulation
  * 0xFF – All Encapsulation supported. 
* Packets - Not Implemented
Bytes - Not Implemented

## Returns

If the function succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

‘IsPresent’ struct inside ‘PACKETMONITOR_PROTOCOL_CONSTRAINT’ behaves as a flag to specify which corresponding field contains a value.

## Remarks

This can be called either before or after activating a Session.

## See also

[Packet Monitor (Pktmon) reference](../pktmon-reference.md)
