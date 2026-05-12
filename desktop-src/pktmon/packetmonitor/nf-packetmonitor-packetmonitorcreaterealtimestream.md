---
title: PacketMonitorCreateRealtimeStream
description: Sets up the packet streaming capability inside Packet Monitor.
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
 - PacketMonitorCreateRealtimeStream
---

# PacketMonitorCreateRealtimeStream function

## Description

This function sets up the packet streaming capability inside Packet Monitor. Through this streaming capability, user mode applications can read packets captured in real time.  

This capability enables monitoring traffic in real time, and is useful in measuring latency, monitoring packet drops, etc. The Packet data is un-parsed, and is presented as a byte buffer. Real Time Stream is a type of output to a Session. When attached to a session, the stream will receive the packets as configured on that session. 

The Streaming capability is achieved when the `pktmonapi.dll` sets up a ring buffer to receive the packets from the driver.

## Syntax

```cpp
HRESULT
WINAPI
PacketMonitorCreateRealtimeStream(
    _In_ PACKETMONITOR_HANDLE handle,
    _In_ PACKETMONITOR_REALTIME_STREAM_CONFIGURATION const* configuration,
    _Out_ PACKETMONITOR_REALTIME_STREAM* realtimeStream
);
```

## Parameters

### [in] handle

Handle to Packet Monitor obtained from ‘PacketMonitorInitialize’.

### [in] configuration

Configuration of type PACKETMONITOR_REALTIME_STREAM_CONFIGURATION for real time Streaming.

### [out] realtimeStream

Pointer to store the handle created for Streaming. This will be used to attach to a session. 

This is declared as ‘DECLARE_HANDLE(PACKETMONITOR_REALTIME_STREAM)’.

## Returns

If the function succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## Remarks

### Struct type definitions

#### PACKETMONITOR_REALTIME_STREAM_CONFIGURATION

```cpp
typedef struct PACKETMONITOR_REALTIME_STREAM_CONFIGURATION
{
    VOID* UserContext;                                      
    PACKETMONITOR_STREAM_EVENT_CALLBACK *EventCallback;      
    PACKETMONITOR_STREAM_DATA_CALLBACK *DataCallback;        

    UINT16 BufferSizeMultiplier;                            

    UINT16 TruncationSize;                                  
} PACKETMONITOR_REALTIME_STREAM_CONFIGURATION;
```

* UserContext – Optional User context to refer in the Event and Data callback functions. 
* EventCallBack – Optional callback of PACKETMONITOR_STREAM_EVENT_CALLBACK type which will be triggered for Streaming related events. 
  * It is recommended for the user side application to implement this callback to receive streaming related events. 
* DataCallBack – Optional callback of type PACKETMONITOR_STREAM_DATA_CALLBACK which will be triggered for each packet arriving from the stream in real time. Do note that if the computations in this callback are too expensive one may end up reading from the stream slower than packets are written to it, ultimately leading to missed packets. 
* BufferSizeMultiplier – Factor by which the Default Buffer size should be multiplied to set up the Ring Buffer. 
  * Default Packet buffer size is – 256Kb. Allowed Range for BufferSizeMultiplier is from 1 to 10.
* TruncationSize – Truncation size of packet data. The default is 128 bytes. Maximum is 9000 bytes. 

#### PACKETMONITOR_STREAM_EVENT_CALLBACK

```cpp
typedef VOID CALLBACK PACKETMONITOR_STREAM_EVENT_CALLBACK(
    _In_opt_ VOID* context,
    _In_ PACKETMONITOR_STREAM_EVENT_INFO const* StreamEventInfo,
    _In_ PACKETMONITOR_STREAM_EVENT_KIND eventKind
);
```

* context – If specified in the Streaming setup configuration. 
* StreamEventInfo – Union of type PACKETMONITOR_STREAM_EVENT_INFO which maps to corresponding event when the callback is triggered. 
* eventKind – Type of event generated (PACKETMONITOR_STREAM_EVENT_KIND) when the callback is triggered. 

#### PACKETMONITOR_STREAM_DATA_CALLBACK

```cpp
typedef VOID CALLBACK PACKETMONITOR_STREAM_DATA_CALLBACK(
    _In_opt_ VOID* context,
    _In_ PACKETMONITOR_STREAM_DATA_DESCRIPTOR const* data
);
```

* context – If specified during Streaming setup configuration. 
* Data – Packet Data in format of PACKETMONITOR_STREAM_DATA_DESCRIPTOR.

#### PACKETMONITOR_ STREAM_DATA_DESCRIPTOR

```cpp
typedef struct PACKETMONITOR_STREAM_DATA_DESCRIPTOR
{
    VOID const* Data;         
    UINT32 DataSize;          

    UINT32 MetadataOffset;    
    UINT32 PacketOffset;      
    UINT32 PacketLength;      
    UINT32 MissedPacketWriteCount;  
    UINT32 MissedPacketReadCount;   
} PACKETMONITOR_STREAM_DATA_DESCRIPTOR;
```

* Data – Pointer to the Start of Packet Data. 
* DataSize – Total Length of Packet Data. Note that this is different from the actual packet payload length. 
* MetadataOffset – Offset to the Packet Metadata (PACKETMONITOR_STREAM_METADATA) starting from the ‘Data’ pointer. 
* PacketOffset – Offset to the Packet Payload starting from ‘Data’ pointer. 
* PacketLength – Length in bytes for Packet payload. 
* MissedPacketWriteCount – Number of packets missed to be written to the stream before the previous packet.  
* MissedPacketReadCount – Number of packets missed while reading. This may happen due to some errors during reading.

#### PACKETMONITOR_ STREAM_METADATA

```cpp
typedef struct PACKETMONITOR_STREAM_METADATA
{
    UINT64  PktGroupId;         
    UINT16  PktCount;           
    UINT16  AppearanceCount;    
    UINT16  DirectionName;      
    UINT16  PacketType;         
    UINT16  ComponentId;        
    UINT16  EdgeId;             
    UINT16  Reserved;           
    UINT32  DropReason;         
    UINT32  DropLocation;       
    UINT16  Processor;          
    LARGE_INTEGER TimeStamp;    
} PACKETMONITOR_STREAM_METADATA;
```

* PktGroupId – Group Id for packets belonging to the same processor. 
* AppearanceCount – Packet Count belonging to the same Net Buffer List. 
* DirectionName – Enum value of ‘PKTMON_DIRECTION_TAG’. Specifies the direction for which the packet was reported. 
* PacketType – Packet Payload type as ‘PKTMON_PACKET_TYPE ‘.
* ComponentId – Id of component/data source which reported the packet. The ComponentId can be queried from the API ‘PacketMonitorEnumDataSources’.
* EdgeId – Edge Id of the component boundary from which packet was reported. An edge represents a pair of entry/exit points. 
* Reserved – Reserved field. 
* DropReason – Packet drop reason code value as mentioned in - ‘PKTMON_DROP_REASON’.
* DropLocation – Packet Drop location as mentioned int - ‘PKTMON_DROP_LOCATION’
* Processor – Processor Number when the packet was reported. 
* TimeStamp – Timestamp when the packet was reported. This is retrieved using ‘KeQuerySystemTime’.

#### PKTMON_DIRECTION_TAG

```cpp
typedef enum PKTMON_DIRECTION_TAG
{
    PktMonDirTag_Unspecified = 0,
    PktMonDirTag_In,
    PktMonDirTag_Out,
    PktMonDirTag_Rx,
    PktMonDirTag_Tx,
    PktMonDirTag_Ingress,
    PktMonDirTag_Egress
} PKTMON_DIRECTION_TAG;
* PktMonDirTag_In/PktMonDirTag_Rx/ PktMonDirTag_Ingress – These all represent Receiving path of packet. 
  * PktMonDirTag_In – Reported by a upper/lower Edge of a component.  Each component registers its lower or/and upper edge. 
  * PktMonDirTag_Rx – Reported by a Network Interface.
  * PktMonDirTag_Ingress  - Reported by VmSwitch.
* PktMonDirTag_Out/ PktMonDirTag_Tx/ PktMonDirTag_Egress – They represent Sending path of packet. 
  * PktMonDirTag_out – Reported by a upper/lower Edge of a component.  
  * PktMonDirTag_Tx – Reported by a Network Interface.
  * PktMonDirTag_Egress  - Reported by VmSwitch.
```

#### PKTMON_PACKET_TYPE

```cpp
typedef enum _PKTMON_PACKET_TYPE
{
    PktMonPayload_Unknown,
    PktMonPayload_Ethernet,
    PktMonPayload_WiFi,
    PktMonPayload_IP,
    PktMonPayload_HTTP,
    PktMonPayload_TCP,
    PktMonPayload_UDP,
    PktMonPayload_ARP,
    PktMonPayload_ICMP,
    PktMonPayload_ESP,
    PktMonPayload_AH,
    PktMonPayload_L4Payload,
} PKTMON_PACKET_TYPE;
```

Only possible values for Packet Type are as below:
* PktMonPayload_IP – Packet is an IP packet which means the first byte of payload points to the start of an IP header. 
* PktMonPayload_Ethernet – Packet is an Ethernet Packet i.e. the first byte of the packet payload points to Ethernet Header. 
* PktMonPayload_WiFi - Packet is a Wifi Packet i.e. the first byte of the packet payload points to Wifi Header.
* PktMonPayload_HTTP – Packet is a HTTP payload type. First Byte would point to HTTP header.
* PktMonPayload_TCP – Packet is a TCP payload type i.e. the first byte of the packet payload points to TCP Header.
* PktMonPayload_UDP - Packet is a UDP payload type i.e. the first byte of the packet payload points to UDP Header.
* PktMonPayload_ARP - Packet is an ARP payload type i.e. the first byte of the packet payload points to ARP Header.
* PktMonPayload_ICMP - Packet is an ICMP payload type i.e. the first byte of the packet payload points to ICMP Header.
* PktMonPayload_ESP - Packet is an ESP payload type i.e. the first byte of the packet payload points to ESP Header.
* PktMonPayload_AH - Packet is an AH payload type i.e. the first byte of the packet payload points to AH Header.
* PktMonPayload_ L4Payload – Payload type here is any of the transport layer type i.e. the first byte of the packet payload could point to either a TCP header or a UDP header. 

#### PKTMON_DROP_LOCATION

