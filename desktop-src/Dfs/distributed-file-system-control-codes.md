---
title: Distributed File System Control Codes
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1d9bebe6-f494-41e5-8a8d-51bf98eaa374
ms.prod: windows-server-dev
ms.technology: windows-distributed-file-system-(dfs)
ms.tgt_platform: multiple
description: 
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Distributed File System Control Codes

The following are the Distributed File System (DFS) control codes:

## In this section

<dl> <dt>

[**FSCTL\_DFS\_GET\_PKT\_ENTRY\_STATE**](/previous-versions/windows/desktop/api/LmDfs/)
</dt> <dd>

The [**FSCTL\_DFS\_GET\_PKT\_ENTRY\_STATE**](/previous-versions/windows/desktop/api/LmDfs/) control code can get the same information as the [**NetDfsGetClientInfo**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsgetclientinfo) function but can provide better performance in some configurations with high latencies to the DFS servers. It is not recommended to use the **FSCTL\_DFS\_GET\_PKT\_ENTRY\_STATE** control code unless there are performance issues.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.

</dd> </dl>

 

 




