---
title: PacketMonitorEnumDataSources
description: Retrieves list of Data Sources from within Windows networking stack which are registered with Pktmon to report packet flows/drops.
ms.topic: reference
ms.date: 07/03/2024
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - Pktmonapi.dll
api_name:
 - PacketMonitorEnumDataSources
---

# PacketMonitorEnumDataSources function

## Description

Retrieves list of Data Sources from within Windows networking stack which are registered with Pktmon to report packet flows/drops.

Retrieves list of Data Sources information from the windows networking stack. Each Data source within the network stack corresponds to a component which reports packet flows and drops to pktmon driver. Packet Monitor captures packets with correlation to these components a.k.a. data sources.

## Syntax

```cpp
HRESULT
WINAPI
PacketMonitorEnumDataSources(
    _In_ PACKETMONITOR_HANDLE handle,
    _In_ PACKETMONITOR_DATA_SOURCE_KIND sourceKind,
    _In_ BOOLEAN showHidden,
    _In_ SIZE_T bufferCapacity,
    _Out_ SIZE_T* bytesNeeded,
    _Out_writes_bytes_opt_(bufferCapacity) PACKETMONITOR_DATA_SOURCE_LIST* dataSourceList
    );
```

## Parameters

### [in] handle

Handle to Packet Monitor obtained from ’PacketMonitorInitialize’.

### [in] sourceKind

Data Source Kind as a filter to apply on the output list. 

Example – If ‘PacketMonitorDataSourceKindNetworkInterface’ is provided then only data sources of Network Interface type will be retrieved. 

Below are the Enum values to choose from.

```cpp
typedef enum PACKETMONITOR_DATA_SOURCE_KIND
{
    PacketMonitorDataSourceKindAll,
    PacketMonitorDataSourceKindNetworkInterface
} PACKETMONITOR_DATA_SOURCE_KIND;
```

### [in] showHidden

If True, the output list will include every single data source ID; in some cases, multiple entries in the list may map to the same underlying networking component If false, the output list will include a single entry for each data source and suppress potential duplicate entries. By Default, this is false. 

### [in] bufferCapacity

Size of output buffer (dataSourceList) provided. 

### [out] bytesNeeded

Pointer to a SIZE_T variable to store the actual size of the data source information list.  

### [out] dataSourceList

Pointer to an output buffer of ‘bufferCapacity’ size to store Data source information retrieved from the driver. 

## Returns

If the function succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## Remarks

Certain networking components will register with the Packet Monitor driver several times, so some data sources will have multiple IDs associated with it. 

If enumerating data sources with the intention of using the returned list to call PacketMonitorAddSingleDataSourceToSession, one should call PacketMonitorEnumDataSources with showHidden set to false.

If enumerating data sources for the purpose of correlating stream events (which include a component ID) with the data source they are coming from, one should call PacketMonitorEnumDataSources with showHidden set to true. The logging output from Packet Monitor may report a data source ID different than the one used to select the data source, so the hidden and duplicate IDs must be enumerated to correlate outputs with their data source.

Struct Definitions: PACKETMONITOR_DATA_SOURCE_SPECIFICATION

```cpp
typedef enum PACKETMONITOR_DATA_SOURCE_KIND
{
    PacketMonitorDataSourceKindAll,
    PacketMonitorDataSourceKindNetworkInterface,
} PACKETMONITOR_DATA_SOURCE_KIND;
 
typedef union PACKETMONITOR_IP_ADDRESS
{
    ULONG IPv4;
    UCHAR IPv4_bytes[PACKETMONITOR_IPV4_ADDRESS_SIZE];
 
    ULONGLONG IPv6[PACKETMONITOR_IPV6_ADDRESS_SIZE / sizeof(ULONGLONG)];
    UCHAR IPv6_bytes[PACKETMONITOR_IPV6_ADDRESS_SIZE];
} PACKETMONITOR_IP_ADDRESS;

typedef struct PACKETMONITOR_DATA_SOURCE_SPECIFICATION
{
    PACKETMONITOR_DATA_SOURCE_KIND Kind;
    WCHAR Name[PACKETMONITOR_MAX_NAME_LENGTH];
    WCHAR Description[PACKETMONITOR_MAX_STRING_LENGTH];
 
    UINT32 Id;
    UINT32 SecondaryId;
    
    UINT32 ParentId;
 
    union
    {
        struct
        {
            UINT Guid : 1;
            UINT IpV6Address : 1;
            UINT IpV4Address : 1;
            UINT MacAddress : 1;
 
        } IsPresent;
 
        UINT IsPresentValue;
    };
    
    union
    {
        GUID Guid;
        PACKETMONITOR_IP_ADDRESS IpAddress;
        UCHAR MacAddress[PACKETMONITOR_MAC_ADDRESS_SIZE];
    } Detail;
} PACKETMONITOR_DATA_SOURCE_SPECIFICATION;

typedef struct PACKETMONITOR_DATA_SOURCE_LIST
{
    UINT32 NumDataSources;
    PACKETMONITOR_DATA_SOURCE_SPECIFICATION const* DataSources[ANYSIZE_ARRAY];
} PACKETMONITOR_DATA_SOURCE_LIST;
```

PACKETMONITOR_DATA_SOURCE_LIST
* NumDataSources – Count of DataSources returned. 
* DataSources – Array of DataSources

PACKETMONITOR_DATA_SOURCE_SPECIFICATION
* Kind – Kind of Data Source. Currently Pktmon only supports ‘PacketMonitorDataSourceKindAll’ or ‘PacketMonitorDataSourceKindNetworkInterface’
* Name – Name of the DataSource returned. 
* Description – Description of the DataSource. 
* Id – Primary Id of the data source registered with Pktmon. 
* SecondaryId – Id for related component when data sources register with Pktmon multiple times. When analyzing etw events/streaming, we may need both IDs(primary and secondary) to correlate events/packets to the component they were captured on. 
* ParentId – This is the PrimaryId of hierarchical data source. It will be 0 if no parent. For example, virtual NIC will have ID of vmswitch as parent, etc. 
* IsPresent – This union specifies which information is present for this specific data source.
  * Guid – Present when IsPresent.Guid is TRUE. 
  * IPAddress – Present when either IsPresent.IPV6Address or IsPresent .IpV4Address is TRUE. This is stored in Network Byte order. 
  * MacAddress – Present when IsPresent.MacAddress is TRUE. 

PACKETMONITOR_IP_ADDRESS
* Stores the IP Address in Network byte order. 
* PACKETMONITOR_IPV4_ADDRESS_SIZE is 4
* PACKETMONITOR_IPV6_ADDRESS_SIZE is 16

## See also

[Packet Monitor (Pktmon) reference](../pktmon-reference.md)
