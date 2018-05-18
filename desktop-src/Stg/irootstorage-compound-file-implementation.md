---
title: IRootStorage - Compound File Implementation
description: COM's compound file implementation of IRootStorage allows you to support saving files in low-memory or low disk-space situations. For information on how this interface behaves, see IRootStorage.
ms.assetid: '0847929e-63ce-42f9-9d47-2e7222e003bb'
keywords: ["IRootStorage Strctd Stg ,compound file implementation"]
---

# IRootStorage - Compound File Implementation

COM's compound file implementation of [**IRootStorage**](irootstorage.md) allows you to support saving files in low-memory or low disk-space situations. For information on how this interface behaves, see **IRootStorage**.

## When to Use

Use the system-supplied implementation of [**IRootStorage**](irootstorage.md) only to support saving files under low-memory conditions.

## Remarks

It is possible to call COM's implementation of [**IRootStorage::SwitchToFile**](irootstorage-switchtofile.md) to do a normal save-as operation to another file. However, applications that do this might not be compatible with future generations of COM storage. To avoid this possibility, applications performing a save-as operation should manually create the second compound file and invoke [**IStorage::CopyTo**](istorage-copyto.md). The **IRootStorage::SwitchToFile** method should be used only in emergency (low-memory or disk-space) situations.

## Related topics

<dl> <dt>

[**IRootStorage**](irootstorage.md)
</dt> <dt>

[**IRootStorage::SwitchToFile**](irootstorage-switchtofile.md)
</dt> </dl>

 

 




