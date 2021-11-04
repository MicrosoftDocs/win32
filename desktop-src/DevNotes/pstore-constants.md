---
description: The following constants are used by PStore.
ms.assetid: 4bdccb86-2e0e-461c-9a74-184861b7db1e
title: PStore Constants (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PST_E_OK
- PST_E_TYPE_EXISTS
- PST_AUTHENTICODE
- PST_BINARY_CHECK
- PST_SECURITY_DESCRIPTOR
api_type: 
- HeaderDef
api_location: 
- Pstore.h
---

# PStore Constants

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

The following constants are used by PStore.

Protected Storage Error Codes



| Constant/value                                                                                                                                                                                                                               | Description                                                        |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|
| <span id="PST_E_OK"></span><span id="pst_e_ok"></span><dl> <dt>**PST\_E\_OK**</dt> <dt>0x00000000L</dt> </dl>                             | The operation was successful.<br/>                           |
| <span id="PST_E_TYPE_EXISTS"></span><span id="pst_e_type_exists"></span><dl> <dt>**PST\_E\_TYPE\_EXISTS**</dt> <dt>0x800C0004L</dt> </dl> | The data item already exists in the protected storage. <br/> |



Access Clause Values



| Constant/value                                                                                                                                                                                                                                      | Description                                                                             |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|
| <span id="PST_AUTHENTICODE"></span><span id="pst_authenticode"></span><dl> <dt>**PST\_AUTHENTICODE**</dt> <dt>1</dt> </dl>                       | Points to a [**PST\_AUTHENTICODEDATA**](pst-authenticodedata.md) structure.<br/> |
| <span id="PST_BINARY_CHECK_"></span><span id="pst_binary_check_"></span><dl> <dt>**PST\_BINARY\_CHECK** </dt> <dt>2</dt> </dl>                   | Points to a **PST\_BINARYCHECKDATA** structure.<br/>                              |
| <span id="PST_SECURITY_DESCRIPTOR"></span><span id="pst_security_descriptor"></span><dl> <dt>**PST\_SECURITY\_DESCRIPTOR**</dt> <dt>4</dt> </dl> | Points to a valid Windows security descriptor. <br/>                              |



## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl> |



 

 
