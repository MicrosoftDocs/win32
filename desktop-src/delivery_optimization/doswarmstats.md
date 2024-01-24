---
title: DOSwarmStats structure (Deliveryoptimization.h)
description: Contains fields for download and upload statistics for a file.
ms.assetid: 66B2498A-38E0-44E4-96C1-F778BD9AA593
keywords:
- DOSwarmStats structure
topic_type:
- apiref
api_name:
- DOSwarmStats
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# DOSwarmStats structure

Contains fields for download and upload statistics for a file.

## Syntax


```C++
typedef struct _DOSwarmStats {
  LPWSTR       fileId;
  LPWSTR       sourceURL;
  UINT64       fileSize;
  UINT64       totalBytesDownloaded;
  UINT64       bytesFromLanPeers;
  UINT64       bytesFromGroupPeers;
  UINT64       bytesFromInternetPeers;
  UINT64       bytesFromHttp;
  UINT64       bytesFromDoinc;
  UINT64       bytesToLanPeers;
  UINT64       bytesToGroupPeers;
  UINT64       bytesToInternetPeers;
  UINT         httpConnectionCount;
  UINT         doincConnectionCount;
  UINT         lanConnectionCount;
  UINT         groupConnectionCount;
  UINT         internetConnectionCount;
  UINT         downloadDuration;
  DownloadMode downloadMode;
  SwarmStatus  status;
  BOOL         isBackground;
} DOSwarmStats;
```



## Members

<dl> <dt>

**fileId**
</dt> <dd>

Null-terminated string that was specified with the **AddFileWithRanges** call.

</dd> <dt>

**sourceURL**
</dt> <dd>

Null-terminated string that contains the name of the file on the server (for example, https://&lt;server&gt;/&lt;path&gt;/file.ext).

</dd> <dt>

**fileSize**
</dt> <dd>

Size of the file in bytes.

</dd> <dt>

**totalBytesDownloaded**
</dt> <dd>

Total number of bytes transferred.

</dd> <dt>

**bytesFromLanPeers**
</dt> <dd>

Number of bytes transferred from LAN peers.

</dd> <dt>

**bytesFromGroupPeers**
</dt> <dd>

Number of bytes transferred from group peers.

</dd> <dt>

**bytesFromInternetPeers**
</dt> <dd>

Number of bytes transferred from Internet peers.

</dd> <dt>

**bytesFromHttp**
</dt> <dd>

Number of bytes transferred from http.

</dd> <dt>

**bytesFromDoinc**
</dt> <dd>

For internal use only.

</dd> <dt>

**bytesToLanPeers**
</dt> <dd>

Number of bytes transferred to LAN peers.

</dd> <dt>

**bytesToGroupPeers**
</dt> <dd>

Number of bytes transferred to group peers.

</dd> <dt>

**bytesToInternetPeers**
</dt> <dd>

Number of bytes transferred to Internet peers.

</dd> <dt>

**httpConnectionCount**
</dt> <dd>

Count of http connections.

</dd> <dt>

**doincConnectionCount**
</dt> <dd>

For internal use only.

</dd> <dt>

**lanConnectionCount**
</dt> <dd>

Count of LAN connections.

</dd> <dt>

**groupConnectionCount**
</dt> <dd>

Count of group connections.

</dd> <dt>

**internetConnectionCount**
</dt> <dd>

Count of Internet connections.

</dd> <dt>

**downloadDuration**
</dt> <dd>

Duration of the file transfer in milliseconds.

</dd> <dt>

**downloadMode**
</dt> <dd>

The download mode used, see [**DownloadMode**](downloadmode.md).

</dd> <dt>

**status**
</dt> <dd>

The status of a file transfer, see [**SwarmStatus**](swarmstatus.md).

</dd> <dt>

**isBackground**
</dt> <dd>

True, if this is a background transfer.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl> |



 

 