```cpp
typedef enum _PKTMON_DROP_LOCATION
{
    //
    // NDIS drop locations
    //
    PMLOC_NDIS_FAKE_FILTER_SEND                     = 0xE0001001,
    PMLOC_NDIS_FAKE_FILTER_RECEIVE                  = 0xE0001002,
    PMLOC_NDIS_NEXT_RECEIVE                         = 0xE0001003,
    PMLOC_NDIS_NEXT_SEND                            = 0xE0001004,
    PMLOC_NDIS_M_FAKE_SEND                          = 0xE0001005,
    PMLOC_NDIS_SORT_NBL                             = 0xE0001006,
    PMLOC_NDIS_M_DISPATCH_RECEIVE                   = 0xE0001007,
    PMLOC_NDIS_M_DUMMY_RECEIVE                      = 0xE0001008,
    PMLOC_NDIS_POWER_RESUME                         = 0xE0001009,
    PMLOC_NDIS_SS_RESUME                            = 0xE000100A,
    PMLOC_NDIS_WDM_SET_BUSY                         = 0xE000100B,
    PMLOC_NDIS_WDF_SET_BUSY                         = 0xE000100C,
 
    //
    // VMSwitch drop locations
    //
    PMLOC_VMS_EXT_FILTER_DEST_PROC1                 = 0xE0002001,
    PMLOC_VMS_EXT_FILTER_DEST_PROC2                 = 0xE0002002,
    PMLOC_VMS_EXT_MP_SEND_NBL1                      = 0xE0002003,
    PMLOC_VMS_EXT_MP_SEND_NBL2                      = 0xE0002004,
    PMLOC_VMS_EXT_MP_SEND_NBL3                      = 0xE0002005,
    PMLOC_VMS_EXT_PT_ROUTE_NBL_BW                   = 0xE0002006,
    PMLOC_VMS_EXT_PT_ROUTE_NBL1                     = 0xE0002007,
    PMLOC_VMS_EXT_PT_ROUTE_NBL2                     = 0xE0002008,
    PMLOC_VMS_EXT_PT_ROUTE_NBL3                     = 0xE0002009,
    PMLOC_VMS_EXT_PT_ROUTE_NBL4                     = 0xE000200A,
    PMLOC_VMS_EXT_PT_ROUTE_NBL5                     = 0xE000200B,
    PMLOC_VMS_EXT_PT_ROUTE_NBL6                     = 0xE000200C,
    PMLOC_VMS_PT_NIC_RCV_NBL1                       = 0xE000200D,
    PMLOC_VMS_PT_NIC_RCV_NBL2                       = 0xE000200E,
    PMLOC_VMS_PT_NIC_IMM_SEND1                      = 0xE000200F,
    PMLOC_VMS_PT_NIC_IMM_SEND2                      = 0xE0002010,
    PMLOC_VMS_PT_NIC_IMM_SEND3                      = 0xE0002011,
    PMLOC_VMS_PT_NIC_IMM_SEND4                      = 0xE0002012,
    PMLOC_VMS_SC_QOS_APPLY_RES                      = 0xE0002013,
    PMLOC_VMS_ROUTER_FWD_PKT1                       = 0xE0002014,
    PMLOC_VMS_ROUTER_FWD_PKT2                       = 0xE0002015,
    PMLOC_VMS_ROUTER_FWD_PKT3                       = 0xE0002016,
    PMLOC_VMS_ROUTER_FWD_PKT4                       = 0xE0002017,
    PMLOC_VMS_ROUTER_FWD_PKT5                       = 0xE0002018,
    PMLOC_VMS_ROUTER_FWD_PKT6                       = 0xE0002019,
    PMLOC_VMS_ROUTER_FWD_PKT7                       = 0xE000201A,
    PMLOC_VMS_ROUTER_SRC_PROC1                      = 0xE000201B,
    PMLOC_VMS_ROUTER_SRC_PROC2                      = 0xE000201C,
    PMLOC_VMS_ROUTER_DST_PROC1                      = 0xE000201D,
    PMLOC_VMS_ROUTER_DST_PROC2                      = 0xE000201E,
    PMLOC_VMS_ROUTER_DST_PROC3                      = 0xE000201F,
    PMLOC_VMS_ROUTER_DST_PROC4                      = 0xE0002020,
    PMLOC_VMS_LBFO_SEND_INTERN                      = 0xE0002021,
    PMLOC_VMS_VM_NIC_PVT_PKT_FWD                    = 0xE0002022,
    PMLOC_VMS_SC_QOS_FLUSH_DELAY                    = 0xE0002023,
    PMLOC_VMS_SC_QOS_TIMEOUT                        = 0xE0002024,
    PMLOC_VMS_SC_QOS_UPDATE_FLOW                    = 0xE0002025,
    PMLOC_VMS_SC_QOS_SEND_NBL                       = 0xE0002026,
    PMLOC_VMS_DIO_NIC_PVT_FWD1                      = 0xE0002027,
    PMLOC_VMS_DIO_NIC_PVT_FWD2                      = 0xE0002028,
    PMLOC_VMS_DIO_NIC_PVT_FWD3                      = 0xE0002029,
    PMLOC_VMS_DIO_NIC_PVT_FWD4                      = 0xE000202A,
    PMLOC_VMS_DIO_NIC_PVT_FWD5                      = 0xE000202B,
    PMLOC_VMS_EXT_FLTR_INGRESS                      = 0xE000202C,
    PMLOC_VMS_EXT_FLTR_SRC_PROC                     = 0xE000202D,
    PMLOC_VMS_EXT_FLTR_DST_PROC1                    = 0xE000202E,
    PMLOC_VMS_EXT_FLTR_DST_PROC2                    = 0xE000202F,
    PMLOC_VMS_EXT_MP_SEND                           = 0xE0002030,
    PMLOC_VMS_EXT_PT_ROUTE                          = 0xE0002031,
    PMLOC_VMS_EXT_PT_RCV                            = 0xE0002032,
    PMLOC_VMS_MP_NIC_SEND1                          = 0xE0002033,
    PMLOC_VMS_MP_NIC_SEND2                          = 0xE0002034,
    PMLOC_VMS_MP_NIC_SEND3                          = 0xE0002035,
    PMLOC_VMS_MP_NIC_PVT_FWD1                       = 0xE0002036,
    PMLOC_VMS_MP_NIC_PVT_FWD2                       = 0xE0002037,
    PMLOC_VMS_MP_NIC_PVT_FWD3                       = 0xE0002038,
    PMLOC_VMS_MP_NIC_PVT_FWD4                       = 0xE0002039,
    PMLOC_VMS_MP_NIC_PVT_FWD5                       = 0xE000203A,
    PMLOC_VMS_MP_NIC_PVT_FWD6                       = 0xE000203B,
    PMLOC_VMS_HLP_DEST_GROUP                        = 0xE000203C,
    PMLOC_VMS_PT_NIC_RCV1                           = 0xE000203D,
    PMLOC_VMS_PT_NIC_RCV2                           = 0xE000203E,
    PMLOC_VMS_PT_NIC_RCV3                           = 0xE000203F,
    PMLOC_VMS_PT_NIC_RCV4                           = 0xE0002040,
    PMLOC_VMS_PT_NIC_RCV5                           = 0xE0002041,
    PMLOC_VMS_PT_NIC_RCV6                           = 0xE0002042,
    PMLOC_VMS_PT_NIC_RCV7                           = 0xE0002043,
    PMLOC_VMS_PT_NIC_RCV8                           = 0xE0002044,
    PMLOC_VMS_PT_NIC_FWD1                           = 0xE0002045,
    PMLOC_VMS_PT_NIC_FWD2                           = 0xE0002046,
    PMLOC_VMS_PT_NIC_FWD3                           = 0xE0002047,
    PMLOC_VMS_PT_NIC_FWD4                           = 0xE0002048,
    PMLOC_VMS_PT_NIC_FWD5                           = 0xE0002049,
    PMLOC_VMS_IPSEC_OUT_PROC                        = 0xE000204A,
    PMLOC_VMS_IPSEC_IN_PROC                         = 0xE000204B,
    PMLOC_VMS_IPSEC_MULTI_DST                       = 0xE000204C,
    PMLOC_VMS_RESERVED_1                            = 0xE000204D,
    PMLOC_VMS_POLICY_ENFORCER                       = 0xE000204E,
    PMLOC_VMS_POLICY_APPLY1                         = 0xE000204F,
    PMLOC_VMS_POLICY_APPLY2                         = 0xE0002050,
    PMLOC_VMS_VM_NIC_FWD                            = 0xE0002051,
    PMLOC_VMS_VM_PM_PROC                            = 0xE0002052,
    PMLOC_VMS_POLICY_ENFORCER2                      = 0xE0002053,
    PMLOC_VMS_EXT_INGR_FLTR                         = 0xE0002054,
    PMLOC_VMS_EXT_EGR_FLTR                          = 0xE0002055,
    PMLOC_VMS_WNV_FRWD1                             = 0xE0002056,
    PMLOC_VMS_WNV_FRWD2                             = 0xE0002057,
    PMLOC_VMS_WNV_COMPLETE                          = 0xE0002058,
    PMLOC_VMS_RNDIS_DEV_INDIC1                      = 0xE0002059,
    PMLOC_VMS_RNDIS_DEV_INDIC2                      = 0xE000205A,
    PMLOC_VMS_RNDIS_DEV_INDIC3                      = 0xE000205B,
    PMLOC_VMS_RNDIS_DEV_INDIC4                      = 0xE000205C,
    PMLOC_VMS_RNDIS_DEV_INDIC5                      = 0xE000205D,
    PMLOC_VMS_RNDIS_DEV_INDIC6                      = 0xE000205E,
    PMLOC_VMS_RNDIS_DEV_INDIC7                      = 0xE000205F,
    PMLOC_VMS_RNDIS_DEV_INDIC8                      = 0xE0002060,
    PMLOC_VMS_RNDIS_DEV_INDIC9                      = 0xE0002061,
    PMLOC_VMS_RNDIS_DEV_INDIC10                     = 0xE0002062,
    PMLOC_VMS_RNDIS_DEV_INDIC11                     = 0xE0002063,
    PMLOC_VMS_DIO_NIC_DELIVER_PD                    = 0xE0002064,
    PMLOC_VMS_EXT_MP_DELIVER_PD_EGR                 = 0xE0002065,
    PMLOC_VMS_EXT_PT_DELIVER_PD_INGR                = 0xE0002066,
    PMLOC_VMS_EXT_PT_ROUTE_PD1                      = 0xE0002067,
    PMLOC_VMS_EXT_PT_ROUTE_PD2                      = 0xE0002068,
    PMLOC_VMS_EXT_PT_ROUTE_PD3                      = 0xE0002069,
    PMLOC_VMS_EXT_PT_ROUTE_PD4                      = 0xE000206A,
    PMLOC_VMS_EXT_PT_ROUTE_PD5                      = 0xE000206B,
    PMLOC_VMS_MP_NIC_DELIVER_PD1                    = 0xE000206C,
    PMLOC_VMS_MP_NIC_DELIVER_PD2                    = 0xE000206D,
    PMLOC_VMS_MP_NIC_DELIVER_PD3                    = 0xE000206E,
    PMLOC_VMS_PT_NIC_POST_PD_TX1                    = 0xE000206F,
    PMLOC_VMS_PT_NIC_POST_PD_TX2                    = 0xE0002070,
    PMLOC_VMS_VM_NIC_DELIVER_PD                     = 0xE0002071,
    PMLOC_VMS_VM_NIC_RNDIS_SEND                     = 0xE0002072,
    PMLOC_VMS_VM_NIC_DELIVER_PD1                    = 0xE0002073,
    PMLOC_VMS_VM_NIC_DELIVER_PD2                    = 0xE0002074,
    PMLOC_VMS_MP_NIC_SEND4                          = 0xE0002075,
    PMLOC_VMS_RNDIS_DEV_INDIC12                     = 0xE0002076,
    PMLOC_VMS_VM_NIC_DELIVER_NBL1                   = 0xE0002077,
    PMLOC_VMS_VM_NIC_DELIVER_NBL2                   = 0xE0002078,
 
    //
    // NetVsc drop locations
    //
    PMLOC_NETVSC_VF_SEND1                           = 0xE0003001,
    PMLOC_NETVSC_VF_SEND2                           = 0xE0003002,
    PMLOC_NETVSC_RECEIVE_MSG                        = 0xE0003003,
    PMLOC_NETVSC_MP_SEND                            = 0xE0003004,
    PMLOC_NETVSC_MULTI_SEND                         = 0xE0003005,
    PMLOC_NETVSC_RELEASE_NBL                        = 0xE0003006,
 
    //
    // Tcpip FL drop locations
    //
    PMLOC_TCPIP_FL_RCV_NON_PRE_VAL                  = 0xE0004001,
    PMLOC_TCPIP_FL_RCV_CALLOUT                      = 0xE0004002,
    PMLOC_TCPIP_FL_FAST_SEND                        = 0xE0004003,
    PMLOC_TCPIP_FL_SEND_PKT_HLP                     = 0xE0004004,
    PMLOC_TCPIP_FL_PARSE_PKT                        = 0xE0004005,
    PMLOC_TCPIP_FL_ACCEPT_PKT                       = 0xE0004006,
    PMLOC_TCPIP_FL_RCV_ARP                          = 0xE0004007,
    PMLOC_TCPIP_FL_SEND_ARP                         = 0xE0004008,
    PMLOC_TCPIP_FL_RCV_TEREDO                       = 0xE0004009,
    PMLOC_TCPIP_FL_SEND_TEREDO                      = 0xE000400A,
 
    //
    // TCPIP NL drop locations
    //
    PMLOC_TCPIP_NL_SEND_FWD                         = 0xE0004100,
    PMLOC_TCPIP_NL_SEND_FWD_ALLOWED                 = 0xE0004101,
    PMLOC_TCPIP_NL_SEND_FWD_INSPECT                 = 0xE0004102,
    PMLOC_TCPIP_NL_SEND_FWD_POST_INSPECT            = 0xE0004103,
    PMLOC_TCPIP_NL_SEND_HELPER                      = 0xE0004104,
    PMLOC_TCPIP_NL_RCV_V4_OPTS                      = 0xE0004105,
    PMLOC_TCPIP_NL_RCV_V4_VALIDATE1                 = 0xE0004106,
    PMLOC_TCPIP_NL_RCV_V4_VALIDATE2                 = 0xE0004107,
    PMLOC_TCPIP_NL_RCV_V4_VALIDATE3                 = 0xE0004108,
    PMLOC_TCPIP_NL_RCV_V4_VALIDATE4                 = 0xE0004109,
    PMLOC_TCPIP_NL_RCV_V4_VALIDATE5                 = 0xE000410A,
    PMLOC_TCPIP_NL_RCV_V4_VALIDATE6                 = 0xE000410B,
    PMLOC_TCPIP_NL_SEND_V4_FRAG1                    = 0xE000410C,
    PMLOC_TCPIP_NL_SEND_V4_FRAG2                    = 0xE000410D,
    PMLOC_TCPIP_NL_SEND_V4_FRAG3                    = 0xE000410E,
    PMLOC_TCPIP_NL_SEND_V4_FRAG4                    = 0xE000410F,
    PMLOC_TCPIP_NL_SEND_V4_FRAG_INSPECT             = 0xE0004110,
    PMLOC_TCPIP_NL_SEND_V4_FRAG_IPSEC               = 0xE0004111,
 
    PMLOC_TCPIP_NL_RCV_V6_OPTS1                     = 0xE0004112,
    PMLOC_TCPIP_NL_RCV_V6_OPTS2                     = 0xE0004113,
    PMLOC_TCPIP_NL_RCV_V6_OPTS3                     = 0xE0004114,
    PMLOC_TCPIP_NL_RCV_V6_OPTS4                     = 0xE0004115,
    PMLOC_TCPIP_NL_RCV_V6_OPTS5                     = 0xE0004116,
    PMLOC_TCPIP_NL_RCV_V6_OPTS6                     = 0xE0004117,
    PMLOC_TCPIP_NL_RCV_V6_OPTS7                     = 0xE0004118,
    PMLOC_TCPIP_NL_RCV_V6_OPTS8                     = 0xE0004119,
    PMLOC_TCPIP_NL_RCV_V6_OPTS9                     = 0xE000411A,
    PMLOC_TCPIP_NL_RCV_V6_OPTS10                    = 0xE000411B,
    PMLOC_TCPIP_NL_RCV_V6_OPTS11                    = 0xE000411C,
    PMLOC_TCPIP_NL_RCV_V6_OPTS12                    = 0xE000411D,
    PMLOC_TCPIP_NL_RCV_V6_OPTS13                    = 0xE000411E,
    PMLOC_TCPIP_NL_RCV_V6_OPTS14                    = 0xE000411F,
    PMLOC_TCPIP_NL_RCV_V6_VALIDATE1                 = 0xE0004120,
    PMLOC_TCPIP_NL_RCV_V6_VALIDATE2                 = 0xE0004121,
    PMLOC_TCPIP_NL_RCV_V6_VALIDATE3                 = 0xE0004122,
    PMLOC_TCPIP_NL_RCV_V6_VALIDATE4                 = 0xE0004123,
    PMLOC_TCPIP_NL_RCV_V6_VALIDATE5                 = 0xE0004124,
    PMLOC_TCPIP_NL_RCV_V6_VALIDATE6                 = 0xE0004125,
    PMLOC_TCPIP_NL_SEND_V6_FRAG1                    = 0xE0004126,
    PMLOC_TCPIP_NL_SEND_V6_FRAG2                    = 0xE0004127,
    PMLOC_TCPIP_NL_SEND_V6_FRAG3                    = 0xE0004128,
    PMLOC_TCPIP_NL_SEND_V6_FRAG4                    = 0xE0004129,
    PMLOC_TCPIP_NL_SEND_V6_FRAG5                    = 0xE000412A,
    PMLOC_TCPIP_NL_SEND_V6_FRAG6                    = 0xE000412B,
    PMLOC_TCPIP_NL_SEND_V6_FRAG_INSPECT             = 0xE000412C,
    PMLOC_TCPIP_NL_SEND_V6_FRAG_IPSEC               = 0xE000412D,
 
    PMLOC_TCPIP_NL_SEND_INJECT_FWD1                 = 0xE000412E,
    PMLOC_TCPIP_NL_SEND_INJECT_FWD2                 = 0xE000412F,
    PMLOC_TCPIP_NL_SEND_INJECT_FWD3                 = 0xE0004130,
    PMLOC_TCPIP_NL_RCV_ESP                          = 0xE0004131,
    PMLOC_TCPIP_NL_RCV_CLONE_FOR_RAW1               = 0xE0004132,
    PMLOC_TCPIP_NL_RCV_CLONE_FOR_RAW2               = 0xE0004133,
    PMLOC_TCPIP_NL_RCV_DELIVERED                    = 0xE0004134,
    PMLOC_TCPIP_NL_RCV_DISPATCH1                    = 0xE0004135,
    PMLOC_TCPIP_NL_RCV_DISPATCH2                    = 0xE0004136,
    PMLOC_TCPIP_NL_RCV_DISPATCH3                    = 0xE0004137,
    PMLOC_TCPIP_NL_RCV_DISPATCH4                    = 0xE0004138,
    PMLOC_TCPIP_NL_RCV_RECEIVE_PKTS                 = 0xE0004139,
    PMLOC_TCPIP_NL_SEND_NEIGHBOR_QUEUE1             = 0xE000413A,
    PMLOC_TCPIP_NL_SEND_NEIGHBOR_QUEUE2             = 0xE000413B,
    PMLOC_TCPIP_NL_SEND_NEIGHBOR_QUEUE3             = 0xE000413C,
    PMLOC_TCPIP_NL_SEND_LB_INSPECT                  = 0xE000413D,
    PMLOC_TCPIP_NL_SEND_LB_SPLIT1                   = 0xE000413E,
    PMLOC_TCPIP_NL_SEND_LB_SPLIT2                   = 0xE000413F,
    PMLOC_TCPIP_NL_RCV_FWD_MCAST1                   = 0xE0004140,
    PMLOC_TCPIP_NL_RCV_FWD_MCAST2                   = 0xE0004141,
    PMLOC_TCPIP_NL_RCV_FWD_MCAST3                   = 0xE0004142,
    PMLOC_TCPIP_NL_RCV_FWD_MCAST4                   = 0xE0004143,
    PMLOC_TCPIP_NL_RCV_FWD_MCAST5                   = 0xE0004144,
    PMLOC_TCPIP_NL_RCV_FWD_MCAST6                   = 0xE0004145,
    PMLOC_TCPIP_NL_RCV_FWD_MCAST7                   = 0xE0004146,
    PMLOC_TCPIP_NL_RCV_FWD_MCAST8                   = 0xE0004147,
    PMLOC_TCPIP_NL_RCV_FWD_MCAST9                   = 0xE0004148,
    PMLOC_TCPIP_NL_RCV_FWD_MCAST10                  = 0xE0004149,
    PMLOC_TCPIP_NL_SEND_FWD_MCAST1                  = 0xE000414A,
    PMLOC_TCPIP_NL_SEND_FWD_MCAST2                  = 0xE000414B,
    PMLOC_TCPIP_NL_SEND_FWD_MCAST3                  = 0xE000414C,
    PMLOC_TCPIP_NL_RCV_IPSNPI_CLIENT_DROP           = 0xE000414D,
    PMLOC_TCPIP_NL_SEND_IPSNPI_L3_FWD               = 0xE000414E,
    PMLOC_TCPIP_NL_SEND_IPSNPI_L2_FWD1              = 0xE000414F,
    PMLOC_TCPIP_NL_SEND_IPSNPI_L2_FWD2              = 0xE0004150,
    PMLOC_TCPIP_NL_SEND_IPSNPI_L2_FWD3              = 0xE0004151,
    PMLOC_TCPIP_NL_SEND_IPSNPI_L2_FWD4              = 0xE0004152,
    PMLOC_TCPIP_NL_SEND_IPSNPI_L2_FWD5              = 0xE0004153,
    PMLOC_TCPIP_NL_RCV_IPSNPI_INJECT1               = 0xE0004154,
    PMLOC_TCPIP_NL_RCV_IPSNPI_INJECT2               = 0xE0004155,
    PMLOC_TCPIP_NL_RCV_IPSNPI_INJECT3               = 0xE0004156,
    PMLOC_TCPIP_NL_RCV_IPSNPI_INJECT4               = 0xE0004157,
    PMLOC_TCPIP_NL_SEND_PACKETIZE1                  = 0xE0004158,
    PMLOC_TCPIP_NL_SEND_PACKETIZE2                  = 0xE0004159,
    PMLOC_TCPIP_NL_SEND_PACKETIZE3                  = 0xE000415A,
    PMLOC_TCPIP_NL_SEND_PACKETIZE4                  = 0xE000415B,
    PMLOC_TCPIP_NL_SEND_PACKETIZE5                  = 0xE000415C,
    PMLOC_TCPIP_NL_SEND_PACKETIZE6                  = 0xE000415D,
    PMLOC_TCPIP_NL_SEND_PACKETIZE7                  = 0xE000415E,
    PMLOC_TCPIP_NL_SEND_PACKETIZE8                  = 0xE000415F,
    PMLOC_TCPIP_NL_SEND_COMMON1                     = 0xE0004160,
    PMLOC_TCPIP_NL_SEND_COMMON2                     = 0xE0004161,
    PMLOC_TCPIP_NL_SEND_COMMON3                     = 0xE0004162,
    PMLOC_TCPIP_NL_SEND_COMMON4                     = 0xE0004163,
    PMLOC_TCPIP_NL_SEND_COMMON5                     = 0xE0004164,
    PMLOC_TCPIP_NL_SEND_COMMON6                     = 0xE0004165,
    PMLOC_TCPIP_NL_SEND_COMMON7                     = 0xE0004166,
    PMLOC_TCPIP_NL_SEND_COMMON8                     = 0xE0004167,
    PMLOC_TCPIP_NL_SEND_COMMON9                     = 0xE0004168,
    PMLOC_TCPIP_NL_SEND_COMMON10                    = 0xE0004169,
    PMLOC_TCPIP_NL_SEND_COMMON11                    = 0xE000416A,
    PMLOC_TCPIP_NL_SEND_COMMON12                    = 0xE000416B,
    PMLOC_TCPIP_NL_SEND_COMMON13                    = 0xE000416C,
    PMLOC_TCPIP_NL_SEND_COMMON14                    = 0xE000416D,
    PMLOC_TCPIP_NL_SEND_COMMON15                    = 0xE000416E,
    PMLOC_TCPIP_NL_SEND_COMMON16                    = 0xE000416F,
    PMLOC_TCPIP_NL_SEND_COMMON_INSPECT              = 0xE0004170,
    PMLOC_TCPIP_NL_SEND_IPSNPI_COMPLETE             = 0xE0004171,
    PMLOC_TCPIP_NL_SEND_IPSNPI_CLIENT_L3_FWD        = 0xE0004172,
    PMLOC_TCPIP_NL_SEND_IPSNPI_CLIENT_L2_FWD        = 0xE0004173,
    PMLOC_TCPIP_NL_SEND_IPSNPI_CLIENT_INJECT        = 0xE0004174,
 
    PMLOC_TCPIP_NL_RCV_V4_ICMP_ECHO_REQUEST         = 0xE0004175,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REPLY1         = 0xE0004176,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REPLY2         = 0xE0004177,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REPLY3         = 0xE0004178,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REPLY4         = 0xE0004179,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REPLY5         = 0xE000417A,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST1       = 0xE000417B,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST2       = 0xE000417C,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST3       = 0xE000417D,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST4       = 0xE000417E,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST5       = 0xE000417F,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST6       = 0xE0004180,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST7       = 0xE0004181,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST8       = 0xE0004182,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST9       = 0xE0004183,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST10      = 0xE0004184,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST11      = 0xE0004185,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST12      = 0xE0004186,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST13      = 0xE0004187,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST14      = 0xE0004188,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST15      = 0xE0004189,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST16      = 0xE000418A,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST17      = 0xE000418B,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST18      = 0xE000418C,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST19      = 0xE000418D,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST20      = 0xE000418E,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST21      = 0xE000418F,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ECHO_REQUEST22      = 0xE0004190,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_ECHO_REPLY           = 0xE0004191,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_TIMESTAMP1           = 0xE0004192,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_TIMESTAMP2           = 0xE0004193,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_TIMESTAMP3           = 0xE0004194,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_TIMESTAMP4           = 0xE0004195,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_ADDRMASK             = 0xE0004196,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_ADDRMASK            = 0xE0004197,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_ERROR                = 0xE0004198,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RECEIVE              = 0xE0004199,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RECEIVE_CTRL         = 0xE000419A,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_RS                  = 0xE000419B,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RA1                  = 0xE000419C,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RA2                  = 0xE000419D,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RA3                  = 0xE000419E,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RA4                  = 0xE000419F,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RA5                  = 0xE00041A0,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RS1                  = 0xE00041A1,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RS2                  = 0xE00041A2,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RS3                  = 0xE00041A3,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RS4                  = 0xE00041A4,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_RS5                  = 0xE00041A5,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_RA1                 = 0xE00041A6,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_RA2                 = 0xE00041A7,
    PMLOC_TCPIP_NL_SEND_V4_ICMP_RA3                 = 0xE00041A8,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_REDIRECT1            = 0xE00041A9,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_REDIRECT2            = 0xE00041AA,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_REDIRECT3            = 0xE00041AB,
    PMLOC_TCPIP_NL_RCV_V4_ICMP_REDIRECT4            = 0xE00041AC,
 
    PMLOC_TCPIP_NL_RCV_V6_ICMP_ECHO_REQUEST         = 0xE00041AD,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REPLY1         = 0xE00041AE,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REPLY2         = 0xE00041AF,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST1       = 0xE00041B0,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST2       = 0xE00041B1,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST3       = 0xE00041B2,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST4       = 0xE00041B3,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST5       = 0xE00041B4,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST6       = 0xE00041B5,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST7       = 0xE00041B6,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST8       = 0xE00041B7,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST9       = 0xE00041B8,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST10      = 0xE00041B9,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST11      = 0xE00041BA,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST12      = 0xE00041BB,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST13      = 0xE00041BC,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST14      = 0xE00041BD,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST15      = 0xE00041BE,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST16      = 0xE00041BF,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST17      = 0xE00041C0,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST18      = 0xE00041C1,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST19      = 0xE00041C2,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST20      = 0xE00041C3,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_ECHO_REQUEST21      = 0xE00041C4,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_ECHO_REPLY           = 0xE00041C5,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_ERROR                = 0xE00041C6,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RECEIVE              = 0xE00041C7,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RECEIVE_CTRL         = 0xE00041C8,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NS1                  = 0xE00041C9,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NS2                  = 0xE00041CA,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NS3                  = 0xE00041CB,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NS4                  = 0xE00041CC,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NS5                  = 0xE00041CD,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NS6                  = 0xE00041CE,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NS7                  = 0xE00041CF,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NS8                  = 0xE00041D0,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NA1                  = 0xE00041D1,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NA2                  = 0xE00041D2,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NA3                  = 0xE00041D3,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NA4                  = 0xE00041D4,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NA5                  = 0xE00041D5,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_NA6                  = 0xE00041D6,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_NS                  = 0xE00041D7,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_NA                  = 0xE00041D8,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_RS                  = 0xE00041D9,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA1                  = 0xE00041DA,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA2                  = 0xE00041DB,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA3                  = 0xE00041DC,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA4                  = 0xE00041DD,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA5                  = 0xE00041DE,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA6                  = 0xE00041DF,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA7                  = 0xE00041E0,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA8                  = 0xE00041E1,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA9                  = 0xE00041E2,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA10                 = 0xE00041E3,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA11                 = 0xE00041E4,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA12                 = 0xE00041E5,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA13                 = 0xE00041E6,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA14                 = 0xE00041E7,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RA15                 = 0xE00041E8,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_RS                   = 0xE00041E9,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_RA                  = 0xE00041EA,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_REDIRECT1            = 0xE00041EB,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_REDIRECT2            = 0xE00041EC,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_REDIRECT3            = 0xE00041ED,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_REDIRECT4            = 0xE00041EE,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_REDIRECT5            = 0xE00041EF,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_REDIRECT6            = 0xE00041F0,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_REDIRECT7            = 0xE00041F1,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_REDIRECT8            = 0xE00041F2,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_REDIRECT9            = 0xE00041F3,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_REDIRECT            = 0xE00041F4,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_QUERY1           = 0xE00042F5,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_QUERY2           = 0xE00042F6,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_QUERY3           = 0xE00042F7,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_QUERY4           = 0xE00042F8,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_QUERY5           = 0xE00042F9,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_QUERY6           = 0xE00042FA,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_QUERY7           = 0xE00042FB,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_REPORT1          = 0xE00042FC,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_REPORT2          = 0xE00042FD,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_REPORT3          = 0xE00042FE,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_REPORT4          = 0xE00042FF,
    PMLOC_TCPIP_NL_RCV_V6_ICMP_MLD_REPORT5          = 0xE0004230,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_MLD_REPORT1         = 0xE0004231,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_MLD_REPORT2         = 0xE0004232,
    PMLOC_TCPIP_NL_SEND_V6_ICMP_MLD_REPORT3         = 0xE0004233,
 
    PMLOC_TCPIP_NL_SEND_ICMP_ERROR1                 = 0xE0004234,
    PMLOC_TCPIP_NL_SEND_ICMP_ERROR2                 = 0xE0004235,
    PMLOC_TCPIP_NL_SEND_ICMP_ERROR3                 = 0xE0004236,
    PMLOC_TCPIP_NL_SEND_ICMP_ERROR4                 = 0xE0004237,
    PMLOC_TCPIP_NL_SEND_ICMP_ERROR5                 = 0xE0004238,
    PMLOC_TCPIP_NL_SEND_ICMP_ERROR6                 = 0xE0004239,
    PMLOC_TCPIP_NL_SEND_ICMP_ERROR7                 = 0xE000423A,
    PMLOC_TCPIP_NL_SEND_ICMP_CTRL                   = 0xE000423B,
    PMLOC_TCPIP_NL_SEND_ICMP_REDIRECT1              = 0xE000423C,
    PMLOC_TCPIP_NL_SEND_ICMP_REDIRECT2              = 0xE000423D,
    PMLOC_TCPIP_NL_SEND_ICMP_REDIRECT3              = 0xE000423E,
 
    PMLOC_TCPIP_NL_RCV_ARP_RESPONSE1                = 0xE000423F,
    PMLOC_TCPIP_NL_RCV_ARP_RESPONSE2                = 0xE0004240,
    PMLOC_TCPIP_NL_RCV_ARP_REQUEST                  = 0xE0004241,
 
    //
    // TCPIP TL drop locations
    //
    PMLOC_TCPIP_TL_RCV_TCP_MATCH                    = 0xE0004500,
    PMLOC_TCPIP_TL_RCV_TCP_LISTENER                 = 0xE0004501,
    PMLOC_TCPIP_TL_RCV_TCP_LISTENER_INSPECT1        = 0xE0004502,
    PMLOC_TCPIP_TL_RCV_TCP_LISTENER_INSPECT2        = 0xE0004503,
    PMLOC_TCPIP_TL_RCV_TCP_SYN_RECEIVE_INSPECT      = 0xE0004504,
    PMLOC_TCPIP_TL_RCV_TCP_INSPECT                  = 0xE0004505,
    PMLOC_TCPIP_TL_RCV_TCP_RECEIVE                  = 0xE0004506,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL1                 = 0xE0004507,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL2                 = 0xE0004508,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL3                 = 0xE0004509,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL4                 = 0xE000450A,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL5                 = 0xE000450B,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL6                 = 0xE000450C, // Free for use.
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL7                 = 0xE000450D,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL8                 = 0xE000450E,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL9                 = 0xE000450F,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL10                = 0xE0004510,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL11                = 0xE0004511,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL12                = 0xE0004512,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL13                = 0xE0004513,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL14                = 0xE0004514,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL15                = 0xE0004515,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL16                = 0xE0004516,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL17                = 0xE0004517,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL18                = 0xE0004518,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL19                = 0xE0004519,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL20                = 0xE000451A,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL21                = 0xE000451B, // Free for use.
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL22                = 0xE000451C,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL23                = 0xE000451D, // Free for use.
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL24                = 0xE000451E,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL25                = 0xE000451F,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL26                = 0xE0004520,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL27                = 0xE0004521, // Free for use.
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL28                = 0xE0004522,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL29                = 0xE0004523,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL30                = 0xE0004524,
    PMLOC_TCPIP_TL_RCV_TCP_CAREFUL31                = 0xE0004525, // Free for use.
    PMLOC_TCPIP_TL_RCV_TCP_TIME_WAIT_INSPECT        = 0xE0004526,
    PMLOC_TCPIP_TL_RCV_TCP_TIME_WAIT1               = 0xE0004527,
    PMLOC_TCPIP_TL_RCV_TCP_TIME_WAIT2               = 0xE0004528,
    PMLOC_TCPIP_TL_RCV_TCP_TIME_WAIT3               = 0xE0004529,
    PMLOC_TCPIP_TL_RCV_TCP_TIME_WAIT4               = 0xE000452A,
    PMLOC_TCPIP_TL_RCV_TCP_TIME_WAIT5               = 0xE000452B,
    PMLOC_TCPIP_TL_RCV_TCP_VALIDATE1                = 0xE000452C,
    PMLOC_TCPIP_TL_RCV_TCP_VALIDATE2                = 0xE000452D,
    PMLOC_TCPIP_TL_RCV_TCP_VALIDATE3                = 0xE000452E,
    PMLOC_TCPIP_TL_RCV_TCP_VALIDATE4                = 0xE000452F,
    PMLOC_TCPIP_TL_RCV_TCP_VALIDATE5                = 0xE0004530,
 
    PMLOC_TCPIP_TL_RCV_UDP_INSPECT                  = 0xE0004600,
    PMLOC_TCPIP_TL_RCV_UDP_DELIVER1                 = 0xE0004601,
    PMLOC_TCPIP_TL_RCV_UDP_DELIVER2                 = 0xE0004602,
    PMLOC_TCPIP_TL_RCV_UDP_DELIVER3                 = 0xE0004603,
    PMLOC_TCPIP_TL_RCV_UDP_DELIVER4                 = 0xE0004604,
    PMLOC_TCPIP_TL_RCV_UDP_BEGIN_DELIVERY1          = 0xE0004605,
    PMLOC_TCPIP_TL_RCV_UDP_BEGIN_DELIVERY2          = 0xE0004606,
    PMLOC_TCPIP_TL_RCV_UDP_BEGIN_DELIVERY3          = 0xE0004607,
    PMLOC_TCPIP_TL_RCV_UDP_BEGIN_DELIVERY4          = 0xE0004608,
    PMLOC_TCPIP_TL_RCV_UDP_BEGIN_DELIVERY5          = 0xE0004609,
    PMLOC_TCPIP_TL_RCV_UDP_RECEIVE1                 = 0xE000460A,
    PMLOC_TCPIP_TL_RCV_UDP_RECEIVE2                 = 0xE000460B,
    PMLOC_TCPIP_TL_RCV_UDP_RECEIVE3                 = 0xE000460C,
 
    PMLOC_TCPIP_TL_RCV_RAW_DELIVER1                 = 0xE0004700,
    PMLOC_TCPIP_TL_RCV_RAW_DELIVER2                 = 0xE0004701,
    PMLOC_TCPIP_TL_RCV_RAW_DELIVER3                 = 0xE0004702,
    PMLOC_TCPIP_TL_RCV_RAW_DELIVER4                 = 0xE0004703,
    PMLOC_TCPIP_TL_RCV_RAW_RECEIVE                  = 0xE0004704,
 
    PMLOC_TCPIP_MAX                                 = 0xE0004FFF,
 
    //
    // Http drop locations
    //
    PMLOC_HTTP_WSK_RECEIVE                          = 0xE0005001,
    PMLOC_HTTP_WSK_SEND                             = 0xE0005002,
 
    //
    // VFP drop locations
    //
    PMLOC_VFP_UNKNOWN                                             = 0xE0006000,
    PMLOC_VFP_VALIDATE_MAPPING_OR_PEND_PKT_MAP_NULL               = 0xE0006001,
    PMLOC_VFP_CREATE_PEND_MAPPINGMAPNULL                          = 0xE0006002,
    PMLOC_VFP_DUP_PKT_NO_PKT_DUP                                  = 0xE0006003,
    PMLOC_VFP_DUP_PKT_PEND_PKT_LIMITEXCEEDED                      = 0xE0006004,
    PMLOC_VFP_DUP_NETBUFFERLIST_NB_LSGTMAX_PKT                    = 0xE0006005,
    PMLOC_VFP_DUP_PDBUFFER_NB_LSGTMAX_PKT                         = 0xE0006006,
    PMLOC_VFP_PEND_ORIG_PKT_NO_PKT_DUP                            = 0xE0006007,
    PMLOC_VFP_PEND_ORIG_PKT_PEND_PKT_LIMITEXCEEDED                = 0xE0006008,
    PMLOC_VFP_PEND_ORIG_NETBUFFERLIST_NB_LSGTMAX_PKT              = 0xE0006009,
    PMLOC_VFP_DUP_NETBUFFERLIST_RET_STATUS_PEND                   = 0xE0006010,
    PMLOC_VFP_PARSE_HDR_NB_PROT_TCP_FRAG_PKT                      = 0xE0006011,
    PMLOC_VFP_PARSE_HDR_NB_PROT_TCP_MIN_HDR_SZLIMIT               = 0xE0006012,
    PMLOC_VFP_PARSE_HDR_NB_PROT_TCP_MIN_HDR_NULL                  = 0xE0006013,
    PMLOC_VFP_PARSE_HDR_NB_PROT_TCP_HDR_SZLIMIT                   = 0xE0006014,
    PMLOC_VFP_PARSE_HDR_NB_PROT_TCP_FULL_HDR_NULL                 = 0xE0006015,
    PMLOC_VFP_PARSE_HDR_NB_PROT_UDP_FRAG_PKT                      = 0xE0006016,
    PMLOC_VFP_PARSE_HDR_NB_PROT_UDP_MIN_HDR_SZLIMIT               = 0xE0006017,
    PMLOC_VFP_PARSE_HDR_NB_PROT_UDP_MIN_HDR_NULL                  = 0xE0006018,
    PMLOC_VFP_PARSE_HDR_NB_PROT_UDP_FRAG_PKT_RDMA                 = 0xE0006019,
    PMLOC_VFP_PARSE_HDR_NB_PROT_UDP_HDR_SZLIMITRDMA               = 0xE0006020,
    PMLOC_VFP_PARSE_HDR_NB_PROT_UDP_FRAG_PKT_VXLAN                = 0xE0006021,
    PMLOC_VFP_PARSE_HDR_NB_PROT_UDP_HDR_SZLIMITVXLAN              = 0xE0006022,
    PMLOC_VFP_PARSE_HDR_NB_PROT_UDP_FULL_HDR_NULLVXLAN            = 0xE0006023,
    PMLOC_VFP_PARSE_HDR_NB_PROT_UDP_HDR_INVALID                   = 0xE0006024,
    PMLOC_VFP_PARSE_HDR_NB_PROT_UDP_INCONSISTENT_ETH_TYPE         = 0xE0006025,
    PMLOC_VFP_PARSE_HDR_NB_PROT_RESERVED                          = 0xE0006026,
    PMLOC_VFP_PARSE_HDR_NB_PROT_ICMP_FRAG_PKT                     = 0xE0006027,
    PMLOC_VFP_PARSE_HDR_NB_PROT_ICMP_MIN_HDR_SZLIMIT              = 0xE0006028,
    PMLOC_VFP_PARSE_HDR_NB_PROT_ICMP_MIN_HDR_NULL                 = 0xE0006029,
    PMLOC_VFP_PARSE_HDR_NB_PROT_ICMP_HDR_SZLIMIT                  = 0xE0006030,
    PMLOC_VFP_PARSE_HDR_NB_PROT_ICMP_FULL_HDR_NULL                = 0xE0006031,
    PMLOC_VFP_PARSE_HDR_NB_PROT_GRE_FRAG_PKT                      = 0xE0006032,
    PMLOC_VFP_PARSE_HDR_NB_PROT_GRE_MIN_HDR_SZLIMIT               = 0xE0006033,
    PMLOC_VFP_PARSE_HDR_NB_PROT_GRE_MIN_HDR_NULL                  = 0xE0006034,
    PMLOC_VFP_PARSE_HDR_NB_PROT_GRE_UNSUP_PORT_EDROUTING          = 0xE0006035,
    PMLOC_VFP_PARSE_HDR_NB_PROT_GRE_HDR_SZLIMIT                   = 0xE0006036,
    PMLOC_VFP_PARSE_HDR_NB_PROT_GRE_FULL_HDR_NULL                 = 0xE0006037,
    PMLOC_VFP_PARSE_HDR_NB_PROT_IPV6_FRAG_PKT                     = 0xE0006038,
    PMLOC_VFP_PARSE_HDR_NB_PROT_IPV6_UNPARSED_HDR                 = 0xE0006039,
    PMLOC_VFP_PARSE_HDR_NB_NO_PROT_PA_PKT                         = 0xE0006040,
    PMLOC_VFP_PARSE_HDR_NB_NO_PROT                                = 0xE0006041,
    PMLOC_VFP_PARSE_HDR_NB_PROT_ESP_FRAG_PKT                      = 0xE0006042,
    PMLOC_VFP_PARSE_HDR_NB_PROT_ESP_MIN_HDR_SZLIMIT               = 0xE0006043,
    PMLOC_VFP_PARSE_HDR_NB_PROT_ESP_MIN_HDR_NULL                  = 0xE0006044,
    PMLOC_VFP_PARSE_HDR_NB_UNSUPPORTED_PROT                       = 0xE0006045,
    PMLOC_VFP_EXTRACT_ETHERNET_HDR_NB_HDR_NULL                    = 0xE0006046,
    PMLOC_VFP_EXTRACT_ETHERNET_HDR_NB_HDR_SIZELIMIT               = 0xE0006047,
    PMLOC_VFP_PARSE_IP_HDR_NB_IPV4_MIN_HDR_SZLIMIT                = 0xE0006048,
    PMLOC_VFP_PARSE_IP_HDR_NB_IPV4_HDR_NULL                       = 0xE0006049,
    PMLOC_VFP_PARSE_IP_HDR_NB_IPV4_HDR_SZLIMIT                    = 0xE0006050,
    PMLOC_VFP_PARSE_IP_HDR_NB_IPV4_INVALID_PROT_VERSION           = 0xE0006051,
    PMLOC_VFP_PARSE_IP_HDR_NB_IPV4_FULL_HDR_NULL                  = 0xE0006052,
    PMLOC_VFP_PARSE_IP_HDR_NB_IPV6_MIN_HDR_SZLIMIT                = 0xE0006053,
    PMLOC_VFP_PARSE_IP_HDR_NB_IPV6_HDR_NULL                       = 0xE0006054,
    PMLOC_VFP_PARSE_IP_HDR_NB_IPV6_INVALID_PROT_VERSION           = 0xE0006055,
    PMLOC_VFP_PARSE_IP_HDR_NB_INVALID_PROT                        = 0xE0006056,
    PMLOC_VFP_GENERATE_UNIFIEDFLOW_IDFROM_PKT_ENCAP_HDR_INVALID   = 0xE0006057,
    PMLOC_VFP_GENERATE_UNIFIEDFLOW_IDFROM_PKT_INVALID             = 0xE0006058,
    PMLOC_VFP_DEFAULT_FWD_PKT_GFT_PORT_NULL                       = 0xE0006059,
    PMLOC_VFP_DEFAULT_FWD_PKT_NO_PORT_TOSEND                      = 0xE0006060,
    PMLOC_VFP_DEFAULT_FWD_PKT_NONIP                               = 0xE0006061,
    PMLOC_VFP_DEFAULT_FWD_PKT_UNICAST_PORT_NOTREADY               = 0xE0006062,
    PMLOC_VFP_DEFAULT_FWD_PKT_UNICAST_NO_DESTINATION              = 0xE0006063,
    PMLOC_VFP_PROCESS_OUTGOING_PKT_QUEUED                         = 0xE0006064,
    PMLOC_VFP_PROCESS_OUTGOING_PKT_MACGUARD                       = 0xE0006065,
    PMLOC_VFP_PROCESS_OUTGOING_PKT_BROADCAST_MACGUARD             = 0xE0006066,
    PMLOC_VFP_PROCESS_OUTGOING_PKT_INVALID_PKT                    = 0xE0006067,
    PMLOC_VFP_PROCESS_OUTGOING_PKT_INVALID_PKT_ARP                = 0xE0006068,
    PMLOC_VFP_PROCESS_OUTGOING_PKT_INTERCEPT_HDR_NULL             = 0xE0006069,
    PMLOC_VFP_PROCESS_OUTGOING_PKT_HDR_NULL                       = 0xE0006070,
    PMLOC_VFP_PROCESS_OUTGOING_PKT_TYPE_REQ_OR_NUD                = 0xE0006071,
    PMLOC_VFP_PROCESS_OUTGOING_PKT_ADDRESS_INFO_VIRTUALIZED       = 0xE0006072,
    PMLOC_VFP_PROCESS_OUTGOING_PKT_HDR_NOTNULL                    = 0xE0006073,
    PMLOC_VFP_PROCESS_OUTGOING_PKT_INTERCEPT_HDR_NOTNULL          = 0xE0006074,
    PMLOC_VFP_PROCESS_INCOMING_PKT_ETHER_HDR_NULL                 = 0xE0006075,
    PMLOC_VFP_PROCESS_INCOMING_PKT_ETHER_HDR_NULL_NONIP           = 0xE0006076,
    PMLOC_VFP_PROCESS_INCOMING_PKT_HDR_NOTNULL                    = 0xE0006077,
    PMLOC_VFP_PROCESS_INCOMING_PKT_ETHER_HDR_NOT_NULL_NONIP       = 0xE0006078,
    PMLOC_VFP_PROCESS_OUTGOING_ARP_INVALID_ARP_PKT                = 0xE0006079,
    PMLOC_VFP_PROCESS_OUTGOING_ARP_INVALID_HDR                    = 0xE0006080,
    PMLOC_VFP_PROCESS_OUTGOING_ARP_INVALID_ETHERNET_HDR           = 0xE0006081,
    PMLOC_VFP_PROCESS_OUTGOING_ARP_INVALID_IPADDRESS              = 0xE0006082,
    PMLOC_VFP_PROCESS_OUTGOING_ARP_PKT_LIMITER                    = 0xE0006083,
    PMLOC_VFP_RECEIVE_SINGLEDESTINATION_PORT_BLOCKED              = 0xE0006084,
    PMLOC_VFP_RECEIVE_SINGLEDESTINATION_NIC_SUSPENDED             = 0xE0006085,
    PMLOC_VFP_RECEIVE_MULTIPLEDESTINATION_PORT_BLOCKED            = 0xE0006086,
    PMLOC_VFP_RECEIVE_MULTIPLEDESTINATION_NIC_SUSPENDED           = 0xE0006087,
    PMLOC_VFP_SEND_NETBUFFERLISTS_PORT_BLOCKED                    = 0xE0006088,
    PMLOC_VFP_START_PROCESSING_PKT_NOT_PARSED                     = 0xE0006089,
    PMLOC_VFP_INTERCEPT_TRANSPORT_PROT_PKT_INTERCEPT              = 0xE0006090,
    PMLOC_VFP_VFP_PROCESS_INCOMING_ARP_INVALID_ARP_PKT            = 0xE0006091,
    PMLOC_VFP_VFP_PROCESS_INCOMING_ARP_HDR_EXTRACTION_FAIL        = 0xE0006092,
    PMLOC_VFP_VFP_PROCESS_INCOMING_ARP_INVALID_IPADDRESS          = 0xE0006093,
    PMLOC_VFP_VFP_PROCESS_INCOMING_ARP_NONUNICAST_RESPONSE        = 0xE0006094,
    PMLOC_VFP_PKTMON_SWITCH_CONTEXT_REG_DISABLED                  = 0xE0006095,
 
    //
    // Slbmux drop locations
    //
    PMLOC_SLBMUX_PACKET_PARSE_FAIL                                = 0xE0007001, 
    PMLOC_SLBMUX_ACT_TYPE_DROP                                    = 0xE0007002,
 
    //
    // Ipsec drop locations
    //
    PMLOC_IPSEC_ESP_INBOUND_INIT                                  = 0xE0008001,
    PMLOC_IPSEC_ESP_INBOUND_AUTH                                  = 0xE0008002,
    PMLOC_IPSEC_ESP_INBOUND_AUTH_COMPLETE                         = 0xE0008003,
    PMLOC_IPSEC_ESP_INBOUND_DECRYPT                               = 0xE0008004,
    PMLOC_IPSEC_ESP_INBOUND_DECRYPT_COMPLETE                      = 0xE0008005,
    PMLOC_IPSEC_ESP_OUTBOUND_INIT                                 = 0xE0008006,
    PMLOC_IPSEC_ESP_OUTBOUND_PROCESS                              = 0xE0008007,
    PMLOC_IPSEC_ESP_OUTBOUND_COMPLETE                             = 0xE0008008,
    PMLOC_IPSEC_TL_PACKET_INBOUND_PROCESSING                      = 0xE0008009,
    PMLOC_IPSEC_TL_PACKET_OUTBOUND_PROCESSING                     = 0xE000800A,
    PMLOC_IPSEC_GET_SESSION_INFO                                  = 0xE000800B,
    PMLOC_IPSEC_OUTBOUND_TUNNEL_CLASSIFY                          = 0xE000800C,
    PMLOC_IPSEC_INBOUND_TUNNEL_CLASSIFY                           = 0xE000800D,
    PMLOC_IPSEC_SEND_TUNNEL_DATAGRAM                              = 0xE000800E,
    PMLOC_IPSEC_ASYNC_PEND_COMPLETE                               = 0xE000800F,
 
    //
    // NetCx drop locations
    //
    PMLOC_NETCX_NETPACKET_LAYOUT_PARSE_FAIL                       = 0xE0009001,
    PMLOC_NETCX_SOFTWARE_CHECKSUM_FAILURE                         = 0xE0009002,
    PMLOC_NETCX_NIC_QUEUE_STOP                                    = 0xE0009003,
    PMLOC_NETCX_INVALID_NETBUFFER_LENGTH                          = 0xE0009004,
    PMLOC_NETCX_NBL_LSO_FAILURE                                   = 0xE0009005,
    PMLOC_NETCX_NBL_USO_FAILURE                                   = 0xE0009006,
    PMLOC_NETCX_BUFFER_BOUNCE_FAILURE                             = 0xE0009007,
 
} PKTMON_DROP_LOCATION;
```

