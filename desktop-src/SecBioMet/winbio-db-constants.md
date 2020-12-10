---
title: WINBIO_DB Constants (Winbio\_types.h)
description: Specify the database to be used for a system pool.
ms.assetid: 2cffa455-5834-4a35-b8d8-f9d1feddcaa1
topic_type:
- apiref
api_name:
- WINBIO_DB_DEFAULT
- WINBIO_DB_BOOTSTRAP
- WINBIO_DB_ONCHIP
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_DB Constants

The following constants can be used when calling [**WinBioOpenSession**](/windows/desktop/api/Winbio/nf-winbio-winbioopensession) to specify the database to be used for a system pool.



| Constant                                                                                                                                                                         | Description                                                                                                                                                                                          |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_DB_DEFAULT"></span><span id="winbio_db_default"></span><dl> <dt>**WINBIO\_DB\_DEFAULT**</dt> </dl>       | Each biometric unit in the sensor pool uses the default database specified in the default biometric unit configuration.<br/>                                                                   |
| <span id="WINBIO_DB_BOOTSTRAP"></span><span id="winbio_db_bootstrap"></span><dl> <dt>**WINBIO\_DB\_BOOTSTRAP**</dt> </dl> | Can be used for scenarios prior to starting Windows. Typically, the database is part of the sensor chip or is part of the BIOS and can only be used for template enrollment and deletion.<br/> |
| <span id="WINBIO_DB_ONCHIP"></span><span id="winbio_db_onchip"></span><dl> <dt>**WINBIO\_DB\_ONCHIP**</dt> </dl>          | The database resides on the sensor chip.<br/>                                                                                                                                                  |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Constants](client-application-constants.md)
</dt> </dl>

 

 





