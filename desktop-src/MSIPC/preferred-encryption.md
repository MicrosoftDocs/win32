---
title: Preferred encryption
description: Used to specify the encryption package.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '99A2B1F5-21A3-4149-931E-30C6891DA0A6'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPC_ENCRYPTION_PACKAGE_AES256_CBC4K
- IPC_ENCRYPTION_PACKAGE_AES128_CBC4K
- IPC_ENCRYPTION_PACKAGE_AES128_ECB
api_location:
- Ipcprot.h
api_type:
- HeaderDef
---

# Preferred encryption

Used to specify the encryption package.

<dl> <dt>

<span id="IPC_ENCRYPTION_PACKAGE_AES256_CBC4K"></span><span id="ipc_encryption_package_aes256_cbc4k"></span>**IPC\_ENCRYPTION\_PACKAGE\_AES256\_CBC4K**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Use this flag to explicitly set encryption for AES 256


</dt> </dl> </dd> <dt>

<span id="IPC_ENCRYPTION_PACKAGE_AES128_CBC4K"></span><span id="ipc_encryption_package_aes128_cbc4k"></span>**IPC\_ENCRYPTION\_PACKAGE\_AES128\_CBC4K**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



Use this flag to set encryption for AES 128


</dt> </dl> </dd> <dt>

<span id="IPC_ENCRYPTION_PACKAGE_AES128_ECB"></span><span id="ipc_encryption_package_aes128_ecb"></span>**IPC\_ENCRYPTION\_PACKAGE\_AES128\_ECB**
</dt> <dd> <dl> <dt>

3
</dt> <dt>



Use this flag to set encryption for AES 128, also know as *deprecated algorithms*.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



 

 