#### PKTMON_DROP_REASON

```cpp
typedef enum _PKTMON_DROP_REASON
{
    //
    // Matching VMS_PACKET_DROP_REASON
    //
    PktMonDrop_Unknown                      = 0,
    PktMonDrop_InvalidData                  = 1,
    PktMonDrop_InvalidPacket                = 2,
    PktMonDrop_Resources                    = 3,
    PktMonDrop_NotReady                     = 4,
    PktMonDrop_Disconnected                 = 5,
    PktMonDrop_NotAccepted                  = 6,
    PktMonDrop_Busy                         = 7,
    PktMonDrop_Filtered                     = 8,
    PktMonDrop_FilteredVLAN                 = 9,
    PktMonDrop_UnauthorizedVLAN             = 10,
    PktMonDrop_UnauthorizedMAC              = 11,
    PktMonDrop_FailedSecurityPolicy         = 12,
    PktMonDrop_FailedPvlanSetting           = 13,
    PktMonDrop_Qos                          = 14,
    PktMonDrop_Ipsec                        = 15,
    PktMonDrop_MacSpoofing                  = 16,
    PktMonDrop_DhcpGuard                    = 17,
    PktMonDrop_RouterGuard                  = 18,
    PktMonDrop_BridgeReserved               = 19,
    PktMonDrop_VirtualSubnetId              = 20,
    PktMonDrop_RequiredExtensionMissing     = 21,
    PktMonDrop_InvalidConfig                = 22,
    PktMonDrop_MTUMismatch                  = 23,
    PktMonDrop_NativeFwdingReq              = 24,
    PktMonDrop_InvalidVlanFormat            = 25,
    PktMonDrop_InvalidDestMac               = 26,
    PktMonDrop_InvalidSourceMac             = 27,
    PktMonDrop_InvalidFirstNBTooSmall       = 28,
    PktMonDrop_Wnv                          = 29,
    PktMonDrop_StormLimit                   = 30,
    PktMonDrop_InjectedIcmp                 = 31,
    PktMonDrop_FailedDestinationListUpdate  = 32,
    PktMonDrop_NicDisabled                  = 33,
    PktMonDrop_FailedPacketFilter           = 34,
    PktMonDrop_SwitchDataFlowDisabled       = 35,
    PktMonDrop_FilteredIsolationUntagged    = 36,
    PktMonDrop_InvalidPDQueue               = 37,
    PktMonDrop_LowPower                     = 38,
 
    //
    // General errors
    //
    PktMonDrop_Pause                        = 201,
    PktMonDrop_Reset                        = 202,
    PktMonDrop_SendAborted                  = 203,
    PktMonDrop_ProtocolNotBound             = 204,
 
    //
    // NetVsc errors
    //
    PktMonDrop_MicroportError               = 401,
    PktMonDrop_VfNotReady                   = 402,
    PktMonDrop_MicroportNotReady            = 403,
    PktMonDrop_VMBusError                   = 404,
 
    //
    // Tcpip FL errors
    //
    PktMonDrop_FL_LoopbackPacket            = 601,
    PktMonDrop_FL_InvalidSnapHeader         = 602,
    PktMonDrop_FL_InvalidEthernetType       = 603,
    PktMonDrop_FL_InvalidPacketLength       = 604,
    PktMonDrop_FL_HeaderNotContiguous       = 605,
    PktMonDrop_FL_InvalidDestinationType    = 606,
    PktMonDrop_FL_InterfaceNotReady         = 607,
    PktMonDrop_FL_ProviderNotReady          = 608,
    PktMonDrop_FL_InvalidLsoInfo            = 609,
    PktMonDrop_FL_InvalidUsoInfo            = 610,
    PktMonDrop_FL_InvalidMedium             = 611,
    PktMonDrop_FL_InvalidArpHeader          = 612,
    PktMonDrop_FL_NoClientInterface         = 613,
 
    //
    // VFP errors
    //
    PktMonDrop_ArpGuard                     = 701,
    PktMonDrop_ArpLimiter                   = 702,
    PktMonDrop_DhcpLimiter                  = 703,
    PktMonDrop_BlockBroadcast               = 704,
    PktMonDrop_BlockNonIp                   = 705,
    PktMonDrop_ArpFilter                    = 706,
    PktMonDrop_Ipv4Guard                    = 707,
    PktMonDrop_Ipv6Guard                    = 708,
    PktMonDrop_MacGuard                     = 709,
    PktMonDrop_BroadcastNoDestinations      = 710,
    PktMonDrop_UnicastNoDestination         = 711,
    PktMonDrop_UnicastPortNotReady          = 712,
    PktMonDrop_SwitchCallbackFailed         = 713,
    PktMonDrop_Icmpv6Limiter                = 714,
    PktMonDrop_Intercept                    = 715,
    PktMonDrop_InterceptBlock               = 716,
    PktMonDrop_NDPGuard                     = 717,
    PktMonDrop_PortBlocked                  = 718,
    PktMonDrop_NicSuspended                 = 719,
 
    //
    // Http errors
    //
    PktMonDrop_Http_ReceiveSuppressed       = 801,
 
    //
    // Tcpip NL errors
    //
    PktMonDrop_NL_BadSourceAddress                          = 901,
    PktMonDrop_NL_NotLocallyDestined                        = 902,
    PktMonDrop_NL_ProtocolUnreachable                       = 903,
    PktMonDrop_NL_PortUnreachable                           = 904,
    PktMonDrop_NL_BadLength                                 = 905,
    PktMonDrop_NL_MalformedHeader                           = 906,
    PktMonDrop_NL_NoRoute                                   = 907,
    PktMonDrop_NL_BeyondScope                               = 908,
    PktMonDrop_NL_InspectionDrop                            = 909,
    PktMonDrop_NL_TooManyDecapsulations                     = 910,
    PktMonDrop_NL_AdministrativelyProhibited                = 911,
    PktMonDrop_NL_BadChecksum                               = 912,
    PktMonDrop_NL_ReceivePathMax                            = 913,
    PktMonDrop_NL_HopLimitExceeded                          = 914,
    PktMonDrop_NL_AddressUnreachable                        = 915,
    PktMonDrop_NL_RscPacket                                 = 916,
    PktMonDrop_NL_ForwardPathMax                            = 917,
    PktMonDrop_NL_ArbitrationUnhandled                      = 918,
    PktMonDrop_NL_InspectionAbsorb                          = 919,
    PktMonDrop_NL_DontFragmentMtuExceeded                   = 920,
    PktMonDrop_NL_BufferLengthExceeded                      = 921,
    PktMonDrop_NL_AddressResolutionTimeout                  = 922,
    PktMonDrop_NL_AddressResolutionFailure                  = 923,
    PktMonDrop_NL_IpsecFailure                              = 924,
    PktMonDrop_NL_ExtensionHeadersFailure                   = 925,
    PktMonDrop_NL_IpsnpiClientDrop                          = 926,
    PktMonDrop_NL_UnsupportedOffload                        = 927,
    PktMonDrop_NL_RoutingFailure                            = 928,
    PktMonDrop_NL_AncillaryDataFailure                      = 929,
    PktMonDrop_NL_RawDataFailure                            = 930,
    PktMonDrop_NL_SessionStateFailure                       = 931,
    PktMonDrop_NL_IpsnpiModifiedButNotForwarded             = 932,
    PktMonDrop_NL_IpsnpiNoNextHop                           = 933,
    PktMonDrop_NL_IpsnpiNoCompartment                       = 934,
    PktMonDrop_NL_IpsnpiNoInterface                         = 935,
    PktMonDrop_NL_IpsnpiNoSubInterface                      = 936,
    PktMonDrop_NL_IpsnpiInterfaceDisabled                   = 937,
    PktMonDrop_NL_IpsnpiSegmentationFailed                  = 938,
    PktMonDrop_NL_IpsnpiNoEthernetHeader                    = 939,
    PktMonDrop_NL_IpsnpiUnexpectedFragment                  = 940,
    PktMonDrop_NL_IpsnpiUnsupportedInterfaceType            = 941,
    PktMonDrop_NL_IpsnpiInvalidLsoInfo                      = 942,
    PktMonDrop_NL_IpsnpiInvalidUsoInfo                      = 943,
    PktMonDrop_NL_InternalError                             = 944,
    PktMonDrop_NL_AdministrativelyConfigured                = 945,
    PktMonDrop_NL_BadOption                                 = 946,
    PktMonDrop_NL_LoopbackDisallowed                        = 947,
    PktMonDrop_NL_SmallerScope                              = 948,
    PktMonDrop_NL_QueueFull                                 = 949,
    PktMonDrop_NL_InterfaceDisabled                         = 950,
 
    PktMonDrop_NL_IcmpGeneric                               = 951,
    PktMonDrop_NL_IcmpTruncatedHeader                       = 952,
    PktMonDrop_NL_IcmpInvalidChecksum                       = 953,
    PktMonDrop_NL_IcmpInspection                            = 954,
    PktMonDrop_NL_IcmpNeighborDiscoveryLoopback             = 955,
    PktMonDrop_NL_IcmpUnknownType                           = 956,
    PktMonDrop_NL_IcmpTruncatedIpHeader                     = 957,
    PktMonDrop_NL_IcmpOversizedIpHeader                     = 958,
    PktMonDrop_NL_IcmpNoHandler                             = 959,
    PktMonDrop_NL_IcmpRespondingToError                     = 960,
    PktMonDrop_NL_IcmpInvalidSource                         = 961,
    PktMonDrop_NL_IcmpInterfaceRateLimit                    = 962,
    PktMonDrop_NL_IcmpPathRateLimit                         = 963,
    PktMonDrop_NL_IcmpNoRoute                               = 964,
    PktMonDrop_NL_IcmpMatchingRequestNotFound               = 965,
    PktMonDrop_NL_IcmpBufferTooSmall                        = 966,
    PktMonDrop_NL_IcmpAncillaryDataQuery                    = 967,
    PktMonDrop_NL_IcmpIncorrectHopLimit                     = 968,
    PktMonDrop_NL_IcmpUnknownCode                           = 969,
    PktMonDrop_NL_IcmpSourceNotLinkLocal                    = 970,
    PktMonDrop_NL_IcmpTruncatedNdHeader                     = 971,
    PktMonDrop_NL_IcmpInvalidNdOptSourceLinkAddr            = 972,
    PktMonDrop_NL_IcmpInvalidNdOptMtu                       = 973,
    PktMonDrop_NL_IcmpInvalidNdOptPrefixInformation         = 974,
    PktMonDrop_NL_IcmpInvalidNdOptRouteInformation          = 975,
    PktMonDrop_NL_IcmpInvalidNdOptRdnss                     = 976,
    PktMonDrop_NL_IcmpInvalidNdOptDnssl                     = 977,
    PktMonDrop_NL_IcmpPacketParsingFailure                  = 978,
    PktMonDrop_NL_IcmpDisallowed                            = 979,
    PktMonDrop_NL_IcmpInvalidRouterAdvertisement            = 980,
    PktMonDrop_NL_IcmpSourceFromDifferentLink               = 981,
    PktMonDrop_NL_IcmpInvalidRedirectDestinationOrTarget    = 982,
    PktMonDrop_NL_IcmpInvalidNdTarget                       = 983,
    PktMonDrop_NL_IcmpNaMulticastAndSolicited               = 984,
    PktMonDrop_NL_IcmpNdLinkLayerAddressIsLocal             = 985,
    PktMonDrop_NL_IcmpDuplicateEchoRequest                  = 986,
    PktMonDrop_NL_IcmpNotAPotentialRouter                   = 987,
    PktMonDrop_NL_IcmpInvalidMldQuery                       = 988,
    PktMonDrop_NL_IcmpInvalidMldReport                      = 989,
    PktMonDrop_NL_IcmpLocallySourcedMldReport               = 990,
    PktMonDrop_NL_IcmpNotLocallyDestined                    = 991,
 
    PktMonDrop_NL_ArpInvalidSource                          = 992,
    PktMonDrop_NL_ArpInvalidTarget                          = 993,
    PktMonDrop_NL_ArpDlSourceIsLocal                        = 994,
    PktMonDrop_NL_ArpNotLocallyDestined                     = 995,
 
    PktMonDrop_NL_NlClientDiscard                           = 996,
 
    PktMonDrop_NL_IpsnpiUroSegmentSizeExceedsMtu            = 997,
 
    //
    // INET discard reasons
    //
    PktMonDrop_INET_SourceUnspecified                       = 1200,
    PktMonDrop_INET_DestinationMulticast                    = 1201,
    PktMonDrop_INET_HeaderInvalid                           = 1202,
    PktMonDrop_INET_ChecksumInvalid                         = 1203,
    PktMonDrop_INET_EndpointNotFound                        = 1204,
    PktMonDrop_INET_ConnectedPath                           = 1205,
    PktMonDrop_INET_SessionState                            = 1206,
    PktMonDrop_INET_ReceiveInspection                       = 1207,
    PktMonDrop_INET_AckInvalid                              = 1208,
    PktMonDrop_INET_ExpectedSyn                             = 1209,
    PktMonDrop_INET_Rst                                     = 1210,
    PktMonDrop_INET_SynRcvdSyn                              = 1211,
    PktMonDrop_INET_SimultaneousConnect                     = 1212,
    PktMonDrop_INET_PawsFailed                              = 1213,
    PktMonDrop_INET_LandAttack                              = 1214,
    PktMonDrop_INET_MissedReset                             = 1215,
    PktMonDrop_INET_OutsideWindow                           = 1216,
    PktMonDrop_INET_DuplicateSegment                        = 1217,
    PktMonDrop_INET_ClosedWindow                            = 1218,
    PktMonDrop_INET_TcbRemoved                              = 1219,
    PktMonDrop_INET_FinWait2                                = 1220,
    PktMonDrop_INET_ReassemblyConflict                      = 1221,
    PktMonDrop_INET_FinReceived                             = 1222,
    PktMonDrop_INET_ListenerInvalidFlags                    = 1223,
    PktMonDrop_INET_TcbNotInTcbTable                        = 1224,
    PktMonDrop_INET_TimeWaitTcbReceivedRstOutsideWindow     = 1225,
    PktMonDrop_INET_TimeWaitTcbSynAndOtherFlags             = 1226,
    PktMonDrop_INET_TimeWaitTcb                             = 1227,
    PktMonDrop_INET_SynAckWithFastopenCookieRequest         = 1228,
    PktMonDrop_INET_PauseAccept                             = 1229,
    PktMonDrop_INET_SynAttack                               = 1230,
    PktMonDrop_INET_AcceptInspection                        = 1231,
    PktMonDrop_INET_AcceptRedirection                       = 1232,
 
    //
    // Slbmux Error
    //
    PktMonDrop_SlbMux_ParsingFailure                            = 1301,
    PktMonDrop_SlbMux_FirstFragmentMiss                         = 1302,
    PktMonDrop_SlbMux_ICMPErrorPayloadValidationFailure         = 1303,
    PktMonDrop_SlbMux_ICMPErrorPacketMatchNoSession             = 1304,
    PktMonDrop_SlbMux_ExternalHairpinNexthopLookupFailure       = 1305,
    PktMonDrop_SlbMux_NoMatchingStaticMapping                   = 1306,
    PktMonDrop_SlbMux_NexthopReferenceFailure                   = 1307,
    PktMonDrop_SlbMux_CloningFailure                            = 1308,
    PktMonDrop_SlbMux_TranslationFailure                        = 1309,
    PktMonDrop_SlbMux_HopLimitExceeded                          = 1310,
    PktMonDrop_SlbMux_PacketBiggerThanMTU                       = 1311,
    PktMonDrop_SlbMux_UnexpectedRouteLookupFailure              = 1312,
    PktMonDrop_SlbMux_NoRoute                                   = 1313,
    PktMonDrop_SlbMux_SessionCreationFailure                    = 1314,
    PktMonDrop_SlbMux_NexthopNotOverExternalInterface           = 1315,
    PktMonDrop_SlbMux_NexthopExternalInterfaceMissNATInstance   = 1316,
    PktMonDrop_SlbMux_NATItselfCantBeInternalNexthop            = 1317,
    PktMonDrop_SlbMux_PacketRoutableInItsArrivalCompartment     = 1318,
    PktMonDrop_SlbMux_PacketTransportProtocolNotSupported       = 1319,
    PktMonDrop_SlbMux_PacketIsDestinedLocally                   = 1320,
    PktMonDrop_SlbMux_PacketDestinationIPandPortNotSubjectToNAT = 1321,
    PktMonDrop_SlbMux_MuxReject                                 = 1322,
    PktMonDrop_SlbMux_DipLookupFailure                          = 1323,
    PktMonDrop_SlbMux_MuxEncapsulationFailure                   = 1324,
    PktMonDrop_SlbMux_InvalidDiagPacketEncapType                = 1325,
    PktMonDrop_SlbMux_DiagPacketIsRedirect                      = 1326,
    PktMonDrop_SlbMux_UnableToHandleRedirect                    = 1327,
 
    //
    // Ipsec Errors
    //
    PktMonDrop_Ipsec_BadSpi                                     = 1401,
    PktMonDrop_Ipsec_SALifetimeExpired                          = 1402,
    PktMonDrop_Ipsec_WrongSA                                    = 1403,
    PktMonDrop_Ipsec_ReplayCheckFailed                          = 1404,
    PktMonDrop_Ipsec_InvalidPacket                              = 1405,
    PktMonDrop_Ipsec_IntegrityCheckFailed                       = 1406,
    PktMonDrop_Ipsec_ClearTextDrop                              = 1407,
    PktMonDrop_Ipsec_AuthFirewallDrop                           = 1408,
    PktMonDrop_Ipsec_ThrottleDrop                               = 1409,
    PktMonDrop_Ipsec_Dosp_Block                                 = 1410,
    PktMonDrop_Ipsec_Dosp_ReceivedMulticast                     = 1411,
    PktMonDrop_Ipsec_Dosp_InvalidPacket                         = 1412,
    PktMonDrop_Ipsec_Dosp_StateLookupFailed                     = 1413,
    PktMonDrop_Ipsec_Dosp_MaxEntries                            = 1414,
    PktMonDrop_Ipsec_Dosp_KeymodNotAllowed                      = 1415,
    PktMonDrop_Ipsec_Dosp_MaxPerIpRateLimitQueues               = 1416,
    PktMonDrop_Ipsec_NoMemory                                   = 1417,
    PktMonDrop_Ipsec_Unsuccessful                               = 1418,
 
    //
    // NetCx Drop Reasons
    //
    PktMonDrop_NetCx_NetPacketLayoutParseFailure                = 1501,
    PktMonDrop_NetCx_SoftwareChecksumFailure                    = 1502,
    PktMonDrop_NetCx_NicQueueStop                               = 1503,
    PktMonDrop_NetCx_InvalidNetBufferLength                     = 1504,
    PktMonDrop_NetCx_LSOFailure                                 = 1505,
    PktMonDrop_NetCx_USOFailure                                 = 1506,
    PktMonDrop_NetCx_BufferBounceFailureAndPacketIgnore         = 1507,
 
} PKTMON_DROP_REASON
```

