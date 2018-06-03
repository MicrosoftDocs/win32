---
title: Cryptography Functions
description: Cryptography functions are used by applications to manage Checkpointing data for cluster resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 74677418-CA63-4B4E-9844-A3A47AFFAD49
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cryptography Functions

Cryptography functions are used by applications to manage [Checkpointing](checkpointing.md) data for cluster resources.

## In this section

<dl> <dt>

[*CloseClusterCryptProvider*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pclose_cluster_crypt_provider)
</dt> <dd>

Closes a handle to a Cryptographic Service Provider (CSP). The **PCLOSE\_CLUSTER\_CRYPT\_PROVIDER** type defines a pointer to this function.

</dd> <dt>

[*ClusterDecrypt*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pcluster_decrypt)
</dt> <dd>

Decrypts [Checkpointing](checkpointing.md) data for a Cryptographic Service Provider (CSP).

</dd> <dt>

[*ClusterEncrypt*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pcluster_encrypt)
</dt> <dd>

Encrypts [Checkpointing](checkpointing.md) data for a Cryptographic Service Provider (CSP).

</dd> <dt>

[*FreeClusterCrypt*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pfree_cluster_crypt)
</dt> <dd>

TBD

</dd> <dt>

[*OpenClusterCryptProvider*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-popen_cluster_crypt_provider)
</dt> <dd>

Opens a handle to a Cryptographic Service Provider (CSP) in order to manage the encryption of [Checkpointing](checkpointing.md) data for a cluster resource. The **POPEN\_CLUSTER\_CRYPT\_PROVIDER** type defines a pointer to this function.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> <dt>

[Checkpointing](checkpointing.md)
</dt> </dl>

 

 




