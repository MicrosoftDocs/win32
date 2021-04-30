---
description: Specify the protection levels for Copy Generation Management System&\#8212;Analog (CGMS-A).
ms.assetid: 739e2f9e-b8f1-4ee1-8706-9a069773a3de
title: CGMS-A Protection Flags (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CGMS-A Protection Flags

The constants in the following table specify the protection levels for Copy Generation Management System Analog (CGMS-A).



| Constant/value                                                                                                                                                                                                                                                                                                 | Description                                                                                                                       |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| <span id="OPM_CGMSA_OFF"></span><span id="opm_cgmsa_off"></span><dl> <dt>**OPM\_CGMSA\_OFF**</dt> <dt>0x00</dt> </dl>                                                                                       | CGMS-A is disabled. <br/>                                                                                                   |
| <span id="OPM_CGMSA_COPY_FREELY"></span><span id="opm_cgmsa_copy_freely"></span><dl> <dt>**OPM\_CGMSA\_COPY\_FREELY**</dt> <dt>0x01</dt> </dl>                                                              | The protection level is Copy Freely.<br/>                                                                                   |
| <span id="OPM_CGMSA_COPY_NO_MORE"></span><span id="opm_cgmsa_copy_no_more"></span><dl> <dt>**OPM\_CGMSA\_COPY\_NO\_MORE**</dt> <dt>0x02</dt> </dl>                                                          | The protection level is Copy No More. <br/>                                                                                 |
| <span id="OPM_CGMSA_COPY_ONE_GENERATION"></span><span id="opm_cgmsa_copy_one_generation"></span><dl> <dt>**OPM\_CGMSA\_COPY\_ONE\_GENERATION**</dt> <dt>0x03</dt> </dl>                                     | The protection level is Copy One Generation. <br/>                                                                          |
| <span id="OPM_CGMSA_COPY_NEVER"></span><span id="opm_cgmsa_copy_never"></span><dl> <dt>**OPM\_CGMSA\_COPY\_NEVER**</dt> <dt>0x04</dt> </dl>                                                                 | The protection level is Copy Never.<br/>                                                                                    |
| <span id="OPM_CGMSA_REDISTRIBUTION_CONTROL_REQUIRED"></span><span id="opm_cgmsa_redistribution_control_required"></span><dl> <dt>**OPM\_CGMSA\_REDISTRIBUTION\_CONTROL\_REQUIRED**</dt> <dt>0x08</dt> </dl> | Redistribution control (also called the *broadcast flag*) is required. This flag can be combined with the other flags.<br/> |



## Remarks

These flags are equivalent to the **COPP\_CGMSA\_Protection\_Level** enumeration constants used in the Certified Output Protection Protocol (COPP).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Constants](media-foundation-constants.md)
</dt> </dl>

 

 