#### PACKETMONITOR_ STREAM_EVENT_INFO

```cpp
typedef struct PACKETMONITOR_STREAM_EVENT_INFO
{
    union
    {
        PACKETMONITOR_STREAM_START_INFO_OUT StreamStartInfo;     
        PACKETMONITOR_STREAM_STOP_INFO_OUT StreamStopInfo
        PACKETMONITOR_STREAM_PROCESS_INFO_OUT StreamProcessInfo; 
    };
} PACKETMONITOR_STREAM_EVENT_INFO;
```

* StreamStartInfo – Struct PACKETMONITOR_STREAM_START_INFO_OUT is passed when eventKind is ‘PacketMonitorStreamEventStarted’. 
* StreamStopInfo – Struct PACKETMONITOR_STREAM_STOP_INFO_OUT is passed when eventKind is ‘PacketMonitorStreamEventStopped’ and ‘PacketMonitorStreamEventFatalError’. 
* StreamProcessInfo - Struct PACKETMONITOR_STREAM_PROCESS_INFO_OUT is passed when event kind is ‘PacketMonitorStreamEventProcessInfo.

#### PACKETMONITOR_ STREAM_ EVENT_KIND

```cpp
typedef enum PACKETMONITOR_STREAM_EVENT_KIND
{
    PacketMonitorStreamEventStarted,         
    PacketMonitorStreamEventStopped,        
    PacketMonitorStreamEventFatalError,      
    PacketMonitorStreamEventProcessInfo,     
} PACKETMONITOR_STREAM_EVENT_KIND;
```

PacketMonitorStreamEventStarted – Streaming started.
PacketMonitorStreamEventStopped – Streaming stopped.
PacketMonitorStreamEventFatalError – Fatal error occurred, and streaming stopped. 
PacketMonitorStreamEventProcessInfo – Error or Warning event generated during streaming. 

#### PACKETMONITOR_ STREAM_START_INFO_OUT

```cpp
typedef struct PACKETMONITOR_STREAM_START_INFO_OUT
{
    ULONG PacketBufferSizeInBytes;   
    UINT16 TruncationSize;           
} PACKETMONITOR_STREAM_START_INFO_OUT;
```

* PacketBufferSizeInBytes – Size of Packet Buffer created after successful call to this API. 
* TruncationSize – Configured truncation size of packet. 

#### PACKETMONITOR_ STREAM_STOP_INFO_OUT

```cpp
typedef struct PACKETMONITOR_STREAM_STOP_INFO_OUT
{
    BOOLEAN IsFatalError;   
    DWORD Reason;           
} PACKETMONITOR_STREAM_STOP_INFO_OUT;
```

* IsFatalError – Flag indicating that the event is a fatal error. 
* Reason – DWORD error code.  Possible values currently are:
  * ERROR_INVALID_DATA(13) - Happens when the packet data is corrupt while reading. Signifies and internal error during streaming. 
  * ERROR_INTERNAL_ERROR – Internal error inside Pktmon. 

#### PACKETMONITOR_ STREAM_PROCESS_INFO_OUT

```cpp
typedef struct PACKETMONITOR_STREAM_PROCESS_INFO_OUT
{
    BOOLEAN IsWarning;  
    DWORD Reason;       
    UINT64 PacketLength;    
} PACKETMONITOR_STREAM_PROCESS_INFO_OUT;
```

* IsWarning – Flag to indicate that the event is a warning. 
* Reason – DWORD error code indicating the warning or error. Possible Values currently supported are:
  * ERROR_INSUFFICIENT_BUFFER(122) – Indicates that the packet data size was larger than the internal buffer size of 9000 bytes. 
* PacketLength – Packet Length of the packet received on the stream.

## See also

[Packet Monitor (Pktmon) reference](../pktmon-reference.md)
